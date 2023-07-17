"C:\Users\xmika\Downloads\world-db\world.sql" 

mysql> USE world;
Database changed
mysql> SHOW TABLES;
+-----------------+
| Tables_in_world |
+-----------------+
| city            |
| country         |
| countrylanguage |
+-----------------+
3 rows in set (0.00 sec)

mysql> SELECT COUNT(*) FROM city;
+----------+
| COUNT(*) |
+----------+
|     4079 |
+----------+
1 row in set (0.00 sec)

mysql> SELECT COUNT(*) FROM country;
+----------+
| COUNT(*) |
+----------+
|      239 |
+----------+
1 row in set (0.00 sec)

mysql> DESCRIBE country;
+----------------+---------------------------------------------------------------------------------------+------+-----+---------+-------+
| Field          | Type                                                                                  | Null | Key | Default | Extra |
+----------------+---------------------------------------------------------------------------------------+------+-----+---------+-------+
| Code           | char(3)                                                                               | NO   | PRI |         |       |
| Name           | char(52)                                                                              | NO   |     |         |       |
| Continent      | enum('Asia','Europe','North America','Africa','Oceania','Antarctica','South America') | NO   |     | Asia    |       |
| Region         | char(26)                                                                              | NO   |     |         |       |
| SurfaceArea    | decimal(10,2)                                                                         | NO   |     | 0.00    |       |
| IndepYear      | smallint                                                                              | YES  |     | NULL    |       |
| Population     | int                                                                                   | NO   |     | 0       |       |
| LifeExpectancy | decimal(3,1)                                                                          | YES  |     | NULL    |       |
| GNP            | decimal(10,2)                                                                         | YES  |     | NULL    |       |
| GNPOld         | decimal(10,2)                                                                         | YES  |     | NULL    |       |
| LocalName      | char(45)                                                                              | NO   |     |         |       |
| GovernmentForm | char(45)                                                                              | NO   |     |         |       |
| HeadOfState    | char(60)                                                                              | YES  |     | NULL    |       |
| Capital        | int                                                                                   | YES  |     | NULL    |       |
| Code2          | char(2)                                                                               | NO   |     |         |       |
+----------------+---------------------------------------------------------------------------------------+------+-----+---------+-------+
15 rows in set (0.00 sec)

mysql> SELECT COUNT(region) FROM country;
+---------------+
| COUNT(region) |
+---------------+
|           239 |
+---------------+
1 row in set (0.00 sec)

mysql> SELECT SUM(Population) FROM country;
+-----------------+
| SUM(Population) |
+-----------------+
|      6078749450 |
+-----------------+
1 row in set (0.00 sec)

mysql> SELECT SUM(Capital) FROM country;
+--------------+
| SUM(Capital) |
+--------------+
|       480543 |
+--------------+
1 row in set (0.00 sec)

mysql> SELECT MIN(GNP) FROM country;
+----------+
| MIN(GNP) |
+----------+
|     0.00 |
+----------+
1 row in set (0.00 sec)

mysql> SELECT MAX(GNP) FROM country; 
+------------+
| MAX(GNP)   |
+------------+
| 8510700.00 |
+------------+
1 row in set (0.00 sec)

mysql> SELECT AVG(GNP) FROM country; 
+---------------+
| AVG(GNP)      |
+---------------+
| 122823.882427 |
+---------------+
1 row in set (0.00 sec)

mysql> SELECT Continent, COUNT(*) AS number
    -> FROM Country
    -> GROUP BY Continent;
+---------------+--------+
| Continent     | number |
+---------------+--------+
| North America |     37 |
| Asia          |     51 |
| Africa        |     58 |
| Europe        |     46 |
| South America |     14 |
| Oceania       |     28 |
| Antarctica    |      5 |
+---------------+--------+
7 rows in set (0.00 sec)

mysql> SELECT * FROM (SELECT ROW_NUMBER() OVER() AS ROWNUM, SUM(SurfaceArea) AS AREA, Continent FROM country GROUP BY Continent) AS Tab WHERE ROWN
UM%2=0;
+--------+-------------+-----------+
| ROWNUM | AREA        | Continent |
+--------+-------------+-----------+
|      2 | 31881005.00 | Asia      |
|      4 | 23049133.90 | Europe    |
|      6 |  8564294.00 | Oceania   |
+--------+-------------+-----------+
3 rows in set (0.00 sec)