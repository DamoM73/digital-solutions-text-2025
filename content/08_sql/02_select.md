# SELECT Statement

:::{dropdown} Learning Goals
- know how to execute simple SQL SELECT commands.
- know how to execute simple SQL SELECT commands that only return the unique values.
:::

## SELECT

The SQL `SELECT` statement is used to retrieve specific data from tables within a relational database. The data is return in the form of a table.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/af4LckivJT8?si=s2x0uVst8VPKIzGn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

:::{tip} Summary
:class: dropdown
This video provides a basic tutorial on the SQL SELECT statement, presented by W3Schools. Here’s a breakdown of the key points:

- **Purpose of SELECT**: The SELECT statement is used to retrieve or "select" data from a database. The video likens it to using tongs to pick specific candies from a jar.
- **Selecting Specific Columns**: You can choose which columns of data you want to see.
  - **Syntax**: SELECT column1, column2, ... FROM table_name;
  - **Example**: The video demonstrates how to select the CustomerName and City columns from a table named Customers with the query: SELECT CustomerName, City FROM Customers;.
- **Selecting All Columns**: To retrieve all columns from a table without listing each one, you can use the asterisk (*) wildcard.
  - **Syntax**: SELECT * FROM table_name;
  - **Example**: The query SELECT * FROM Customers; is used to display all data from every column in the Customers table.

The video uses a sample "Customers" table to visually demonstrate how these queries work and what the resulting output looks like. It concludes by encouraging viewers to practice using the interactive editor on w3schools.com.
:::

Go to the [W3schools Tutorial](https://www.w3schools.com/sql/sql_select.asp) on the `SELECT` statement, and complete their exercises.

## SELECT DISTINCT

The `SELECT DISTINCT` statement is used in SQL to return only unique (non-duplicate) values from a column or combination of columns in a query result.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/yuYKEx6VDPE?si=8ySchkLXQEdiD6Wl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

:::{tip} Summary
:class: dropdown
- **Purpose of `SELECT DISTINCT`**: The statement is used to filter out duplicate rows from a query result, returning only a unique set of values. The video uses the analogy of picking out only the unique crayon colors from a large, mixed box.

- **Syntax**: The basic syntax is `SELECT DISTINCT column_name FROM table_name;`. This query will return a list of all unique values from the specified column in the given table.

- **Example**: Using a sample `Customers` table, the video demonstrates that a simple `SELECT Country FROM Customers;` query would list the country for every single customer, including many duplicates (e.g., "Mexico" appearing multiple times). By using `SELECT DISTINCT Country FROM Customers;`, the query returns a clean list where each country appears only once.

- **Counting Distinct Values**: The video also shows how to count the number of unique values using `COUNT(DISTINCT column_name)`.
    - The query `SELECT COUNT(DISTINCT Country) FROM Customers;` returns the total number of unique countries in the table.

- **MS Access Workaround**: It is noted that Microsoft Access does not support the `COUNT(DISTINCT)` syntax. A workaround is provided using a subquery: `SELECT Count(*) FROM (SELECT DISTINCT Country FROM Customers);`.
:::

Go to the [W3schools Tutorial](https://www.w3schools.com/sql/sql_distinct.asp) on the `SELECT DISTINCT` statement and complete their exercises.

:::{seealso} SELECT Activities
:class: dropdown
Using the **Movies** database:

1. Display the name of all the directors
2. Display the name of all the members
3. Display all the details in the movie table
4. Display all the years of release with no duplications
5. Display the number of all movies on hire and when they are due back
:::