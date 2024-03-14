

# here we have server codes 

from flask import Flask, jsonify, request

from flask_cors import CORS

from pymongo import MongoClient

url = "mongodb+srv://investob848:python_workings@cluster0.t8nusx1.mongodb.net/?retryWrites=true&w=majority&appName=cluster0"
client = MongoClient( url )
db = client["react1"]
collection = db["react1"]



app = Flask(__name__)

CORS(app, origins="*")



@app.route("/", methods=["GET"])
def getData():
    data = list(collection.find())
    for i in data:
        i["_id"] = str(i["_id"])
    return jsonify(data)


@app.route("/", methods=["POST"])
def postData():
    data = request.get_json()
    print(type(collection.insert_one(data)))
    print(data)
    return "posted"


# start the server 

if __name__ == "__main__":
    app.run(debug=True)

