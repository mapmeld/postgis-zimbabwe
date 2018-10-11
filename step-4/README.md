# Step 4

SQL and Geographic Data

In this step, we'll apply what we learned / reviewed about SQL to the exciting new
geospatial queries in PostGIS.

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

# activate PostGIS
CREATE EXTENSION postgis;
```

As the db admin user, import GeoJSON and other files using ogr2ogr (part of GDAL install). Here's how we imported a GeoJSON file into a "zimbabwe_districts" table
(and then some more).

```bash
ogr2ogr -f "PostgreSQL" PG:"dbname=pyzim" zimbabwe-districts.geojson
ogr2ogr -f "PostgreSQL" PG:"dbname=pyzim" health.geojson
```

Tips for importing other formats of geodata:
https://morphocode.com/using-ogr2ogr-convert-data-formats-geojson-postgis-esri-geodatabase-shapefiles/

If you imported a CSV table with latitude and longitude columns and want to make it into a geo table, here you go:

```sql
ALTER TABLE schools ADD COLUMN point;
UPDATE schools SET point = ST_MakePoint(longitude, latitude);
```

Then run ```psql pyzim``` and alter wkb_geometry to a GEOGRAPHY type. If you
don't have a GEOGRAPHY type, you ought to run ```CREATE EXTENSION postgis;``` first.

```sql
ALTER TABLE zimbabwe_districts RENAME TO districts;
ALTER TABLE districts ALTER wkb_geometry TYPE GEOGRAPHY;

ALTER TABLE health ALTER wkb_geometry TYPE GEOGRAPHY;
ALTER TABLE health RENAME wkb_geometry TO point;
```

Importing Geo Data: OpenStreetMap

There are tons of community-built data on OpenStreetMap (OSM), including a monthly-updated, 340MB zipped buildings shapefile from https://data.humdata.org/dataset/hotosm_zwe_buildings

I used http://overpass-turbo.eu/ to download ~120 wells mapped on OpenStreetMap

```
node
  [man_made=water_well]
  ({{bbox}});
out;
```

You can also download tourism=attraction and tourism=hotel datasets:



Importing Geo Data: Other

I found a database of Health Facility points from the Zimbabwe Ministry of Health (dated January 2007 :-\ )

### Interactive Tutorial

Connect to the database (```psql pyzim -U py```) and use SQL with new geo commands
with districts.

You will need the previous steps to have succeeded for the geodata to appear here.

TBD: really want cloud DB and Jupyter notebooks because it is hard to use ogr2ogr

```sql

# point data
SELECT * FROM health LIMIT 1;

SELECT ST_AsText(point) FROM health LIMIT 1;
SELECT ST_AsGeoJSON(point) FROM health LIMIT 1;
SELECT ST_AsGeoJSON(point), nameoffaci FROM health LIMIT 1;

# shape data
SELECT * FROM districts LIMIT 1;
SELECT ST_AsGeoJSON(wkb_geometry) FROM districts LIMIT 1;

# we are given a lng/lat (integer values) inside Zimbabwe
# explain that lng/lat order is important
# explain that lng/lat coordinates are decimals but this is just demo

SELECT adm1, adm2 FROM districts
WHERE ST_Intersects(wkb_geometry, ST_AsPoint(31, -18));
```

We can also improve performance in large datasets by adding a spatial index on
any geography-type columns.

Only the first command is necessary here, but the others can improve performance.
For more read: http://revenant.ca/www/postgis/workshop/indexing.html

```sql
CREATE INDEX district_gix ON districts USING GIST (wkb_geometry);
VACUUM ANALYZE districts;
CLUSTER districts USING districts_gix;
ANALYZE districts;
```

### Learnings

- Given SQL experience, basic to intermediate SQL knowledge
- Reminder of how a common SQL JOIN would work (trains and train reviews)
- New functions and concepts (ST_AsGeoJSON, (even spatial JOIN?)) for PostGIS
