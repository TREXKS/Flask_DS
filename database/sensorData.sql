#sensors table

DROP TABLE IF EXISTS sensors;
DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE sensors {
  id INT primary key;
  airTemp VARCHAR(255) NOT NULL;
  airHumidity VARCHAR(255) NOT NULL;
  waterTemp VARCHAR(255) NOT NULL;
}

CREATE TABLE users (
    uid serial NOT NULL PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE systems (
    id serial NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
);

CREATE TABLE units (
    id serial NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    SystemID int references System(id))

);

CREATE TABLE sensors (
    id serial NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
);

CREATE TABLE crops (
    id serial NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
);
