import sqlite3

def get_number_of_artists_in_chinook(cursor):
    """Count artists"""
    query = """SELECT count(*) FROM Artist"""
    print(query)
    return cursor.execute(query)

def get_most_expensive_invoice_script(cursor):
    """What order (Invoice) was the most expensive?"""
    query = """SELECT MAX(Invoice.Total) as maxTotal, InvoiceId, CustomerId 
                FROM Invoice"""
    print(query)
    return cursor.execute(query)


def get_cheapest_invoice_script(cursor):
    """What order (Invoice) was the cheapest?"""
    query = """SELECT MIN(Invoice.Total) as maxTotal, InvoiceId, CustomerId 
                FROM Invoice"""
    print(query)
    return cursor.execute(query)


def get_city_with_most_orders_script(cursor):
    """Which city (BillingCity) has the most orders?"""
    query = """SELECT MAX(Invoice.BillingCity) as maxTotal FROM Invoice"""
    print(query)
    return cursor.execute(query)


def get_count_aac_tracks_script(cursor):
    """Calculate (or count) how many tracks have this MediaType: Protected AAC audio file."""
    query = """SELECT count(Track.MediaTypeId)
                FROM MediaType
                INNER JOIN Track ON MediaType.MediaTypeId=Track.MediaTypeId
                WHERE MediaType.name='Protected AAC audio file';"""
    print(query)
    return cursor.execute(query)

#def get_count_aac_tracks_script(cursor):
#    """Calculate (or count) how many tracks have this MediaType: Protected AAC audio file."""
#    query = """SELECT count(*) FROM Track WHERE MediaTypeId='2';"""
#    print(query)
#    return cursor.execute(query)


def get_artist_most_albums_script(cursor):
    #Find out what Artist has the most albums? Top 3
    query = """SELECT COUNT(Album.ArtistId) AS counts, Artist.Name AS name
                FROM Album
                INNER JOIN Artist 
                ON Album.ArtistId=Artist.ArtistId
                GROUP BY name
                ORDER BY counts DESC
                LIMIT 3;"""
    print(query)
    return cursor.execute(query)

def get_genre_most_tracks_script(cursor):
    """What genre has the most tracks?"""
    query = """SELECT count(Track.GenreId), Track.GenreId, Genre.Name
                FROM Track
                INNER JOIN Genre ON Track.GenreId=Genre.GenreId
                GROUP BY Track.GenreId
                ORDER BY count(Track.GenreId) DESC
                LIMIT 1"""
    print(query)
    return cursor.execute(query)


def get_customer_most_money_spent_script(cursor):
    """Which customer spent the most money so far?"""
    query = """SELECT count(Invoice.CustomerId), Customer.CustomerId, Customer.FirstName, Customer.LastName
                FROM Invoice
                INNER JOIN Customer ON Customer.CustomerId=Invoice.CustomerId
                GROUP BY Invoice.CustomerId
                ORDER BY count(InvoiceId) DESC
                LIMIT 1"""
    print(query)
    return cursor.execute(query)


def get_songs_bought_with_each_order_script(cursor):
    """What songs were bought with each order?"""
    query = """SELECT Track.Name, InvoiceLine.InvoiceId
                FROM InvoiceLine
                INNER JOIN Track ON Track.TrackId=InvoiceLine.TrackId
                ORDER BY Track.Name ASC;"""
    print(query)
    return cursor.execute(query)

if __name__ == '__main__':
    conn = sqlite3.connect("Chinook_Sqlite.sqlite")
    cursor = conn.cursor()

    for r in get_number_of_artists_in_chinook(cursor):
        print(r)

    for r in get_most_expensive_invoice_script(cursor):
        print(r)

    for r in get_cheapest_invoice_script(cursor):
        print(r)

    for r in get_city_with_most_orders_script(cursor):
        print(r)

    for r in get_count_aac_tracks_script(cursor):
        print(r)

    for r in get_artist_most_albums_script(cursor):
        print(r)

    for r in get_genre_most_tracks_script(cursor):
        print(r)

    for r in get_customer_most_money_spent_script(cursor):
        print(r)

    for r in get_songs_bought_with_each_order_script(cursor):
        print(r)