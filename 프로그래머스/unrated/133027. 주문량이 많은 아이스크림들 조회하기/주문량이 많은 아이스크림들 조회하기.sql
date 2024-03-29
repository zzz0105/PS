# SELECT JULY.FLAVOR FROM JULY JOIN FIRST_HALF ON JULY.FLAVOR = FIRST_HALF.FLAVOR 
# GROUP BY FLAVOR ORDER BY SUM(JULY.TOTAL_ORDER)+FIRST_HALF.TOTAL_ORDER DESC LIMIT 3

SELECT FIRST_HALF.FLAVOR 
FROM (SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOT FROM JULY GROUP BY FLAVOR) JULY_FL
    JOIN FIRST_HALF ON JULY_FL.FLAVOR=FIRST_HALF.FLAVOR
ORDER BY JULY_FL.TOT+FIRST_HALF.TOTAL_ORDER DESC 
LIMIT 3