# Step 5

We're now going to talk about an API server which uses PostGIS as the database.
PostGIS is PostgreSQL, so you might not need to change too much about your setup.

You might like to use Django or another web server. To make everything simple, I am
going to use the Flask framework.  I've also installed simplejson because one of
our tables uses a Decimal type which Python doesn't like to make into a JSON Number.

### Technical Setup

Launch the Flask server:

```bash
pip install flask psycopg2 simplejson
python3 serve.py
```

The server will now be available on http://localhost:5000/
When you edit serve.py, the server will restart!

### Interactive Tutorial

Let's make it so that when you click on the map, we reply with information about
that point (specifically, the district).

```python
from flask import Flask
from flask import request
import simplejson as json
...
@app.route('/local')
def about():
    cursor.execute("""SELECT adm1, adm2
          FROM districts
          WHERE ST_Intersects(wkb_geometry, ST_MakePoint(%s, %s))""",
        (request.args.get('lng'), request.args.get('lat')))
    result = cursor.fetchone()
    return json.dumps(result)
```

If there is no district, this API only returns ```null```. Let's choose a nicer way
for the API to reply that the point is not in Zimbabwe.

```python
if result is None:
  return json.dumps({"adm1": "Foreign", "adm2": "Foreign"})
```

It is not so interesting to show only a name on the map. Let's use the ST_AsGeoJSON function which we learned earlier, to return the boundary of the local district and display it on the map.

```sql
SELECT adm1, adm2, ST_AsGeoJSON(wkb_geometry) FROM districts
...
```

What if instead of knowing more about my location, we want to know the nearest health
facility:

```sql
SELECT *, ST_AsGeoJSON(point),
  ST_Distance(point, ST_MakePoint(%s, %s))
FROM health
WHERE ST_Distance(point, ST_MakePoint(%s, %s)) < 50000
ORDER BY ST_Distance(point, ST_MakePoint(%s, %s)) DESC
LIMIT 1
```

We will need to repeat params like this: ```(lng, lat, lng, lat, lng, lat)```.

What if we also want its district? Near a border, it might not be the same district that we are in now.

```sql
SELECT *, ST_AsGeoJSON(point),
  ST_Distance(point, ST_MakePoint(%s, %s))::int
FROM health
JOIN districts ON ST_Intersects(districts.wkb_geometry, health.point)
WHERE ST_Distance(point, ST_MakePoint(%s, %s)) < 50000
ORDER BY ST_Distance(point, ST_MakePoint(%s, %s)) ASC
LIMIT 1
```

### Learnings
