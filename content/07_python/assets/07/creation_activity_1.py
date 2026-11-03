import sqlite3


class Datastore:
    """
    Datastore for the manufacturing database (ERD & RS Activity 1)
    """

    def __init__(self):
        """
        initialises the datastore
        """

        self.conn = sqlite3.connect("manufacturing.db")
        self.cursor = self.conn.cursor()

        self.build_database()
        self.conn.commit()

    def build_database(self):
        """
        builds the database, creating tables without foreign keys first
        """

        self.cursor.execute(
            """
            CREATE TABLE "Product" (
                "product_id" INTEGER,
                "name" TEXT NOT NULL,
                "quantity" INTEGER NOT NULL,
                PRIMARY KEY("product_id" AUTOINCREMENT)
            );
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE "Supplier" (
                "supplier_id" INTEGER,
                "name" TEXT NOT NULL,
                "email" TEXT NOT NULL,
                PRIMARY KEY("supplier_id" AUTOINCREMENT)
            );
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE "Component" (
                "component_id" INTEGER,
                "name" TEXT NOT NULL,
                "description" TEXT NOT NULL,
                PRIMARY KEY("component_id" AUTOINCREMENT)
            );
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE "Component Supplier" (
                "component_id" INTEGER,
                "supplier_id" INTEGER,
                PRIMARY KEY("component_id", "supplier_id"),
                FOREIGN KEY("component_id") REFERENCES "Component"("component_id"),
                FOREIGN KEY("supplier_id") REFERENCES "Supplier"("supplier_id")
            );
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE "Product Components" (
                "product_id" INTEGER,
                "component_id" INTEGER,
                "quantity" INTEGER NOT NULL,
                PRIMARY KEY("product_id", "component_id"),
                FOREIGN KEY("product_id") REFERENCES "Product"("product_id"),
                FOREIGN KEY("component_id") REFERENCES "Component"("component_id")
            );
            """
        )


# main.py
db = Datastore()
