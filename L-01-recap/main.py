from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("hiking.sqlite")

db.execute("DROP TABLE User;")

db.execute("""CREATE TABLE IF NOT EXISTS User(
                id integer primary key autoincrement, 
                name text, 
                age integer);
            """)

db.print_tables(verbose=True)

db.execute("""INSERT INTO 
            User (name, age) 
            VALUES 
            ('Matt', 31), 
            ('Verena', 36),
            ('Ruby', 7),
            ('Ada', 8),
            ('Dom', 16)
            ;""")

db.execute("""
            UPDATE User 
            SET age=41 
            WHERE id=1;
            """)

result = db.execute("SELECT * FROM User;")
db.pretty_print("SELECT * FROM User;")

