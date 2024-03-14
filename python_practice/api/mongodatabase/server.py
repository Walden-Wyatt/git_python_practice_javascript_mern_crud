


from flask import Flask, jsonify, request, render_template

from pymongo import MongoClient



app = Flask(__name__)


uri = "mongodb+srv://investob848:python_workings@cluster0.t8nusx1.mongodb.net/?retryWrites=true&w=majority&appName=cluster0"


client = MongoClient(uri)

db = client["hobby"]

collection = db["hobbies"]




itemsList = []


@app.route("/", methods=['GET'] )
def home():

    return "Home Page"


@app.route("/items", methods=["GET"] )
def get_item():

    return render_template("index.html")
    # return jsonify(collection)



@app.route("/items", methods=['POST'])
def add_item():

    fname = request.form['fname']
    lname = request.form['lname']
    hobby = request.form['hobby']


    # let us perform insert operations 

    collection.insert_one({"firstName": fname, "lastName": lname, "hobby": hobby })

    # itemsList.append( {"firstName": fname, "lastName": lname, "hobby": hobby } )

    collectionList = list(collection.find())
    for newColl in collectionList:
        newColl["_id"]  = str(newColl["_id"])


    # return collectionList
    # return render_template("dynamic.html")
    return jsonify(collectionList)

    






app.run(debug=True)




















