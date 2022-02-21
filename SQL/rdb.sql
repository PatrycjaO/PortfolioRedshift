CREATE TABLE IF NOT EXISTS wind.facttable (
  regionid integer NOT NULL,
  region TEXT,
  lat real,
  lon real,
  weatheronline_sun integer,
  weatheronline_key integer
  );

CREATE TABLE IF NOT EXISTS wind.forecastdata (
  timestamp integer,
  regionid integer NOT NULL,
  temperature_c real,
  wind_speed_m_per_s real,
  wind_direction real,
  wind_gust real,
  cloudcover_pct real,
  weathercode integer
  );

CREATE TABLE IF NOT EXISTS wind.energydata (
  timestamp integer,
  regionid integer NOT NULL,
  windpower_kwh real,
  solarpower_kwh real,
  windSpeed_m_per_s real,
  cloudcover_pct real,
  temperature_c real
  );
