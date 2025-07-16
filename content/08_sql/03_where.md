# WHERE

:::{dropdown} Learning Goals
By the end of this section you will:
:::

## WHERE Clause

The SQL `WHERE` clause is used to filter records in a database query to include only those that meet specified conditions.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/L9GBpVXq-zc?si=3pLlpAYuJSFaRtZe" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

:::{tip} Summary
:class: dropdown
- **Core Function**: The WHERE clause is used to extract only those records that fulfill a specified condition. It acts like a filter, allowing you to narrow down your results from a larger dataset.
Versatility: The video emphasizes that the WHERE clause is not limited to SELECT statements. It is a fundamental part of other crucial SQL commands like UPDATE and DELETE, enabling you to specify which rows to modify or remove. It's described as a "Swiss Army knife" for SQL queries.
- **Basic Syntax**: The general structure for using the clause is:
`SELECT column1, column2, ... FROM table_name WHERE condition;`
- **Filtering Different Data Types**:
    - **Text Fields**: When filtering based on text values (like a country name), the value must be enclosed in single quotes. For example: WHERE Country = 'Mexico'.
    - **Numeric Fields**: Numeric values do not require quotes. For example: WHERE CustomerID = 1.
- **Using Operators**: The WHERE clause can be used with a variety of operators to create precise filtering conditions. The video lists the following common operators:
    - `=` (Equal)
    - `>` (Greater than)
    - `<` (Less than)
    - `>=` (Greater than or equal)
    - `<=` (Less than or equal)
    - `<>` or `!=` (Not equal)
    - `BETWEEN` (Within a certain range)
    - `LIKE` (Search for a pattern)
    - `IN` (To specify multiple possible values for a column)

The video uses practical examples from a "Customers" table to illustrate how to apply these concepts, making it clear and easy to follow.
:::

Go to the [W3schools Tutorial](https://www.w3schools.com/sql/sql_where.asp) on the `WHERE` clause and complete their exercises.

## AND Operator

The SQL `AND` operator is used to filter records by returning only rows where all specified conditions are true.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/r1V39Iia4j0?si=xls49MU7D0cKXz9X" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

:::{tip} Summary
:class: dropdown
The video provides a tutorial on using the AND operator in SQL to filter records based on multiple conditions.
**Key Concepts**
- **Purpose**: The AND operator is used in the WHERE clause to filter results from a query, ensuring that all specified conditions are met.
- **Syntax**:

```{code} sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;
```

- **Functionality**: For a record to be included in the result set, every condition linked by the AND operator must be true.

**Examples from the video**

Selecting Customers from Spain with a name starting with 'G':

```{code} sql
SELECT * FROM Customers
WHERE Country = 'Spain'
AND CustomerName LIKE 'G%';
```

Selecting Customers from Germany, in Berlin, with a Postal Code greater than 12000:

```{code} sql
SELECT * FROM Customers
WHERE Country = 'Germany'
AND City = 'Berlin'
AND PostalCode > '12000';
```

**Combining AND and OR**
The video also demonstrates how to combine AND and OR operators. It emphasizes the importance of using parentheses () to group conditions and ensure the logic is evaluated correctly.

Example with parentheses (correct logic): This query finds customers from Spain whose names start with either 'G' or 'R'.

```{code} sql
SELECT * FROM Customers
WHERE Country = 'Spain'
AND (CustomerName LIKE 'G%' OR CustomerName LIKE 'R%');
```

Example without parentheses (incorrect logic): Without parentheses, the query would return all customers from Spain whose names start with 'G', plus all customers from any country whose names start with 'R'.

```{code} sql
SELECT * FROM Customers
WHERE Country = 'Spain'
AND CustomerName LIKE 'G%' OR CustomerName LIKE 'R%';
```

**AND vs. OR Operator**
**AND**: Displays a record if ALL conditions are true.
**OR**: Displays a record if ANY of the conditions are true.
The video concludes by encouraging viewers to practice using these concepts on the W3Schools website.
:::

Go to the [W3schools Tutorial](https://www.w3schools.com/sql/sql_and_or.asp) on the `AND`, `OR` and `NOT` operators and complete their exercises.

## LIKE Operator

Go to the [W3schools Tutorial](https://www.w3schools.com/sql/sql_like.asp) on the `LIKE` operator and complete their exercises.

## NULL Values

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/RKUYYrmv6gw?si=vPVPaoz6SaqoCyjf" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

:::{tip} Summary
:class: dropdown
This video from W3Schools provides a clear and concise explanation of NULL values in SQL. Here's a summary of the key points covered:
- **What is a NULL value?** A NULL value in an SQL table represents a field with no value. It's essentially an empty or unknown value, different from a zero or a space. It signifies that the data for that particular field is missing.
- **How to handle NULL values**: When a field in a table is optional, you can insert or update a record without providing a value for that field. In such cases, SQL automatically assigns a NULL value to it.
- **Querying for NULL values**: To find records with NULL values, you cannot use standard comparison operators like '=' or '<>'. Instead, you must use the IS NULL operator in your WHERE clause.
- **Querying for non-NULL values**: Conversely, to find records where a field has a value (i.e., is not NULL), you should use the IS NOT NULL operator.
- 
The video emphasizes that mastering the use of IS NULL and IS NOT NULL is crucial for effectively managing and querying data in SQL databases where some information might be incomplete.
:::

Go to the - [W3schools Tutorial](https://www.w3schools.com/sql/sql_null_values.asp) on `NULL` values and complete their exercises.

:::{seealso} WHERE Activities
:class: dropdown
**Using the Movies database**

1. Display the name of all the US directors
2. Display the name of the all non-US directors
3. Display the name of all the members who owe money
4. Display all the movies that have 'the' in their title
5. Display all the movies that start with Z

**Using the Repairs database**

6. List the owners whose repair is ready to collect
7. List the owners whose iMac is still being repaired

**Using the World database**

8. Which countries have not achieved independence but still have a capital
9. List all details of countries that are missing information?
10. List countries that are either constitutional monarchies or republics
:::