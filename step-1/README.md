# Step 1

What kind of website uses PostGIS?

As an introduction to the workshop, I want to show some examples of how
people use online maps.  These examples will use local datasets (in this
case, Zimbabwe).

All of these examples will be powered by a Python server (Flask framework)
and PostGIS database (PostgreSQL + extensions).

Everything will be explained in the later steps.

### Installing and running locally

Install Python, pip, PostgreSQL, and PostGIS extensions.

Then follow these instructions to set up the database and read-only user:

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

Import the trains table (TBD: replace with large CSV import)

```
DROP TABLE trains; # overwrite any old trains table
CREATE TABLE trains (start TEXT, finish TEXT, seats INT, id INT, price FLOAT);
INSERT INTO trains (start, finish, seats, id, price) VALUES ('Harare', 'Victoria Falls', 100, 1, 100);
INSERT INTO trains (start, finish, seats, id, price) VALUES ('Harare', 'Bulawayo', 25, 2, 10);
```

Launch the Flask server:

```bash
pip install flask psycopg2
python3 serve.py
```

The server will now be available on http://localhost:5000/
When you edit serve.py, the server will restart!

### Interactive Tutorial

### Learnings

- Is your computer set up to run a Python server and database?
- What are your PostgreSQL connection parameters?
- Concept of Connection and Cursor objects
- Read-only user py:zim for this tutorial (see /messy and /messy2)
- Responding in JSON format

TBD: currently py:zim can create their own tables
