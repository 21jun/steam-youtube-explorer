from database.pymysql_conn import DataBase
from util.text import clean_text
import pandas as pd


if __name__ == "__main__":

    db = DataBase()

    SQL = """
    SELECT * FROM yt_video_info;
    """
    df = db.to_df(SQL)

    query = "SELECT text FROM yt_comment where videoId='{videoId}';"
    for index, row in df.iterrows():
        game_name = row['gameName'].lower()

        title = clean_text(row['videoTitle'])
        title_cnt = title.count(game_name)

        tags = clean_text(row['tags'])
        tags_cnt = tags.count(game_name)

        description = clean_text(row['description'])
        desc_cnt = description.count(game_name)

        video_id = row['videoId']
        comments = db.to_df(query.format(videoId=video_id))
        comment_cnt = 0
        for index, comment in comments.iterrows():
            text = clean_text(comment['text'])
            comment_cnt += text.count(game_name)

        print(game_name, video_id, title_cnt, tags_cnt, desc_cnt, comment_cnt)
        update_q = """
        UPDATE yt_video_info 
        SET title_cnt = {title_cnt}, desc_cnt={desc_cnt}, tags_cnt={tags_cnt}, comment_cnt={comment_cnt}
        WHERE id={id}
        """
        # db.cur.execute(qq)
        db.cur.execute(update_q.format(title_cnt=title_cnt,
                                       desc_cnt=desc_cnt, tags_cnt=tags_cnt,
                                       comment_cnt=comment_cnt, id=row['id']))
