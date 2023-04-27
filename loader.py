import os
import json
import pymongo
from dataclasses import dataclass

@dataclass
class User:
    _id: str
    username: str
    email: str
    password: str
    ssn: str
    home_address: str
    age: int

# Connect to MongoDB using the connection string from the environment variable
client = pymongo.MongoClient(os.environ['MONGODB_CONNECTION_STRING'])
db = client.mydatabase
users_collection = db.users

# Retrieve the encrypted users from the MongoDB collection
raw_users = []
for user in users_collection.find():
    raw_users.append(user)

# Load the encrypted users into User objects
users = []
for raw_user in raw_users:
    user_dict = {}
    for key, value in raw_user.items():
        if key == '_id':
            # Convert the ObjectId to a string
            value = str(value)
        user_dict[key] = value
    user = User(**user_dict)
    users.append(user)

# Print the user objects
for user in users:
    print(user)
