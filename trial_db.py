import pymongo
from pymongo import MongoClient
import arrow
import sys

import secrets.admin_secrets
import secrets.client_secrets

MONGO_CLIENT_URL = "mongodb://{}:{}@{}:{}/{}".format(
    secrets.client_secrets.db_user,
    secrets.client_secrets.db_user_pw,
    secrets.admin_secrets.host, 
    secrets.admin_secrets.port, 
    secrets.client_secrets.db)

try: 
    dbclient = MongoClient(MONGO_CLIENT_URL)
    db = getattr(dbclient, secrets.client_secrets.db)
    print("Got database")
    collection = db.dated
    print("Using sample collection")
except Exception as err:
    print("Failed")
    print(err)
    sys.exit(1)

#prints out all of the records in the database
#TODO: This is how Sam does it. Use as Guide
records = [ ] 
for record in collection:
   print(record)

