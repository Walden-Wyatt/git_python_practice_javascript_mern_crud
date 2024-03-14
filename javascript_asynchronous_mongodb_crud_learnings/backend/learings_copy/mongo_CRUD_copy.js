

// var mongodb = require("mongodb")
// // Now inside [mongodb] an Object gets loaded

// // console.log(mongodb)
// /*
//  Output :-
//    PS C:\ Users\user\ Desktop\mern_app\ backend> node index_crud.js { BSON: [Getter], Binary: [Getter], BSONRegExp: [Getter], BSONSymbol: [Getter], Code: [Getter], DBRef: [Getter], Decimal128: [Getter], Double: [Getter], Int32: [Getter], Long: [Getter], Map: [Getter], MaxKey: [Getter], MinKey: [Getter], ObjectId: [Getter], Timestamp: [Getter], ChangeStreamCursor: [Getter], ObjectID: [Function: ObjectId] { getInc: [Function (anonymous)], generate: [Function (anonymous)], createPk: [Function (anonymous)], createFromTime: [Function (anonymous)], createFromHexString: [Function (anonymous)], isValid: [Function (anonymous)], fromExtendedJSON: [Function (anonymous)], index: 16160105 }, MongoBulkWriteError: [Getter], MongoAPIError: [Getter], MongoAWSError: [Getter], MongoBatchReExecutionError: [Getter], MongoChangeStreamError: [Getter], MongoCompatibilityError: [Getter], MongoCursorExhaustedError: [Getter], MongoCursorInUseError: [Getter], MongoDecompressionError: [Getter], MongoDriverError: [Getter], MongoError: [Getter], MongoExpiredSessionError: [Getter], MongoGridFSChunkError: [Getter], MongoGridFSStreamError: [Getter], MongoInvalidArgumentError: [Getter], MongoKerberosError: [Getter], MongoMissingCredentialsError: [Getter], MongoMissingDependencyError: [Getter], MongoNetworkError: [Getter], MongoNetworkTimeoutError: [Getter], MongoNotConnectedError: [Getter], MongoParseError: [Getter], MongoRuntimeError: [Getter], MongoServerClosedError: [Getter], MongoServerError: [Getter], MongoServerSelectionError: [Getter], MongoSystemError: [Getter], MongoTailableCursorError: [Getter], MongoTopologyClosedError: [Getter], MongoTransactionError: [Getter], MongoUnexpectedServerResponseError: [Getter], MongoWriteConcernError: [Getter], AbstractCursor: [Getter], Admin: [Getter], AggregationCursor: [Getter], CancellationToken: [Getter], ChangeStream: [Getter], ClientSession: [Getter], Collection: [Getter], Db: [Getter], FindCursor: [Getter], GridFSBucket: [Getter], GridFSBucketReadStream: [Getter], GridFSBucketWriteStream: [Getter], ListCollectionsCursor: [Getter], ListIndexesCursor: [Getter], Logger: [Getter], MongoClient: [Getter], OrderedBulkOperation: [Getter], UnorderedBulkOperation: [Getter], Promise: [Getter], BatchType: [Getter], GSSAPICanonicalizationValue: [Getter], AuthMechanism: [Getter], Compressor: [Getter], CURSOR_FLAGS: [Getter], AutoEncryptionLoggerLevel: [Getter], MongoErrorLabel: [Getter], ExplainVerbosity: [Getter], LoggerLevel: [Getter], ServerApiVersion: [Getter], BSONType: [Getter], ReturnDocument: [Getter], ProfilingLevel: [Getter], ReadConcernLevel: [Getter], ReadPreferenceMode: [Getter], ServerType: [Getter], TopologyType: [Getter], ReadConcern: [Getter], ReadPreference: [Getter], WriteConcern: [Getter], CommandFailedEvent: [Getter], CommandStartedEvent: [Getter], CommandSucceededEvent: [Getter], ConnectionCheckedInEvent: [Getter], ConnectionCheckedOutEvent: [Getter], ConnectionCheckOutFailedEvent: [Getter], ConnectionCheckOutStartedEvent: [Getter], ConnectionClosedEvent: [Getter], ConnectionCreatedEvent: [Getter], ConnectionPoolClearedEvent: [Getter], ConnectionPoolClosedEvent: [Getter], ConnectionPoolCreatedEvent: [Getter], ConnectionPoolMonitoringEvent: [Getter], ConnectionPoolReadyEvent: [Getter], ConnectionReadyEvent: [Getter], ServerClosedEvent: [Getter], ServerDescriptionChangedEvent: [Getter], ServerHeartbeatFailedEvent: [Getter], ServerHeartbeatStartedEvent: [Getter], ServerHeartbeatSucceededEvent: [Getter], ServerOpeningEvent: [Getter], TopologyClosedEvent: [Getter], TopologyDescriptionChangedEvent: [Getter], TopologyOpeningEvent: [Getter], SrvPollingEvent: [Getter] } PS C:\Users\user\Desktop\mern_app\backend>
// */



// // ------------------------



// // Now inside [mongodb] there is Variable called [ MongoClient ] which will have a "Class" as its value --> let us load it and assign it to a variable
// var connectMongodb = mongodb.MongoClient

// // console.log(connectMongodb)
// /*
//  Output :- [class MongoClient extends TypedEventEmitte
//  Inside [ connectMongodb ] variable there will a Class which will get loaded, There are many methods and Properties by using them we can access the MongoDB to perform CRUD Operations

// */



// // ------------------------

// var url = "mongodb+srv://mern_mar11:mern_mar11@cluster0.7ocxykt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

// /*
// Now [connectMongodb] will have a method called [connect()] by using this method we can load the MongoDB project inside some Global variable (which we will be creating).
//  This Method accepts 2 arguements [ Mongodb_url_path and Call Back Function ]

//  1. [ Mongodb_url_path ]
//    # here we have provide the connection string of MongoDB so that we can connect to MongoDB database

//  2. [ Call Back Function ]
//    # There we have to provide a Call Back function  --> By using this callback function we can get the Project from the MongoDB
//     # This call back function will accept 2 arguements [ Error and client ]
//      # [ Error ] - This arguement will have Error message, This Error variable will have value or invoked in 2 situations
//        # 1. When You did not allowed the Currect IP Address to access the MongoDB Server
//        # 2. when there is mistake in MongoDB [username or password ]

//      # [ client ] =
//         This 'client' arguement will have MongoDB Project Instance, here inside the "client" parameter our Project which is present inside MongoDB as well as the Project which we are tring to access will get Loaded
//         By using this client paramete we can access the Database
//         Inside [client] variable we there will be list of [databases] will be present which we have created inside that specific project
//         client method will return an object, by using [db("database_name")] method we can access the Databases which is present inside the MongoDB Project

//         # here we will create a variable in the Global Environment by assigning "undefined" as its value
//         # The same Global variable we will be pass inside this Callback function and assign the [client] parameter as its value
//          # Now we can access "client" parameter in the Global Environment --> by this we are Ultemately accessing MongoDB Project


//        */



// // Here we have Global Variable where we will be storing MongoDB Project which is present inside "client" parameter of [connect()] Callback function
// /*
// We cannot able to access [client] parameter value which is present inside [ connectMongodb.connect()] method this is Because of Asynchronous Nature
//  # here [ var mongoDb_project; ] is synchronous code -- > All synchronous code will execute First
//  # [ connectMongodb.connect() ] is an Asynchronous code ==> which means this code will get executed after synchronous code
//   # when synchronous variable depends on the Value which has been written from Asynchronous code ---> in such situation synchronous variable will be "undefined"
//     # This is because Synchronous Code Gets Executed Even before Asynchronous code which has the value for [ Synchronous variable ] --> so ultemately the Synchronous variable will have "undefined" as its value.
// */
// var mongoDb_project;




// connectMongodb.connect(
//   url,
//   (error, client) => {
//     if (error) {
//       console.log("Error while Connecting")
//     }
//     else {
//       // console.log("Connected Successfully")

//       // here we have re-assigned [mongoDb_project] where the value is 'client' ---> Now 'mongoDb_project will have [ Mongodb project Instance ] ---> Inside [ Mongodb project Instance ] we can find list of Databases.
//       mongoDb_project = client

//       console.log(mongoDb_project)


//     }
//   }
// )


// // Now let us access [ mongoDb_project ]

// console.log(mongoDb_project)









var abc = "hello"

console.log(abc)

let func = () => {

    abc = "New Hello"

}

func()

console.log(abc)




// All the Datas which we get from Other server to our current Fill all those Datas will be a Promise object
// Just because we are getting the Datas from other Server it is called as Asynchronous Code :-
/* 
What will happen in Asynchronous Code ? The datas which is Inside the Asynchronous Variable (Code) will be a Promise 
  --> To get the Datas which is inside the Promise Object we have 2 solutions 
   1. Using [ then----Catch ] block 
   2. Use [ Async ----- Await  ] keyword.

  # So To access any Datas which is inside the Asynchronous Function ----> we have to Access it with only Asynchronous functions Only 
  # So when we want to use Any of Asynchronous codes inside any of Regular Functions in Javascript ===> we have to convert that Regular Functions into Asynchronous functions ---> Then when we try to access the Codes of other Asynchronous Function we can easily access those codes.

*/







