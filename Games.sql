Games

mysql> DESCRIBE customers;
+--------------+-------------+------+-----+---------+----------------+
| Field        | Type        | Null | Key | Default | Extra          |
+--------------+-------------+------+-----+---------+----------------+
| customer_id  | int         | NO   | PRI | NULL    | auto_increment |
| name         | varchar(40) | NO   |     | NULL    |                |
| email        | varchar(60) | NO   |     | NULL    |                |
| house_number | int         | NO   |     | NULL    |                |
| postcode     | varchar(8)  | NO   |     | NULL    |                |
+--------------+-------------+------+-----+---------+----------------+
5 rows in set (0.01 sec)

mysql> DESCRIBE products;
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| product_id | int          | NO   | PRI | NULL    | auto_increment |
| title      | varchar(60)  | NO   |     | NULL    |                |
| price      | decimal(6,2) | NO   |     | NULL    |                |
| stock      | int          | NO   |     | NULL    |                |
+------------+--------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)

mysql> DESCRIBE orders;
+-------------+------+------+-----+---------+----------------+
| Field       | Type | Null | Key | Default | Extra          |
+-------------+------+------+-----+---------+----------------+
| order_id    | int  | NO   | PRI | NULL    | auto_increment |
| customer_id | int  | NO   | MUL | NULL    |                |
| product_id  | int  | NO   | MUL | NULL    |                |
| date_placed | date | NO   |     | NULL    |                |
+-------------+------+------+-----+---------+----------------+
4 rows in set (0.00 sec)

select * from Customers;
+-------------+-----------+-------------------------------------+--------------+----------+
| customer_id | name      | email                               | house_number | postcode |
+-------------+-----------+-------------------------------------+--------------+----------+
|           1 | McNugget  | noisynugget@wahoooo.com             |           13 | X52 8ZQ  |
|           2 | Shakira   | hipsdontlie@song.com                |           22 | HO12 54T |
|           3 | Spongebob | CirclePants@tv.com                  |           25 | Q35 8GL  |
|           4 | Gary      | SneakySnailWithHighIQ@watchthis.com |            2 | H33 H11  |
|           5 | Jeff      | MyNameJeff@song.co                  |           17 | O36 8CH  |
+-------------+-----------+-------------------------------------+--------------+----------+
5 rows in set (0.00 sec)

mysql> select * from products;  
+------------+---------------------------+-------+-------+
| product_id | title                     | price | stock |
+------------+---------------------------+-------+-------+
|          1 | Goat Simulator            | 43.00 |    35 |
|          2 | Washing Machine Simulator | 12.00 |    59 |
|          3 | Carpet Simulator          |  3.00 |    72 |
|          4 | Simulator Simulator       |  2.00 |    89 |
|          5 | God Mode                  |  1.00 |   100 |
+------------+---------------------------+-------+-------+
5 rows in set (0.00 sec)

mysql> select * from orders;   
+----------+-------------+------------+-------------+
| order_id | customer_id | product_id | date_placed |
+----------+-------------+------------+-------------+
|        1 |           1 |          1 | 2023-07-17  |
|        2 |           4 |          3 | 2023-06-12  |
|        3 |           2 |          4 | 2023-03-01  |
|        4 |           3 |          5 | 2023-05-12  |
|        5 |           5 |          2 | 2023-02-11  |
+----------+-------------+------------+-------------+
5 rows in set (0.00 sec)

mysql> SELECT *
    -> FROM customers
    -> WHERE name='Spongebob';
+-------------+-----------+--------------------+--------------+----------+
| customer_id | name      | email              | house_number | postcode |
+-------------+-----------+--------------------+--------------+----------+
|           3 | Spongebob | CirclePants@tv.com |           25 | Q35 8GL  |
+-------------+-----------+--------------------+--------------+----------+
1 row in set (0.00 sec)