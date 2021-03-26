"""
Flask: Using templates
"""

from setup_db import select_students
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, g

app = Flask(__name__)


DATABASE = './database.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    # get the database connection
    conn = get_db()
    return render_template("index.html", 
                    # select_students executes SELECT SQL statement on database connetion
                    # returns list of students
                    students=select_students(conn))


# Add additional routes here.


if __name__ == "__main__":
    app.run(debug=True)