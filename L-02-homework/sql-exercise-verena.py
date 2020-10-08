import sqlite3

def get_playlist_length(cursor):
    """Wieviele Minuten Spielzeit hat jede Playlist?
        Liste die Spielzeit in Minuten absteigend zusammen mit der PlaylistID auf."""
    query = """ 
            """
    print(query)
    return cursor.execute(query)

if __name__ == '__main__':
    conn = sqlite3.connect("Chinook_Sqlite.sqlite")
    cursor = conn.cursor()

    for r in get_playlist_length(cursor):
        print(r)