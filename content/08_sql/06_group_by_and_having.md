# GROUP BY and HAVING

:::{dropdown} Learning Goals
By the end of this section you will:
:::

## GROUP BY Clause

The SQL `GROUP BY` statement is used to group rows that have the same values in specified columns into summary rows, often in conjunction with aggregate functions to perform calculations on each group. While the SQL HAVING statement is used to filter groups of rows created by the `GROUP BY` clause based on specified conditions, typically involving aggregate functions.

Go to the [W3schools Tutorial](https://www.w3schools.com/sql/sql_groupby.asp) on the `GROUP BY` Statement and complete thier exercises.

## HAVING Clause

The `HAVING` clause is used to filter groups of records created by the `GROUP BY` clause based on a specified condition.

Go to the [W3schools Tutorial](https://www.w3schools.com/sql/sql_having.asp) on the `HAVING` Clause and complete their exercises.

:::{seealso} GROUP BY and HAVING Activities
:class: dropdown
**Using the Movies database**

1. How many directors are there from each country?
2. How many movies does each member number have on hire?
3. How many movies are stocked from each year?

**Using the School database**

4. What is the average result for each subject(code)?
5. How many boys and girls in each grade?

**Using the Shares database**

6. How many companies are there in each risk category?
7. What is the cheapest, medium risk and cheapest low risk share on the New York Stock Exchange?

**Using the Chinook database**

8. How many customers are there from each country with more than one customer?
9. What are the AlbumIds of all ablums that run for more than an hour (3600 secs)?
10. Provide an alphabetical list of countries and total sales if their sales where over $100
:::