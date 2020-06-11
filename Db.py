import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_user_table(conn):
    sql = """ CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL,
                        accesslevel TEXT NOT NULL
                    );
                    """
    create_table(conn, sql)

def create_client_table(conn):
    sql = """ 
            CREATE TABLE IF NOT EXISTS clients (
                client_id INTEGER PRIMARY KEY,
                fullname TEXT NOT NULL,
                street TEXT NOT NULL,
                zipcode TEXT NOT NULL,
                city TEXT NOT NULL,
                emailaddress TEXT NOT NULL,
                phonenumber TEXT NOT NULL
            );
            """
    create_table(conn, sql)

def create_user(conn, username, password, accesslevel):
    cursor = conn.cursor()
    sql = """   INSERT INTO users (username, password, accesslevel)
                VALUES ("%s", "%s", "%s") """ % (username, password, accesslevel)
    cursor.execute(sql)
    conn.commit()
    print("Value inserted")
    cursor.close()



def main():
    conn = create_connection(r"sqlite.db")
    if conn is not None:
        create_user_table(conn)
        create_client_table(conn)


