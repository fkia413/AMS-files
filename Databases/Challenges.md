List all actors. SELECT * FROM actor;    
Find the surname of the actor with the forename 'John'. SELECT last_name FROM actor WHERE first_name='John';  
Find all actors with surname 'Neeson'. SELECT * FROM actor WHERE last_name='Neeson';  
Find all actors with ID numbers divisible by 10. SELECT * FROM actor WHERE (actor_id % 4) =0;  
What is the description of the movie with an ID of 100? SELECT description FROM film  WHERE film_id=100;  
Find every R-rated movie. SELECT * FROM film WHERE rating='R';   
Find every non-R-rated movie. SELECT * FROM film WHERE rating!='R';  
Find the ten shortest movies. SELECT * FROM film ORDER BY length DESC LIMIT 10;  
Find the movies with the longest runtime, without using LIMIT. SELECT * FROM film ORDER BY length ASC;  
Find all movies that have deleted scenes. SELECT * FROM film WHERE special_features='Deleted Scenes';  
Using HAVING, reverse-alphabetically list the last names that are not repeated. SELECT last_name FROM actor GROUP BY last_name HAVING count(last_name)=1 ORDER BY last_name DESC;  
Using HAVING, list the last names that appear more than once, from highest to lowest frequency. SELECT last_name, COUNT(*) FROM actor GROUP BY last_name HAVING COUNT(last_name)>1;   
Which actor has appeared in the most films? SELECT actor_id, COUNT(*) as frequency FROM film_actor GROUP BY actor_id HAVING COUNT(actor_id)>5 ORDER BY COUNT(*) DESC;  
When is 'Academy Dinosaur' due? SELECT (film_id) FROM film WHERE title='Academy Dinosaur'; SELECT (inventory_id) FROM inventory WHERE film_id=1;  SELECT (return_date) FROM rental WHERE inventory_id=1;  
**What is the average runtime of all films?** this is where I got up to Leon, I ran behind a moving car and now I'm **exhausted** HAHA HA ...  
List the average runtime for every film category.
List all movies featuring a robot.
How many movies were released in 2010?
Find the titles of all the horror movies.
List the full name of the staff member with the ID of 2.
List all the movies that Fred Costner has appeared in.
How many distinct countries are there?
List the name of every language in reverse-alphabetical order.
List the full names of every actor whose surname ends with '-son' in alphabetical order by their forename.
Which category contains the most films?