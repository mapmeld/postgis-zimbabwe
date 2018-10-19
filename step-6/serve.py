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

@app.route('/wards')
def local():
    """
    return any matching wards in a buffer area
    """
    cursor.execute("""SELECT ST_AsGeoJSON(wkb_geometry) AS ward,
      ADM1_EN, ADM2_EN, ADM3_EN
    FROM wards
    WHERE ST_Intersects(wkb_geometry,
      ST_Buffer(ST_MakePoint(%s, %s), 0.001)
    )""",
        (request.args.get('lng'), request.args.get('lat')))

    try:
        results = cursor.fetchall()
        return json.dumps(results)
    except:
        return json.dumps({"adm1": "Foreign", "adm2": "Foreign"})

if __name__ == '__main__':
    app.run(debug=True)
