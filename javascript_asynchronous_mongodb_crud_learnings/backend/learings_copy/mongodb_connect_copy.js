const express = require("express");
const mongodb = require("mongodb");

/*


# Important :-
 # if you come across any Issues with any of the Packages which you have installed to make use in your code try this solution 
   # solution :- Try to install Previous version of the Package than the current pagkage you have installed (lower version) than the current Version

   # ex: MongoDB 6.5.0 is the Latest version of "mongodb" package --- when we use this version MongoDB is not displaying any message weather it has been connected or not when we use [if...else] block -- This is actully an error 
    # so i tried to insatll MongoDB(4.1.0) which is the Previous (Lower version) when compared to MongoDB(6.5.0)
    # This Approach can be used for all the Packages which you have installed, If you any errors with the Packages which you have installed.

    # MongoDB Testing :-
    # Supported Version of MongoDB -- Express -- node
      # MongoDB -- [ 4.17.2, 4.17.1, 4.17.0, 4.1.0 ]
    # Not Supported Version of MongoDB -- Express -- node
      # MongoDB -- [ 6.5.0, 6.4.0, 6.3.0, 6.2.0, 6.1.0, 6.0.0, 5.9.2, 5.9.1, 5.9.0  ]

    # Please try install and use only Supported version of MongoDB which has been given above.


*/

const app = express();
const MongoClient = mongodb.MongoClient;

const connectionString = "mongodb+srv://investob848:python_workings@cluster0.t8nusx1.mongodb.net/?retryWrites=true&w=majority&appName=cluster0";

MongoClient.connect(connectionString, (err, client) => {
    if (err) {
        console.error("Error connecting to MongoDB:", err);
    } else {
        console.log("Successfully connected to MongoDB!");

        // Additional operations or code inside the MongoDB connection callback if needed
    }
});

app.listen(5000, () => {
    console.log("Express server is running on port 5000");
});




// -----------------------------------------------------








// const express = require('express');
// const mongoose = require('mongoose');

// const app = express();
// const PORT = 3000;
// connectionString = "mongodb+srv://mern_mar11:mern_mar11@cluster0.7ocxykt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

// // Connect to MongoDB using Mongoose
// mongoose.connect(connectionString, { useNewUrlParser: true, useUnifiedTopology: true });

// // Check the connection
// const db = mongoose.connection;
// db.on('error', console.error.bind(console, 'MongoDB connection error:'));
// db.once('open', () => {
//     console.log('Connected to MongoDB');

//     // Additional setup or database operations can be performed here

//     // Start the Express server
//     app.listen(PORT, () => {
//         console.log(`Server is running on http://localhost:${PORT}`);
//     });
// });

// // Define your Mongoose schemas, models, routes, and other Express middleware below





//---------------------------------------------------------------------------------------------------------





// const { MongoClient, ServerApiVersion } = require('mongodb');
// const uri = "mongodb+srv://mern_mar11:mern_mar11@cluster0.7ocxykt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";

// // Create a MongoClient with a MongoClientOptions object to set the Stable API version
// const client = new MongoClient(uri,
//     //     {
//     //     serverApi: {
//     //         version: ServerApiVersion.v1,
//     //         strict: true,
//     //         deprecationErrors: true,
//     //     }
//     // }

// );

// async function run() {
//     try {
//         // Connect the client to the server	(optional starting in v4.7)
//         await client.connect();
//         // Send a ping to confirm a successful connection
//         await client.db("ciplox").command({ ping: 1 });
//         console.log("Pinged your deployment. You successfully connected to MongoDB!");
//     } finally {
//         // Ensures that the client will close when you finish/error
//         await client.close();
//     }
// }
// run().catch(console.dir);



