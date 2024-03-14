


#  Here let us create backend server using Python 


from flask import Flask, jsonify, request
from flask_cors import CORS

# let us write code for Mongodb 

from pymongo import MongoClient


# make sure to import this to use ObjectID 
from bson import ObjectId





url = "mongodb+srv://investob848:python_workings@cluster0.t8nusx1.mongodb.net/?retryWrites=true&w=majority&appName=cluster0"
client = MongoClient(url)  # Here we have loaded [ Project Instance ]
# inside [ Project Instance ] we will have Properties and values(class) - The properties will be Databases which is present inside the [ Project Instance ]
 # the values will be Class Construtor of Databases --> Every database will have unique Class Construtor 



db = client["hobby"] # Here we are tring to access specific database 
# Inside [ db ] Database instance will get loaded ---> inside [ Database Instance ] object we can see the properties ---> all the Properties will have [ Collection Constrctor ] as values --> There will be multiple collections inside a Single Database 


collection = db["fullStackHobby"] # here accessed collection where we can find documents, which is the actual data which we are looking for.

# Now let us convert [ObjectID] to string datatype 




app = Flask(__name__)


CORS(app, origins="*")

# ------------------------------

 # GET Route

@app.route("/")
def getData():

    data = list(collection.find())
    # print( data )

    for i in data:
        i["_id"] = str(i["_id"])
    # print(data)
        
    return jsonify(data)



# ----------------------


# POST Route 


@app.route("/", methods=["POST"])
def postData():

    data = request.get_json()
    collection.insert_one(data)
    print(data)
    return "POST DATA"



# ----------------------------------

# [ /<string:id> ] this is used to get the dynamic values which will be passed in the url
#  here we are getting value which comes after [ / ] in the URL that is the [ id ] ====  ex :- [ http://127.0.0.1:5000/65e8a3973f6dbe243c142ba1  ] 
   # from this URL we are only getting [ 65e8a3973f6dbe243c142ba1 ] this value, This value will be passed as an Arguement for [ _id ] of  [ deleteData(_id) ] - 
   # by using [ _id ] parameter we can create a Query which will delete the object
#   [ <string:_id> ]
  # <string: = here we are specifying the Data, that there the value will be from String datatype
  # _id = here we are providing Name for the string value, This Name must exactly match with the [ key ] which is present inside the [Documents ] which is inside collection 
@app.route("/<string:_id>", methods=["DELETE"])
def deleteData(_id):
    query = {"_id": ObjectId(_id)} # make sure to use [ _id ] not just [ id ], because that is key name which is present inside the database

    # [ collection.delete_one() ]  - this method will accept 1 arguement which must an Object 
     # The Object must be have [key_value] pairs, where [ key_value ] must match with the Value present inside the Database, Based on the Matched [ key_value ] appropriate data will get deleted.
    collection.delete_one(query)

    return "Data Deleted Successfully"
    



# ----------------------------------------------------------



@app.route("/<string:_id>", methods=["PUT"])
def updateData(_id):
    query = {"_id": ObjectId(_id)}
    new_data = request.get_json()

    update_data ={"$set": new_data}
    collection.update_one(query , update_data)

    return "Updated successfully"







# Here we have started the Server 
if __name__ == "__main__":
    app.run(debug=True)















