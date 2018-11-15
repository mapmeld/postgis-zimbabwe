const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const compression = require('compression');
const cors = require('cors');

const ropg = require('read-only-pg');
client = new ropg.Client({
  database: 'pyzim',
  user: 'py',
  host: 'localhost',
  password: 'zim'
});
client.connect((err) => {
  console.log(err || 'verified read-only')
});

var app = express();

app.use(cors());
app.use(express['static'](__dirname + '/static'));
app.use(bodyParser.json({ limit: '50mb' }));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(compression());
app.use(cookieParser());

app.post('/sql', (req, res) => {
  client.query(req.body.sql, (err, response) => {
    return res.json(err || response.rows);
  });
});

app.listen(8000, () => {
  console.log('app is running');
});

module.exports = app;
