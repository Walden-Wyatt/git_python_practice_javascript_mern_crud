

// here let us build our backend


/*

List of Errors :-
1. [ Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at http://localhost:5000/. (Reason: CORS header ‘Access-Control-Allow-Origin’ missing). Status code: 200. ]
 when you get this error which means our Backend server (express) is not allowing us to access the datas which is present inside it, by default all the Library which we use to write backend will not allow the frontend to access the datas
   To Overcome this Issue we have make use of [CORS] library which will stop the express library from restricting the frontend to access the datas ---> All the Backend codes are written   using [ CORS ] for Peaceful interaction with frontend and Backend

   How to set up CORS ?
   1. install cors using [ npm install cors]
   2. load the cors library inside you express file -- [ require("cors")] assign it to a variable [ cors ] --- now [cors] will have a function defination
   3. now invoke [cors()] and pass as a Arguement for [ use() ] middleware ---> [ expressInstance.use(cors()) ]
   4. If you want you want your express server to be accessed only by specific IP address, follow the  below cors pattern
     a - [  const allowedOrigins = ['http://example1.com', 'http://example2.com']; app.use(cors({ origin: function (origin, callback) { if (allowedOrigins.includes(origin) || !origin) { callback(null, true); } else { callback(new Error('Not allowed by CORS')); } } }));   ]
 This is very important code to learn as it access our websites backend datas.

*/






// load necessary packages [ express and mongoose ]

const express = require("express")
const mongoose = require("mongoose")
const dotenv = require("dotenv")
const CORS = require("cors")
const bson = require("bson")


/*
To access variables from [.env] file follow the below steps 
1. install [ dotenv ]  ---> 2. load [ dotenv ] package using [ require('dotenv') ] assign it to a variable ===> by using the variable call/invoke [ .config() ] method ---> now you can easily access [.env] variables

*/


dotenv.config()




// --------------------------------------------------------

// Code for Mongodb connection
// provide database name in the URL 
const url = process.env.MONGODB_CONNECTION_URL
mongoose.connect(url, { useNewUrlParser: true, useUnifiedTopology: true })
    .then((data) => {
        console.log("MongoDB Connected Successfully")
        // console.log(data)
    })
    .catch((error) => {
        console.log("Mongodb Error while connecting !")
        console.log(error)
    })




// create schema

// load schema

const Schema = mongoose.Schema;

// create schema

const createSchema_pattern = new Schema({
    firstname: {
        type: String,
        required: true,
        unique: false
    },
    lastname: {
        type: String,
        required: true,
        unique: false
    },
    hobby: {
        type: String,
        required: true,
        unique: false
    }
})



// let us create a Model --> to perform CRUD Operations make use of this [ CollectionModel ] class
const CollectionModel = mongoose.model("mern_collection", createSchema_pattern)


//- -----------------------------------------------------------


// Now let write Server code using [ express js ]

const app = express()


// here let us set up CORS by passing it to a middleware 
app.use(CORS())


// make sure to use [ app.use(express.json()) ] this code because this is the code which can be used to parse the data which we got from the frontend, if you do not use this then we cannot able to get the datas.
app.use(express.json())

// let us create GET route
app.get("/", async (req, res) => {
    try {
        // using [CollectionModel] let us load the Documents which is inside [ MongoDB ]
        const getData = await CollectionModel.find({})
        // res.send(getData)
        // console.log(getData)
        res.json(getData)
    }
    catch (error) {
        console.log(error)
        /*
        Error :- [ Error: mern_collection validation failed: hobby: Path `hobby` is required., lastname: Path `lastname` is required., firstname: Path `firstname` is required.  ]
         This error occurs when we fail to provide value for the Required filed, for all the required property value has to be passed mandatorily if not we might encounter above error. 
        */
    }

})


// -----------------------------------------------------------------------------------


// POST Data
// Here let us perform Post request

app.post("/", async (req, res) => {

    try {
        const postedData = await new CollectionModel(req.body)
        const saveData = await postedData.save()

        if (saveData) {
            console.log("Posted Data successfully")
        } else {
            console.log("Failed to Post the Data")
        }
    }
    catch (error) {
        console.log(error)
    }

})



// -----------------------------------------------------------------------------------


// DELETE Data


app.delete("/:id", async (req, res) => {

    try {

        const { id } = req.params
        // console.log(id)
        const ObjectId = new bson.ObjectId(id)
        const deleteData = await CollectionModel.deleteOne({ _id: ObjectId })

        console.log(deleteData)
        if (deleteData.deletedCount == 0) {
            console.log("Failed to delete data")
        } else {
            console.log("Data Deleted successfully !")
        }

    }
    catch (error) {
        console.log(error)
    }

})


// ---------------------------------------------

// Update Route using [PUT] method -- here let us create Update Route

app.put("/:id", async (req, res) => {
    const { id } = req.params
    const { body } = req
    const ObjectId = new bson.ObjectId(id)

    // write the code to update the mongodb database
    // update filter query 
    const filterQuery = { _id: ObjectId }
    const newUpdateData = { $set: body }


    const updateData = await CollectionModel.updateOne(filterQuery, newUpdateData)

    if (updateData.acknowledged) {
        console.log("Updated Successfully")
    } else {
        console.log("Failed to Update Data")
    }



})








app.listen(process.env.PORT, () => {
    console.log("Express Server running on PORT 5000")
})


























