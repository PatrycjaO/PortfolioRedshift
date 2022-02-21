# connect to RS via Python:  https://docs.aws.amazon.com/redshift/latest/mgmt/python-connect-examples.html
# AWS secretsmanager + Python: https://dashbird.io/blog/aws-secrets-manager-python/
import psycopg2
import psycopg2.extras
import json
import os

def lambda_handler(event, context):
    
    copy = "COPY wind.forecastdata FROM 's3://" +os.environ.get("BUCKET") +"/weather_forecast/daily_weatherforecast.csv' IAM_ROLE '" +os.environ.get("ARNRSS3") +"' DELIMITER ',' CSV IGNOREHEADER AS 1 IGNOREBLANKLINES;"
    
    try:
        conn = psycopg2.connect(dbname=os.environ.get("DB_NAME"), user=os.environ.get("DB_USER"), password=os.environ.get("DB_PASS"), host=os.environ.get("DB_HOST"), port=int(os.environ.get("DB_PORT")))
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
        
        conn.commit()
        print("cursor committed")
        
    except:
        print('Table not created')
    
    try:
        cursor.execute(copy) 
        print("Write successfull!")
        conn.commit()
        print("connection committed")

    except:
        print("Write not successfull!")
        
    conn.commit()
    print("connection committed a")
    
    cursor.close()
    print("cursor closed")
    
    conn.close()
    print("connecion closed")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
