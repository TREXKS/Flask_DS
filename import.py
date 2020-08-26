# Import csv to postgresql db

import psycopg2
import pandas as pd

conn = psycopg2.connect("host=localhost dbname=sensordata_db user=postgres password=TaSaR7!!")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS sensordata_db, users, units, systems, sensors, crops, sensor_unit, subs, sensor_info, crop_info;")


cur.execute('''CREATE TABLE users (
    uid SERIAL PRIMARY KEY NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL);''')

conn.commit()

cur.execute('''CREATE TABLE systems (
    id SERIAL PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    user_id int references users(uid));''')

conn.commit()

cur.execute('''CREATE TABLE units (
    id SERIAL PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    system_id int references systems(id),
    user_id int references users(uid));''')

conn.commit()

cur.execute('''CREATE TABLE sensordata_db (
    id SERIAL PRIMARY KEY NOT NULL,
    airTemp TEXT NOT NULL,
    airHumidity TEXT NOT NULL,
    waterTemp TEXT NOT NULL);''')

conn.commit()

cur.execute('''CREATE TABLE crops (
    id SERIAL PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    unit_id int references units(id));''')

conn.commit()

cur.execute('''CREATE TABLE sensors (
    id SERIAL PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    unit_id int references units(id));''')

conn.commit()

# Sensor Info

cur.execute('''CREATE TABLE sensor_info (
    id SERIAL PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    unit TEXT NOT NULL,
    manufacturer TEXT NOT NULL);''')

conn.commit()


# Crop Info
cur.execute('''CREATE TABLE crop_info (
    id SERIAL PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    soil TEXT NOT NULL,
    position TEXT NOT NULL,
    frost TEXT NOT NULL,
    feeding TEXT NOT NULL,
    companions TEXT NOT NULL,   
    spacing TEXT NOT NULL,
    sow TEXT NOT NULL,
    notes TEXT NOT NULL, 
    harvesting TEXT NOT NULL,
    troubleshooting TEXT NOT NULL);''')

conn.commit()

# cur.execute('''


#     # INSERT INTO crops (name, unit_id) VALUES ( 'tomatos', 0);
#     # INSERT INTO sensors (name, unit_id) VALUES ( 'pH', 0);


# ''')

# conn.commit()


df_sensor = pd.read_csv('./static/data/sensorData.csv', index_col=0)

for idx, u in df_sensor.iterrows():

    # Data cleaning


    q = cur.execute(
        '''INSERT INTO sensordata_db (airTemp, airHumidity, waterTemp) VALUES (%s,%s,%s)''',
        (u.airTemp, u.airHumidity, u.waterTemp)
    )
conn.commit()


df_sensor_info = pd.read_csv('./static/data/sensors.csv', index_col=0)

for idx, u in df_sensor_info.iterrows():

    # Data cleaning


    q = cur.execute(
        '''INSERT INTO sensor_info (name, unit, manufacturer) VALUES (%s,%s,%s)''',
        (u.name, u.Unit, u.Manufacturer)
    )
conn.commit()


df_crop_info = pd.read_csv('./static/data/plant_info.csv', index_col=0)

for idx, u in df_crop_info.iterrows():

    # Data cleaning


    q = cur.execute(
        '''INSERT INTO crop_info (name, soil, position, frost, feeding, companions, spacing, sow, notes, harvesting, troubleshooting) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
        (u.Name, u.Soil, u.Position, u.Frost, u.Feeding, u.Companions, u.Spacing, u.Sow, u.Notes, u.Harvesting, u.Troubleshooting)
    )
conn.commit()
        
   
cur.close()
conn.close()
