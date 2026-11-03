import sqlite3


class Datastore:

    def __init__(self):
        self.connection = sqlite3.connect("data/moives.db")
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    # --- GET METHODS WITH PARAMETERS

    def get_directors_from_country(self, country: str):
        # Execute SQL Statement
        self.cursor.execute(
            """
            SELECT dirname
            FROM director
            WHERE country = :country
            """,
            {
                "country": country
            }
        )

        # Retrieve Results
        results = self.cursor.fetchall()

        # Return Results
        return results

    def get_members_owing_more_than(self, amount: float):
        self.cursor.execute(
            """
            SELECT memname, owes
            FROM members
            WHERE owes > :amount
            """,
            {"amount": amount}
        )
        return self.cursor.fetchall()

    def get_movies_with_word(self, word: str):
        self.cursor.execute(
            """
            SELECT movname
            FROM movie
            WHERE movname LIKE :pattern
            """,
            {"pattern": f"%{word}%"}
        )
        return self.cursor.fetchall()

    def get_movies_released_in(self, year: int):
        self.cursor.execute(
            """
            SELECT movname, year
            FROM movie
            WHERE year = :year
            """,
            {"year": year}
        )
        return self.cursor.fetchall()


# test.py
from pprint import pprint

database = Datastore()

pprint(database.get_directors_from_country("US"))
pprint(database.get_members_owing_more_than(20))
pprint(database.get_movies_with_word("the"))
pprint(database.get_movies_released_in(1993))

database.close()
