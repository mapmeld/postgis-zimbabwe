import simplejson as json

from flask import Flask
from flask import request
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

@app.route('/local')
def local():
    """
    return local district name
    make a good error if it isn't in Zimbabwe
    """
    cursor.execute("""SELECT adm1, adm2
            FROM districts
            WHERE ST_Intersects(wkb_geometry, ST_MakePoint(%s, %s))""",
        (request.args.get('lng'), request.args.get('lat')))
    result = cursor.fetchone()

    return json.dumps(result)

    # if result is None:
    #     return json.dumps({"adm1": "Foreign", "adm2": "Foreign"})
    # else:
    #     return json.dumps(result)

@app.route('/health')
def health():
    """
    return nearest health spot and its district
    """

    lng = request.args.get('lng')
    lat = request.args.get('lat')

    cursor.execute("""SELECT *, ST_AsGeoJSON(point),
      ST_Distance(point, ST_MakePoint(%s, %s))::int
    FROM health
    JOIN districts ON ST_Intersects(districts.wkb_geometry, health.point)
    WHERE ST_Distance(point, ST_MakePoint(%s, %s)) < 50000
    ORDER BY ST_Distance(point, ST_MakePoint(%s, %s)) ASC
    LIMIT 1""",
        (lng, lat, lng, lat, lng, lat))
    result = cursor.fetchone()

    if result is None:
        return json.dumps("No health facility within 50km")
    else:
        return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=True)
