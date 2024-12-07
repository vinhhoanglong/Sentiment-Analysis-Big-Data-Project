SELECT 
    day, month, year, 
    sentiment, 
    COUNT(*) AS tweet_count
FROM 
    mydb."table"
GROUP BY 
    year, month, day, sentiment
ORDER BY 
    year, month, day;
    
    
SELECT 
    hour, sentiment, 
    COUNT(*) AS tweet_count
FROM 
    mydb."table"
GROUP BY 
    hour, sentiment
ORDER BY 
    hour;


SELECT *
FROM
    mydb."table"
where
    month = 5
and
    day
between
    1 and 23
    
    
    
SELECT * 
FROM mydb."table"
WHERE month = 5 AND day = 25  AND sentiment = 'NEGATIVE'



select * from mydb."table"
where month = 5 and day = 22



SELECT *
FROM mydb."table"
WHERE 
    month = 6 AND day > 16
    
