const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const compression = require('compression');

const pg = require('read-only-pg');

var app = express();

app.use(express['static'](__dirname + '/static'));
app.use(bodyParser.json({ limit: '50mb' }));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(compression());
app.use(cookieParser());

app.post('/sql', (req, res) => {
  return res.json({ sql: req.body.sql })
});

app.listen(80, () => {
  console.log('app is running');
});

module.exports = app;
