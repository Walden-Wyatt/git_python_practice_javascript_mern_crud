

            # from flask import Flask, request, jsonify


            # products = [{"name": "Gold"}]


            # app = Flask(__name__)


            # # get method 
            # @app.route("/", methods=["GET"])

            # def home():
            #     return jsonify(products)


            # # post method 

            # @app.route("/datas", methods=["POST"])
            # def postData():
            #     data = request.get_json()
            #     products.append(data)
                
            #     return jsonify(products)


            # # start server 
            # app.run(debug=True)


# ----------------------------------------------------------



# Here let us Learn POST request using [ HTML ] from browser

  # Error :- [ AssertionError: View function mapping is overwriting an existing endpoint function: productsroute ]
   # This error occurs when we define more than 1 route function with the same name, we are not allowed to do it
    # if you want to perform different opertions inside the same page, use different function name while routing provide same page as  its path.


from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


products = [{"name": "biryani"}]


@app.route("/", methods=["GET"])

def home():
    print("Home Page")

    return " Home Page "


@app.route("/products", methods=["GET"])
def get_product():
    return render_template("post2.html")


@app.route("/products", methods=["POST"])



# Points to Remember :-
 # 1. [request] method can be used only inside the Function which performs [ POST ] request operations
 # 2. what Python does behind the scenes for [ request ] method which we imported from [ flask ] library ?
   # a. we will provide the Path in the Browser URL 
   # b. our webpage gets Loaded, With Different Elements 
   # c. python will check for Elements for which we can use [name] attribute
   # d. when we perform some action for elements for which we have provided re-direct [ Ex: form tag ]
     # if we click on any Elements which is present inside the [ form ] tag, what form tag does is that 
      # if will check the Route path and method 
       # The [method and route path ] which is present inside server File, which whichever is matched with the specific [method and route ] path those mehods statements will get executed 
        # The Statements which is present inside that specific Route Function will get executed
   # e. To access the Elements value which is inside the [ form ] tag we have to use [ request.form["name_value"]]
       # Syntax Breakdown :- [ request.form["name_value"] ]
        # request.form - this will return dictionary 
         # key - this [ request.form ] dictionaries key will be the Value which we have given in the [ name ] attribute 
         # value = the value for this key will be the value which we will be passing inside the [input] tag, or the value which we specify in the [ value ] attribute.
   # f. 
   # g. 




def add_product():
    data = request.form["products"]
    # dataname = request.form["ddd"] - this is the element from [ h1 ] tag which has [ name ] attribute which we are not allowed to use.
    products.append({"name": data}) 
    return jsonify(products)

app.run(debug=True)



# -------------------------------------------------------------------------------------------------------------------------


# Important Points :-

 # To check weather the data is getting stored or not try to use [ List ] inside the same file and try to append what ever value or changes took place in the element inside the [ list ] which you have created.
  # this is the Best way to debug the values which are present inside the List.


































