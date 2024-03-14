



from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# uri = "mongodb+srv://investob848:pytho_workings@cluster0.t8nusx1.mongodb.net/?retryWrites=true&w=majority&appName=cluster0"
uri = "mongodb+srv://investob848:python_workings@cluster0.t8nusx1.mongodb.net/?retryWrites=true&w=majority&appName=cluster0"

# Create a new client and connect to the server
 
# Here we have loaded [ MongoClient() ] Class, from client class we have to get inside databases 
 # Inside [ client ] - the datatype value which gets stored inside "client" object is Dictionary object
  # so if you want to access some values from inside [ client ] we have to use Bracket Notation ( [] ).
# client = MongoClient(uri, server_api=ServerApi('1'))

client = MongoClient(uri)
# here the arguement for [ MongoClient() ] must a Valid URL, where the url has appropriate [ UserName and Password ]
 # Error :-  [ Traceback (most recent call last): ]
   # when there is an Error in the URL string we will get the above error, Mistake can be [ wrong password, username, or any character in the string is missing, etc ].
    # Here the error is we did not used correct password in the URL [ uri = "mongodb+srv://investob848:pytho_workings@cluster0.t8nusx1.mongodb.net/?retryWrites=true&w=majority&appName=cluster0" ]

# ----------


# Here we have Loaded [ Database() ] class, from [ MongoClient() ] class Instance Object
 # we have created instance for [ Database() ] class and assigned it to a Variable called [ db ]


# db = client["abcd"]
db = client["abc"]
 # Here the value for [ client["database_Name"] ] must be appropriate database Name, Make sure to use Only Database Name not the [ Organizations or Projects ] name 
  # You get Database name with this Path go to [ Organization Name  -> Project Name -->[ load Collections ] --> Database Name --> Collection Name ---> Index Name (to access specific key values) ]
 
 # Error or Output :-  # [ list index out of range ]
  # we get this output when we try to wrong Database name which is not present inside the Project, we have to use Correct Database which is present inside the Project.
  # Error :- [ db = client["abcd"] ] ----> here there is no database called "abcd" inside the python_workings project, we have only 1 database called [ "abc" ].



# -----------



# dic = {"ky": 1}
# print( dic["ky"] )

# Here we have Loaded [ Collection() ] class, from [ Database() ] class Instance Object 
 # we have created instance for [ Collection() ] class and assigned it to a Variable called [ collection ] 
# collection = db["abcd"]
collection = db["abc"]

 # Here the value for db [ db["Collection_Name"]] must be collection Name, because inside the Database we will be tring to Access the Collections
  # Make sure to pass appropriate Collection Name, if you pass wrong collection name you will get the below error.

 # Error or Output :-  # [ list index out of range ]
  # we get this output when we try to wrong Collection name which is not present inside the Database, we have to use Correct Collection which is present inside the Database.
  # Error :- [ collection = db["abcd"] ] ----> here there is no collection called "abcd" inside the python_workings project, we have only 1 Collection called [ "abc" ].



# ------------


data_from_db = list(collection.find())




# Make sure to use [try..expect] block so that it will easy to catch the Errors and display, where our program will not get Interrupted or Crashed.

# Send a ping to confirm a successful connection
try:
    # client.admin.command('ping') # This line of code is not so Important we can use or we can even stop using it.
    print("Pinged your deployment. You successfully connected to MongoDB!")
    # print(client)
     # Output :-
        # MongoClient(host=['ac-bkdiiqn-shard-00-01.t8nusx1.mongodb.net:27017', 'ac-bkdiiqn-shard-00-00.t8nusx1.mongodb.net:27017', 'ac-bkdiiqn-shard-00-02.t8nusx1.mongodb.net:27017'], document_class=dict, tz_aware=False, connect=True, retrywrites=True, w='majority', appname='cluster0', authsource='admin', replicaset='atlas-kpehk8-shard-0', tls=True, server_api=<pymongo.server_api.ServerApi object at 0x0000025B35B2A900>)
      # Here we can see that Client has returned a Class called [ MongClient() ] by passing appropriate Arguements for it

# -------
    
    # print(db)

    # Output :- 
      # Database(MongoClient(host=['ac-bkdiiqn-shard-00-01.t8nusx1.mongodb.net:27017', 'ac-bkdiiqn-shard-00-00.t8nusx1.mongodb.net:27017', 'ac-bkdiiqn-shard-00-02.t8nusx1.mongodb.net:27017'], document_class=dict, tz_aware=False, connect=True, retrywrites=True, w='majority', appname='cluster0', authsource='admin', replicaset='atlas-kpehk8-shard-0', tls=True, server_api=<pymongo.server_api.ServerApi object at 0x0000019D61DAA900>), 'abc')
      # Here we can see that [ Database() ] Class has been Loaded, where the arugements are passed automatically, 


# -------

    # print(collection)
     # Output :-
      # Collection(Database(MongoClient(host=['ac-bkdiiqn-shard-00-00.t8nusx1.mongodb.net:27017', 'ac-bkdiiqn-shard-00-02.t8nusx1.mongodb.net:27017', 'ac-bkdiiqn-shard-00-01.t8nusx1.mongodb.net:27017'], document_class=dict, tz_aware=False, connect=True, retrywrites=True, w='majority', appname='cluster0', authsource='admin', replicaset='atlas-kpehk8-shard-0', tls=True), 'abc'), 'abc')
     # here we can see that we have Loaded [ Collection ] Class


# --------

    # print(data_from_db)
    # Output :-
      # [{'_id': ObjectId('65e492dd0d3c4fd4840669eb'), 'name': 'peter'}, {'_id': ObjectId('65e492f70d3c4fd4840669ec'), 'name': 'john'}]
     # Now we get List Object, inside the List Object we have a Dictionary (key_value pairs ), 
     # Here is where we have actual Values which is present inside the MongoDB, This is the value which we have to fetch and set in the [ GET ] method, ----> from [ GET ] method backend server, we have to Fetch in the From end.  

# -------------

    # print(data_from_db[0] )
     # here we have accssed object which is present in the [0]th index Position, whatever object is present in the 0th index position is displayed 
      # if we want to access the Object which is present inside the Specific Index position we have use Bracket notation or Index operator.




# ---------------


    print(data_from_db[0]["name"])

except Exception as e:
    print(e)



# ---------------------------------
    
# Errors :-
    
  # 1. [ ile "C:\Users\user\Desktop\python_practice\api\mongoDb_connection_check.py", line 18, in <module>
        # client = MongoClient(uri)]
   # When you try to execute this file without connecting to Internet we will get this Error, because we have written MongoDB code which will fetch the database and load inside our file, when this has to happen we have connect to Connect becuase getting datas from MongoDB requires Internet connection.
  










