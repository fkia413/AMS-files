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
