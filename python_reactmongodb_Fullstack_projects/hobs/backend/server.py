
# This is a Server file flask applications


from flask import Flask, request, jsonify, render_template

from pymongo import MongoClient

from flask_cors import CORS 


app = Flask(__name__)

CORS(app, origins="*")  # This line of code will make our API endpoint to be accessed from any server or Browsers
 # now we can perform any operations easily.


# mongodb setup 
url = "mongodb+srv://investob848:python_workings@cluster0.t8nusx1.mongodb.net/?retryWrites=true&w=majority&appName=cluster0"

client = MongoClient(url)
db = client["hobby"]
collection = db["hobbies"]


cors = CORS(app, resources={r"/": {"origin":"*"}})

databaseInfo = [{"firstName": "John", "lastName":"David", "hobbies": "Reading Books" } ]


# get home page 
@app.route("/", methods=["GET"])
# @CORS(app, resources={r"/": {"origins": "*"}})
def home():

    sendData = list(collection.find())

    for i in sendData:
        i["_id"] = str(i["_id"])

    return jsonify(sendData)




# details route 
@app.route("/details", methods=['GET'])
# @CORS(app, resources={r"/details": {"origins": "*"}})
def get_details():

    return "Get post data"



# details add 
@app.route("/details", methods=["POST"])
# @CORS(app, resources={r"/details": {"origins": "*"}})
def add_details():

    # request object will parse all the HTML Element, based on what value we want by making use of appropriate HTML element tag we can get the datas.
     # here we are looking for values where the HTML element is inside [form] tag.
    fname = request.form["fname"]
    lname = request.form["lname"]
    hobbies = request.form["hobbies"]
    
    databaseInfo.append({"firstName": fname, "lastName": lname, "hobbies": hobbies })





app.run(debug=True)




















