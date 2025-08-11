# DELETE

:::{dropdown} Learning Goals
By the end of this section you will:
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

:::{seealso} DELETE Activities
:class: dropdown
**School Database**

1. Delete all results where percent is under 50
2. Delete all results for students born before 2000

**Repairs Database**

3. Delete all repairs that are already ready on 2010‑06‑03
4. Delete all repairs done by technicians with the grade apprentice


:::