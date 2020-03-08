SELECT 
    A.appid,
    A.gameName,
    COUNT(*),
    AVG(A.playerCount),
    MIN(DATE(A.date)) AS first_date
FROM
    (SELECT 
        *
    FROM
        steam.player_count
    WHERE
        playerCount > 0) A,
    (SELECT 
        appid, gameName, MIN(DATE(date)) AS first_date
    FROM
        steam.player_count
    WHERE
        player_count > 0
    GROUP BY 1 , 2
    HAVING DATE(first_date) BETWEEN '2019-03-19' AND '2019-06-30') B
WHERE
    A.appid = B.appid
        AND DATEDIFF(A.date, B.first_date) <= 28
GROUP BY 1 , 2
HAVING AVG(A.playerCount) >= 30;