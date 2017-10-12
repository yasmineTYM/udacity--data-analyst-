"""
Complete the insert_data function to insert the data into MongoDB.
"""

import json

def insert_data(data, db):
    db.arachnid.insert(data)
    # Your code here. Insert the data into a collection 'arachnid'

    pass


if __name__ == "__main__":
    
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    with open('melbourne_australia.osm.json') as f:
        data = json.loads(f.read())
        insert_data(data, db)
        print db.arachnid.find_one()
