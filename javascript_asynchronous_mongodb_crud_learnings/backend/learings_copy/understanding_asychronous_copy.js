

// Here we will Understand how Asychronous Works ?
/*
First All the [ Synchronous codes ] will get Executed
Next All the [ Asynchronous codes ] will get Executed

*/


// When we can use Asychronous Operations in JavaScript ?
/*
 When we want to Perform HTTP Requests
  Basically when we want to get datas from Other Servers using Our Own Server(from our server).
  All the Codes which we use to perform HTTP requests such as getting the datas from other server as well as sending the data to other server using following mehtods [ GET, UPDATE, POST, DELETE, etc ]
  When we Get the Datas and Load it into our File The variable which holds the Data will be a [ Promise Object ]
    when we want to get the Data which is inside the Promise Object we have 2 approaches, 1. use [ then__catch block  ], 2. use [ Asych-Await ] functions

*/



// what are the Different approaches to use Access the Asynchronous Codes ?
/*
 All the Asychronous Will return a Promise Object to access the promise object we have 2 Approaches
  1. use [ then--catch  ] Block
  2. use [ Async -- Await ] functions

*/

// Where will The the Code which we write to Get (load) the Datas from Other Server falls(which catagory), weather it is an Synchronous or Asynchronous Codes ?
/*
All the Datas which we get from other Servers Database into our Current file will be an Asynchronous which will get executed at the End after all Synchronous codes gets executed
 # To access this Asynchronous codes we can use 2 approahes [ then---catch block ] or [ Async --- Await  ]

*/

// How to Access the Variables which is inside One Asychronous from Inside another Functions



// ----------------------------------------------------------------------------------------------------




//  Synchronous And  Asynchronous code difference


/*

// Progarm using [ synchronous code ] and [ Asynchronous code using "async await" functions ]

// Synchronous code
console.log("Synchronous Code")

var synchronousFunction = function () {
    console.log("Synchronous Function")
}

synchronousFunction()


// Asynchronous code

const asyncFunction = async function () {

    /*
    [await] - here we can see that we have used await keyword before the promise Object, we are allowed to use [await] only before the Promise Object
    # When ever you use Code which will perform Some operations inside other Server All those Codes are [ Promise Objects ]
     # some of this Codes are [ fetch() function, axios(), etc ] -- All the Libraries which are used to perform CRUD Operations.
      # For this type of codes we can use [ Asych Function ] or [ then - catch ] block to get the Datas which is present inside the Promise Object

    * /
    await new Promise((res, rej) => {
        res("resolved")
    })
    console.log("Asynchronous code")

}


console.log("other synchronous code")

asyncFunction()


/*

 Order of Execution :-

 node understand_asychronous.js
Synchronous Code
Synchronous Function
other synchronous code
Asynchronous code

Here if we see that we have Provided [ asyncFunction() function ] before [ console.log("other synchronous code") ] code but when you see the Output it is vise versa
 first  [ console.log("other synchronous code") ] is executed
 next [ [ asyncFunction() function ]   ] is executed
  # This is because of Asychronous function

  # ** All the Asychronous  Codes will be executed at the Last Once Synchronous Codes gets Executed
   # There are 2 Types of code in Javascritpt (any programming languages)  --> [ Synchronous Codes ] and [ Asychronous Codes ]
   # [RULE] ---- Remember 1 Thing -- Allways in any Programming Languages ---> First [ Synchronous Codes ] will get executed ---> Next(Last)  [ Asychronous Codes ] will get executed


* /


*/





// ===================================================================================================








// Asychronous Operations using [ Synchronous Code ] and [ Asychronous Code with "then....catch" block ]


/*



// synchronous codes

console.log("Synchronous Code 1")

var synchronousFunction = function () {
    console.log("Synchronous Function 1")
}

synchronousFunction()


// asychronous codes


// Now because this Function returns a Promise which means its an Asychronous Code, This code will get executed at the Last after(All Synchronous) finishes its execution
const asyncFunction = async function () {

    return await new Promise((resolve, reject) => {
        resolve("Asychronous Function 1")
    })
}


// Here we used [then and catch] block to resolve the Asychronous code which is present inside the [ asyncFunction() ].
asyncFunction().then((data) => {
    console.log(data)
}).catch((err) => {
    console.log(err)
})


console.log("Synchronous code 2")


/*

 Output :-

 Synchronous Code 1
Synchronous Function 1
Synchronous cod 2
Asychronous Function 1


# see the Output First all the Synchronous codes are Executed next at last all the Asychronous codes are Executed

# From here we got to know that all the Asychronous codes will get executed at the end




* /







*/











// ======================================================================================================================================================================





/*



// How to access the Variables which is inside Asychronous functions


// Try to access at the Top Level of the File

let promiseObject = new Promise((resolve, reject) => {

    if (!true) {

        console.log("async 2")
        // here if you clearly see that the Actual data is inside another function called [ resolve() ], When we invoke it what ever code is present inside [ resolve ] function will get executed.
        resolve("Hello resolve")

        /*
         the Only Synchronous Code in this block is [ resolve() and reject() ] functions Invokations
         whatever value which we provide inside the [resolve() and reject()] arguement will be an Asychronous code, only those value will get executed in an Asynchronous Manner.
         */


/*
behind the scene
const resolve = function(data){
return data
}

resolve(valeu)
* /

}
else {
// here also even in Error block we can see that there is a function called [ reject() ] when there is some some error the data/statements which is present inside the [ resolve ] function will get executed.
reject("Operation failed")

/*
 the Only Synchronous Code in this block is [ resolve() and reject() ] functions Invokations
 whatever value which we provide inside the [resolve() and reject()] arguement will be an Asychronous code, only those value will get executed in an Asynchronous Manner.
 * /


console.log("async 2") // The code which we provide inside the [ if....else] block will execute in an asynchronous manner
}

console.log("Asycn 1")  // The code which we provide in the Callback Function block will execute in an asynchronous manner
});


// How to access the datas which is inside the Promise object

console.log(promiseObject)


// Approach 1 == [ use then catch ]

promiseObject.then((data) => {
/*
The value inside [data] parameter will be the Value which is passed inside the [ resolve() or reject()  ] arguements
usually resovled datas from server will be passed inside [ resolve() ] function arguement , error message will be passed inside [ reject() ] function arguement
* /
console.log(data)
}).catch((err) => {
console.log(err)
})


console.log("Sync 1")



*/








// ======================================================================================================================================================================



// Returning a Promise Object from inside Async Await Function




// promise object

const asyncPromise_Object = new Promise((resolve, reject) => {

    if (!true) {
        reject("Error in resolving data")
        console.log("Reject data ")
    }
    else {
        resolve("Successfully Fetched Data")
        console.log("Resolved data ")
        /*

         Here if we see [ console.log("Resolved data ") ] this line gets Executed inside [ asycnFunction_promise() ] function even if we do not use [await] keyword 
          where as [ resolve("Successfully Fetched Data") ] this line is not getting executed because this the Actual [ Asychronous Code ] ===> Only when we use [ await ] keyword we can see that value which is retured by [ resolve() or reject() ] function 
           apart from [ resolve() and reject() ] -- those lines where we use this function to invoke - apart from that Line rest all the lines of codes which we write inside the [ Promise ] callback function will be Executed in a Synchronous Manner.
           # From here we got to learn that The Actual Asynchronous Data is present inside [ resolve() and reject()  ] function invocations
           
           # *** Imporatant point to remember The Actual Asynchronous code is [ resolve() and reject() ] ===> To Fetch/get the datas which is retured by [ resolved() or reject() ] function we will be using [ then/catch and async/await ] approaches.


           *** 
          When we Fetch/get the Datas from the Other Database server  using http requests such as [ GET, POST, DELETE, UPDATE, etc ] those Datas will be stored inside the [ resolve() ] Function body 
           if we want to fetch/get the datas inside the [ resolve() ] function we must use [ then/catch ] or [async/await] keywords --> if we do not use The statements which is present inside the [ resolve() ] function will not be Executed 



           What happens in MongoDB and Other HTTP Requests which we use to fetch the Data such as [ Fetch() API, axios library, etc ] ?

            All the Callback Functions which we use to Get the datas from the Server, such [ Mongodb.connect( url, callback_function ), axios, express.get(), express.post(), express.update(), express.delete(), etc  ] --> All the Callback function will Get Loaded inside [ resolve() ] function defination, so if we want to access the statements inside the [ resolve() ] function we have use [ then/catch or asych/await ] becuase all the codes which are present inside the [ resolve() or reject() ] is asynchronous ?





            // ----------------------------------


            Now let us Understand what happens when create MongoDB and use "connect()" method ----> as well as when we try to re-assign Global variable inside [ connect() ] callback Function ?


            
connectMongodb.connect(
  url,
  (error, client) => {
  
  
  The below lines of Code will get loaded inside promise [ resolve() ] method ==> To access this [ resolve() ] method ---> this [ resolve() ] method is an Asynchronous code ---> All the Asychronous codes will be Loaded at the Last (once all the Synchronous codes finishes its executions )   --> To access this asychronous code we have to use [ then/catch block or async/await functions ]
  
    # When we try to re-assign [ Sychronous variable ]  from inside [ Asynchronous Function ] ---> [ Sychronous variable ] is not getting re-assinged that because of 2 reasons 
     # 1. Synchronous Codes gets executed before Asynchronous Codes ---> when synchronous code is dependent on Asynchronous function to re-assign the Values it will not get re-assigned even though asychronous has re-assigned we cannot able to see the re-assigned values -- That is because we have to use [ console.log() ] in the Global Environment which is again an Sycnchronous code itself , The [ console.log() ] in the global environment will run in the Synchronous Manner itself 
     # 2. Variables which is inside Asychronous code are Block scoped ----> Only the code gets resolved it can be accessed outside the block --> If Asychronous Code has to get resolved/executed it has to wait till synchronous codes gets executed as well as for Getting the data then it will console the data in the Terminal 
       # If we want to Resolve/Execute the Asychronous Code  ---> the only 2 places is [then/catch block ] and [ async/await function ] 
       


       # The lines of codes which we write inside The Callback Functions of [ Mongodb.connect(), express.get(), express.post(), express.update(), express.delete(), etc  ]  --> It is like we are directly writing those codes inside promise [ resolve() ] methods (which is inside Promise Class Callback function )   --> To execute all this code We can make use of only [ One await keyword inside async function ] or [ then/catch block ]
        # When we use [async/await ] only one function is enough to Execute all the lines of code which is inside the http methods callback functions, such methods are [ mongodb.connect(), express.get(), express.post(), express.delete(), express.update(), etc ].
         # by this way we are resolving the HTTP requests from inside [async] function by using only one [ await ] keyword


       # LEARNINGS :-
        # If you want to access variables which has http requests data make sure to use it inside the [ Async/await Function ] or [ then/catch ]
        # It is always better to use [ async/await function ] as it simplifies by overcoming Callbacks which we have to use in [then/catch] block 
        # There is No way to Re-assign Global Variable (synchronous code) from inside the Asynchronous Codes such as (Asynchronous Funcitons) and (then/catch) block 
        # Remember to Access Asynchronous codes make sure to access it from inside [ Asynchronous codes ] ---> Mainly use [ async/await ] function for Easy accessing.

  
  
    
     %%%%%%%%%%%%%%%%%%%%%%%%---------------------------%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
  
   

    if (error) {  console.log("Error while Connecting") }
    else {// console.log("Connected Successfully")

        // here we have re-assigned [mongoDb_project] where the value is 'client' ---> Now 'mongoDb_project will have [ Mongodb project Instance ] ---> Inside [ Mongodb project Instance ] we can find list of Databases.
      mongoDb_project = client

      console.log(mongoDb_project)
  }

   %%%%%%%%%%%%%%%%%%%%%%%%%%%-----------------------------%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


})







            // ----------------------------------



        */
    }
})



const asychFunction_promise = async function () {

    try {
        const result = asyncPromise_Object;
        console.log(result)
    }
    catch (error) {
        console.log(error)
    }

}


console.log(asychFunction_promise())

















