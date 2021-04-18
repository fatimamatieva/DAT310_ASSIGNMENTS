# BRUKERNAVN: username
# PASSORD: password


from db import *
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask, request, redirect, url_for, session, g

app = Flask(__name__)
app.debug = True
app.secret_key = 'some_secret'

# get_X() creates resource X if it does not exist, caching it as g.X.
# teardown_X() closes or otherwise deallocates the resource if it exists. It is registered as a teardown_appcontext() handler.
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect("database.db")
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/login", methods=["POST"])
def login():
    conn = get_db()
    user = get_bruker(conn,request.form["username"])
    user["addresses"] = get_addresser(conn, user["userid"])
    print(user)
    session["userid"] = user["userid"]
    return user

@app.route("/logout")
def logout():
    return redirect(url_for("/"))

@app.route("/")
def redirected():
    return "You were redirected"

if __name__ == "__main__":
    app.run()