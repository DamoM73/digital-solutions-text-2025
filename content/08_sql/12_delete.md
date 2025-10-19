# DELETE 📝

:::{dropdown} Learning Goals
By the end of this section you will:
- know how to delete records from a database
- understand that relational databases require a specific deletion order
- know how to delete data that is contained in mulitple tables.
:::

The `DELETE` statement is used to delete existing records in a table.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/s7ehCYyEmVw?si=qGTF0FEmkkDjh8IF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe><p>&nbsp;</p>

:::{tip} Summary
:class: dropdown
This video provides a tutorial on the SQL `DELETE` statement, explaining how to remove unwanted records from a database table. 

Key points covered in the video include: 

- **`DELETE` Statement Syntax:** The basic syntax is `DELETE FROM table_name WHERE condition;`. The `WHERE` clause is crucial as it specifies which records to delete.

- **Importance of the `WHERE` Clause:** The video strongly emphasizes the importance of the `WHERE` clause. If you omit it, all records in the table will be deleted. This is likened to accidentally deleting all your contacts. 

- **Practical Example:** A demonstration shows how to delete a specific customer, "Alfreds Futterkiste," from a "Customers" table using the `DELETE` statement with a `WHERE` clause. 

- **Deleting All Records:** To clear all data from a table without deleting the table itself, you can use `DELETE FROM Customers;`. This leaves the table structure intact for future use.

- **`DELETE` vs. `DROP TABLE`:** The video clarifies the difference between the `DELETE` and `DROP TABLE` statements. `DELETE` removes records from a table, while `DROP TABLE` permanently removes the entire table and its structure from the database.

The video concludes by advising viewers to always double-check their commands before execution to prevent accidental data loss and encourages them to practice using the interactive editor on w3schools.com.
:::

Go to the [W3schools Tutorial](https://www.w3schools.com/sql/sql_delete.asp) on the DELETE Statement and complete their exercises.

## DELETE order

When deleting data that is stored in multiple tables, the order that entires are deleted is important. You cannot delete an entry where it's primary key is used as a foreign keys in another table, ie. for the one-to-many cardinality, it is on the one side. Therefore, you need to start with the entry that is not associated with a foreign key.

Let's look at the Movies database as an example. 

![movie erd](./assets/moives.png)

Say we wanted to delete **Mel Gibson** from the director database.

- We cannot delete a **Mel Gibson** straight away since there may be movies that have his `dirnumb` (**118**) as a foreign key, so we have delete all movies with the `dirnumb` **118** first.
- But we will not be able to delete the movie, if it is currently onhire. That is, the `movienumb` is in the **movies_onhire** table. Therefore, we need to delete any record of **Mel Gibson** movies from the **movies_onhire** table. 
- We do not need to be worried about member nubmers as the `memberid` is on the many side to the one-to-many relationship.

### The steps that need to be taken are

1. Delete any records involving **Mel Gibson** movies from the **movies_onhire** table

```{literalinclude} ./assets/delete_example_step_1.sql
:language: sql
```

2. Delete any movies from the movies table that have **Mel Gibson** as the director

```{literalinclude} ./assets/delete_example_step_2.sql
:language: sql
```

3. Finally delete **Mel Gibson** from the director table

```{literalinclude} ./assets/delete_example_step_3.sql
:language: sql
```

:::{seealso} DELETE Activities
:class: dropdown
**School Database**

1. Delete all results where percent is under 50
2. Delete all results for students born before 2000

**Repairs Database**

3. Delete all repairs that are already ready on 2010‑06‑03
4. Delete all repairs done by technicians with the grade apprentice

**Chinoook Database**

5. Delete all customers and their invoices from Brazil
6. Delete an artist and all related data (tracks, playlist entries, albums) for 'Queen'
:::