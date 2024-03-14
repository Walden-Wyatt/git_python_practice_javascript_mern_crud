



# Backend Server 


from flask import Flask, jsonify, request


# -------------------------------------------------


# let us import [CORS] from [flask_cors] this is mainly used to share and get the datas from differenct servers such as as Frontend(react server) and Backend(flask server )
from flask_cors import CORS



# ----------------------------------- 

from bson import ObjectId


# -------------------------------------------------


# Now let us write Database code,
 # The data which we got from the Frontend --> Those datas will be sent to the Database such as [MongoDB, MySQL]

# Import [pymongo, MongoCliet ] -- this the Class which we will be using to connect to the MongoDB database 
from pymongo import MongoClient

# Now let us load one of the Project from Mongodb, Projects might have [ Databases --> inside database "Collections" --> inside collections "Appropriate methods to perform CRUD (Create, Read, Update, Delete) operations"]
url = "mongodb+srv://investob848:python_workings@cluster0.t8nusx1.mongodb.net/?retryWrites=true&w=majority&appName=cluster0"

# Now "client" will have Instace of [ Dec2 --> python_workings ] which is one of the Project inside MongoDB 
client = MongoClient(url)

# [db] -- here "db" will have Class called [ hobby ] which is actually a database --> This database will be present inside [ client ] project instance which is above 
 # note that we have used bracket notation which means the [client] has an Instance of Dictionary
db = client["hobby"]


# [collection] = here inside "collection" variable there will Collection of documents will be loaded 
 # documents are nothing but Objects which has [Key_Value] pairs which we store inside the Collection, Individual set of datas which we get from server will be stored in the document(other for Objects ).
collection = db["sunday2"]


# Now "collection" will have built-in methods and Properties by using it we can perform CRUD Operations inside the database such as [ Create, Read, Update, Delete, etc ].



# *** Imporatant Point ****** 

  # 1. Weather you login to MongoDB or nor from the Browser it will not affect any of the Operation which we perform in our Applications using [MongoDB Methods ]
    # Any Operations means operations such as [GET, POST, PUT, DELETE, etc ] ----> methods means [ collection.find(), collection.insert_one(), colection.update_one(), collection.delete_one(), etc ]
    # do not waste your time checking MongoDB Website for some Issues which you get into your application CRUD Operations 
     # Only 2 things which you have check or make changes is :- 
      # 1. Provide which all IP Addresses can access the MongoDB Database 
      # 2. Check and provide for Access to Database based on the Person Email address.





# -------------------------------------------------



app = Flask(__name__)

# now pass [app] server as an arguement for [CORS ] class
CORS(app,
     origins="*" # this tills the python flask server to allow any type of requests inside it, requests such as [ GET, POST, PUT, DELETE ]
     )




# -------------------------------------


# get route 
@app.route("/")
def get_data():
    
    # here by usig [collection] let us get the data which is inside the [MongoDB ] database 

   # data = collection.find()
    # [find()] method will return a cursor object Class ---> Inside this cursor our datas which is inside the class will be stored 
      # To access this Cursor object we have to convert it into a List datatype, cursor objects can be converted into list it is allowed in python
    
    # Convert to list datatype 

    data = list( collection.find( ) )


    # print( data )
    # Output :-
    # [{'_id': ObjectId('65edaabb3dae9fd36ad778d8'), 'firstname': 'albert', 'lastname': 'martin', 'hobby': 'gamming'}]
     # This is the Output before we converted [ObjectId] to [string]


    # change [ObjctId() ] datatype to [ string ], because when we try to convert the data to JSON object ObjectId cannot be converted its because only [String] datatype can be converted to JSON 
      # We are only allowed to Sent and Receive JSON object to the Frontend and backend 
    # let us romove using [for] loop

    for i in data:
        i["_id"] = str(i["_id"])

    # Output :-
    # [{'_id': '65edaabb3dae9fd36ad778d8', 'firstname': 'albert', 'lastname': 'martin', 'hobby': 'gamming'}]
         # this is the Output after we have converted the [ObjectId] to [string]
    # note that [for] loop has only changed the Datatype of [ObjectID] rest all the things inside the [ List ] is the same, if we want to change specific properties name , datatype value of the properties from the List of Objects(Dictionaries) we can use [for] loop and specify exactly what we want to change.
    # print(data)


# Now let us convert [data] to JSON  using [ jsonify ] and sent it to the frontend 
 # Make sure to use [return] keyword else we might get error
    return jsonify(data)



# ------------------------------------


# Let us create the [POST] Route to send the datas to the MongoDB Database


@app.route("/",
           methods=["POST"] # For [post, put and delete ] we have pass 2nd arguement called [methods] and specify what Operation we are going to perform, we can even specify multiple Methods inside the single route that is inside the list object which we passed as a value for [methods], methos includes [POST, GET, DELETE, PUT]
           )
def postData():

    print("Data POSTED Successfully")

    # TypeError: The view function for 'postData' did not return a valid response. The function either returned None or ended without a return statement.
      # we get the above error when we do not use [ return ] keyword inside the [ post ] route, This same error will also occur when we do not use for [ GET, DELETE, UPDATE ] routes,make sure to use "return" keyword to return some datas.
      # even if you just use [return] but do not provide any values after the return -- > you will get this error.
    # return "hello"  or return 

    # now let us create a Post which will be sending some datas to MongoDB database, we will acheive this by using [insert_one] method 

      # First let us load the data which was sent by the Frontend --> To load the data we will be using [ request.get_json() ] method 
       # when we send some data using Post request All the Datas will be wrapped inside the "URL" --> inside case of POST request those data are not visible in the URL, incase of GET request we can see those datas.
    load_Frontend_Data = request.get_json() # Here Object might have been loaded [ { key: "values" }]

    # print(load_Frontend_Data)

    # now let us send the above data to the MongoDB Database using [ insert_one() ] method 
    collection.insert_one(load_Frontend_Data)


    # return load_Frontend_Data
    return "Data POSTED Successfully"

    # Now POST Route is done


# ----------------------------------------------------------



# Delete Route 

@app.route("/<string:id>", # here we have URL to Perform Delete Opearation
           # here we used [<string:id>] - which means we are dynamically getting the URL value, when frontend sends the DELETE Request --> The URL for Delete request will be loaded here 
            # the value which comes after [/] will be caputured by [<string:id> ] - "string" means we are specifing the Datatype ----> "id" is the value in which we will be storing the value (which comes after "/" ) 
            # ex :  [ http://127.0.0.1:5000/SOME_VALUE ] --- here [SOME_VALUE] is the value which will stored inside [id] ====> all the datas which we get from URL are of String Datatype so we used [<string> ] datatype.
           
        #    methods="DELETE" # Here we have specified route to perform Delete Operation
           # Error:- [ TypeError: Allowed methods must be a list of strings, for example: @app.route(..., methods=["POST"]) ]
            # This error occured because we did not used list as a value for [methods] parameter, when we what to specify some HTTP methods we have give it inside the List, else we will get this error.
           
           methods=["DELETE"]
           )

def deleteData(
    id # here we have use 1 mandatory parameter inside that parameter our URL end value will get stored that is the value which comes after [/] 
     # This Parameter name must be same the name which we used in [<string:id> ], parameter [name] and [id] must be matched, else we will get error.
):
    
    # here let us provide lines of statement which will perform Delete Opearations

    # query to delete specific item (document ) from database 
    querry = {"_id": ObjectId(id)} #  here we have convert [id] to [ObjectID ] datatype, by default [id] will be of string datatype 
     # we do this because inside mongoDb This is format which will accepted by MongoDB, if we fail to use this Format we might encounter error.
    
    collection.delete_one(querry)
    # This is MongoDB method which is used to delete 1 item(document) from the Database 
     # [delete_one() ] method will accept Object where we have to pass Key_Value pairs --> based on this Key_Value pairs the matched document will get deleted from the MongoDB Database


    return "Deleted Successfully"

# Delete route is done




# -----------------------------------------------




@app.route("/<string:id>", methods=["PUT"] )
def updateData(id) :
    # here we have use 1 mandatory parameter inside that parameter our URL end value will get stored that is the value which comes after [/]
    # This Parameter name must be same the name which we used in [<string:id> ], parameter [name] and [id] must be matched, else we will get error.
    
    # here let us provide lines of statement which will perform Update Opearations

    # Create query to update 
    query = {"_id": ObjectId(id)}

    # let us get the updated value which has been sent from the Frontend using [request] function 
    new_data = request.get_json()

    # let us use create update pattern of object 
    update_data = {"$set": new_data}

    # Error :- [  ValueError: update only works with $ operators ]

    # let us use [ update_one() ] method to udpate the document
     # this method accepts 2 arguement, --> 1st - object which find the document based on [id] ==> 2nd -- New data or values which has to be overriden for the Privious properties of the Oject which ultimately updates the values 
    collection.update_one( query, update_data )

# here we returned some value just to overcome the error
    return "Updated Successfully"







if __name__ == "__main__":
    app.run(debug=True)























