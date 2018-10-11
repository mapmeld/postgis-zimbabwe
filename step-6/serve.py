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
    return "Hello Election!"

@app.route('/local')
def local():
    """
    return local district name and GeoJSON boundary
    """
    cursor.execute("""SELECT adm1, adm2
            FROM districts
            WHERE ST_Intersects(wkb_geometry, ST_MakePoint(%s, %s))""",
        (request.args.get('lng'), request.args.get('lat')))
    result = cursor.fetchone()

    if result is None:
        return json.dumps({"adm1": "Foreign", "adm2": "Foreign"})
    else:
        return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=True)
