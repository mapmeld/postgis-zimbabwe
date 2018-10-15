import json, os

from flask import Flask, request
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
    return app.send_static_file('index.html')

@app.route('/about')
def about():
    """
    return a simple list of stats about this point:
    - which Zimbabwe district is it in?
    -- download the district GeoJSON
    - how far is it from its nearest international airports?
    """
    cursor.execute("""SELECT adm1, adm2, ST_AsGeoJSON(wkb_geometry) AS geojson
            FROM districts
            WHERE ST_Intersects(wkb_geometry, ST_MakePoint(%s, %s))""",
        (request.args.get('lng'), request.args.get('lat')))
    result = cursor.fetchone()

    if result is None:
        return json.dumps({"adm1": "Foreign", "adm2": "Foreign"})
    else:
        cursor.execute("""SELECT COUNT(*)
                FROM health
                WHERE ST_DWithin(point, ST_MakePoint(%s, %s), 20000)""",
            (request.args.get('lng'), request.args.get('lat')))
        healthcount = cursor.fetchone()
        result["count"] = healthcount["count"]

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
