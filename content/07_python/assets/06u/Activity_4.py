# Add to the UPDATE METHODS in datastore.py

    def update_album_price(self, album_id: int, price: float) -> int:
        # Execute SQL Statement
        self.cursor.execute(
            """
            UPDATE tracks
            SET UnitPrice = :price
            WHERE AlbumId = :album_id
            """,
            {
                "price": price,
                "album_id": album_id
            }
        )

        # Save Changes
        self.connection.commit()

        # Return Number of Rows Changed
        return self.cursor.rowcount


# test.py

from datastore import Datastore

database = Datastore()

price = float(input("New price for album 1: "))

if price <= 0:
    print("The price must be more than 0")
else:
    changed = database.update_album_price(1, price)
    print(f"Tracks updated: {changed}")

database.close()
