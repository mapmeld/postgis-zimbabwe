# Step 3

Do you know SQL?

Before continuing in the tutorial, I want to cover what we know about SQL. Depending
on skill level, this could be a participatory conversation on what queries we can
do, or it can be an introduction to SQL as a whole.

I also cover psycopg2 here so that everyone is comfortable writing SQL and Python
together.

### Installing and running locally

Install a Python library to help connect to any PostgreSQL database.

```bash
pip install psycopg2
```

TODO: SQLAlchemy? Is that a thing?

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

We can also improve performance in large datasets by adding an index. Let's say we
are adding an index to students' names:

```sql
CREATE INDEX name_index ON students (full_name);
```

### Learnings

- Given SQL experience, basic to intermediate SQL knowledge
- Reminder of how a common SQL JOIN would work (trains and train reviews)
- New functions and concepts (ST_AsGeoJSON, (even spatial JOIN?)) for PostGIS
