import database_load

def main():
    db_connection = database_load.connect_database()
    db_cursor = db_connection.cursor()

    db_cursor.execute("SELECT * FROM games")

    print(db_cursor.fetchone())

main()