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

    def get_customers_contact(self):
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

pprint(database.get_customers_contact())
```

:::{important} Explanation of Code
:class: dropdown
`pprint` is short for pretty print. It's Python's module for printing datastructures in a more human readable way.
:::

:::{seealso} Activities
:class: dropdown
Go back over your queries from the Activites from the SQL sections and write up the SQL statements using Python and `sqlite3`
:::

## Queries with variables

SQL queries with hardcoded variable provide a limited function. They may be useful for retrieving lists, but any filtering becomes a nightmare. If you want the details of each specific customer, you would have write a method for every single customer. Therefore we need functions that accept variables, but methods incorporate variables into SQL statements are open to malicious attacks called SQL injections.

### SQL Injections

![Bobby tables](./assets/06/exploits_of_a_mom.png)

Despite industry addressing SQL injections (SQLi) for decades, they are still one of the most exploited security flaws. This makes them worthwhile spending a bit of time understanding them.

The following Computerphile videos explain SQLi and provide an example of an SQLi in action.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/_jKylhJtPmI?si=FeqizY1w3alFBAFx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

:::{tip} Summary
:class: dropdown
The video explains SQL injection, a common and dangerous method for hacking websites. Here are the main points covered:

- **What is SQL?** SQL (Structured Query Language), sometimes pronounced "sequel," is a simple, English-like programming language used to communicate with and manage databases. It's used to perform actions like selecting, inserting, updating, or deleting data.
- **The Vulnerability:** The vulnerability arises when a website takes user input (like a username from a login form) and directly inserts it into an SQL command without properly sanitizing it first.
- **How the Hack Works:** An attacker can "inject" their own SQL commands into the input field. For example, by including a quotation mark (') or a semicolon (;), they can end the website's intended command and add their own, such as `DROP ALL DATABASES`, which would delete everything.
- **Why it Happens:** This is often a problem with languages like PHP, which are easy to learn and widely used (e.g., WordPress, early Facebook). The low barrier to entry means many developers might not be aware of this security risk and fail to implement proper safeguards.
- **Prevention:** The correct way to prevent SQL injection is by using **prepared statements**. Instead of building a single command string with user input, the developer first sends a template of the command to the database (with placeholders like a question mark `?`) and then sends the user data separately. This ensures the database treats the user input strictly as data, not as executable commands, effectively neutralizing the threat.
:::

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/ciNHn38EyRc?si=KZ-DuvfGvlVIlmgl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

:::{tip} Summary
:class: dropdown
This video explains and demonstrates how SQL injections work. Here's a summary of the key points discussed and demonstrated in the video:

- **What is an SQL Injection?** An SQL injection is a type of cyberattack that targets databases. By inserting malicious SQL code into a website's input fields (like a search bar), attackers can trick the system into revealing sensitive information.
- **Demonstration:** Dr. Mike Pound uses a sample online shop to show how easily this can be done on a vulnerable website.
    - **Normal Search:** Searching for "hammer" correctly returns items with "hammer" in their name.
    - **The Attack:** By entering a single quote (') into the search bar, he triggers a server error. This indicates the site is vulnerable because the quote is being interpreted as part of the code rather than just text.
    - **Extracting Data:** Dr. Pound then uses more advanced SQL commands to trick the database into revealing all the data it holds, including a complete list of usernames and their hashed passwords. He does this by "unioning" the product search results with the data from the user table.
- **Why It's Dangerous:** The video emphasizes how this type of attack can expose confidential user data like usernames, passwords, and other personal information. This can lead to privacy breaches, financial loss, and legal issues for the company that has been hacked.
- **How to Prevent It:** The speaker mentions that proper security measures, like "parameterized queries" and "sanitizing inputs," can prevent these attacks by ensuring user input is treated as text and not as executable code.
:::

Now we understand the threat of SQLi and how to use **parameterised queries** to prevent them, it is time to learn how to do this in Python.

### Creating Parameterised Queries

We will be using the dictionary `sqlite3` method of parameterising our queries. Add the code below to the bottom of the `Datastore` class.

```{code} python
:linenos:
:lineno-start: 33
    def get_customer_contact(self, customer_id):
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

        # Process Results

        # Return Results
        return results
```

:::{important} Explanation of Code

:::