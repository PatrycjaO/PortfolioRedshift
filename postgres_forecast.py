from credentials import credentials
import psycopg2
import psycopg2.extras
import prefect
from prefect import task, Flow

@task
def write2database():

    REGION, BUCKET, ARNRSS3, DB_HOST, DB_NAME, DB_USER, DB_PASS, DB_PORT = credentials()


    copy = "COPY wind.forecastdata FROM 's3://" +BUCKET +"/weather_forecast/daily_weatherforecast.csv' IAM_ROLE '" +ARNRSS3 +"' DELIMITER ',' CSV IGNOREHEADER AS 1 IGNOREBLANKLINES;"

    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
        print('Connection succesful')
    except:
        print('Connection failed')

    cursor = conn.cursor()

    try:
        cursor.execute("""
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
        
        """)
        print('Table created')
    except:
        print('Table not created')
    
    try:
        cursor.execute(copy) 

        print("Write successfull!")

    except:
        print("Write not successfull!")
        
    conn.commit()
    cursor.close()
    conn.close()

try:
    write2database()
except:
    print("Error writing csv to database")

flow = Flow("postgres_forecast", tasks=[write2database])
flow.register(project_name="Redshift")