from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("hiking.sqlite")


def print_all():
    db.pretty_print("SELECT * FROM User;")


def insert_value(sql_db: SQLiteDatabase, username: str, age: int):
    sql_cmd = f"INSERT INTO User(name, age) VALUES ('{username}', {age});"
    print(sql_cmd)
    return sql_db.execute(sql_cmd)


def delete_entry(sql_db: SQLiteDatabase, user_id: int):
    sql_cmd = f"DELETE FROM User WHERE id={user_id};"
    print(sql_cmd)
    return sql_db.execute(sql_cmd)


def update_user_age(sql_db: SQLiteDatabase, user_id: int, age: int):
    sql_cmd = f"UPDATE User SET age={age} WHERE id={user_id};"
    print(sql_cmd)
    return sql_db.execute(sql_cmd)

def update_username(sql_db: SQLiteDatabase, user_id: int, username: str):
    sql_cmd = f"UPDATE User SET name='{username}' WHERE id={user_id};"
    print(sql_cmd)
    return sql_db.execute(sql_cmd)


# CREATE New Table

db.execute("""CREATE TABLE IF NOT EXISTS User(
                id integer primary key autoincrement, 
                name text, 
                age integer);
            """)

db.print_tables(verbose=True)

# Insert Data Into Table

insert_value(db, 'Timo', 41)

print_all()

# Update DB Entries

update_user_age(db, 1, 15)

update_username(db, 1, 'Verena')

print_all()

# DELETE DB Entries

delete_entry(db, 1)

print_all()

# Alter table user, add additional column

db.execute(
    """ALTER TABLE User
        ADD email text;
    """
)

db.print_tables(verbose=True)

# Dropping table User

print("Dropping Table")

db.execute(
    """DROP TABLE User;
    """
)

db.print_tables(verbose=True)

print("Done")
