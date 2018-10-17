# Step 1

What kind of website uses PostGIS?

As an introduction to the workshop, I want to show some examples of how
people use online maps.  These examples will use local datasets (in this
case, Zimbabwe).

All of these examples will be powered by a Python server (Flask framework)
and PostGIS database (PostgreSQL + extensions).

Everything will be explained in the later steps.

### Installing and running locally

If you are setting up the database from scratch, see workshop-config

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
