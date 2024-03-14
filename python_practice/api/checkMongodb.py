

print("hello")



from pymongo import MongoClient


client = MongoClient( "mongodb+srv://investob848:python_workings@cluster0.t8nusx1.mongodb.net/?retryWrites=true&w=majority&appName=cluster0")

# print(client)

db = client["abc"]

# print( db )

collection = db["abc"]
# print(collection )

# make sure to use [ collection.find() ], because all the values inside the collection are iterables, which must be stored inside the list

print(collection.find())
# Here we are tring to convert the datatype which is present inside [ collection.find() ] to the List Datatype only then we can access the Values 
  # ** We are allowed to convert [ Cursor Object ] Datatype to [ List ] Datatype we will not get any Errors. 
datas_collection = list(collection.find())
print( datas_collection )


# Output :-

    # hello

    # <pymongo.cursor.Cursor object at 0x0000015BFEC24BC0>
     # when we try to print the [collection.find()] method outside the [list()] object we will get cursor object (which will be list)
      # if you want to get the actual values from the Cursor object we have print it inside the [ list() ] object.


    # [{'_id': ObjectId('65e492dd0d3c4fd4840669eb'), 'name': 'peter'}, {'_id': ObjectId('65e492f70d3c4fd4840669ec'), 'name': 'john'}]
       # here we printed [ collection.find() ] method inside the [ list() ] object we got this Output, we have converted the "cursor object" to "List datatype".

















