"""Setup at app startup"""
import os
import sqlalchemy
from flask import Flask
from flask_cors import CORS
from yaml import load, Loader
# from sqlalchemy import URL



def init_connection_engine():
    """ initialize database setup
    Takes in os variables from environment if on GCP
    Reads in local variables that will be ignored in public repository.
    Returns:
        pool -- a connection to GCP MySQL
    """


    # detect env local or gcp
    if os.environ.get('GAE_ENV') != 'standard':
        variables = load(open("app.yaml"), Loader=Loader)
        env_variables = variables['env_variables']
        for var in env_variables:
            os.environ[var] = env_variables[var]

    # url_object = URL.create(
    #     "mysql+pymysql",
    #     username="root",
    #     password="cs411",  # plain (unescaped) text
    #     host="35.239.129.150",
    #     database="hireit",
    # )
    pool = sqlalchemy.create_engine(
        # url_object
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DB'),
            host=os.environ.get('MYSQL_HOST'),
            port=os.environ.get('MYSQL_PORT'),
        )
    )

    return pool


app = Flask(__name__)
CORS(app)
db = init_connection_engine()

# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
