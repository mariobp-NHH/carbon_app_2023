from flask import Flask
import boto3
from botocore.exceptions import ClientError

application = Flask(__name__)

secret_name = "carbon-app-2023-secret-key"
region_name = "eu-north-1"

# Create a Secrets Manager client
session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name=region_name
)

try:
    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )
except ClientError as e:
    # For a list of exceptions thrown, see
    # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    raise e

# Decrypts secret using the associated KMS key.
secret = get_secret_value_response['SecretString']

# Your code goes here.
application.config['SECRET_KEY'] = secret    

# application.config['SECRET_KEY'] = '1dcdsdsd5b2ffa3afggfdgfdgfdgf090dfc34f343rffe845fd'


from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(users)

