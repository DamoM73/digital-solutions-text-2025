# Add to the UPDATE METHODS in datastore.py

    def update_customer_phone(self, customer_id: int, phone: str) -> int:
        # Execute SQL Statement
        self.cursor.execute(
            """
            UPDATE customers
            SET Phone = :phone
            WHERE CustomerId = :customer_id
            """,
            {
                "phone": phone,
                "customer_id": customer_id
            }
        )

        # Save Changes
        self.connection.commit()

        # Return Number of Rows Changed
        return self.cursor.rowcount


# test.py

from datastore import Datastore

database = Datastore()

changed = database.update_customer_phone(55, "+61 (02) 9000 1234")
print(f"Rows changed: {changed}")
print(database.get_customer_contact(55))

database.close()
