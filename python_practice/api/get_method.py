

# To perform any of API Operations we need some of the Packages which we have to use such as Flask, Django for Python 
 # For Javascript we can use ExpressJS Package 

        # from flask import Flask, jsonify


        # # now let us create a Flask Instance Object 



        # # ------------------------------


        # # app = Flask(__name__)



        # # @app.route('/', methods=["GET"])


        # # def hello():
        # #     response = {"message": "Hello, World!"}
        # #     return jsonify(response)

        # # # print("Wow")

        # # # hello()

        # # def wow():
        # #     return "Wow Method"


        # # if __name__ == "__main__":
        # #     print("abc")
        # #     app.run(debug=True)
        # #      # [app.run() ] is the Method which will start the Server, if we do not use it our server will not get start, terminal will get terminated immediately
        # #       # so make sure to use them
            


        # # ------------------------------
            



        # # --------------------------------------------------------------------------------------------------------------------------------------------------------------------


        # # [ Practice 2 ]



        # from flask import Flask, jsonify

        # # jsonify - this will convert our python code to JSON format,so that when we load the Datas inside the Browser there will not be any errors 


        # # create an Instance of [ Flask ] class 

        # app = Flask(__name__)

        # # now let create a get route 

        # @app.route("/", methods={'GET'})
        # def get():
        #     response = { "key": "Value 1", "key_2": 202002 }
        #     response = [1,2,3]
        #     response = "hello"
        #     response = 111222
        #     response = True
        #     # We are allowed to use Any Datatype values inside [ jsonify() ] method and Load the Method inside any Browser, we will not get any errors.

        #     response = { "key": "Value 1", "key_2": 202002 }
        #     return jsonify( response )



        # # let us use Function which is not decorated with[ @app ] decorator 

        # def nonDecoratedFunction():
        #     print("This is non Decorated Function")

        # nonDecoratedFunction()

        # # Output :-
        #     # This is non Decorated Function

        # # We are allowed to use any Code under the API functions which has been decorated using [ @app.route() ] method 
        #  # the code which we use can be a Functions, Varialbles, classes, etc all the Codes are Accepted.




        # # Now let us start the server by using [app.run()] method 

        # if __name__ == "__main__":

        #     app.run(debug=True)




# ------------------------------------------------------------------------------------------


# Now let us Try to Fetch the datas from [ https://jsonplaceholder.typicode.com/todos/ ]



from flask import Flask, Request, jsonify


# Flask = used to create the Server and start the server 
# Request = used to set the Request object such as methods, url, status code, etc 
# jsonify = used to convert Python Object to JSON format


from pymongo import MongoClient


app = Flask(__name__)  # here we passed the current file name

# Here we have loaded the Mongo database as whole
client = MongoClient("mongodb+srv://investob848:python_workings@cluster0.t8nusx1.mongodb.net/?retryWrites=true&w=majority&appName=cluster0")


#
db = client["sample_weatherdata"]

collection = db["data"]



@app.route( "/", methods=['GET'] )
def getData():

    data_from_db = list(collection.find())

     # here if we see we have converted [ "_id" ] property to string in the below code 
       # code [ "_id": str(item["_id"]) ]
    json_data = [{"_id": str(item["_id"]) , "callLetters": item.get("callLetters"), "qualityControlProcess": item.get("qualityControlProcess") } for item in data_from_db  ]

   # When you do not convert python objects using [jsonify], by default python converts the Object to JSON data displays in the browser.
    return jsonify({"data": json_data})



app.run()






























