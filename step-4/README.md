# Step 4

SQL and Geographic Data

### Installing and running locally

Install Python, pip, PostgreSQL, and PostGIS extensions.

```
pip install psycopg2
```

IF YOU ARE SETTING UP DATABASE AND READ-ONLY USER FOR THE FIRST TIME:

```
mkdir ~/Documents/pyzimmer # data can be stored in any new directory, just be consistent
initdb pyzimmer/
postgres -D pyzimmer/
createdb pyzim
psql pyzim

# you are now in the PSQL prompt
CREATE USER py;
ALTER USER py WITH PASSWORD 'zim';
GRANT CONNECT ON DATABASE pyzim TO py;
GRANT USAGE ON SCHEMA public TO py;
ALTER DEFAULT PRIVILEGES IN SCHEMA public
  GRANT SELECT ON TABLES TO py;
```

Importing Geo Data: Districts

TODO: explaing districts ogr2ogr

Importing Geo Data: OSM

TODO: add some OpenStreetMap data

### Interactive Tutorial

Connect to the database (```psql pyzim -U py```) and use SQL with new geo commands
with districts.

You will need the previous steps to have succeeded for the geodata to appear here.

TBD: testing out this import and queries
TBD: really want cloud DB and Jupyter notebooks because it is hard to use ogr2ogr

```sql
SELECT * FROM points;
SELECT ST_AsText(point) FROM points;
SELECT ST_AsGeoJSON(point) FROM points;

SELECT * FROM districts LIMIT 1;
SELECT ST_AsGeoJSON(wkb_geometry) FROM districts LIMIT 1;

# we are given a lng/lat (integer values) inside Zimbabwe
# explain that lng/lat coordinates are decimals but this is just demo
# explain that lng/lat order is important

SELECT * FROM districts WHERE ST_Contains(wkb_geometry, ST_AsPoint(31, -18));
```

We can also improve performance in large datasets by adding a spatial index.

TODO: index example

```sql

```

### Learnings

- Given SQL experience, basic to intermediate SQL knowledge
- Reminder of how a common SQL JOIN would work (trains and train reviews)
- New functions and concepts (ST_AsGeoJSON, (even spatial JOIN?)) for PostGIS
