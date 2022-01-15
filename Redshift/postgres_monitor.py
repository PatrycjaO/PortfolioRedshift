# connect to RS via Python:  https://docs.aws.amazon.com/redshift/latest/mgmt/python-connect-examples.html
# AWS secretsmanager + Python: https://dashbird.io/blog/aws-secrets-manager-python/
from credentials import credentials
import psycopg2
import psycopg2.extras

def write2database():

    REGION, ARN, DB_HOST, DB_NAME, DB_USER, DB_PASS, DB_PORT = credentials()
    
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
        print('Connection succesful')
    except:
        print('Connection failed')

    cursor = conn.cursor()

    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS wind.energydata (
          timestamp integer,
          regionid integer NOT NULL,
          windpower_kwh real,
          solarpower_kwh real,
          windSpeed_m_per_s real,
          cloudcover_pct real,
          temperature_c real
          );
        """)
        print('Table created')
    except:
        print('Table not created')
    
    try:
        cursor.execute("""
        COPY wind.energydata
        FROM 's3://???/monitor_data/live_energydata.csv'
        IAM_ROLE 'arn:aws:iam::???:role/RedshiftS3'
        DELIMITER ','
        CSV
        IGNOREHEADER AS 1
        IGNOREBLANKLINES;
        """) 
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