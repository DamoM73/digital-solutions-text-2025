# Add to the UPDATE METHODS in datastore.py

    def rename_playlist(self, playlist_id: int, name: str) -> int:
        # Execute SQL Statement
        self.cursor.execute(
            """
            UPDATE playlists
            SET Name = :name
            WHERE PlaylistId = :playlist_id
            """,
            {
                "name": name,
                "playlist_id": playlist_id
            }
        )

        # Save Changes
        self.connection.commit()

        # Return Number of Rows Changed
        return self.cursor.rowcount


# test.py

from datastore import Datastore

database = Datastore()

if database.rename_playlist(17, "Metal Classics") == 1:
    print("Playlist 17 renamed")
else:
    print("No playlist with id 17")

if database.rename_playlist(100, "Metal Classics") == 1:
    print("Playlist 100 renamed")
else:
    print("No playlist with id 100")

database.close()
