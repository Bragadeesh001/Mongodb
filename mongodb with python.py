#importing the libraries
import pymongo

#creating the client
client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')

#creating database
mydb=client['Student']

#creating collection i.e table name
collection=mydb.studentdetails

#creating records which is stored in collection
records={
    'firstname':'Bragadeesh',
    'lastname': 's',
    'department':'Data science',
}

#inserting this record to the collection
collection.insert_one(records)

#creating multiple records
records=[{
    'firstname':'gowtham',
    'lastname': 'MW',
    'department':'Teaching',
},{
    'firstname':'Sree lekha',
    'lastname': 'G',
    'department':'Python developer',
}]

#inserting many records
collection.insert_many(records)