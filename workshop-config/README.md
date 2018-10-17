# Workshop Config / Step 0

This readme is solely for setting up the cloud PostGIS and Jupyter Notebooks
for multiple workshop participants.

### Installing and running locally

Install Python with pip, GDAL PostgreSQL, and PostGIS extensions.

Set up the database and read-only user:

```bash
pip install csvkit psycopg2

mkdir ~/Documents/pyzimmer # data can be stored in any new directory, just be consistent
initdb pyzimmer/
postgres -D pyzimmer/
createdb pyzim
psql pyzim
```

You are now in the PSQL prompt:

```sql
CREATE USER py;
ALTER USER py WITH PASSWORD 'zim';
GRANT CONNECT ON DATABASE pyzim TO py;
GRANT USAGE ON SCHEMA public TO py;
ALTER DEFAULT PRIVILEGES IN SCHEMA public
  GRANT SELECT ON TABLES TO py;

# activate PostGIS
CREATE EXTENSION postgis;
```

TBD do not allow py to create their own tables

Import the trains table (TBD: replace with a CSV import)

```sql
DROP TABLE trains; # overwrite any old trains table
CREATE TABLE trains (start TEXT, finish TEXT, seats INT, id INT, price FLOAT);
INSERT INTO trains (start, finish, seats, id, price) VALUES ('Harare', 'Victoria Falls', 100, 1, 100);
INSERT INTO trains (start, finish, seats, id, price) VALUES ('Harare', 'Bulawayo', 25, 2, 10);

DROP TABLE train_reviews; # overwrite any old train reviews table
CREATE TABLE train_reviews (train_id INT, stars INT);
INSERT INTO train_reviews (train_id, stars) VALUES (1, 1);
INSERT INTO train_reviews (train_id, stars) VALUES (2, 2);
INSERT INTO train_reviews (train_id, stars) VALUES (1, 3);
INSERT INTO train_reviews (train_id, stars) VALUES (2, 4);
INSERT INTO train_reviews (train_id, stars) VALUES (1, 5);
INSERT INTO train_reviews (train_id, stars) VALUES (2, 1);
```

### Importing the geodata using ogr2ogr (from GDAL)

```bash
ogr2ogr -f "PostgreSQL" PG:"dbname=pyzim" zimbabwe-districts.geojson

csvsql --db postgresql:///pyzim step-4/health.csv --insert
```

### Launching the Jupyter notebooks

- https://jupyter-notebook.readthedocs.io/en/stable/public_server.html
- Enable global access from a non-root user
- Set a password
- disown

Technically we should use JupyterHub. Maybe in the future.

### Launching the static site

```bash
wget -qO- https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
npm install -g http-server

cd workshop-config && sudo http-server -p 80 &
disown
```
