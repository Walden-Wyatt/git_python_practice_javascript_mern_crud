


# import [Flask, jsonify and request] 
from flask import Flask, jsonify, request 

# import [ pymongo ]
from pymongo import MongoClient


# here let use create a url connection string 
url = "mongodb+srv://investob848:python_workings@cluster0.t8nusx1.mongodb.net/?retryWrites=true&w=majority&appName=cluster0"


# load MongoDB using [ MongoClient() ] class
client = MongoClient(url)

# now create a database 
db = client["abc"]

# now create a collection 
collection = db["abc"]



# Now let us create the server using [ @instance_Flask.route("/route_path", methods=["GET" OR "POST" OR "PATCH" OR "PUT" OR "DELETE"]) ] method
app = Flask(__name__)

@app.route("/", methods=["GET"])

# now let us create a Decorated method with custom name, inside the method we have specify the steps on how we are getting and displaying the object by returning it.
def getData():

    # Now try to access the key_value pairs which is inside the [ collection ] instance object using [ find() ] method.

    
    print(collection.find() )
    data_mongo = list(collection.find())

    # return data_mongo
     # Error :- [ TypeError: Object of type ObjectId is not JSON serializable ]
      # we are not allowed to use directly return the values which is present after typecasting using [list] 
    
    # return jsonify( data_mongo )
     # Error :- [ TypeError: Object of type ObjectId is not JSON serializable ]
      # we are not allowed to use directly return the values which is present after typecasting using [list] 
    

    print( data_mongo )
    # Output :-
      # [{'_id': ObjectId('65e492dd0d3c4fd4840669eb'), 'name': 'peter'}, {'_id': ObjectId('65e492f70d3c4fd4840669ec'), 'name': 'john'}]

    # Here we have type casted [ collection.find() ] methods one of the Key called [ "_id" ] to string datatype 
    for item in data_mongo:
        item["_id"] = str(item["_id"])


    print( data_mongo )
    # Output :-
     # [{'_id': '65e492dd0d3c4fd4840669eb', 'name': 'peter'}, {'_id': '65e492f70d3c4fd4840669ec', 'name': 'john'}]
    
    # Here when we use [ for loop ] for an List or Array those changes are taking place, in the above Example we have made chagnes only for Particular Properties, This changes does not affect the Entire List it only made changes only for that particular Property 
     # if you want to make changes for Particular Properties inside any List or Array make sure to use [ for loop ] below the list_variables make necessary changes ---> finally try to print the list_variable below the [ for loop ].
    



    
    # Here we can see that there is not Datatype called [ ObjectID ], here it has been replaced with [ string ] datatype

    # We are getting above error because we are only allowed to use or Type convert Python code to Json Object only when the code has Python Syntax's such as [ variables, arrays, functions, etc ]
      # If the Line of code or syntax has [ Class Object, Class Constructors, etc ] in this situation, those lines of code cannot be converted to [ JSON ] object because [ Classes ] are not Supported in JSON formats
      # before using [ jsonify() ] method and converting the Objects to JSON make sure there is not [ Class constructors, Class Codes, etc ]
        # if there are some codes use [ for loop or any loops ] , convert those Properties which has [ Class constructors ] to [ string datatype ]  



    return jsonify( {"data_mongo": data_mongo })

    # Now we are getting output without any errors.



# let us create a condition weather it has been run from Current File or not and render the datas.

if __name__ == "__main__":
    
# Now let us start the Server by using [ instance_Flask.run(debug=True) ] method
 # when you use the Project in the Development mode we can use [debug=True], During production mode we are not allowed to use it.

    app.run(debug=True)










