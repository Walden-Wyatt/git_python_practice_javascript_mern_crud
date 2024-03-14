

from flask import Flask, jsonify, request, render_template, redirect, url_for

# render_template - this method can be used to render HTML template in the browser

app = Flask(__name__)



# -------------------

        # @app.route("/", methods=["GET"])
        # def hello():
        #     print("Hello")
        #     # Error :- [  TypeError: The view function for 'hello' did not return a valid response. The function either returned None or ended without a return statement.  ]
        #      # when the [ route() ] decorator function does not return any value we will get error, make sure to use return statement and try to return some values.
            
        #     # Here we have written [ HTML ] directly using [ f strings ]
        #     return f"""
        #     <!DOCTYPE html>
        #     <html lang="en">
        #     <head>
        #         <meta charset="UTF-8">
        #         <meta http-equiv="X-UA-Compatible" content="IE=edge">
        #         <meta name="viewport" content="width=device-width, initial-scale=1.0">
        #         <title>My Python HTML Page</title>
        #     </head>
        #     <body>
        #         <h1>Hello, !</h1>
        #         <p>Your age is.</p>
        #     </body>
        #     </html>
        #     """


# -------------------


# Approach 2 using [ render_templete() ] method 


@app.route("/", methods=["GET"])

def hello():

    # Error :- 
      # jinja2.exceptions.TemplateNotFound: post.html 
      # This error occurs because we did not stored all the [post.html ] file inside [ templates ] folder 
       # All the HTML files which we use inside the Flask Library we have to store those [ HTML ] files inside [ templates ] folder 
        # [ templates ] folder must be in the same folder where our [ server ] files are present.
        # Make sure to create [ templates ] folder ---> inside [ templates ] folder create [.html ] files 
    return render_template("post.html") 


# -------------------------------

@app.route("/login", methods=["POST", "GET"])

def postmethod():

    print("Post Method")

    # if you use [ GET ] method we have mandatorily use [ return ] statement else we will get Error.


    if request.method == "POST":
     user = request.form["userValue"]
    #  user = request.form.get("userValue")
     print(user)
     return f"User Value from POST: {user}"
    else:
        return "No userValue provided in GET request."





app.run( debug=True )

















