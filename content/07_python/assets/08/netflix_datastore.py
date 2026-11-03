import csv
import sqlite3


class Datastore:
    """
    Datastore for the Netflix shows database
    """

    def __init__(self, database_file: str, data_file: str):
        """
        initialises the datastore
        """
        self.database_file = database_file
        self.data_file = data_file
        self.conn = sqlite3.connect(self.database_file)
        self.cursor = self.conn.cursor()

        self.populate_database()
        self.conn.commit()

    def populate_database(self):
        """
        populates the database with data from the csv file
        """
        with open(self.data_file, mode="r", encoding="utf-8") as csvfile:
            csv_reader = csv.DictReader(csvfile)

            for record in csv_reader:
                # process show values
                show_id = int(record["show_id"][1:])
                type_id = self.get_id("Types", "type_id", record["type"])

                rating = record["rating"]
                if rating == "" or rating.endswith("min"):
                    rating_id = None
                else:
                    rating_id = self.get_id("Rating", "rating_id", rating)

                self.add_show(
                    show_id,
                    type_id,
                    record["title"],
                    record["date_added"].strip(),
                    int(record["release_year"]),
                    rating_id,
                    record["duration"],
                    record["description"],
                )

                # process the many-to-many values
                for name in self.split_list(record["director"]):
                    director_id = self.get_id("Director", "director_id", name)
                    self.add_link("Show_director", show_id, director_id)

                for name in self.split_list(record["country"]):
                    country_id = self.get_id("Country", "country_id", name)
                    self.add_link("Show_country", show_id, country_id)

                for name in self.split_list(record["cast"]):
                    actor_id = self.get_id("Actor", "actor_id", name)
                    self.add_link("Cast", show_id, actor_id)

                for name in self.split_list(record["listed_in"]):
                    category_id = self.get_id("Category", "category_id", name)
                    self.add_link("Show_category", show_id, category_id)

    def split_list(self, value: str) -> list[str]:
        """
        splits a comma separated CSV value into a list of names,
        removing spaces and blank names
        """
        names = []
        for name in value.split(","):
            name = name.strip()
            if name and name not in names:
                names.append(name)
        return names

    def get_id(self, table: str, id_field: str, name: str) -> int:
        """
        returns the id of the name in the lookup table,
        adding the name first if it isn't in the table
        """
        # table and id_field come from our code, not the user,
        # so it is safe to put them in the SQL with an f-string
        select_sql = f"SELECT {id_field} FROM {table} WHERE name = :name"

        self.cursor.execute(select_sql, {"name": name})
        result = self.cursor.fetchone()

        if result is None:
            self.cursor.execute(
                f"INSERT INTO {table} (name) VALUES (:name)",
                {"name": name},
            )
            self.cursor.execute(select_sql, {"name": name})
            result = self.cursor.fetchone()

        return result[0]

    def add_show(
        self,
        show_id: int,
        type_id: int,
        title: str,
        date_added: str,
        release_year: int,
        rating_id: int | None,
        duration: str,
        description: str,
    ):
        """
        adds a show to the database
        """
        self.cursor.execute(
            """
            INSERT INTO Show (show_id, type, title, date_added, release_year, rating, duration, description)
            VALUES (:show_id, :type, :title, :date_added, :release_year, :rating, :duration, :description)
            """,
            {
                "show_id": show_id,
                "type": type_id,
                "title": title,
                "date_added": date_added,
                "release_year": release_year,
                "rating": rating_id,
                "duration": duration,
                "description": description,
            },
        )

    def add_link(self, table: str, show_id: int, other_id: int):
        """
        adds a row to a linking table (Show_director, Show_country, Cast or Show_category)
        """
        self.cursor.execute(
            f"INSERT INTO {table} VALUES (:show_id, :other_id)",
            {"show_id": show_id, "other_id": other_id},
        )
