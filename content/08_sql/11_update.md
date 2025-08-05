# UPDATE

:::{dropdown} Learning Goals
By the end of this section you will:
:::

The `UPDATE` statement is used to modify the existing records in a table.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/i5aGjhTluxo?si=yf5DZ03PHWuh53K_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe><p>&nbsp;</p>

:::{tip} Summary
:class: dropdown
This video from W3Schools provides a tutorial on the SQL `UPDATE` statement, an essential tool for modifying existing records in a database.

A breakdown of the key concepts covered:
- **Functionality**: The `UPDATE` statement is used to change data in a table. For instance, if a customer's contact information changes, this command allows you to update their record.
- **Syntax**: The basic structure of the command is:
```{code}SQL
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```
- **Single and Multiple Record Updates**L You can modify a single record by specifying a unique identifier in the ``WHERE`` clause. To update multiple records, you can use a broader condition in the `WHERE` clause. For example, you could change the contact name for all customers in a specific country.
- **The Importance of the `WHERE` Clause**: The video strongly emphasizes the need to be careful with the `WHERE` clause. If you omit it, the `UPDATE` statement will modify every single record in the table, which could lead to unintended data loss. It's recommended to first run a `SELECT` query with the same `WHERE` condition to verify which rows will be affected before executing the `UPDATE`.
:::

Go to the [W3schools Tutorial](https://www.w3schools.com/sql/sql_update.asp) on the UPDATE Statement and complete their exercises.

:::{seealso} UPDATE Statement Activities
:class: dropdown
**World Database**

1. The city **Brisbane** has had a recent **population** update. Change its population to **2780063**.
2. The city **Bombay** was renamed. Update its name to **Mumbai**.
3. The percentage of **Spanish** speakers in **ESP** (Spain) was incorrectly recorded. Change it to **92.0**

**Shares Database**

4. Update the long name of the **Computer** industry (Code 3573) to **Computer Hardware & Peripherals**.
5. The client **Debra Parker**, born on **1957-10-10**, has moved to **Brisbane**. Update her city.
6. Reduce the **PurPrice** by **10%** for the holding with the most recent PurDate.

**Chinook Database**

7. Set support rep to **Jane Peacock** for all **Brazilian** customers
8. Increase unit price by **0.20** for all **Rock** tracks
:::