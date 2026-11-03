# SQLite3 - Updating and Deleting

:::{dropdown} Learning Goals
By the end of this section you will:
- know how to run parameterised `UPDATE` statements in Python using `sqlite3`
- know how to run parameterised `DELETE` statements in Python using `sqlite3`
- understand why changes must be saved with `commit()`
- know how to use `rowcount` to check how many rows were changed
:::

In [SQLite3 - Reading](./06_queries.md) we used our **Datastore** class to read data with `SELECT`. Now we'll add methods that change data with `UPDATE` and remove data with `DELETE`. We'll keep using **chinook.db**, the music store database.

We already know how these statements work from the [UPDATE](../08_sql/11_update.md) and [DELETE](../08_sql/12_delete.md) pages in SQL Skills. The new parts are saving our changes and checking what changed.

:::{danger} Back up chinook.db first
:class: dropdown
`UPDATE` and `DELETE` change the database file permanently. Before we start:

1. select **chinook.db** in our **data** folder
2. press **Ctrl/Cmd** + **C** to copy, then **Ctrl/Cmd** + **V** to paste
3. we should now have a **chinook copy.db** file as well as **chinook.db**

To get the original data back at any time, delete **chinook.db** and rename **chinook copy.db** to **chinook.db** (then make a new copy).
:::

## Saving changes with commit

When we run an `UPDATE` or `DELETE`, `sqlite3` doesn't write the change to the database file straight away. It holds the change in a **transaction** until we call `commit()` on the connection. If our program ends, or we close the connection, without calling `commit()`, the change is thrown away.

So every method that changes data follows this pattern:

1. execute the SQL statement
2. save the changes with `self.connection.commit()`
3. return the number of rows that changed

`SELECT` statements don't change anything, so our get methods don't need `commit()`.

## Updating data

Below is our **datastore.py** with a get method from the Reading page and two new update methods. Replace the code in **datastore.py** with the code below.

```{code} python
:linenos:
import sqlite3


class Datastore:

    def __init__(self):
        self.connection = sqlite3.connect("data/chinook.db")
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    # --- GET METHODS

    def get_customer_contact(self, customer_id: int):
        # Execute SQL Statement
        self.cursor.execute(
            """
            SELECT FirstName, LastName, Email, Phone
            FROM customers
            WHERE CustomerId = :customer_id
            """,
            {
                "customer_id": customer_id
            }
        )

        # Retrieve Results
        results = self.cursor.fetchall()

        # Return Results
        return results

    # --- UPDATE METHODS

    def update_customer_email(self, customer_id: int, email: str) -> int:
        # Execute SQL Statement
        self.cursor.execute(
            """
            UPDATE customers
            SET Email = :email
            WHERE CustomerId = :customer_id
            """,
            {
                "email": email,
                "customer_id": customer_id
            }
        )

        # Save Changes
        self.connection.commit()

        # Return Number of Rows Changed
        return self.cursor.rowcount

    def update_genre_price(self, genre_name: str, price: float) -> int:
        # Execute SQL Statement
        self.cursor.execute(
            """
            UPDATE tracks
            SET UnitPrice = :price
            WHERE GenreId = (
                SELECT GenreId
                FROM genres
                WHERE Name = :genre_name
            )
            """,
            {
                "price": price,
                "genre_name": genre_name
            }
        )

        # Save Changes
        self.connection.commit()

        # Return Number of Rows Changed
        return self.cursor.rowcount
```

:::{important} Explanation of Code
:class: dropdown
- **lines 15&ndash;32** &rarr; the `get_customer_contact()` method from the Reading page, so we can check our changes
- **line 36** &rarr; the method takes the customer to change and their new email. `-> int` says it returns a whole number: how many rows changed
- **lines 38&ndash;48** &rarr; the `UPDATE` statement with two named placeholders, `:email` and `:customer_id`. The dictionary gives the value for each placeholder
- **line 42** &rarr; `WHERE` limits the change to one customer. `CustomerId` is the primary key, so at most one row can match
- **line 51** &rarr; `commit()` saves the change to the database file
- **line 54** &rarr; `rowcount` is the number of rows the last statement changed
- **lines 56&ndash;78** &rarr; changes the price of every track in a genre. The genre is chosen by name, so a **subquery** (lines 62&ndash;66) looks up its `GenreId`, just like on the [Subqueries](../08_sql/07_subqueries.md) page
:::

### Testing an update

Create a new file, add the code below and save it as ***test.py***.

```{code} python
:linenos:
from datastore import Datastore

database = Datastore()

print(database.get_customer_contact(55))

changed = database.update_customer_email(55, "mark.taylor@example.com.au")
print(f"Rows changed: {changed}")

print(database.get_customer_contact(55))

database.close()
```

:::{important} Explanation of Code
:class: dropdown
- **line 5** &rarr; prints customer 55's details before the change
- **line 7** &rarr; updates the email and stores the number of rows changed
- **line 10** &rarr; prints the details again to check the change
- **line 12** &rarr; closes the connection to the database
:::

Output:

```{code} text
[('Mark', 'Taylor', 'mark.taylor@yahoo.au', '+61 (02) 9332 3633')]
Rows changed: 1
[('Mark', 'Taylor', 'mark.taylor@example.com.au', '+61 (02) 9332 3633')]
```

### Checking rowcount

`rowcount` tells us whether our `WHERE` clause matched what we expected. Let's change ***test.py*** to update the prices of two genres:

```{code} python
:linenos:
from datastore import Datastore

database = Datastore()

changed = database.update_genre_price("Rock And Roll", 1.29)
print(f"Rock And Roll tracks changed: {changed}")

changed = database.update_genre_price("Polka", 1.29)
print(f"Polka tracks changed: {changed}")

database.close()
```

Output:

```{code} text
Rock And Roll tracks changed: 12
Polka tracks changed: 0
```

There are 12 Rock And Roll tracks, so 12 rows changed. There is no Polka genre in the database, so nothing matched and **no error** was raised. The `UPDATE` just changed 0 rows. Without checking `rowcount`, our program would carry on as if the update had worked.

:::{warning} Always include WHERE
:class: dropdown
An `UPDATE` without a `WHERE` clause changes **every** row in the table. If line 42 of **datastore.py** were left out, `update_customer_email()` would give all 59 customers the same email address, and `rowcount` would be 59.

When an update or delete method returns a `rowcount` much larger than expected, check the `WHERE` clause.
:::

## Deleting data

Add the code below to the bottom of the `Datastore` class in **datastore.py**.

```{code} python
:linenos:
:lineno-start: 80
    # --- DELETE METHODS

    def delete_playlist(self, playlist_id: int) -> int:
        # Execute SQL Statement
        self.cursor.execute(
            """
            DELETE FROM playlists
            WHERE PlaylistId = :playlist_id
            """,
            {
                "playlist_id": playlist_id
            }
        )

        # Save Changes
        self.connection.commit()

        # Return Number of Rows Deleted
        return self.cursor.rowcount
```

:::{important} Explanation of Code
:class: dropdown
- **line 82** &rarr; the method takes the id of the playlist to delete and returns the number of rows deleted
- **lines 86&ndash;87** &rarr; deletes the playlist whose `PlaylistId` matches the `:playlist_id` placeholder
- **line 95** &rarr; saves the change
- **line 98** &rarr; returns the number of rows deleted, which will be 1 if the playlist existed and 0 if it didn't
:::

Then change ***test.py*** to the code below:

```{code} python
:linenos:
from datastore import Datastore

database = Datastore()

playlist_id = 2

deleted = database.delete_playlist(playlist_id)
if deleted == 1:
    print(f"Playlist {playlist_id} deleted")
else:
    print(f"No playlist with id {playlist_id}")

database.close()
```

:::{important} Explanation of Code
:class: dropdown
- **line 5** &rarr; playlist 2 is called "Movies" and has no tracks in it
- **line 7** &rarr; deletes the playlist and stores how many rows were deleted
- **lines 8&ndash;11** &rarr; uses `rowcount` to give the user a useful message
:::

Run ***test.py*** twice. The output is:

```{code} text
Playlist 2 deleted
```

then:

```{code} text
No playlist with id 2
```

The second time, the playlist has already gone, so the `DELETE` matches 0 rows.

:::{warning} DELETE without WHERE
:class: dropdown
A `DELETE` without a `WHERE` clause removes **every** row in the table, and once it is committed there is no undo. This is why we back up our database before testing delete methods.
:::

:::{hint} Deleting rows other tables refer to
:class: dropdown
We deleted playlist 2 because it has no tracks. If a playlist has tracks, its `PlaylistId` is also stored in the `playlist_track` table. Deleting only the playlist would leave rows in `playlist_track` that point to a playlist that no longer exists. To delete it properly, we would delete its rows from `playlist_track` first, then the playlist.
:::

## Summary

| Task | Code |
| --- | --- |
| Change rows | `UPDATE table SET field = :value WHERE ...` |
| Remove rows | `DELETE FROM table WHERE ...` |
| Save changes | `self.connection.commit()` |
| Number of rows changed | `self.cursor.rowcount` |

:::{seealso} Activities
:class: dropdown
Add each method to **datastore.py** and test it in ***test.py***. Remember to restore **chinook.db** from **chinook copy.db** if we want to start again with the original data.

**Activity 1: Update a phone number**

Write an `update_customer_phone(customer_id, phone)` method. Use it to change customer 55's phone number to `+61 (02) 9000 1234`, then print their contact details.

Expected Output:

```text
Rows changed: 1
[('Mark', 'Taylor', 'mark.taylor@yahoo.au', '+61 (02) 9000 1234')]
```

(The email will show our new email instead if we've already run the Updating data example.)

---

**Activity 2: Rename a playlist**

Write a `rename_playlist(playlist_id, name)` method. Rename playlist 17 to `Metal Classics`, then try to rename playlist 100. Use `rowcount` to print whether each rename worked.

Expected Output:

```text
Playlist 17 renamed
No playlist with id 100
```

---

**Activity 3: Clear a playlist**

Write a `clear_playlist(playlist_id)` method that deletes every track from a playlist by deleting its rows from the `playlist_track` table. Clear playlist 16 (Grunge) and print how many tracks were removed.

Expected Output:

```text
Tracks removed from playlist 16: 15
```

---

**Activity 4: Change an album's price**

Write an `update_album_price(album_id, price)` method that sets the `UnitPrice` of every track on an album. In ***test.py***, ask the user for the new price for album 1. Only update the price if it is more than 0.

Expected Output (when the user enters `1.49`):

```text
New price for album 1: 1.49
Tracks updated: 10
```

Expected Output (when the user enters `-1`):

```text
New price for album 1: -1
The price must be more than 0
```
:::
