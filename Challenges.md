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
Using HAVING, reverse-alphabetically list the last names that are not repeated.
Using HAVING, list the last names that appear more than once, from highest to lowest frequency.
Which actor has appeared in the most films?
When is 'Academy Dinosaur' due?
What is the average runtime of all films?
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