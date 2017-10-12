OpenStreetMap Project Data Wrangling with MangoDB<br>
=====
Tuyamei 

Map Area: Melbourne，Australia<br>
https://mapzen.com/data/metro-extracts/metro/melbourne_australia/<br>
the reason I chose Melbourne to analyze is that my boyfriend will go to australia for further study, so I want to explore some information about this place.<br>

1. Problems Encountered in the Map（audit.py）<br>
---------------------------------------------
After initially downloading a small sample size of the Charlotte area and running it against a provisional data.py file, I noticed three main problems with the data, which I will discuss in the following order:<br>
  (1)Over abbreviated street names (“Baxter-Tooradin rd”)<br>
  Once the data was imported to MongoDB, some basic querying revealed street name abbreviations and postal code inconsistencies. I updated all substrings in problematic address strings, such that “Baxter-Tooradin rd” becomes “Baxter-Tooradin road”.<br>
  (2)error spelling ("Maroondah Higway"should be "Highway")<br>
  (3)inconsistent postal code <br>
  right code format is the 4-digit number, while using the zipcodes.py, I find out that there are some other invalid format, such as 3-digit(380,385), or other wrong names <br>

2.Data Overview<br>
---------------------
1.mapparser.py was used to count occurrences of each tag, with a result:<br>
>>>response:
{'bounds': 1,<br>
 'member': 103615,<br>
 'nd': 4581896,<br>
 'node': 3898719,<br>
 'osm': 1,<br>
 'relation': 4729,<br>
 'tag': 2314651,<br>
 'way': 535477}<br>
2.Before  processing the data and add it into your database, I use tags.py check the "k" value for each "<tag>" and see if there are any potential problems.<br>
 "lower", for tags that contain only lowercase letters and are valid,<br>
  "lower_colon", for otherwise valid tags with a colon in their names,<br>
  "problemchars", for tags with problematic characters, and<br>
  "other", for other tags that do not fall into the other three categories.<br>
>>response<br>
{'lower': 1722795, 'lower_colon': 589456, 'other': 2400, 'problemchars': 0}<br>
3. users.py to calculate number of contributing users :<br>
>>resopnse<br>
  2604<br>

5. audit.py to clean the problem of streetname <br> 
6. use data.py to transform the data format from osm to json in order to put data into <br>

7. when import json file into mongodb, I met a lot of problems:<br>
reference:http://www.runoob.com/mongodb/mongodb-dropdatabase.html<br>
http://www.cnblogs.com/now-future/p/6507249.html<br>
https://stackoverflow.com/questions/30953611/mongodb-error-validating-settings-only-one-positional-argument-is-allowed<br>

8.use mongodb <br>
>>number of nodes and ways <br>

>>number of users <br>



3.other ideas <br>
>>the most common city name in our cities collection(mostcommoncity.py)<br>
pipeline = [<br>
            {"$match":{"name":{"$ne":None}}},<br>
            {"$group":{<br>
                    "_id":"$name",<br>
                    "count":{"$sum":1}}},<br>
            {"$sort":{"count":-1}},<br>
            {"$limit":1}<br>
            ]<br>



>>>number of unique user (uniqueuser.py)<br>
pipeline = [<br>
        {<br>
        '$group': {<br>
            "_id": "$created.user"<br>
        }},<br>
        {<br>
        '$group': {<br>
            "_id": "unique users",<br>
            "count": {"$sum": 1},<br>
        }}]<br>




>>>find the most fun place to have fun  (restplace.py)<br>
pipeline = [<br>
                {"$match":{"_id":{"$ne":None}}},<br>
                {<br>
                '$match': {<br>

                    '$or': [<br>
                        {"amenity": "restaurant"},<br>
                        {"amenity": "bar"} ,<br>
                        {"amenity": "pub"} ,<br>
                        {"amenity": "cafe"} ,<br>
                    ],<br>
                    #"address.street": {'$exists': true},<br>
                },<br>
            },<br>
            {<br>
                '$group': {<br>
                    "_id": "$address.street",<br>
                    "count": {"$sum": 1},<br>
                },<br>
            },<br>
            {<br>
                '$sort': {<br>
                    "count": -1<br>
                }<br>
            },<br>
            {<br>
                '$limit': 5,<br>
            }<br>
        ]<br>
>>response:<br>



>>>find the bank owning the most offices (office.py)<br>
pipeline = [<br>
                {"$match": {<br>
                    "amenity": "bank"}},<br>
                {'$group': {<br>
                    "_id": "$name",<br>
                    "count": {"$sum": 1}}},<br>
                {'$sort': {<br>
                    "count": -1}},<br>
                {"$limit": 5}<br>
        ]<br>

>>>top 10 appearing amenities （topamenities.py）<br>
pipeline = [<br>
                {"$match":{"amenity":{"$exists":1}}}, <br>
                {"$group":{"_id":"$amenity",<br>
                            "count":{"$sum":1}}}, <br>
                {"$sort":{"count": 1}}, <br><br>
                {"$limit":10}<br>
                ]

>>>biggest religion (biggestreligion.py)<br>
{"$match":{"amenity":{"$exists":1},<br>
                          "amenity":"place_of_worship"}},<br>
                {"$group":{"_id":"$religion", <br>
                        "count":{"$sum":1}}}, <br>
                {"$sort":{"count": -1}}, <br>
                {"$limit":1}<br>

>>>most popular cuisines <br>
pipeline = [<br>
                {"$match":{"amenity":{"$exists":1}, <br>
                        "amenity":"restaurant"}},   <br>
                {"$group":{"_id":"$cuisine", <br>
                "count":{"$sum":1}}}, <br>
                {"$sort":{"count": -1}}, <br>
                {"$limit":5}<br>
                ]<br>

4.conclusion <br>
------
I think that the openstreet data can be joined with other kinds of data to provide more types of information, in order to allow other kinds of query.
Through the clean process, i found that the abbreviate names are not common , and the data is quite clean. Plus, if working together with a more robust data processor , it would be possible to have more cleaned data in openstreet. 
