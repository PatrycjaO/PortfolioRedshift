# https://dashbird.io/blog/aws-secrets-manager-python/
import awswrangler.secretsmanager as sm

# credentials
def credentials():
	REGION = sm.get_secret_json('REGION').get('region_key')
	ARNRSS3 = sm.get_secret_json('ARNRSS3').get('arnrss3_key')
	BUCKET = sm.get_secret_json('BUCKET').get('bucket_key')
	DB_HOST = sm.get_secret_json('DB_HOST').get('db_host_key')
	DB_NAME = sm.get_secret_json('DB_NAME').get('db_name_key')
	DB_USER = sm.get_secret_json('DB_USER').get('db_user_key')
	DB_PASS = sm.get_secret_json('DB_PASS').get('db_pass_key')
	DB_PORT = sm.get_secret_json('DB_PORT').get('db_port_key')
	return REGION, BUCKET, ARNRSS3, DB_HOST, DB_NAME, DB_USER, DB_PASS, DB_PORT


