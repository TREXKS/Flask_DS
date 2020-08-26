# Import csv to postgresql db

import psycopg2
import pandas as pd

conn = psycopg2.connect("host=localhost dbname=sensordata_db user=postgres password=#######")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS sensordata_db, users, units, systems, sensors, crops, sensor_unit;")

cur.execute('''CREATE TABLE users (
    uid SERIAL PRIMARY KEY NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL);''')

conn.commit()

cur.execute('''CREATE TABLE sensordata_db (
    id SERIAL PRIMARY KEY NOT NULL,
    airTemp TEXT NOT NULL,
    airHumidity TEXT NOT NULL,
    waterTemp TEXT NOT NULL);''')

conn.commit()

cur.execute('''CREATE TABLE sensors (
    id SERIAL PRIMARY KEY NOT NULL,
    name TEXT NOT NULL);''')

conn.commit()

cur.execute('''CREATE TABLE systems (
    id SERIAL PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    units VARCHAR(50) NOT NULL);''')

conn.commit()


cur.execute('''CREATE TABLE crops (
    id SERIAL PRIMARY KEY NOT NULL,
    name TEXT NOT NULL);''')

conn.commit()

cur.execute('''CREATE TABLE units (
    id SERIAL PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    systemid int references systems(id),
    sensorid int references sensors(id),
    cropid int references crops(id));''')

conn.commit()

cur.execute('''CREATE TABLE sensor_unit (
    sensor_id int REFERENCES sensors (id) ON UPDATE CASCADE ON DELETE CASCADE,
    unit_id int REFERENCES units (id) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT id PRIMARY KEY (sensor_id, unit_id));''')

conn.commit()

cur.execute('''


    INSERT INTO crops (name) VALUES ('tomato');
    INSERT INTO crops (name) VALUES ('basil');
    INSERT INTO crops (name) VALUES ('wheat');

    INSERT INTO sensors (name) VALUES ( 'pH');
    INSERT INTO sensors (name) VALUES ( 'humidity');

    INSERT INTO units (name, sensorid, cropid) VALUES ('humidity', 1, 1);

''')

conn.commit()


df_sensor = pd.read_csv('./data/sensorData.csv', index_col=0)

for idx, u in df_sensor.iterrows():

    # Data cleaning


    q = cur.execute(
        '''INSERT INTO sensordata_db (airTemp, airHumidity, waterTemp) VALUES (%s,%s,%s)''',
        (u.airTemp, u.airHumidity, u.waterTemp)
    )
    conn.commit()

cur.close()
conn.close()
