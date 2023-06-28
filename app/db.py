"""
Set up connection to our Astra DB cluster by importing environmental variables 
from config.py

"""
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.cqlengine.connection import register_connection, set_default_connection
import pathlib
import os
from . import config

settings = config.get_settings() # import settings


ASTRA_DB_CLIENT_ID = settings.db_client_id # get client id 
ASTRA_DB_CLIENT_SECRET = settings.db_client_secret # get client secret 

BASE_DIR = pathlib.Path(__file__).parent # get the parent folder of this file, which is "app"
CLUSTER_BUNDLE = str(BASE_DIR / "ignored" / 'connect.zip') # navigate to the cluster

def get_cluster(): # get cluster
    cloud_config= {'secure_connect_bundle': CLUSTER_BUNDLE}
    auth_provider = PlainTextAuthProvider(ASTRA_DB_CLIENT_ID, ASTRA_DB_CLIENT_SECRET)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)

    return cluster 

def get_session(): # connect cluster to local session
    cluster = get_cluster()
    session = cluster.connect()
    register_connection(str(session), session = session)
    set_default_connection(str(session))

    return session 


