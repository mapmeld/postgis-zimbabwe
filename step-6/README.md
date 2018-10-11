# Step 5

Let's take the API a step further and make an election poll place app.

### Technical Setup

Launch the Flask server:

```bash
pip install flask psycopg2 simplejson
python3 serve.py
```

The server will now be available on http://localhost:5000/
When you edit serve.py, the server will restart!

### Interactive Tutorial

Previously we did some queries to find my local district and health facilities.
What if we wanted to do an election app?  In a real example, I would have tables for
candidates and districts. But you have been tasked with making an app which connects
me to my voting district.

What if I live near the border of a district? In some places, people
on one side of the street vote in one building, and people on the other side of
the street go somewhere else.

We need to:

- help user to type in an address (Google Maps + JS)
- send the address location to the database
- add a geospatial BUFFER around the districts, and let people know if there is
more than one potential answer

Fortunately PostGIS can help with geospatial calculations, including ST_Buffer.

Census circle/radius calculation

### Learnings
