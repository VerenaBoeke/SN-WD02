from smartninja_sql.sqlite import SQLiteDatabase
chinook = SQLiteDatabase("Chinook_Sqlite.sqlite")

# HOMEWORK
# Write an SQL command that will print Name from the table Artist
# Print all data from the table Invoice where BillingCountry is Germany
# Count how many albums are in the database. Look into the SQL documentation for help.
# How many customers are from France?

chinook.pretty_print("SELECT Name FROM Artist;")

chinook.pretty_print("SELECT * FROM Invoice WHERE BillingCountry='Germany';")

chinook.pretty_print("SELECT count(AlbumId) FROM Album")

chinook.pretty_print("SELECT count(CustomerId) FROM Customer WHERE Country='France'")
