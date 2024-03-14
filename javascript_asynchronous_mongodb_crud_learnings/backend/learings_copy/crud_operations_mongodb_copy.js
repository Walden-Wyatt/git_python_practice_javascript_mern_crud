

/*

//let us load mongodb
const mongodb = require("mongodb");


//let us create URL connection string for mongodb
url = "mongodb+srv://mern_mar11:mern_mar11@cluster0.7ocxykt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


// let us load [ MongodbClient ] class

// const mongoclient = mongodb.MongoClient;

// // here let us use [connect() ] method to connect to the MongoDB database
// mongoclient.connect(url, (error, client) => {

//     if (error) {
//         console.log("Error while Connecting")
//     }
//     else {
//         // console.log("Connected successfullly")
//         let project = client.db("curd")
//         console.log(project)
//     }

// })

// /*
// Output :- [ Connected successfullly ]
//  # we got this output because behind the scenes [ mongoclient.connect() ] will have awiat keyword or [then/catch] block execute the callback functions lines of codes

// * /


// ---------------------------------



Mongo_Client = mongodb.MongoClient;


// here we this [mongodbFunction() ] will have instance of [curd] database.
// by using this function we can access the collections
async function mongodbFunction() {
    try {
        let client = await Mongo_Client.connect(url)
        return client.db("crud_db")
    }
    catch (error) {
        console.log(error)
    }
}

// if you want to access the datas which is returned by [ mongodbFunction() ] we have to use [then/catch] or [async/await]
// console.log(mongodbFunction())

// Now let us create a Function throught which we can access the datas

async function getMongodbData() {


    /*
     If you see the below code for Every MongoDB methods which we used we have preceeded with [ await ] keyword such as
      [ mongodbFunction(), database.collection(), collection.find(), findData.toArray()  ] which has been given below.

    * /

    try {
        let database = await mongodbFunction()
        // console.log(database)
        // let collection = await database.collection("curd_collection")

        let collection = await database.collection("crud_collection")
        // console.log(collection)

        // let us use [ find() ] method which is inside [ collection ] variable
        // Now inside [ findData ] cursor object has been loaded --> to get the actual data we have to convert it into Array by using [ toArray() ] method which is inside [ cursor ] object
        let findData = collection.find()
        // console.log(findData)

        let actualData = await findData.toArray()
        console.log(actualData)

        /*
        Output :-  []
         Here we got empty array as a Output even thought we have some data inside the Database-
         # This is because when you make mistake in [ Database or Collection ] name, When you provide wrong Database or collection name you get this error
           # [ return client.db("curd_db") ] -- here the database name must be [ "crud_db"] but you have given "curd_db"
         # Code [ let collection = await database.collection("curd_collection")  ] -- here you can see that we have provided wrong collection name, it should be ["crud_collection"] but you provide "curd_collection"

        * /


        // Now we got the Right output :- [  [ { _id: new ObjectId("65f02ee142d4768a076ed013"), name: 'windows' } ]  ]



    }
    catch (error) {
        console.log(error)
    }
}


getMongodbData()



*/




// ------------------------------------------------------------------------------------------------------------------------------------------------------------




/*

 There are 3 Approach where we can use MongoDB Operations
 1. Create Async/Await functions for all the Operations which you will be using to perform CURD operation
   # In this Approach Each and every Function has to be return the next Methods (next step) to perform Operations
    # Example :- [ Client Function has to return "database method" ---> "database method" has to return "collection method" ---> "collection method" has to return "find method" ----> "find method" has to return "toArray method"  ===> Finally we will get the Array of Values which is been loaded into our File.  ]

 2. Create One Async Function for all the Upcoming Operations ( methods used to perform CURD )
   # Inside the Async Function for the Lines which has Async code or ( methods which has Async code ) for those methods we have Preceed with "await" keyword ===> Finally line which will return the [Collection] only for that line we have to preceed "return" keyword
    # Now by using this single method which will have instance of Colllection we can  make use inside any of the HTTP requests such as [ GET, POST, PUT, DELETE, etc ].

 3. Inside [ MongoClient.connect() ] -- we can also write all the CRUD Operations code inside the callback function which we will be passing as a 2 arguement for [ connect() ]

*/






// --------------------------------------------------------------------------------



// Let us use One Function and console all the methods which are responsible for [ Performing Find Operation ]



/*


const mongodb = require("mongodb")

// let us access [ MongoClient ] class

const MongoClient = mongodb.MongoClient


// let us create an url connection string
const url = "mongodb+srv://mern_mar11:mern_mar11@cluster0.7ocxykt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


// Now let us access [ connect() ] method, This method will return a Promise because we are try to connect to other server
// Let us Load Mongodb project
// since we are going to perform Asynchronous tasks we will be craeting a Async function
const asyncCheckFunction = async () => {

    // const connect = await MongoClient.connect() # When you do not pass appropriate arguements for [ connect() ] method you will this error [  TypeError: Cannot read properties of undefined (reading 'startsWith')  ]
    /*

    Error :- [  TypeError: client.db is not a function  ]
     we get this Error when we do not await for connection, as soon as it starts the code gets immediately invoked, which means all the lines of code is an Synchronous code
      // to overcome this error preceed [await] before [ const client = MongoClient.connect(url) ]

      as soon as we used [await ] for [ connect() ] method all the codes gets loaded even if we do not use [ await ] for other Methods which will perform server actions.

    * /
    // const client = MongoClient.connect(url)
    const client = await MongoClient.connect(url)
    console.log(client)

    // let us load Database using [ db ] method
    const database = client.db("crud_db")
    console.log(database)

    // let us load collection using [ collection ] method
    const collection = database.collection("crud_collection")
    console.log(collection)

    // let us laod find  using [ find ] method
    const find = collection.find()
    console.log(find)

}



asyncCheckFunction()



*/








// --------------------------------------------------------------------------------



// Now let us Use Multiple Functions to get the Final Array values


/*


const mongodb = require("mongodb")

const MongoClient = mongodb.MongoClient;

const url = "mongodb+srv://mern_mar11:mern_mar11@cluster0.7ocxykt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"



// function 1 which will return [ Project ]

async function returnClient() {

    const client = await MongoClient.connect(url)
    // console.log(client)
    return client

}

// console.log(returnClient())


// function 2 which will return [ Database ]

async function returnDatabase() {
    // when you want to use the Other fucnctions Promise inside a New function, when the [ await ] and [ function invokation  ] must be wrapped then we have to access appropriate methods and Properties which the method returns
    const database = (await returnClient()).db("crud_db")
    return database
}


// console.log(returnDatabase())



// function 3 which will return collection

async function returnCollection() {
    const collection = (await returnDatabase()).collection("crud_collection")
    return collection
}


// console.log(returnCollection())



// function 4 which will return find methods data

async function returnFind() {
    const find = (await returnCollection()).find()
    return find
}

// console.log(returnFind())




// function 5 which will return Array by converting [findCursor ] object using [ toArray() ] method

async function returnToArray() {
    const toArray = (await returnFind()).toArray()
    return await toArray
}


console.log(returnToArray().then(v => console.log(v)).catch((err) => console.log(err)))


// Output :- [ [ { _id: new ObjectId("65f02ee142d4768a076ed013"), name: 'windows' } ]  ]
// Here we finally got the output



*/




// ---------------------------------------------------------------------------------------------------------



//  2. Create One Async Function for all the Upcoming Operations ( methods used to perform CURD )

// Here we will have only 1 function which will return collection ---> This function can be used in other Request methods to perform appropriate requests


/*



const { json } = require('express')
const mongodb = require('mongodb')
// let us create MongoClient
const MongoClient = mongodb.MongoClient


const url = "mongodb+srv://mern_mar11:mern_mar11@cluster0.7ocxykt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

// now let us load Project

// async function

const collectionData = async function () {
    const client = await MongoClient.connect(url) // because this is an Asynchronous code which will return a Promise let us wrap this with asynchronous Functions

    const database = client.db("crud_db")

    const collection = database.collection("crud_collection")

    return collection

    const find = collection.find().toArray()

    return find

}

console.log(collectionData())



const accessDocumentsData = async function () {
    // const collectionInfo = await (await collectionData()).find().toArray()
    const collectionInfo = await collectionData() // here we have to use [ await ] for [ collectionData() ] method which will return a promise
    const find = collectionInfo.find()  // here we don't need to use [await] for [ find() ] method in this approach, even though if we use it will not have any effect
    const toArray = await find.toArray() // for [ toArray() ] method also we have use [ await ] method because this [find()] variable will have a Promise, in order to resolve it we must use await.
    console.log(toArray)
    /*
    Output :- [ { _id: new ObjectId("65f02ee142d4768a076ed013"), name: 'windows' } ]
     Finally we got the Output successfully

     Now we can use [ collectionData()  ] function inside inside any Function where we will be performing Requests such as [GET, POST, PUT, DELETE, etc ].
    * /


    // -------------------
}

accessDocumentsData()


*/




// -------------------------------------------------------------------------------------------------------------------------------------------------


// Let us Perform Insert Operations using [ InsertOne() and InsertMany() ] method




/*


const mongodb = require("mongodb")

const MongoClient = mongodb.MongoClient

const url = "mongodb+srv://mern_mar11:mern_mar11@cluster0.7ocxykt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


const insertData = { name: "mark burb" }

const insertManyData = [{ name: "Ambani" }, { name: "Abraham" }, { name: "Francis" }]


const insertFunction = async () => {

    try {
        const client = await MongoClient.connect(url)
        // console.log(client)
        const database = client.db("crud_db")
        // console.log(database)
        const collection = database.collection("crud_collection")
        // console.log(collection)

        /* here we used [insertOne() ]  and passed necessary objects which will get inserted inside the Mongodb database
         even if you do not preceed with "await" keyword data gets inserted without any error, But it is always recommended to use await becuase we are performing some operations inside other database (which will be a Asynchronous Code)
        code :- collection.insertOne(insertData)



        ---------------------------------------


        Observation -
         Here if you see that we did not convert Javascript Object into JSON using (stringify) but still we can able to post the data

         what happens when to try to Convert the Javascript data to JSON then try to Insert ?

        const jsonInsertData = JSON.stringify(insertData)
        await collection.insertOne(jsonInsertData)
        Error :- [  TypeError: Cannot create property '_id' on string '{"name":"mark burb"}'  ]
        The above error occurs when you try to convert Javascript code to JSON using "stringify" method ,  we are not allowed to do so please do not do it

        ** Do not convert the javascript code to JSON ---> pass only the Javascript code ---> behind the scene mongodb package will do all those Necessary things



        * /

await collection.insertOne(insertData)


// ------------------------------

/*
 Now let us use [insertMany()] method and try to insert more than 1 documents(object)

 # [insertMany()] - we are successfully inserted the Datas by using (insertMany()) method --->  inside our MongoDb database without any errors
  # if you want to insert Multiple Documents or Objects at once you can use [insertMany()] method

* /

await collection.insertMany(insertManyData)


console.log("Data inserted successfully!")

    }
    catch (error) {
    console.log(error)
}

}

insertFunction()



    */




// -------------------------------------------------------------------------------------------------------------------------------------------------


// Let us Perform Update Operations using [ UpdateOne() or UpdateMany() ] method



/*


const mongodb = require("mongodb")

const Mongo_Client = mongodb.MongoClient

const bson = require("bson")

const url = "mongodb+srv://mern_mar11:mern_mar11@cluster0.7ocxykt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

const updateOperation = async () => {

    const client = await Mongo_Client.connect(url)

    const database = await client.db("crud_db")

    const collection = await database.collection("crud_collection")

    try {

        /*

        await collection.updateOne(
            { name: "windows" },
            { $set: { name: "New Name for Windows" } }
            /*
             { name: "New Name for Windows" }
            Error : - MongoInvalidArgumentError: Update document requires atomic operators
              This Error occurs when we do not use atomic operators to update the document, Atomic operators are [$set, etc], here we have to use [$set]
            * /
        )

        console.log("Updated Successfully")

*/

// Here This updateOne has updated the document without any error


// ------------------------------------------------------------

/*

If you want to Update the Docuement using the (_id) property which is present inside the Document we have to use [ ObjectId ] class from [bson] library
  Import [ ObjectId ] from [ bson ] library ---> when passing the value for [_id] the value has to be passed as an arguement for [ObjectId()] class

*/



/*
 here we will use [_id] as a Filter option to filter the Object(document)
  Here ObjectId() class has to be invoked using [ new ] keyword else you will get the following error [ TypeError: Class constructor ObjectId cannot be invoked without 'new'  ]
 * /
await collection.updateOne(
    // { _id: bson.ObjectId("65f02ee142d4768a076ed013") }, # [ TypeError: Class constructor ObjectId cannot be invoked without 'new'  ], we are suppose to invoke "ObjectID" class with "new" keyword, this how it should be [{_id: new bson.ObjectId("65f02ee142d4768a076ed013")}]
    { _id: new bson.ObjectId("65f02ee142d4768a076ed013") },
    { $set: { name: "Rosa" } }
)

console.log("Updated Succesfully")

// Here we have updated the Document using [ updateOne() ] method




// ------------------------------------------------------------------------

// Now let us update many documents using [ updateMany() ] method

/*
Let us try to Update {name: "john doe"} because we have 2 matching documents
* /

await collection.updateMany(
    // { name: "John doe" },
    // { $set: { name: "Changed John Doe" } }
    { name: "hendry" },
    { $set: { name: "New Chagned Hendry" } }
)

        // Here we have successfully performed [Update Many ] operations






    }
    catch (error) {
    console.log(error)
}




}

updateOperation()





    */





// ----------------------------------------------------------------------------------------------------------------------------------------------------


// Let us Perform Delete Operations using [ DeleteOne() or DeleteMany() ] method


const mongodb = require("mongodb")

const Mongo_Client = mongodb.MongoClient

const url = "mongodb+srv://mern_mar11:mern_mar11@cluster0.7ocxykt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

const deleteOperation = async () => {
    const client = await Mongo_Client.connect(url)
    const database = await client.db("crud_db")
    const collection = await database.collection("crud_collection")

    try {

        /*
         Here we used [ deleteOne() ] method which means only Only document (Object) inside the MongoDB collection gets deleted
         If there are more than one document which the Matched Filter option -- In such situation Only One Document from the MongoDB database Gets deleted 
        */
        await collection.deleteOne({ name: "Changed John Doe" })

        /* 
        Now let us try to Delete more that one document at once using [ deleteMany() ] method

         Let us try to delete [ name:  "New Chagned Hendry" ] where we have more than one document with the same name
        */

        await collection.deleteMany({ name: "New Chagned Hendry" })


        console.log("Deleted Successfully!")



        // [ deleteMany() ] has successfully deleted the Multiple document which has been Matched with the delete query which we have provided

    }
    catch (error) {
        console.log(error)
    }

}



deleteOperation()



/*
If the Query which we have provided does not match in such situation nothing is going to Happen.

*/



// Finally we have performed CRUD [Create, Read, Update, Delete] Operations Using "mongodb" library inside MongoDB Database 





