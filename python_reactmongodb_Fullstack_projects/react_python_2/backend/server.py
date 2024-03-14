


# Here let us create an Backend server 


from flask import Flask, jsonify, request

from flask_cors import CORS

from bson import ObjectId


# --------------------------------------------------------


# Here let us write Database codes 

from pymongo import MongoClient

url = "mongodb+srv://investob848:python_workings@cluster0.t8nusx1.mongodb.net/?retryWrites=true&w=majority&appName=cluster0"
client = MongoClient(url)
db = client["hobby"]
collection = db["details"]



# ---------------------------------------------------------



# create server 

app = Flask(__name__)


CORS(app, origins="*" )



# ------------------------------------------
# get route 
@app.route("/")
def get_route():
    
    data = list(collection.find())

    for i in data:
        i["_id"] = str(i["_id"])

    print(data)
    return jsonify(data)




# ----------------------------------------
# Post Route 

@app.route("/", methods=["POST"])
def post_route():

    data = request.get_json()
    collection.insert_one(data)
    print(data)

    return "data posted"

# let us create delete route 

@app.route("/<string:_id>", methods=["DELETE"])
def delete_route(_id):
    # let us create query so that it will delete the data 
    query = {"_id": ObjectId(_id)}
    collection.delete_one(query)
    return "Deleted Successfully"

    









# start server 
if __name__ == "__main__":
    app.run( debug=True )  








































