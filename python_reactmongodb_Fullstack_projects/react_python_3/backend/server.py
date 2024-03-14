

from flask import Flask, jsonify, request


# -----------------------------
  # MongoDB Code :-


from pymongo import MongoClient

# load project
client = MongoClient("mongodb+srv://investob848:python_workings@cluster0.t8nusx1.mongodb.net/?retryWrites=true&w=majority&appName=cluster0")

db = client["hobby"]

collection = db["persons"]

# ----------------------------



app = Flask(__name__)

# ----------------------------

  # Code to resolve [ CORS ] error 

from flask_cors import CORS 


from bson import ObjectId

CORS(app, # [ app ] - this is the server for which requests will be happening [ get, post, update, delete] requests
      origins="*" 
      # [origins] - "origins" will decide which all servers and request for this backend server 
       # Those servers which we provide here only those servers can request for this backend server 
       # [ * ] - if you want any servers to request for this backend server we can use [*]
      
      )




# ---------------------------


@app.route("/")
def get_Data():
    
    collectionList = list(collection.find())

    print(collectionList)


# here this [ for ] loop will iterate over the Items inside the list ---> for every objects inside the list this will take property with key [_id] ---> make necessary changes and insert only the changes items Object Property inside the List
      # Other items and Object properties will be same it will only the [_id] property
      # [collectionList] will be overridden with newly changed values, after this [for..in] loop Newly changed [collectionList] will get loaded.
    
    # This is what loops such as [ for ... while... and Recursion functions ] can be used to iterate over the list and make necessary changes
    for i in collectionList:
        i["_id"] = str(i["_id"])


    return jsonify(collectionList)




    # -----------------------------------------


@app.route("/", methods=["POST"])
def post_data():

    # [request] library - let us use "request" library to get the data which has been sent from the "frontend" server by using [ request ] library 
    data = request.get_json()
    print(data)
    collection.insert_one(data)

    return "Posted Data"




    # -----------------------------------------

# Delete Route

@app.route("/<string:_id>", methods=["DELETE"])
def delete_route(_id):
    print(_id)  # this value is getting printed above the request url paths and datas

    # let us create query which can be used to delete the document which is inside [ mongodb ] collection 
    # When passing value for ["_id"] make sure to use [ObjectId()] and pass "_id" inside it as an arguement, because that is how the datas have been stored inside the database. Import it from [bson] class
    query = {"_id": ObjectId(_id)}
    collection.delete_one(query)
    return "Deleted successfully"





    # -----------------------------------------

#  Update Operations 

@app.route("/<string:_id>", methods={"PUT"})
# ERROR :- [  ValueError: malformed url rule: '/<string:_id'  ]
 # When you miss closing bracket (>) you will get this error, make sure to use opening and closing brakets properly
def update_route(_id):
    print(_id)
    query = {"_id": ObjectId(_id)}
    # existing_data = collection.find_one(query)
    new_data = request.get_json()
    # existing_data.update(new_data)
    update_data = {"$set": new_data}
    collection.update_one(query, update_data)

    return "Updated successfully"




if __name__ == "__main__":
    app.run(debug=True)






















