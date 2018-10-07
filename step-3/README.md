# Step 3

Do you know SQL?

Before continuing in the tutorial, I want to cover what we know about SQL. Depending
on skill level, this could be a participatory conversation on what queries we can
do, or it can be an introduction to SQL as a whole.

I also cover psycopg2 here so that everyone is comfortable writing SQL and Python
together.

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

IF YOU ARE SETTING UP TRAIN REVIEWS FOR THE FIRST TIME

```
psql pyzim

CREATE TABLE train_reviews (train_id INT, stars INT);
INSERT INTO train_reviews (train_id, stars) VALUES (1, 1);
INSERT INTO train_reviews (train_id, stars) VALUES (2, 2);
INSERT INTO train_reviews (train_id, stars) VALUES (1, 3);
INSERT INTO train_reviews (train_id, stars) VALUES (2, 4);
INSERT INTO train_reviews (train_id, stars) VALUES (1, 5);
INSERT INTO train_reviews (train_id, stars) VALUES (2, 1);
```

### Interactive Tutorial

Connect to the database (```psql pyzim -U py```) and review SQL concepts:

```sql
SELECT start FROM trains;

SELECT * FROM trains;

SELECT * FROM trains LIMIT 1;

SELECT start, finish, seats FROM trains;

SELECT start, finish, seats
      FROM trains
      WHERE seats = 100;

SELECT CONCAT(CONCAT(start, ' to '), finish) AS route,
        price
      FROM trains
      WHERE seats < 100;


SELECT CONCAT(CONCAT(start, ' to '), finish) AS route,
        price
      FROM trains
      WHERE seats > 50
      AND price > 10;

SELECT COUNT(*) ...

SELECT start, COUNT(*) FROM trains GROUP BY start;

SELECT start, finish, AVG(stars) FROM trains
    JOIN train_reviews ON trains.id = train_reviews.train_id
    GROUP BY start, finish;
```

Connect to the database (```psql pyzim -U py```) and learn new concepts with districts.
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

### Learnings

- Given SQL experience, basic to intermediate SQL knowledge
- Reminder of how a common SQL JOIN would work (trains and train reviews)
- New functions and concepts (ST_AsGeoJSON, (even spatial JOIN?)) for PostGIS
