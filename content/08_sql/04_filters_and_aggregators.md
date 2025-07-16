# Filters and Aggregators

:::{dropdown} Learning Goals
By the end of this section you will:
- know how to use the `LIMIT` clause to restrict the number of rows returned
- know how to use `MAX` and `MIN` to return the highest and lowest values in a field
- know how to aggregate values of a column using `COUNT`, `AVG` and `SUM`
:::

SQL filter clauses are used to restrict the number of rows returned by a query based on specified conditions, enabling more precise data retrieval and manipulation. While SQL aggregators are functions used to perform calculations on multiple rows of a table's column and return a single value.

## LIMIT Clause

The `LIMIT` clause in SQL is used to specify the maximum number of rows that a query should return.

Go to the [W3schools Tutorial](https://www.w3schools.com/sql/sql_top.asp) on the `TOP`, `LIMIT`, `FETCH FIRST` or `ROWNUM` Clauses. **Only** do the exercise for the `LIMIT` clause.

## MAX and MIN Functions

The `MAX` function returns the highest value in a column, while the `MIN` function returns the lowest value in a column.

Go to the [W3schools Tutorial](https://www.w3schools.com/sql/sql_min_max.asp) on the `MIN()` and `MAX()` functions and complete their exercises.

## COUNT, AVG and SUM Functions

The `COUNT` function returns the number of rows, `AVG` calculates the average of numeric values, and `SUM` adds up all the numeric values in a column.

[W3schools Tutorial](https://www.w3schools.com/sql/sql_count_avg_sum.asp) on the `COUNT`, `AVG` and `SUM` Functions and complete their exercises.

:::{seealso} Filters and Aggregators Activities
:class: dropdown
**Using the Movies database**

- How many directors are there from Australia?
- How many directors have the name John?
- What is the longest movie?
- If I was to watch all the movies, back-to-back, how many minutes will I need (no pausing for toilet stops)

**Using the Repairs database**

- What is the average repair rate?
- How many repairs are waiting to be picked up?

**Using the Shares database**

- How many companies are there in the high risk category?
- Which company has the biggest difference between their highest and lowest price?
- What is the cheapest, medium or low risk share on the New York Stock Exchange?
- List all shares that are currently within 10% of their highest price?
:::