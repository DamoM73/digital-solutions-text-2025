# INSERT

:::{dropdown} Learning Goals
By the end of this section you will:
- understand that the INSERT INTO statement is used to add rows of data to an SQL table.
- know how to add new data to an SQL table that does not have an autoincrement primary key
- know how to add new data to an SQL table that does have an autoincrement primary key
- know how to add data that spans mutiple tables
:::

## INSERT INTO Statement

The `INSERT INTO` statement in SQL is used to add new rows of data into a table.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Dndsh1dcx-U?si=KChEUSIMwcNLoS9l" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe><p>&nbsp</p>

:::{tip} Summary
:class: dropdown
This video provides a tutorial on using the SQL `INSERT INTO` statement, a fundamental command for adding new records to a database table.

There are two primary ways to structure the `INSERT INTO` statement:

- **Specifying both column names and values:** This is the recommended method as it ensures the correct values are inserted into the intended columns. The syntax is:
    `INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);`

- **Providing only the values:** This is a shorter method, but it requires the values to be in the same order as the columns in the database table. The syntax is:
    `INSERT INTO table_name VALUES (value1, value2, ...);`

The video also demonstrates the following:

- **Inserting data into specific columns:** You can insert data into select columns, and the remaining columns will be populated with default values or `NULL`.
- **Auto-incrementing fields:** When a table has an auto-incrementing primary key, such as a `CustomerID`, you don't need to provide a value for that column, as it will be generated automatically.
- **Inserting multiple records at once:** You can add multiple rows with a single `INSERT INTO` statement by separating each set of values with a comma. This is more efficient than writing individual `INSERT` statements for each record.
:::

Go to the [W3schools Tutorial](https://www.w3schools.com/sql/sql_insert.asp) on the INSERT Statement and complete their exercises.

:::{seealso} INSERT INTO Activities
:class: dropdown
**Movies Database**

1. Insert a new movie **The Year of Living Dangerously** with movie number **1047**, run time of **115** and director number **135**, released in the year **1982**.
2. Add a new member named **Emma Stone**, from **Scottsdale, Arizona**. The last membership number in the database is 5064.

**School Database**

3. Insert a new teacher named **Carter, N**, who teaches **Grade 9** in Room **B4**.
4. Add a new result for student number **2230**, subject number **17**, **50** percent.
5. Add a new subject (no. **19**) called **digital technologies**, taught by **Carter, N**

**Chinook Database**

6. Insert a new artist named **Imagine Dragons**.
7. Insert an album titled **Evolve** by Imagine Dragons. Assume their ArtistId is **276**.
8. Insert a customer named **Zara Lee**, company **ZaraTech**, in **Brisbane**. Email is **zlee@example.com**. Assume SupportRepId is **3**.
9. Create a playlist called **Study Beats**, then add the track with TrackId **3456** to the playlist.
10. Insert data about an invoice involving a new customer named **Leo Tran** who works from **TranTech** in **Melbourne**, with email of **leo.tran@example.com**. The invoice was created by support rep **4** for the amount costing **39.95**.
:::