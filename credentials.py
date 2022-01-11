# https://dashbird.io/blog/aws-secrets-manager-python/
import awswrangler.secretsmanager as sm

# credentials
REGION = sm.get_secret_json('REGION').get('region_key')
ARN = sm.get_secret_json('ARN').get('arn_key')
DB_HOST = sm.get_secret_json('DB_HOST').get('db_host_key')
DB_NAME = sm.get_secret_json('DB_NAME').get('db_name_key')
DB_USER = sm.get_secret_json('DB_USER').get('db_user_key')
DB_PASS = sm.get_secret_json('DB_PASS').get('db_pass_key')
DB_PORT = sm.get_secret_json('DB_PORT').get('db_port_key')
