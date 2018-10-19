# Step 2

Where do I find geo data for my website?

To make the tutorial as relevant as possible, I want to show how it's possible to
download information about my workshop country (in this case, Zimbabwe) and import
it into PostGIS.  This can be difficult to install and troubleshoot, so I might end
up showing most of this on the projector. Even if students cannot import data in the workshop, they can run future steps with the tables in the PostGIS cloud instance or the Jupyter notebooks.

All of these datasets will be imported into a PostGIS database (PostgreSQL + extensions).

Data will be used in the later steps.

### Installing and running locally

Install ogr2ogr by installing GDAL.

### Interactive Tutorial

Here we are talking about different data sources. I'm interested to hear where
PyZim members have found good geo-data before.

- Downloading Districts and Wards

I wanted to find districts and election ward boundaries. I was able to locate them
on data.humdata.org

I also found health data here, but it is not updated since 2007.

- Downloading OSM data

(TBD: brief intro to OpenStreetMap)

There are tons of community-built data on OpenStreetMap (OSM), including a monthly-updated, 340MB zipped buildings shapefile from https://data.humdata.org/dataset/hotosm_zwe_buildings

I used http://overpass-turbo.eu/ to download ~120 wells mapped on OpenStreetMap

```
node
  [man_made=water_well]
  ({{bbox}});
out;
```

You can also download tourism=attraction and tourism=hotel datasets.

Camps, hotels, and wells GeoJSON files are all available in this directory.

- Importing Geo CSVs

There's a good example in Step 4 of uploading a CSV which has latitude and longitude.

### Learnings

- Do members of PyZim know good sources for local open data?
- What is OpenStreetMap?
- How can I get data to make quality websites?
- Links for installing ogr2ogr on my computer
