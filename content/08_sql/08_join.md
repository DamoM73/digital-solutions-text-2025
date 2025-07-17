# JOIN

Joins are used in SQL to combine rows from two or more tables based on a related column between them. Instead of writing multiple subqueries, joins let you pull data from different tables into a single result. This is helpful when related information is stored across separate tables, such as customers and their orders. By using joins, you can view and analyse all the connected data in one query result.

Go to the [W3schools Tutorial](https://www.w3schools.com/sql/sql_join.asp) on Joins and complete their exercises (we will only be worried about inner joins)

## The JOIN Clause

The SQLite JOIN clause is used to combine rows from two or more tables based on a related column they share. Go to the [W3schools Tutorial](https://www.w3schools.com/sql/sql_join_inner.asp) on the `INNER JOIN` Keyword and complete their exercises. Note, in SQLite we can just use **JOIN** in place of INNER JOIN.

:::{hint} Creating JOINS
1. Start by thinking about the exact data you want to display in your results
2. Work out which tables contain that data
3. Identify how those tables are linked using common columns (like IDs)
4. Use `SELECT` to choose the columns you need from each table using their full name (`table.field`)
5. Start your query with `FROM` table1 (table1 is the table where most of the data you want to display comes from.)
6. Add `JOIN` for each additional table using `ON tableX.column = tableY.column` to connect them
7. Run the query and check the results show all the required information correctly
:::

:::{seealso} JOIN Activities
:class: dropdown
**Using Repairs database**
1. List all job numbers and the name of the technian assigned to it.
2. List all technicians and what they are qualified in.
3. Create a job listing which lists the job number, technician name, type, owner and whether it is ready. Sort the listing to the ready devices are first.
4. Create an invoice listing that, for each finished repair shows the job number, the owner, the type, the time the repair took and the cost (time * rate).

**Using the Chinook database**

5. List all albums, including artist name, sorted by artist name.
6. List the name, and only the name, of all the tacks that are in some form of metal genre.
7. List the details of all Def Leppard tracks (Name, album name, genre name, composer, length in seconds, and unit price).

**Using the Schools database**

8. List all students and the subject results (name, subject name and percent)
9. What is the gender breakdown for each subject?
10. What is the average percentage of students results for each teacher?
:::