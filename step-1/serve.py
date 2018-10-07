import json

from flask import Flask
import psycopg2
from psycopg2.extras import RealDictCursor

try:
    conn = psycopg2.connect("dbname='pyzim' user='py' host='localhost' password='zim'") # port=####
except:
    print("I am unable to connect to the database")

cursor = conn.cursor(cursor_factory=RealDictCursor)

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/about')
def about():
    """
    return a simple list of stats about this point:
    - which Zimbabwe district is it in?
    -- download the district GeoJSON
    - how far is it from its nearest international airports?
    """
    cursor.execute("SELECT * FROM trains")
    result = cursor.fetchone()
    return json.dumps(result)

@app.route('/messy')
def messy():
    """
    attempt to drop the trains table
    """
    cursor.execute("DROP TABLE trains")
    result = cursor.fetchone()
    return json.dumps(result)

@app.route('/messy2')
def messy2():
    """
    attempt to modify the trains table
    """
    cursor.execute("INSERT INTO trains (start, finish) VALUES ('Atlantic Ocean', 'Indian Ocean')")
    result = cursor.fetchone()
    return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=True)
