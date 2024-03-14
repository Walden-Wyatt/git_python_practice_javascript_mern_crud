var Express = require("express");
var MongoDb = require("mongodb");
var MongoClient = MongoDb.MongoClient;
var cors = require("cors");
const multer = require("multer");

var app = Express();

var url = "mongodb+srv://mern_mar11:mern_mar11@cluster0.7ocxykt.mongodb.net/?retryWrites=true&w=majority&appName=cluster0"
// mongodb+srv://mern_mar11:<password>@cluster0.7ocxykt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
var db;

MongoClient.connect(url, (error, client) => {
  if (error) {
    // console.log("Error in connection");
    console.log(error)
  }
  else {
    console.log("connected successfully")
    // console.log(client)
    /*

    What each and every Output Represents ?

  # 1.
    Output :-
     replicaSet: 'atlas-dp58eh-shard-0',
    [Symbol(@@mdb.enableMongoLogger)]: false
    # When you get this as an Output at the end of the Object which is present insdie [ client ] which means we have succssfully connected to [MongoDB]
    

  # 2. 
    Output :-
   namespace: MongoDBNamespace { db: 'ciplox', collection: undefined }
    }
    }

    # When you get this Output when you try to console the variable which holds database instance that is ( db = client.db("ciplox") )
     # when you console [db] if you get the above output which means you have successfully Loaded the Database inside you File, 
      # Now from [db] variable we can try to access the Collection and Modify the Documents (datas) which is inside the Collection


  # 3. 
   writeConcern: WriteConcern { w: 'majority' }
    }
    }
    # when you get this Output when try to console the varialbe which has instance of collection which means we have successfylly loaded the collection into our file 
     # Ex : [ collection = db.collection("ciplox_col") ], in this code when you try to console "collection" variable when you get the above output which means you have successfully loaded the Collection into you file.
     # By using this [collection] variable we can perform "CURD Operations" by making use of the following methods [ find(), find_one(), insert_many(), insert_one(), update_one(), update_many(), delete_one(), delete_many(), etc ].


    -----------

    # When you get below 2 errors which means code inside [if] block will get Executed Instead [else] block will get Executed ?
    
    # 1. When the URL Of MongoDB is wrong, when there is Mistake in Password, Username?
      # In this case You will get error --> when you get error [if ] block statements will get executed 
      Error :- MongoServerError: bad auth : authentication failed
        MongoServerError: bad auth : Authentication failed.


    
    # 2. When you did not Allowed specific IP Addresses to access the MongoDB [ Project --> Database ] ?
       Error [  MongoServerSelectionError: E8170000:error:0A000438:SSL routines:ssl3_read_bytes:tlsv1 alert internal error:c:\ws\deps\openssl\openssl\ssl\record\rec_layer_s3.c:1586:SSL alert number 80  ]
       # when you find this Error message please go to MongoDB Allow the [ Current IP  address or The IP Address of the Machine which you are Using ) 
         if you want the Database to be accessed from any IP Address then use [ ALLOW ACCESSS FROM ANYWHERE, 0.0.0.0 ] --- This is not recommended as your Database might get hacked.
        # Try to Use Only Specific IP Address to access the MongoDB Database inside MongoDB Website.


    
    # 3
      # Error :- MongoParseError: option apname is not supported
      # when [ appName ] this part of URL is not correct in such situations we will get this Error in our mongodb connection

      # Error :- Error: querySrv ENOTFOUND _mongodb._tcp.cluster0.7cxykt.mongodb.net
       # when this [ cluster0.7cxykt.mongodb.net  ] part of the URL is not correct in such situation we will get this Error, make sure to use Correct Characters at this part of URL.

    # 4
      # Error :- MongoParseError: Invalid scheme, expected connection string to start with "mongodb://" or "mongodb+srv://"
       # this error you will get When you make changes in this part or URL [ "mongodb+srv://" ], When part of URL is not correct in such situation we will get this Error.


    # 5
      # Error :- MongoParseError: mongodb+srv URI cannot have port number 
        # when [@] this part of the URL is error, when you don't use "@" you will encounter this error message.


    # 6
      # Error :-  MongoParseError: option rerywrites is not supported
      # when [ rerywrites ] this part of the URL has some error in such situation we will get this Error Message
       # here we missed "t" characters the correct value must be ["retryWrites"]


    # 7
      # Error :- MongoParseError: Expected retryWrites to be stringified boolean value, got: tue
       # when [ true& ] part of the code is not correct 
        # mainly when we fail or miss to use [&] character at the place where "@" comes in such situation we will get this Error.


    # 8
      # Error :- MongoParseError: Expected retryWrites to be stringified boolean value, got: true@=majority
       # when [ true@w=majority ] this part of code have some error you will get this Error message 
         # when you failed to use [w] in that place wherever "w" comes you will get this Error Message.

    # 9
      # Error : MongoParseError: Expected retryWrites to be stringified boolean value, got: true@w=majority
        when [ true@w=majority ] this part of the code has some error we might get error
        # Here we missed out [&] character, instead of using "&" we used "@" character, make sure to use "&" ---> correct value is [ true&w=majority ]


    # 10
      # Error : MongoAPIError: URI cannot contain options with no value
       # when [ =cluster0 ] part of the code have some mistake we get this error 
        # main reason is when we do not provide any character after [ = ] we get this error, make sure to provide minimum 1 character to overcome this error 
         # correct solution is to provide actual Name of the cluster which you have given in the Project Database during creation.


       */





    //--------------------------------------------------------------




    db = client.db("ciplox")
    // console.log(db)

    /*
    1. 
    # When you do not provide any database for [ client.db() ] by default it will point or load to ["test"] database,
    # when you provide some database name for [ client.db("ciplox") ] it will point or load that specific database
     # when you provide wrong database name for [ client.db("wrongdatabase") ] it will still point to that wrong database itself

    */




    //--------------------------------------------------------------




    // collection = db.collection("ciplox_col")
    // console.log(collection)

    /*

    Error :- [  MongoInvalidArgumentError: Collection name must be a String ]
     # This error occurs when we fail to provide string value as an arguement for [db.collection() ] method

    Error :- [ MongoInvalidArgumentError: Collection names cannot be empty ]
     # This error occurs when we provide Empty string as a Value for [db.collection("") ] method 

     # When we provide wrong Collection Name this error will be gone, but when try to access the database using [ CRUD ] methods such as ( find(), update_one(), etc. ) you will get the Errors


    */




    // -----------------------------------------


    collection = db.collection("ciplox_col")
    // console.log(collection)
    /*
    Output :- 
    writeConcern: WriteConcern { w: 'majority' }
    }
    }

    # We loaded the Collection successfully
    */




    findVariable = collection.find()
    // arrayFind = findVariable.toArray()
    // console.log(arrayFind)

    /*

    Output :-
    <ref *3> FindCursor {
_events: [Object: null prototype] {},

# When you get this Output at the beginning of the Object which gets loaded when we console [findVariable] which has the instance of [find()] method of MongoDB
 # This output indicates that we have successfully loaded the MongoDB data into our file
 # here we see the output has "FindCursor" [ FindCursor {  _events: [Object: null prototype] {}, ] - which means we are getting a cursor object 
  # we cannot access the Cursor object inside our file, To Access the Cursor Object variable we have to Convert it to a Array Datatype and store it inside the variable , ( ex :let us keep : arrayCursor )
    # now after coverting it to Array datatype and stored it inside the [ arrayCursor ] variable, when we try to console the [arrayCursor ] variable we will get the Array value inside the Array we can find the The Objects with [key_value] pairs,which is actually a Documents (in mongodb terms)
    # Now finally we have loaded the MongoDB data into our file Now can perform CRUD Operations based on our need
    # To Convert the Cursor Object to Array Datatype we have 1 way 
      1. By Using [ .toArray() ] method = 
        The [find()] method will return a Cursor Object --> Inside the Cursor Object we have a Method called [toArray()] which will convert the Cursor Object to Array Datatype --> this method will not accept any Arguements 
        [toArray(()] method will return a Promise ---> To get the Data from the [toArray()] variable we have to make use of either [ 1. then_&_catch block ] or [ 2. Async funcion Await keyword ]



    */



    toArrayvariable = findVariable.toArray()
      .then((data) => {
        console.log(data)
      })
      .catch((err) => {
        console.log(err)
      })



    /* Output :
      [ { _id: new ObjectId("65ef229cde252b48f8305938"), name: 'albert' } ]

      Here Finally we got the Output --- We have successfully Loaded MongoDB data into our file

    */

  }

})






