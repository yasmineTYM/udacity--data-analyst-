OpenStreetMap Project Data Wrangling with MangoDB
Tuyamei 

Map Area: Melbourne，Australia
https://mapzen.com/data/metro-extracts/metro/shanghai_china/  

1. Problems Encountered in the Map（audit.py）
After initially downloading a small sample size of the Charlotte area and running it against a provisional data.py file, I noticed three main problems with the data, which I will discuss in the following order:
  ●  Over ­abbreviated street names (“Baxter-Tooradin rd”)
  ● error spelling ("Maroondah Higway"should be "Highway")
  ● inconsistent postal code 
Over‐abbreviated Street Names
Once the data was imported to MongoDB, some basic querying revealed street name abbreviations and postal code inconsistencies. I updated all substrings in problematic address strings, such that “Baxter-Tooradin rd” becomes “Baxter-Tooradin road”.
inconsistent postal code 
right code format is the 4-digit number, while using the zipcodes.py, I find out that there are some other invalid format, such as 3-digit(380,385), or other wrong names 

2.Data Overview
1.mapparser.py was used to count occurrences of each tag, with a result:
{'bounds': 1,
 'member': 103615,
 'nd': 4581896,
 'node': 3898719,
 'osm': 1,
 'relation': 4729,
 'tag': 2314651,
 'way': 535477}
2.Before  processing the data and add it into your database, I use tags.py check the "k" value for each "<tag>" and see if there are any potential problems.
 "lower", for tags that contain only lowercase letters and are valid,
  "lower_colon", for otherwise valid tags with a colon in their names,
  "problemchars", for tags with problematic characters, and
  "other", for other tags that do not fall into the other three categories.
{'lower': 1722795, 'lower_colon': 589456, 'other': 2400, 'problemchars': 0}
3. users.py to calculate number of contributing users :
2604

5. audit.py to clean the problem of streetname  
6. use data.py to transform the data format from osm to json in order to put data into 

7. when import json file into mongodb, I met a lot of problems:
reference:http://www.runoob.com/mongodb/mongodb-dropdatabase.html
http://www.cnblogs.com/now-future/p/6507249.html
https://stackoverflow.com/questions/30953611/mongodb-error-validating-settings-only-one-positional-argument-is-allowed

8.use mongodb 
>>number of nodes and ways 

>>number of users 



3.other ideas 
>>the most common city name in our cities collection(mostcommoncity.py)
pipeline = [
            {"$match":{"name":{"$ne":None}}},
            {"$group":{
                    "_id":"$name",
                    "count":{"$sum":1}}},
            {"$sort":{"count":-1}},
            {"$limit":1}
            ]



>>>number of unique user (uniqueuser.py)
pipeline = [
        {
        '$group': {
            "_id": "$created.user"
        }},
        {
        '$group': {
            "_id": "unique users",
            "count": {"$sum": 1},
        }}]




>>>find the most fun place to have fun  (restplace.py)
pipeline = [
                {"$match":{"_id":{"$ne":None}}},
                {
                '$match': {

                    '$or': [
                        {"amenity": "restaurant"},
                        {"amenity": "bar"} ,
                        {"amenity": "pub"} ,
                        {"amenity": "cafe"} ,
                    ],
                    #"address.street": {'$exists': true},
                },
            },
            {
                '$group': {
                    "_id": "$address.street",
                    "count": {"$sum": 1},
                },
            },
            {
                '$sort': {
                    "count": -1
                }
            },
            {
                '$limit': 5,
            }
        ]
>>response:



>>>find the bank owning the most offices (office.py)
pipeline = [
                {"$match": {
                    "amenity": "bank"}},
                {'$group': {
                    "_id": "$name",
                    "count": {"$sum": 1}}},
                {'$sort': {
                    "count": -1}},
                {"$limit": 5}
        ]

>>>top 10 appearing amenities （topamenities.py）
pipeline = [
                {"$match":{"amenity":{"$exists":1}}}, 
                {"$group":{"_id":"$amenity",
                            "count":{"$sum":1}}}, 
                {"$sort":{"count": 1}}, 
                {"$limit":10}
                ]

>>>biggest religion (biggestreligion.py)
{"$match":{"amenity":{"$exists":1},
                          "amenity":"place_of_worship"}},
                {"$group":{"_id":"$religion", 
                        "count":{"$sum":1}}}, 
                {"$sort":{"count": -1}}, 
                {"$limit":1}

>>>most popular cuisines 
pipeline = [
                {"$match":{"amenity":{"$exists":1}, 
                        "amenity":"restaurant"}},   
                {"$group":{"_id":"$cuisine", 
                "count":{"$sum":1}}}, 
                {"$sort":{"count": -1}}, 
                {"$limit":5}
                ]

4.conclusion 
I think that the openstreet data can be joined with other kinds of data to provide more types of information, in order to allow other kinds of query.
Through the clean process, i found that the abbreviate names are not common , and the data is quite clean. Plus, if working together with a more robust data processor , it would be possible to have more cleaned data in openstreet. 
