/* 
 * Problem Set 5, MongoDB Programming Problems
 */

/*********************************************************************
 * REMEMBER:
 *  1. For each problem, you should assign your MongoDB method call 
 *     to the variable called "results" that we have provided. 
 *     Follow the model shown in the sample query below.
 *  2. You should *not* make any other additions or modifications to
 *     this file.
 *  3. You should test that the queries in this file are correct by
 *     executing all of the queries in the file from the command line.
 *     See the assignment for more details.
 *********************************************************************/

/* Do not modify the following lines. */
db = db.getSiblingDB('imdb')
function printResults(results) {
    if (results instanceof DBQuery) {
        results.forEach(printjson)
    } else if (Array.isArray(results)) {
	printjson(results)
    } else if (!isNaN(results)) {
        print(results)
    } else {
        printjson(results.result)
    }
}

/*
 * Sample query: Find the names of all movies in the database from 1990.
 */

print()
print("results of sample query")
print("-----------------------")

results0 = db.movies.find( { year: 1990 }, 
                           { name: 1, _id: 0 } )

printResults(results0)


/*
 * Query 1. Put your method call for this query below,
 * assigning it to the results variable that we have provided.
 */

print()
print("results of query 1")
print("------------------")

results1 = db.movies.find( { year: 2000, rating: "PG-13" }, 
                           { name: 1, runtime: 1, _id: 0 } )

printResults(results1)


/*
 * Query 2. Put your method call for this query below,
 * assigning it to the results variable that we have provided.
 */

print()
print("results of query 2")
print("------------------")

results2 = db.people.find( { $or: [ {name: "Regina King"}, {name: "Mahershala Ali"} ] },
			{ name: 1, pob: 1, dob: 1, _id: 0} )

printResults(results2)


/*
 * Query 3. Put your method call for this query below,
 * assigning it to the results variable that we have provided.
 */

print()
print("results of query 3")
print("------------------")

results3 = db.oscars.find(  {type: "BEST-PICTURE", year: {$gte: 1990, $lte: 1999}     }, {year: 1, "movie.name": 1, _id: 0} )

printResults(results3)


/*
 * Query 4. Put your method call for this query below,
 * assigning it to the results variable that we have provided.
 */

print()
print("results of query 4")
print("------------------")

results4 = db.people.find( {pob: /France$/, hasDirected: true},
			{ name: 1, pob: 1, _id: 0} )

printResults(results4)


/*
 * Query 5. Put your method call for this query below,
 * assigning it to the results variable that we have provided.
 */

print()
print("results of query 5")
print("------------------")

results5 = db.movies.aggregate( {$group: { _id: "$rating", average_runtime: {$avg: "$runtime"}  }   } )

printResults(results5)


/*
 * Query 6. Put your method call for this query below,
 * assigning it to the results variable that we have provided.
 */

print()
print("results of query 6")
print("------------------")

results6 = db.movies.aggregate( {$group: { _id: "$rating", average_runtime: {$avg: "$runtime"}  }   }, 
				{$project: { _id: 0, rating: "$_id", average_runtime: "$average_runtime"}	}		)

printResults(results6)


/*
 * Query 7. Put your method call for this query below,
 * assigning it to the results variable that we have provided.
 */

print()
print("results of query 7")
print("------------------")

results7 = db.oscars.aggregate( {$group: { _id: "$movie.name", num_oscars: {$sum: 1}  }   }, 
				{$match: {num_oscars: 4}      }		)

printResults(results7)


/*
 * Query 8. Put your method call for this query below,
 * assigning it to the results variable that we have provided.
 */

print()
print("results of query 8")
print("------------------")

results8 = db.movies.distinct("actors.name", {"directors.name": "Steven Spielberg"})

printResults(results8)


/*
 * Query 9. Put your method call for this query below,
 * assigning it to the results variable that we have provided.
 */

print()
print("results of query 9")
print("------------------")

results9 = db.movies.aggregate( {$match: {genre: /N/}   },
				{$sort:  {runtime: -1}  },
				{$limit: 1},
				{$project: {_id: 0, runtime: "$runtime", longest_animated: "$name"}  } )

printResults(results9)


/*
 * Query 10. Put your method call for this query below,
 * assigning it to the results variable that we have provided.
 */

print()
print("results of query 10")
print("-------------------")

results10 = db.oscars.aggregate({$match: {year: 2003} },
				{$project: {_id: 0, movie: "$movie.name", actor: "$person.name", type: "$type"} })





printResults(results10)
