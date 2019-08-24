#
# CS 460: Problem Set 1, SQL Programming Problems
#

#
# For each problem, use a text editor to add the appropriate SQL
# command between the triple quotes provided for that problem's variable.
#
# For example, here is how you would include a query that finds the
# names and years of all movies in the database with an R rating:
#
sample = """
    SELECT name, year
    FROM Movie
    WHERE rating = 'R';
"""

#
# Problem 4. Put your SQL command between the triple quotes found below.
#
problem4 = """
SELECT name, pob, dob
FROM Person
WHERE name = 'Emma Stone' OR name = 'Rachel Weisz';
"""

#
# Problem 5. Put your SQL command between the triple quotes found below.
#
problem5 = """
SELECT COUNT(id)
FROM Movie
WHERE runtime > 200;
"""

#
# Problem 6. Put your SQL command between the triple quotes found below.
#
problem6 = """
SELECT M.name, O.type, O.year
FROM Person AS P, Oscar AS O, Movie AS M
WHERE P.name = 'Christian Bale' 
	AND P.id = O.person_id
	AND M.id = O.movie_id;
"""

#
# Problem 7. Put your SQL command between the triple quotes found below.
#
problem7 = """
SELECT COUNT(DISTINCT D.director_id)
FROM Director D, Actor A, Person P, Person G
WHERE D.director_id = P.id AND 
	P.pob NOT LIKE '%USA' AND 
	A.actor_id = G.id AND
	G.pob NOT LIKE '%USA' AND
	D.movie_id = A.movie_id;
"""

#
# Problem 8. Put your SQL command between the triple quotes found below.
#
problem8 = """
SELECT DISTINCT M.year, AVG(M.runtime)
FROM Movie M
GROUP BY M.year
HAVING M.year > 1999;
"""

#
# Problem 9. Put your SQL command between the triple quotes found below.
#
problem9 = """
SELECT P.name, P.dob
FROM Person P
WHERE P.name LIKE 'Sam %';    
"""

#
# Problem 10. Put your SQL command between the triple quotes found below.
#
problem10 = """
SELECT M.name
FROM Movie M
WHERE M.runtime <(SELECT MIN(W.runtime)
					FROM Movie W, Oscar U
					WHERE W.id = U.movie_id
						AND U.type = 'BEST-PICTURE');        
"""

#
# Problem 11. Put your SQL command between the triple quotes found below.
#
problem11 = """
SELECT P.name, COUNT(D.director_id)
FROM Person P, Director D, Movie M
WHERE P.id = D.director_id
	AND D.movie_id = M.id
	AND M.earnings_rank < 201
GROUP BY D.director_id
HAVING COUNT(D.director_id) > 3
ORDER BY COUNT(D.director_id) DESC;
"""

#
# Problem 12. Put your SQL command between the triple quotes found below.
#
problem12 = """
SELECT M.earnings_rank, M.name, COUNT(O.type)
FROM Movie M LEFT OUTER JOIN Oscar O 
	ON M.id = O.movie_id
WHERE M.earnings_rank < 26
GROUP BY M.name
ORDER BY M.earnings_rank;
"""

#
# Problem 13. Put your SQL command between the triple quotes found below.
#
problem13 = """
SELECT COUNT(DISTINCT B.actor_id)
FROM Actor B
WHERE B.actor_id NOT IN (SELECT DISTINCT A.actor_id
						FROM Actor A, Movie M
						WHERE A.movie_id = M.id
						AND M.earnings_rank < 200);
           
"""

#
# Problem 14. Put your SQL command between the triple quotes found below.
# So far
problem14 = """
SELECT M.name AS 'movie', 'director' AS 'function'
FROM Person P, Director D, Movie M
WHERE D.director_id = P.id AND P.name = 'Denzel Washington' AND D.movie_id = M.id
UNION 
SELECT N.name AS 'movie', 'actor' AS 'function'
FROM Person Q, Actor B, Movie N
WHERE B.actor_id = Q.id AND Q.name = 'Denzel Washington' AND B.movie_id = N.id
ORDER BY M.name;
"""

#
# Problem 15. Put your SQL command between the triple quotes found below.
#
problem15 = """
SELECT M.name, O.year
FROM Movie M, Oscar O
WHERE M.id = O.movie_id
	AND O.type = 'BEST-PICTURE'
	AND M.year = (SELECT MAX(N.year)
		FROM Movie N, Oscar P
		WHERE N.id = P.movie_id
			AND P.type = 'BEST-PICTURE'
			AND N.rating = 'G');     
"""

#
# Problem 16. Put your SQL command between the triple quotes found below.
#
problem16 = """
UPDATE Movie
SET rating = 'PG-13'
WHERE name = 'Indiana Jones and the Temple of Doom'
"""
