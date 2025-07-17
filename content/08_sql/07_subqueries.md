# Subqueries

:::{dropdown} Learning Goals
By the end of this section you will:
- understand that query results can be used as the basis for further queries.
- know how to create subqueries to interrogate data across multiple tables.
:::

All SQL queries return a result in the form of a table, and this result table can be used as the basis for another query—this is called a subquery. Subqueries allow you to build more complex logic by using the output of one query as input for another.

## The `IN` Operator

The SQL `IN` operator is used to check if a value matches any value in a list or the result of a subquery. Go to the [W3schools Tutorial](https://www.w3schools.com/sql/sql_in.asp) on the `IN` Operator and complete their exercises.

:::{hint} Writing Subqueries
1. Identify the final result you want:
   - what fields do you want to display indicates the table
   - this becomes the **outer query**
2. Determine what data or filtering is needed to get to that result:
   - the field will appear in the **outer query** `WHERE` clause is your filter
   - the **inner query** needs to return a table consisting of this field
3. The **inner query** provides values for the **outer query**
4. Write the **inner query** first to ensure it returns the correct data
5. Place the **inner query** in parentheses and then write it into the `WHERE` clause of the **outer query**.
   - Make sure the data type and structure of the **inner query** matches what the **outer query** expects
6. Test both queries separately if needed, then combine and run the full subquery structure
:::

Note that subqueries can be endlessly nested.

:::{seealso} Subqueries Activities
:class: dropdown
**Using the Schools database**

1. What are all the percentage results for all the students in grade 7
2. What the subject name of the subject taught by the teacher in room A2?
3. What is the name of the subjects where students score over 90%?
4. List the names of all students who do science.
5. List the names of the students in grades 4 or 5 who scored over 50% for language.

**Repairs database**

6. Who owns devices being repaired by Ted Carrol?
7. What are the names of the technicians who are still not expert (N) at repairing Macs?
8. What rate will Byrne be charged for repairs?
9. List the owners whose devices have a high (H) priority for repair.
10.  What level of qualification has the technician who is doing James' repair job?
:::
