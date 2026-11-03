# Add to the DELETE METHODS in datastore.py

    def clear_playlist(self, playlist_id: int) -> int:
        # Execute SQL Statement
        self.cursor.execute(
            """
            DELETE FROM playlist_track
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


# test.py

from datastore import Datastore

database = Datastore()

removed = database.clear_playlist(16)
print(f"Tracks removed from playlist 16: {removed}")

database.close()
