# SQLite3 - Querying

:::{dropdown} Learning Goals
By the end of this section you will:

:::

Once you have create a connection and cursor, there are two steps to running a query in using `sqlite3` and Python:

1. Excute the SQL query statement
2. Fetch the results

## Queries without variables

### Execute the SQL query statement

The SQL query statement is provided as a string. Below is an example of how I format the code using a multiline string. It makes it easier to read, and, therefore, increases maintainability.

```{code} python
:linenos:
cursor.execute(
    """
    SELECT name, phone_num
    FROM customers
    """
)
```

### Fetch the results

Once the query has been executed, you need to fetch the results that are stored in the cursor. You have three fetching options:

1. `fetchall()` - returns all the results
2. `fetchone()` - returns the next result
3. `fetchmany(size)` - returns the `size` number of rows

```{code} python
:linenos:
cursor.execute(
    """
    SELECT name, phone_num
    FROM Customers
    """
)

reults = cursor.fetchall()
```

### Full example

Here is a full example of running a simple SQL Query. Note the layout and use of comments to structure our Datastore class.

**Datastore**

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

    def get_customer_contact(self):
        # Execute SQL Statement
        self.cursor.execute(
            """
            SELECT FirstName, LastName, Email, Phone
            FROM customers
            """
        )

        # Retrieve Results
        results = self.cursor.fetchall()

        # Process Results

        # Return Results
        return results

```

**Test**

Here is the code for `test.py`. When you run it, notice the stucture of the returned values.

```{code} python
:linenos:
from datastore import Datastore
from pprint import pprint

database = Datastore()

pprint(database.get_customer_contact())
```

:::{important} Explanation of Code
:class: dropdown
`pprint` is short for pretty print. It's Python's module for printing datastructures in a more human readable way.
:::