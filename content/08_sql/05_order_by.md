# ORDER BY 📝

:::{dropdown} Learning Goals
By the end of this section you will:
- know how to sort a query's results
- know how to sort using mulitple fields
:::

## ORDER BY Clause

The SQL `ORDER BY` keyword is used to sort the result set of a query by one or more columns, either in ascending (ASC) or descending (DESC) order.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/uUO-ynRJKo0?si=XKo2mgMZuSKH-3aO" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

:::{tip} Summary
:class: dropdown
 **Sorting in Ascending and Descending Order:** 
 - The `ORDER BY` keyword is used to sort the results of a query. 
 - By default, it sorts the data in ascending order (ASC). 
 - To sort in descending order, you must use the `DESC` keyword. 

 **Sorting Different Data Types:** 
 - **Numerical Data:** When applied to numerical columns like "Price," the clause sorts the values from smallest to largest (ascending) or largest to smallest (descending). 
 - **Text Data:** For text-based columns such as "ProductName," `ORDER BY` will sort the data alphabetically. 

 **Sorting by Multiple Columns:** 
 - You can sort by more than one column to create a more refined, hierarchical sorting of your data. 
 - The data will be sorted based on the first column specified, and then the second column will be used to sort any rows that have the same value in the first column. 

 **Mixing Sort Orders:** 
 -  It is possible to sort one column in ascending order and another in descending order within the same query. To do this, you specify `ASC` or `DESC` after each column name in the `ORDER BY` clause. 

 The video also encourages viewers to visit w3schools.com to practice what they've learned
:::

Go to the [W3schools Tutorial](https://www.w3schools.com/sql/sql_orderby.asp) on the `ORDER BY` Keyword and complete their exercises.

:::{seealso} ORDER BY Activities
:class: dropdown
**Using the Movies database**

1. List all the movies names in ascedning alphabetical order
2. What is the 5 newest movies in stock?
3. Display the movies in chronological order, and then alphabetical order within each year.

**Using the School Database**

4. List the name of the grade 6 students in alphabetical order
5. What is the top three results in percentage
6. List all the boys' birthdays in order, then all the girls' birthdays in order, with their names
:::