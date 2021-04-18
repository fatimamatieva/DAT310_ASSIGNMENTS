import sqlite3
from werkzeug.security import generate_password_hash


# BRUKERNAVN: username
# PASSORD: password


def bruker_table(conn):
    cur = conn.cursor()
    try:
        sql = ("CREATE TABLE users ("
               "userid INTEGER, "
               "username VARCHAR(10), "
               "passwordhash VARCHAR(10), ")
        cur.execute(sql)
        conn.commit
    except sqlite3.Error as e:
        print(e)
    cur.close()

def addresser_table(conn):
    cur = conn.cursor()
    try:
        sql = ("CREATE TABLE addresses ("
               "addressid INTEGER, "
               "user INTEGER, "
               "name TEXT, "
               "tel TEXT, "
               "email TEXT, ")
        cur.execute(sql)
        conn.commit
    except sqlite3.Error as e:
        print(e)
    cur.close()

def add_bruker(conn, username, hash):
    cur = conn.cursor()
    try:
        sql = ("INSERT INTO users (username, passwordhash) VALUES (?,?)")
        cur.execute(sql, (username, hash))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    cur.close()

def add_addresser(conn, name, email,tel, userid):
    cur = conn.cursor()
    try:
        sql = ("INSERT INTO addresses (user,name, email, tel) VALUES (?,?,?,?)")
        cur.execute(sql, (userid, name, email, tel))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    cur.close()

def get_addresser(conn, userid):
    cur = conn.cursor()
    try:
        sql = ("SELECT name, tel, email FROM addresses WHERE user = ?")
        cur.execute(sql, (userid,))
        addresser = []
        for row in cur:
            (name, tel, email) = row
            addresser.append({
                "name": name,
                "tel": tel,
                "email": email
            })
        return addresser
    except sqlite3.Error as e:
        print(e)
    cur.close()

def get_bruker(conn, username):
    cur = conn.cursor()
    try:
        sql = ("SELECT userid, username FROM users WHERE username = ?")
        cur.execute(sql, (username,))
        for row in cur:
            (id, name) = row
            return {
                "username": name,
                "userid": id
            }
        else:
            return {
                "username": username,
                "userid": None
            }
    finally:
        cur.close()

def login_hash(conn, username):
    cur = conn.cursor()
    try:
        sql = ("SELECT passwordhash FROM users WHERE username=?")
        cur.execute(sql, (username, ))
        for row in cur:
            (passhash, ) = row
            return passhash
    finally:
        cur.close()

if __name__ == "__main__":
    conn = sqlite3.connect("database.db")
    bruker_table(conn)
    addresser_table(conn)
    add_bruker(conn,"username", generate_password_hash("password"))
    add_addresser(conn, "Don John", "don.john@ymail.com", "12-322-622", 1)
    add_addresser(conn, "Elizabeth Westland", "e47wl@outlook.com", "66-112-312", 1)
    add_addresser(conn, "John Smith", "john.smith@gmail.com", "12-345-678", 1)
    add_addresser(conn, "Kevin Magnussen", "+31 997-11-21", "kevinrulez@noemail.com", 1)
    conn.close()
