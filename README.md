SETUP:

psql
CREATE DATABASE sensordata_db;

set
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/sensordata_db'

*note: if you have a password on sql you need to add that here*
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:PASSWORD@localhost:5432/sensordata_db'

*and here in import.py*
conn = psycopg2.connect("host=localhost dbname=sensordata_db user=postgres password=PASSWORD")

run:
python import.py
flask run
