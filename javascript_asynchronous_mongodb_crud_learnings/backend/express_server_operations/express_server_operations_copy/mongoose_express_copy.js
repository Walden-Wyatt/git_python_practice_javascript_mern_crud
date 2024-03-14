

// Here we will be Learning on how to perform CRUD Operations using Express and MongoDb

// Here we will be using Express and Mongoose library to perform CRUD Operations

// load express and mongoose library

const express = require("express")
const mongoose = require("mongoose");


// create code for Mongodb
const url = "mongodb+srv://mern_mar11:mern_mar11@cluster0.7ocxykt.mongodb.net/express_mongoose?retryWrites=true&w=majority&appName=Cluster0"

// create schema 
const Schema = mongoose.Schema;
const createSchemaPattern = new Schema({
    name: {
        type: String,
        required: true,
        unique: false
    }
})


// create model 
const CollectionModel = mongoose.model("express_mongoose_collection", createSchemaPattern)


// now let us connect to Mongodb using connect method

const connectionInfo = mongoose.connect(url, {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then((data) => {
    console.log("Connected successfully")
}).catch((error) => {
    console.log(console.error())
})


console.log(connectionInfo)


// -------------------------------------

// express code

// create the server instance
const app = express()


/*
 Middleware --> below code is very important as it will parse the Data which has been sent from the other server (frontend server, api testing server, etc )
 if you do not use the below code which means we cannot able perform requests such as [ POST, PUT, DELETE ] where we will be getting the datas from other servers.
 
     When a request comes into your Express application, the express.json() middleware intercepts it before it reaches your route handlers.
    It reads the data from the request body and parses it as JSON.
    It then attaches the parsed JSON data to the req.body property of the request object.
    This allows your route handlers to access the JSON data from the request body using req.body.

 it is the means for communication between [ Client or API server ] and our [Local server or express server ]

 // when we get request from the Client server [ express.json() ] will stop the (interpreter will stop reading next lines of code ) --> [express.json() ] will add incoming data_value inside [ req.body ] property ---> after adding (interpreter) will start reading the next lines of codes ==> Now when it reaches [ post route ], this route will have [res.body] property now this property will have data which has been fetched from the Client(frontend or API tool), previously [res.body] was "null"  --> Now inside [app.post() ] callback function when we try to console "req.body" property --> we will be getting the Data which has been sent from the [ Client or API tool ].
 */
app.use(express.json())



app.get("/", async (req, res) => {

    // let us create try...catch block to overcome error in the below lines of codes

    try {
        console.log("Hello get data")
        const getData = await CollectionModel.find({})
        console.log(getData)
        /*
         Why is that you're not getting data ? Remember 1 things we have to create the documents inside the Collection which was created by the Mongoose Library --> if we try to provide our own [database and collection name ] and try to access we will not get the data --> even though the [ database and collection ] name are correct still we will not get the datas.
        */

        res.send(getData)
    }
    catch (error) {
        console.log(error)
    }


})




// --------------------------------------------------------------------------------------------------------------------------------------------------------





// Here let us write the code to Perform POST Request

// use [req.body()] to get the data which has  been sent from the other server or frontend server

app.post("/", async (req, res) => {

    try {


        const postedData = req.body
        /* The data which is stored inside [ postedData ] is a Javascript Object --> we converted this data using the above method [ app.use(express.json())] 
          when you string as a datatype value which means its a [json] datatype --> when you get [ object ] which means its [ javascript ] object datatype
        */

        // Now let us try to post the data inside [ Mongodb ]

        /*
        what happens when we convert the data to JSON object using (stringify) and try to post the converted daata inside database ?
    
         Error :- [ TypeError: First argument to `Model` constructor must be an object, **not** a string. Make sure you're calling `mongoose.model()`, not `mongoose.Model()`.  ]
          we get this error when we try to convert the data  which we fetched using [ req.body ] using [ JSON.stringify()] --> when we do this our javascript object will be converted to JSON ---> we are not allowed to use String as value for [ new CollectionModel() ] --> only objecct is allowed 
           By default when we get the data -->the data will be of Javascript Object ---> when we use it inside [ new CollectionModel() ] behind the scene this methods converts it into JSON and posts it inside the Database.
    
           // do not try to post [ JSON ] data 
           
         [CODE ]  -- const postedData_toJson = JSON.stringify(postedData)
        */


        const postIntoMongoDB = new CollectionModel(postedData)
        console.log(postIntoMongoDB)


        const savePost = await postIntoMongoDB.save()


        if (savePost) {
            console.log("Data posted successfully")
        } else {
            console.log("Fail to post data")
        }

    } catch (error) {
        console.log(error)
    }

})


// Here we have successfully Implemented POST Requests





// ----------------------------------------------------------------------------------------------------------------------------------------------------------






// Now let us Implement [ UPDATE Route ]
// Here let us learn on how to perform Update Operation using [put] method


app.put("/:id", async (req, res) => {

    const { id } = req.params;
    const { name } = req.body;

    console.log(typeof req.params.id)

    /*
    [ "/:id" ] -- here we can see that we inside the URL we used ":id" --> this is actually a Paramete which can be used to get some datas from the URL 
     what ever value which we pass after [/] will be stored inside [res.params.id ] --> this "id" property refers to the name which we have given in the URL --> we can can use any name instead of "id"  --> to access params information we have to use "id" or any other custom name

    */


    /*
     [req] --- the data which we get from the Client(Frontend or API ) will be stored inside [req] specifically [req.body] --> The Places where we can use "req" is when we perform [ POST, PUT, DELETE ] operations
     [res] -- the data which we send to the client(Frontend or API) will be stored inside [res] ---> The places where we can use "res" is when we perform [ GET ] operations.
     */






    // load colllection use [ findOneAndUpdate() ] method 

    /* 
    create filter query 
     Here make sure to use [ req.params.id ] as a filter option, do not use Manual values because we will be getting the Datas from the Client (frontend or api)
    */
    // const filterUpdate = { name: id }
    // let us directly use [ req.params.id ] as a value for [name] property 
    const filterUpdate = { name: req.params.id }  // we can directly use [ req.params.id ] for [ name ] property we will not get any errors.




    /*
     let us create New Value ---> New Value will be present inside [ req.body ] because that the place where the values which was sent from the Client (frontend or api) will get stored.

     */

    // const newUpdateValue = { $set: { name: name } }
    const newUpdateValue = { $set: req.body }  // we can even directly use [req.body] as a value for [$set] anyhow [ res.body] will have an object only


    const updateData = await CollectionModel.findOneAndUpdate(filterUpdate, newUpdateValue)

    console.log(updateData)

    // now let us conditionally render the message weather or not the database got updated

    if (updateData) {
        console.log("Updated Successfully")
    }
    else {
        console.log("Fail to Update")
    }





})



// Here we have Successfully Implemented Update Operations





// --------------------------------------------------------------------------------------------------------------------------------------------------------------------




// Now Let us Implement [ Delete Operation ]
// To implement this we will be using [ delete ] route


app.delete("/:id", async (req, res) => {

    const { id } = req.params
    console.log(id)


    try {

        // ----------------------
        // let us create delete operation using [ deleteOne() ] method

        // const deleteData = await CollectionModel.deleteOne( { name: req.params.id } )
        // console.log(deleteData)
        // ----------------------



        // Here let us use [ deleteMany() ] to delete Multiple Document at once ---> those documents which has been matched with the Query pattern all those documents will get Deleted at Once.


        const deleteMany = await CollectionModel.deleteMany({ name: id })

        console.log(deleteMany)


        /*
         now let us conditionally send the message weather the data got deleted or not --> To do this let us make of [ deleteCounte ] property which we got as returned value from [ CollectionModel.deleteOne()  ] which is currently inside [deleteData]
           because delete count is the place where we get to now the data got deleted or not [0] means falsy value any number other than "0" [1-9] is a Truthy value
         */

        if (deleteMany.deletedCount == 0) {
            console.log("Failed to delete the data")
        } else {
            console.log("Deleted Successfully !")
        }

        /* Output :- [ { acknowledged: true, deletedCount: 4 }  ] -- here we can see that we have successfully deleted multiple docuements at once using [deleteMany()] method
        */




    }
    catch (error) {
        console.log(error)
    }

})



// Here we have Successfully Performed Delete Oprations using Express and MongoDB



/*
Points Observered :-

 Express is mainly used to Get the Routes or Track the Routes 
 MongoDB is the Place where CRUD operations actual happens ---> inside every Express routes we will be performing associated Operations, Means inside every route we will be write Code using mongoose library which will perform some operations inside the MongoDB database.

*/















// start the Server 
app.listen(5000, () => {
    console.log("Server stated")
})


/*

It is not mandatory to use Http request methods in between [ express() instance ] and [ app.listen() ] method 
we can use [ app.get() , app.post(), app.update() and app.delete() ] methods at any place, that we can even use this methods below [ app.listen() ] method --> but using above [ app.listen() ] method is a convention

[ CODE ] :-
app.get("/", (req, res) => {
console.log("Hello get data")
res.send("GET DATA")
})
*/




































































