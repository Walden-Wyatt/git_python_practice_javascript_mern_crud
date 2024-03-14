

# Backend

from flask import Flask, jsonify, request

from pymongo import MongoClient

from flask_cors import CORS 

from bson import ObjectId



app = Flask(__name__)

CORS(app, origins="*")


# -------------

url = "mongodb+srv://investob848:python_workings@cluster0.t8nusx1.mongodb.net/?retryWrites=true&w=majority&appName=cluster0"
client = MongoClient(url)
db = client["hobby"]
collection = db["sunday"]




@app.route("/")
def getData():

    data = list(collection.find())
    

    for i in data:
        i["_id"] = str(i["_id"])

    return jsonify(data)


# ----------------------------------------------


@app.route("/", methods=["POST"])
def postData():
    data = request.get_json()
    print(data)

    collection.insert_one(data)
    return "SERVER POSTED DATA"




# -------------------------------------------------------


@app.route("/<string:id>", methods=["DELETE"])
def deleteData(id):
    query = {"_id": ObjectId(id)}
    collection.delete_one( query )
    return "Deleted Successfully"


# ---------------------------------------------------

@app.route("/<string:id>", methods=["PUT"])
def updateData(id):
    newData = request.get_json()
    print(newData)
    print(id)
    query = {"_id": ObjectId(id)}
    update_data = {"$set": newData}
    collection.update_one(query, update_data )
    return "Updated Successfully"






if __name__ == "__main__":
    app.run(debug=True)














