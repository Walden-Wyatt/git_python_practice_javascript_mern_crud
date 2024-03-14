


/*

1. Import mongoose
2. create a variable which holds URL
  A. In the url next to [ mongodb.net/ ] ---> you have to provide [ DATABASE_NAME ] --> To create your own database or Access the Specific database.
3. Create a Schema Class using [ mongooseInstance.Schema ] class
4. Create a Model Class using [ mongooseInstance.model() ] method ---> pass 2 arguements --> 1. modelName ( CollectionName ) ----> 2. SchemaVariable
5. Create an Async Function so that Inside the Function we will wrap all the Asynchronous Code to get the values using [ await ] keyword
6. Connect to MongoDB using [ mongoose.connect() ] method -- pass appropriate arguements --> 1. URL ----> 2. { useNewUrlParser: true, useUnifiedTopology: true }
7. Access Documents using [ Model variable ] which you have Created ---> You will finds methods such as [ find(), update(), delete(), etc ]
   A. Make sure to use [await] keyword before this methods, becuase this methods are used to perform Asynchronous Operations.
*/



/*

const mongoose = require("mongoose")

var url = "mongodb+srv://mern_mar11:mern_mar11@cluster0.7ocxykt.mongodb.net/Apple?retryWrites=true&w=majority&appName=cluster0"
/*

[ CODE ] var url = "mongodb+srv://mern_mar11:mern_mar11@cluster0.7ocxykt.mongodb.net/Apple?retryWrites=true&w=majority&appName=cluster0"


To Create or Access your own Database ---> You have to Create the Database in the Connection URL
 The Place to Create/ provide Database name is ---> in the URL you will find [ mongodb.net/] --> next to "/" you have to Create/Provide the New Or Existing Database Name ---> when you do that the part of url will look like this [ ......  mongo.net/DATABASE_NAME?retryWrites  ....... ]
 If The Provided Database is Existing then there will not be any New Database gets created ---> If no Database Name then New Database will get Created.
* /

const Schema = mongoose.Schema
const yourSchema = new Schema({
    name: String,
})


// here we are actually creating a collection, Now [YourModel] is a Collection
const YourModel = mongoose.model('YourModel', yourSchema)

async function getData() {


    try {

        const client = await mongoose.connect(url,
            // { useNewUrlParser: true, useUnifiedTopology: true } // this 2nd arguement option object is not important, if you get some error you can make use of the options
        )
        /* Error :- [ MongooseError: Operation `hoddies.find()` buffering timed out after 10000ms ]
          The above Error occurs when you try to access the documents using [ YourModel.find({}) ] method without connecting to the Database using [ mongoose.connect() ]  method
        * /

        const documents = await YourModel.find({})
        console.log(documents)

    }
    catch (error) {
        console.log(error)
    }

}


getData()



*/

// ---------------------------------------------------------------------------------------------------------------------------------------------------------




// GET Data using [find()] method


/*

// load mongoose
const mongoose = require("mongoose")


// create connection URL --- specify Dataname in the URL after [ mongodb.net/]
const url = "mongodb+srv://mern_mar11:mern_mar11@cluster0.7ocxykt.mongodb.net/persons?retryWrites=true&w=majority&appName=cluster0"


// load Schema
const Schema = mongoose.Schema;


// -----------------------

// In MVC Approach --- The Below code is called a Model ---> This will fall under [ Model ] approach

// create Schema by invoking Schema call with "new" keyword ----> 1 arguement --> 1. Object with Keys = name, values = Datatype
const yourSchema = new Schema({
    name: String
})


// create model using [model()] method ---> 2 arguements --> 1. collection name --> 2. schema variable
const YourModel = mongoose.model("collectionName", yourSchema)




// ----------------------------



/*
 Once when you connect to the MongoDB Datbase the above code will get executed ----> The Above code has to do list of Things
  1. load Project ---> create database (based on the name provided in the URL ) ---> Creates Collection (based on the name provided in mongoose.model() method ) ---->  Inserts Pattern for the Documents (on how data has to be stored ) --->

 */




/*

// create an Async function to access the Datas inside MongoDB

const getData = async () => {

  // connect to database using [connect] method ---> Now the what ever we specified above will get Executed ---> Once we connect to database above things will get executed
  const connect = await mongoose.connect(url)

  /*
   perform [get] operation using [find()] method to load the datas which is present inside the collections ---> ultemately we are loading [ Documents ]
   Now all the CRUD Operation methods will be present inside [ YourModel ] class which we defined above, by using that class we can access the Datas
   * /
const documents_findData = await YourModel.find({})
console.log(documents_findData)
}



getData()




    */








// ----------------------------



// Posting or Insert or sending the data to database



/*



// load the mongoose
const mongoose = require("mongoose")


// create url
const url = "mongodb+srv://mern_mar11:mern_mar11@cluster0.7ocxykt.mongodb.net/DatabaseName?retryWrites=true&w=majority&appName=cluster0"


// load Schema
const Schema = mongoose.Schema

// create Schema
const createSchema = new Schema({
    name: {
        type: String, // [type] decides what type of data has to be stored
        required: true, // [required] property will decide weather the value for this [name] property has to be provided mandatorily or not ---> if you want user to Mandatorily/compulsorily provide value for this [name] property then we can use "true" as a value --> else we can use "false" as a value.
        unique: false // if you want the Values to be unique we can use this, that is when use passes some value for [name] --> mongodb will check weather this is some docuement which has same value for the name field --> if yes mongodg will throw error as well as it will not create value inside the database ---> if not creates document and assigns value for the [name] field
    }
})


// create Model ---> creating collection --> Now all the CRUD operation methods will get loaded inside [ YourModel_Collection ] variable , by using this variable we can perform CRUD Operations ---> [ YourModel_Collection ] variable is actually a Class
const YourModel_Collection = mongoose.model("CollectionName", createSchema)



// now let us create a Asynchronous function to perform CRUD Operations , here we  will specifically perform [ post data ] operation

const postData = async () => {

    // connect to mongodb database
    const connect = await mongoose.connect(url)

    // perform [post] operation
    /*
    To post or Insert or Create the Data we have to Invoke the [ YourModel_Collection ] class preceeding with New Keyword ----> This Class will accept 1 arguement that the object which we will be sending  inside the Database (This will create a New Document)
    * /
    const postData = await new YourModel_Collection({
        name: "Hello first name"
    })


    /*
    Once if send the Data we have to save the data inside the database using[save()] method-- -> This method will be aviable inside the Variable which we created for Posting the the data-- -> In the above case it will be inside[postData] variable.
     [save()] method will return a Promise ---> when resolve the promise preceeded with [ await ] keyword you will get the object(document) ---> This is the Object(document) which you have sent using [ new YourModel_Collection() ] class
    * /
    const saveData = postData.save()

    console.log(await saveData)

    // here checking the [saveData] value weather the [saveData] has Truthy or Falsy value --> we are displaying weather the data send successfully or not.
    if (saveData) {
        console.log("Inserted Data Successfull")
    }
    else {
        console.log("Inserted Data Failed")
    }



}



postData()




*/





// ----------------------------------------------






/*



// [ Practice 2 ] post data


// load mongoose
const mongoose = require("mongoose")

// load url --> specify database name
const url = "mongodb+srv://mern_mar11:mern_mar11@cluster0.7ocxykt.mongodb.net/DatabaseName_2?retryWrites=true&w=majority&appName=cluster0"

// load Schema class
const Schema = mongoose.Schema

// create Schema pattern
const schemaPattern = new Schema({
    name: {
        type: String,
        required: true,
        unique: false
    }
})


// create Model --> this [ YourModel_collection ] is the class which is used to send the datas, by passing 1 arguement for the class constructor we can send the datas
const YourModel_collection = mongoose.model("collection_2", schemaPattern)


// create async function to perform CRUD Operations

/*

 Here in the Below [ postData ] we have statements(lines) which performs Database Operations ---> but for those lines of code we did not used [await ] keyword but Still the Database Operation is successful without any Errors ---> now let us learn when to use [await]

 When to use [await] keyword and [then/catch ] block ---> Exactly at which line should we have to use [await] keyword and [then/catch ] block  ?

  Answer :-
   1. [ await ] keyword has to be used only for those Lines which performs HTTP requests (interact with server )
   2. Only when Other Server Sends some data to our sever --> The data send by the server will be a [Promise] object (because data has been send from other servers database )  --> In Order to view the Data which has been sent by the Other server we will be using [ await ] keyword ---> [await] keyword will convert the Other database code to Object Syntax (which is used in our programming language).

    The lines which satisfies above 2 conditions only for those lines we have to use [ await ] keyword
    if you see so what the Methods which interacts with database as well as gets the data from other database ---->
      [ get() ] --> "get()" method will interact with the other database and gets the data from the other database ---> Now in order the View (convert the data to current programming language ) we will be using [await]   ---> [await] must be used exactly at the line where we loaded the data using [get()] method , the line where the use [get()] method for the line we have to use "await" keyword.


        WARNING :- [ 'await' has no effect on the type of this expression.  ]
         when you get this warning understand that the Code which you using [await] is not going to return any Promise Object
          by default vsCode itself will show some [warning] into our code by displaying [...] elepsis ---> when we get this we have to understance we have perfromed some Http interactions but the line of code for which we used [await] is not going to return any Promise Object --> if there is not promise object then there is not point in using [ await ] or [then/catch ] block

          Example :- // const postData = await new YourModel_collection()
            # here we will get warning this is becuase [ new YourModel_collection() ] code is not returning any {promise object } ---> so there is no point in using [await] to view the data
             [ { name: 'Post Data', _id: new ObjectId('65f13e6f48d2244a3b8c6adb') }  ]  ----> This is the Data which has been returned from the above code (i.e,  new YourModel_collection() )  ---> Here we can clearly see that this is not a Promise Object
              Now we got to know when to use [ async/await ] ----> [then/catch ]


      *** [ async/await ] ----> [then/catch ] can be used only when there is some code which Interacts with Other Server and returns some datas from the Other Server



      ** The Same thing is Done using [ then/catch ] block
          Here instead of using [ await ] keyword we will be using [ then and catch ] block --- Follow the same instructions which has been specified above Instead of [ await ] keyword try to use [ then/catch ] block
          Above explanation is applicable for [ then/catch ] block ===> In that explanation for implementing [then/catch] approach replace [await] keyword with [then/catch] block --> now you learnt how to use [async/await] as well as [then/catch] block




          * /

const postData = async () => {

    // let us connect to database
    // const connect = await mongoose.connect(url)
    const connect = mongoose.connect(url)


    // let us send the data using [ YourModel_collection ] class
    // const postData = await new YourModel_collection(
    const postData = new YourModel_collection(
        { // Here while Posting or Creating or Inserting the Data we have to follow the pattern which we have provided in the Schema
            name: "Post Data"
        }
    )

    console.log(postData)


    // now let us save the data -- only when we save the data the data gets sent/inserted inside the MongoDb database
    // here [await] is not necessary to use because we are not getting any datas, even though this performs Database operations because we are not getting any datas so its not necessary to use [await]
    // const saveData = await postData.save()
    const saveData = await postData.save()

    // let us check [saveData] and conditionally render the message

    if (saveData) {
        console.log("Inserted successfully!")
    }
    else {
        console.log("Inserted Failed!")
    }
}



postData()




*/






// -----------------------------------------------------------------------------------------------------------------------------------------------------------



// Let us perform Update Operation using  mongoose




/*



const mongoose = require('mongoose')

const url = "mongodb+srv://mern_mar11:mern_mar11@cluster0.7ocxykt.mongodb.net/DatabaseName_update?retryWrites=true&w=majority&appName=cluster0"


const Schema = mongoose.Schema;

const createSchemaPattern = new Schema({
    name: {
        type: "string",
        require: true,
        unique: false
    }
})


// create Model -- creating collection
const YourModel_collection = mongoose.model("collection_Update", createSchemaPattern)



// create async function

const updateData = async () => {

    // let us connect to database
    const connect = await mongoose.connect(url)

    // console.log(connect)

    /* findOneAndUpdate method will accept 3 arguement
      1. filter object
      2. New Update object
    * /

    const filterObject = { name: "pat" }
    const updateObject = { $set: { name: "Rat" } }

    /*
     here we use [await] that is because first we get the data --> then we convert it to javascript format ---> then override the existing data with new data --> finally we are inserting it into the database.
      if you do not use [await] keyword we cannot able to get the data ---> if we cannot able to get the data we cannot able to override the existing data with new value ---> if we cannot able to override the data we cannot able to insert new updated data inside the MongoDB server --> so it is important to use [await] keyword

     * /
    const updatedValue = await YourModel_collection.findOneAndUpdate(
        filterObject,
        updateObject,
        // { new: true } if you use this or don't use this there will be no changes when you try to print the (updatedValue) variable an Object will be returned
    )

    console.log(updatedValue)
    // output :-[  null ]  ----> we got this output that is because we did not use [ {new: true }]
    // here [await YourModel_collection.findOneAndUpdate() ] will return the data which we are going to be updating the, not the New data which we will be sending.



}



updateData()



*/






// -----------------------------------------------------------------------------


// [ Practice 2 ] Update Operation




/*


const mongoose = require("mongoose")

const url = "mongodb+srv://mern_mar11:mern_mar11@cluster0.7ocxykt.mongodb.net/DatabaseName_update2?retryWrites=true&w=majority&appName=cluster0"

const Schema = mongoose.Schema;

const createSchemaPattern = new Schema({
    name: {
        type: String,
        required: true,
        unique: false
    }
})


// create Model --> creating collection
const collectionModel = mongoose.model("collection_Update2", createSchemaPattern)



// create Async function

const updateFunction = async () => {


    try {

        // connection to mongodb
        const connnect = await mongoose.connect(url)

        // use [findAndUpdateOne() ] method

        // filter query
        const filter = { name: "node" }
        const updateData = { $set: { name: "New Node" } }

        const updatedValue = await collectionModel.findOneAndUpdate(
            filter,
            updateData,
            // {new: true}
        )

        console.log(updatedValue)
        // when filter query document which we passed inside [ findOneAndUpdate() ] is not present inside the MongoDB database in such situation [findOneAndUpdate()] method will return "null" value  which is a falsy value --> if such document is not present which means we cannot able to update the document ultimately we failed to update the database using [findOneAndUpdate()] method --> by using this [updatedValue] we can conditionally render the message based on value return by [ findOneAndUpdate() ] that is [ null or Existing object  ]

        // condition
        if (updatedValue) {
            console.log("Updated successfully")
        }
        else {
            console.log("Failed to Update")
        }


        // Output :- [ Failed to Update ]


    }

    catch (error) {
        console.log("Error while connecting \n", error)
    }

}


updateFunction()




*/





// ---------------------------------------------------------------------------------------------------------------------------------------------------------------------



// Let us Learn to perform [ Delete ] Operation using [ DeteleOne and DeleteMany ] methods



/*

// let us load mongoose
const mongoose = require('mongoose');

// create connection string
const url = "mongodb+srv://mern_mar11:mern_mar11@cluster0.7ocxykt.mongodb.net/database_delete?retryWrites=true&w=majority&appName=cluster0"


// let us load Schema class
const Schema = mongoose.Schema;

// let us create Schema using Schema class
const createSchemaPattern = new Schema({
    name: {
        type: String,
        required: true,
        unique: false
    }
})


// now let us create Model -> ultimately creating Collection --> this is the Variable which will have all the Methods to perform CRUD operations
const CollectionModel = mongoose.model("collection_delete", createSchemaPattern)


// let us create Async function

const deleteData = async () => {

    // connect to mongodb
    const connect = mongoose.connect(url)

    // let us use delete method to delete the data
    /*
    Output :- { acknowledged: true, deletedCount: 0 }
      when we use await keyword -> this also has promise inside it -> when we use we are getting the value
       in the above output when we you get [deletedCount: 0] --> which means not document has been deleted ---> there are 2 situations where we get this output --> 1. when the query to delete document,such document is not present ..... 2. when the there is not error in delete operations such as wrong url etc.
    * /
const deletedData = await CollectionModel.deleteOne({ name: "pat" })
// Output :- { acknowledged: true, deletedCount: 1 } --> here we an see that [deletedCount] is "1" ===> which means there where some document which has matched with the query --> first matched document got deleted
// [deleteOne()] method will delete only 1st matched document from the Database



console.log(deletedData)


// -------------------------------


// Now let us use [deleteMany()] method and try to delete more than 1 document at once

const deleteManyDocuments = await CollectionModel.deleteMany({ name: "rat" })

console.log(deleteManyDocuments)

/*
 Output :- [ { acknowledged: true, deletedCount: 3 } ] --
  here we can see that [deletedCount is 3 ] --> we had 3 document with the query [  { name: "rat" } ] all the 3 got deleted with a single method called [ deleteMany() ]
* /



// -----------------------------------


/*
 To close the Mongoose server from running we can use [ mongoose.connection.close() ] == mongoose is the instance of 'mongoose' library/class
   [ mongoose.connection.close() ] this method will automatically close the server after executing all the above lines which is used to perfrom some operations in Mongodb
 * /
mongoose.connection.close()


}



deleteData()



*/






// --------------------------------------------------------------------------------------



// [ Practise 2 ] Delete Operations


// load the mongoose 
const mongoose = require("mongoose")

// provide database name in the url
const url = "mongodb+srv://mern_mar11:mern_mar11@cluster0.7ocxykt.mongodb.net/database_delete2?retryWrites=true&w=majority&appName=cluster0"

// let us load Schema class
const Schema = mongoose.Schema;

// let us create Schema using Schema class
const createSchema = new Schema({
    name: {
        type: String,
        required: true,
        unique: false
    }
})


// now let us create Model -> ultimately creating Collection --> this is the Variable which will have all the Methods to perform CRUD operations
const CollectionModel = mongoose.model("collection_delete2", createSchema)


// connect
// even we can use [ mongoose.connect() ] outside the Async function if you want to get/view the values from this method and perform some operation then we can use this inside async function or use [then/catch] block 
const connect = mongoose.connect(url)

// let us create Async function

const deleteOperation = async () => {

    // delete one
    // const deletedData = await CollectionModel.deleteOne({ name: "pat" })

    // console.log(deletedData)

    // if (deletedData) {
    //     console.log("Deleted successfully!")
    // } else {
    //     console.log("Failed to delete")
    // }


    /* Output :- { acknowledged: true, deletedCount: 1 }
    Deleted successfully! */


    // -------------------


    // Now let us use [deleteMany()] method and try to delete more than 1 document at once 

    const deleteManyDocuments = await CollectionModel.deleteMany({ name: 'pat' })

    if (deleteManyDocuments) {
        console.log("Deleted many documents")
        console.log(deleteManyDocuments)
    } else {
        console.log("failed to delete")
    }


    /*
    Output :- { acknowledged: true, deletedCount: 3 }
    we had 3 documents all the documents are deleted.

    */


    // let us close the mongoose server 

    mongoose.connection.close()
}





deleteOperation()






// Now We learned all the Mongoose methods to perform CRUD Operations [ Create, Read, Update, Delete ]
















