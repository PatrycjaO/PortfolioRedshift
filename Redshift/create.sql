-- create schema
CREATE SCHEMA IF NOT EXISTS wind;

-- create tables in order to load in available data in .csv format
DROP TABLE IF EXISTS wind.forecastdata;
CREATE TABLE wind.forecastdata (
  timestamp TEXT,
  regionid TEXT,
  temperature_c TEXT,
  wind_speed_m_per_s TEXT,
  wind_direction TEXT,
  wind_gust TEXT,
  cloudcover_pct TEXT,
  weathercode TEXT
  );


DROP TABLE IF EXISTS wind.energydata;
CREATE TABLE wind.energydata (
  timestamp TEXT,
  regionid TEXT,
  windpower_kwh TEXT,
  solarpower_kwh TEXT,
  windSpeed_m_per_s TEXT,
  cloudcover_pct TEXT,
  temperature_c TEXT
  );

DROP TABLE IF EXISTS wind.facttable;
CREATE TABLE wind.facttable (
  regionid TEXT,
  region TEXT,
  lat TEXT,
  lon TEXT,
  weatheronline_sun TEXT,
  weatheronline_key TEXT
  );