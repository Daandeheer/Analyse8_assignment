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

conn = create_connection(r"sqlite.db")


def create_table(create_table_sql):
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

def create_user_table():
    sql = """   CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    accesslevel TEXT NOT NULL
                ); """
    create_table(sql)

def create_client_table():
    sql = """   CREATE TABLE IF NOT EXISTS clients (
                    client_id INTEGER PRIMARY KEY,
                    fullname TEXT NOT NULL,
                    street TEXT NOT NULL,
                    zipcode TEXT NOT NULL,
                    city TEXT NOT NULL,
                    emailaddress TEXT NOT NULL,
                    phonenumber TEXT NOT NULL
                ); """
    create_table(sql)

def create_user(username, password, accesslevel):
    sql = """   INSERT INTO users (username, password, accesslevel)
                VALUES ("%s", "%s", "%s") """ % (username, password, accesslevel)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()

def create_init_user(password):
    sql = """   INSERT INTO users (username, password, accesslevel)
                VALUES ("Superuser1", "%s", "super admin") """ % password
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()

def check_username_exists(username):
    # Checks in the db if the username exists.
    # In the case that the username does not exist and the username 
    # is not equal to that of the super admin, the function returns True, 
    # which makes the program continue.
    sql = """   SELECT user_id 
                FROM users 
                WHERE username="%s" """ % username
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()

    if result == None or username != "Superuser1":
        return True
    else:
        return False

def create_client(fullname, street, zipcode, city, emailaddress, phonenumber):
    sql = """   INSERT INTO clients (fullname, street, zipcode, city, emailaddress, phonenumber)
                VALUES ("%s", "%s", "%s", "%s", "%s", "%s") """ % (fullname, street, zipcode, city, emailaddress, phonenumber)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()

def auth_login(username, password):
    sql = """   SELECT username, accesslevel 
                FROM users
                WHERE username="%s" and password="%s" """ % (username, password)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    result = cursor.fetchone()
    cursor.close()
    
    return result

def main():
    if conn is not None:
        create_user_table()
        create_client_table()