from database.pymysql_conn import DataBase
import pandas as pd


db = DataBase()

SQL = "SELECT * FROM get_new_games ;"
df = db.to_df(SQL)
print(df)
