import sqlite3


class Datastore:

    def __init__(self):
        self.connection = sqlite3.connect("data/moives.db")
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    # --- GET METHODS

    def get_director_names(self):
        # Execute SQL Statement
        self.cursor.execute(
            """
            SELECT dirname
            FROM director
            """
        )

        # Retrieve Results
        results = self.cursor.fetchall()

        # Return Results
        return results

    def get_member_names(self):
        self.cursor.execute(
            """
            SELECT memname
            FROM members
            """
        )
        return self.cursor.fetchall()

    def get_all_movies(self):
        self.cursor.execute(
            """
            SELECT *
            FROM movie
            """
        )
        return self.cursor.fetchall()

    def get_release_years(self):
        self.cursor.execute(
            """
            SELECT DISTINCT year
            FROM movie
            """
        )
        return self.cursor.fetchall()

    def get_movies_on_hire(self):
        self.cursor.execute(
            """
            SELECT movienumber, duedate
            FROM movies_onhire
            """
        )
        return self.cursor.fetchall()


# test.py
from pprint import pprint

database = Datastore()

pprint(database.get_director_names())
pprint(database.get_member_names())
pprint(database.get_all_movies())
pprint(database.get_release_years())
pprint(database.get_movies_on_hire())

database.close()
