


# Asynchronous Appraoch 


 # Here we will be learning about Asynchronous Appraoch, how to write asynchronous codes and how will it get Executed behind the scenes. 

  # Asychronous Code is nothing but a Function, where we will preceed [ async ] keyword before the Function and use [ await ] keyword inside the function


async def asyncFunction():
    print("Hello, Asynchronous Function")


# asyncFunction()

# Error :- 
    # C:\Users\user\Desktop\python_practice\asynchronous\asynchronous.py:16: RuntimeWarning: coroutine 'asyncFunction' was never awaited
    #   asyncFunction()
    # RuntimeWarning: Enable tracemalloc to get the object allocation traceback


# when we do not use [ await ] keyword inside the Function we will get this error 




# ---------------------------
    


# Using [ await ] keyword 

async def asyncFunction():
    print("Hello, Asynchronous Function")
    # await print("await for some times")

# print( type(asyncFunction()) )
    


# Output :-

# C:\Users\user\Desktop\python_practice\asynchronous\asynchronous.py:35: RuntimeWarning: coroutine 'asyncFunction' was never awaited
#   print( type(asyncFunction()) )
# RuntimeWarning: Enable tracemalloc to get the object allocation traceback


# <class 'coroutine'>

 # Here we can clearly see that the function returns a coroutine Object


 # What is Coroutine ?

   # Coroutine is an Object in python, when we use [ async ] keyword before any Functions there will be "Coroutine" gets object created




# ---------------------------


import asyncio 

# how to use [ await ] keyword 

 # What happens when we use [await] keyword Outside the function, that is in the Top level of the file.

 # To execute coroutine we have to await keyword


async def awaitFunction():
    print("Abc")
   

# to execute the below function we have to use [await] keyword
    
# await awaitFunction() 

# Error :- 
#  SyntaxError: 'await' outside function , "await" allowed only within async function
# but when we use [ await ] keyword outside the [ asnc function ] we will get the above error





# ------------------------------------




# what happens when we use [ await ] keyword inside the Regular functions ?

def regularFunction():
    print("Hello")
    # await print("hello")

# Error:- "await" allowed only within async function  ,  SyntaxError: 'await' outside async function
    # We get above Error when we use [ await ] keyword inside the Regular Function which we are not allowed to do
     # which means [ await ] keyword can only be used inside the Function which has [ async ] keyword preceeded ( async functions )





# ------------------------------------
    

# Here we have proper syntax for Asynchrous functions

async def async_function():
    print("Hello Async Function")
    await print("Stop the execution of this Function")
    print("End the Execution")

# when we access this function by directly calling it we will encounter the below error:-
     # Error :- RuntimeWarning: Enable tracemalloc to get the object allocation traceback
# async_function()
    
    # we are not allowed to access the Asynchronous functions directly by calling it instead we have 2 Approachs to access 
     # 1. using [Event Loops]
     # 2. Using [ tasks ]
    



# ------------------------------------
    


# What is Event loops how to use it  ?
    
    # Event loop helps us to write Asynchronous codes, it mainly used in accessing the Asychronous functions which has [ async and await ] keywords

# import [ asyncio ]
    
import asyncio

 # by using [ asyncio.run( corountine ) ] we can create an Event loop and execute the Program 

async def asyncFunction():
    print("Hello")
    print( "Here we have awaited" )
    print( "End......" )


# asyncio.run( asyncFunction() ) 
 # [ asyncio.run( asyncFunction() )  ]
  # here for [ asyncio.run() ] we have to pass coroutine ( functions which have async keyword )
  # when passing the arguement we have to invoke the function



# Output :-

# Hello
# Here we have awaited
# End......


# Here you can see that now we have executed the program


# ----------------------------------------------------------


# Now  let us use [ await ] keyword 

async def asyncFunction_await():
    print("Hello await")
    await asyncio.sleep(5)
    print("Waited and printed the values")

# asyncio.run( asyncFunction_await() )


# print("Line of code outside the Function")

# print("2nd Line of code outside the Function")
    


# when you execute the above program untill the [await] line of code gets executed and finishes the next lines of code does int get executed, 
  # weather the lines of code comes inside the Funcition scope or outside in the global scope, next lines of code does not get executed.



# ----------------------------------------------------------


# Tasks 

 # Tasks will not pause the Code when the line has function has [ await ] keyword
 # when it finds synchronous code [ await ] keyword, those codes will be sent to event queues where async functions will start performing those operations inside the Event queues
  # as soon as event queues finishs the execution of [ await ] keyword, program control flow will come to the [ await ] line then executes the code finally prints the values


import asyncio

async def asyncFunction_task():
    print("Async function Tasks ")

    # Error :- RuntimeWarning: Enable tracemalloc to get the object allocation traceback 
     # when we try to call aynch functions fron inside the [ regular function or Async function ] we have use [ awiat ] keyword before its invocation 
    # await asyncFunction_awaitkeyword()

    tasks = asyncio.create_task( asyncFunction_awaitkeyword() )
    print("Next lines of code")

async def asyncFunction_awaitkeyword():
    print("Await function statements")
    await asyncio.sleep(1)

# asyncio.run( asyncFunction_task() )


# Output :-

    # Async function Tasks 
    # Next lines of code       
    # Await function statements

 # here why is that [  # Next lines of code   ] got printed before [ # Await function statements ] that is because of Asynchronous Operations using tasks ( aasyncio.create_task( coroutineFunction() ))



# Here we can see that order of execution 
 # The correct order of execution must be as below 

# Output :- This is how the execution must have happened from [ Synchronous point of view ], but if you see the above Output it is complelely different

   # "Async function Tasks "
   # "Await function statements"
   # "Next lines of code"




# ---------------------------------------------------------------------------------



# How to access return value from a Async Functions
  # Future
    
# To create and Execute the Async Functions we have to use [ asyncio.run(coroutine )]
     # the arguement for [  asyncio.run(coroutine ) ] must be an entry point coroutine that is which has all other coroutines wrapped inside a Single Coroutine called [ main() ] ( it need not be "main" it can have any other name )











# ---------------------------------------------------------------------------------


# Line of code tracking between code written inside the Async Functions as well as code written outside the Functions



async def coroutine1():
    print("Start")
    # error :- RuntimeWarning: coroutine 'sleep' was never awaited asyncio.sleep(4)
     # whenever we use async codes such as [ asyncio.sleep(), etc ] we have await it, else we will get the above error
    await asyncio.create_task(  asyncio.sleep(4) )
    print("End coroutine 1")

print("Hello")

# Output :-
    # Hello
    # Start
    # End coroutine 1

# When you clearly see the execution order we can observe that the code which is outside the async function (synchronous codes) gets executed first then it moves to the codes which is present inside the [ Asynchronous function ] gets executed 
 # From here we can clearly learn that the order of execution will be as below 
  # 1 - First all the Synchronous Codes which are present inside the File gets executed 
  # 2 - [ Asynchronous code execution ] Once all the Synchronous Codes which are present inside the got execution then python interpreter will start executing the [ Asynchronous codes ]


# asyncio.run( coroutine1() )


print("""


""")



# --------------------------------------------------------------------------------------------------------------------------------------------------



# How to create  Multiple Tasks inside the [ main() ] coroutine 



async def task1():
    print("Task 1 Function")
    # await print("Wait to execute this program")
    # Error :- TypeError: object NoneType can't be used in 'await' expression
      # for every await keyword which we use there should be Asynchronous code written which has async and await keyword
    
    await asyncio.sleep(10)
    print("End task 1")
    


print("some sync code")

async def task2():
    print("Task 2 Function")
    await asyncio.sleep(5)
    print("End task 2")


# asyncio.run( task1(), task2() )
# Error :- TypeError: run() takes 1 positional argument but 2 were given
 # we are not allowed to pass more than 1 coroutine functions for [ asyncio.run() ] method, if we pass we will get above error.
    



async def main():

    # task1 = asyncio.create_task( task1() )
    # task2 = asyncio.create_task( task2() )

    # Error :- 
        #  task1 = asyncio.create_task( task1() )
        #                               ^^^^^
        #  UnboundLocalError: cannot access local variable 'task1' where it is not associated with a value   
    
         # we are not allowed to use any custom [ functions, variables, clases  ] inside  [ asyncio.create_task( ) ]
    print("hello")

    task1 = asyncio.create_task( task1() )





# asyncio.run( main() )
# Error :- ValueError: a coroutine was expected, got None
 # when we pass [ Regular function ] as an argument for [ asyncio.run() ] method we will get the above error.

# asyncio.run( main() )
    
    # Above code is error code 


print("""


""")





# ----------------------------------------------------------------------------



async def fetch_data():
    print("Start Fetching")
    await asyncio.sleep(2)
    print("Done Fetching")


print("Before print_numbers ")

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def finalfunction():
    print("final functions")
    await asyncio.sleep(0)
    print("next line of code")


async def main():

    # here we have Created taks that is [ task1 and task2 ]
      # now [ task1 and task2 ] have Asynchronous functions, if we want to access the asynchronous functions value we have await, so that once the Function finishes its process it will get executed.
    task1 = asyncio.create_task( fetch_data() )
    task2 = asyncio.create_task( print_numbers() )
    task3 = asyncio.create_task( finalfunction() )
    # Here we have to use await for [ task1 ] just because it has asynchronous function values

    # What happens when we do not use [ await ] keyword before the tasks ?
     # If you do not use [ await before the tasks ] those Asynchronous functions will not get finished completely, it means it program will not read every lines of code which is present inside the async function 
      # once if the [ create_task() ] method finds first occurance of [ await ] keyword inside the Asynchronous functions,  the code which comes next to the [ await ] line inside the asynchronous functions will not read and printed by the [ create_task() ] method.
       # Only those lines of codes which comes before the First occurance of [ await ] keyword inside the asynchronous functions will be read and printed by the [ create_task() ] method
    
     # When all the lines of code is not read which means Asynchronous functions are not completed fully, it is completed or read only half of the statements from the Asychronous functions functions 
       # To resolve this we have to use [ await ] keyword before all the Tasks  which we create inside the [main()] function.
    
    # Output without using [ await ] keywords before the tasks which we have creatd :-

        # Before print_numbers
        # Start Fetching
        # 0
        # final functions
    

    # ------------------------

    await task1
    await task2
    await task3

    # Output after using [ await ] keywords before the tasks which we have created :

    
# Before print_numbers
# Start Fetching
# 0
# final functions
# next line of code
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# Done Fetching
# 8
# 9

# ---------------------------------------------------
    

# Here we have event loop for [ main() ]
# asyncio.run( main() ) 


print("""


""")





# -----------------------------------------------------------------------------------------------------------------------------------------------------


# Think suppose we have 3 asynchronous functions and main asynchronous function

async def function1():
    print("function1 starting...")
    await asyncio.sleep(10)
    print("End of FUNCTION ONE")


async def function2():
    print("function2 starting...")
    await asyncio.sleep(5)
    print( "End of FUNCTION TWO")


async def function3():
    print("function3 starting...")
    await asyncio.sleep(2)
    print("End of FUNCTION THREE")


async def main2():

    # here let us create tasks for the above functions 
    task1 = asyncio.create_task( function1() )
    task2 = asyncio.create_task( function2() )
    task3 = asyncio.create_task( function3() )

    # Output :- 
      # Before awaiting for tasks using [ await ] keyword

        # function1 starting...
        # function2 starting...
        # function3 starting...
    
    # Here we can see that the code which comes next to asynchronous functions ( that is after the line which has "await" keyword ) does not executed, This has happened for all the functions 
    # Thats because all the fuction got resolved immediately without waiting for other lines 

    # If you want to print entire codes which comes inside the each asynchronous functions we have to use await functions using [ await ] keyword 

    # --------------------

    # What suppose if the [ Tasks function ] which we awaited using [ await ] keyword takes more time to execute when compare to Other 2 functions ?  

      # In this situation Those Tasks Functions which took lesser time than the awaited Task fuction which took more time will the executed completely
        # All the statements which are present inside the [ Task functions ] which took lesser time will get executed
         # In this situation overall program execution time is not millisecond ( to execute immediately ) it the time which the [ Task function which takes more time ]
         # Because there are more time to perform operations , the other task function with lesser time to execute will also be executed
    

# --------

# Here we have awaited only [ task1 ]
    await task1

    # Output :
     # here we have awaited only [ task1 ] using [ await ] keyword :-
            
        # function1 starting...
        # function2 starting...
        # function3 starting...
        # End of FUNCTION THREE
        # End of FUNCTION TWO
        # End of FUNCTION ONE
                    

            
            # ----------
    
    # Check the Above Output 
    # here we have awaited only [ task1 ] using [ await ] keyword 

    # Here if you see all the statements from [ task2 and task3 ] task functions got executed even if we did not awaited for [ task2 and task3 ] using "await" keyword
      # This has happened because time taken for [ task1 ] to completely execute is higher than [ task2 and task3 ], that is reason [ task2 and task3 ] entire statements inside the function got executed 
    
    # Even if the [ task2 and task3 ] is not awaited the Execution of the [ task1, task2 and task3] functions are concurrant and parallel ?
      # which means which code inside each functions completes the execution, python interpreter will switch to that specific async function executes and prints the values then moves to Next function which got executed, This process will keep on continuing untill the overall asynchronous functions are executed 

       # What is time taken for the all the [ tasks ] to be executed when it is given inside the [ main() ] function ?
        # The Overall time taken for  [ main() ] function to completely finish its execution will depend on which Asychronous function has the highest time to execute 
         # The one single asynchronous function out of all the asynchronous functions which Takes the highest time will the time for overall time for [main()] function to completely finish its execution. 
    


# ----
    
     # Analysing the Output 
    
    # Output :
     # here we have awaited only [ task1 ] using [ await ] keyword :-
            
        # function1 starting...
        # function2 starting...
        # function3 starting...
        # End of FUNCTION THREE
        # End of FUNCTION TWO
        # End of FUNCTION ONE
    
    # 1ST 
    # Initially all the codes from all the functions which comes before the [ await ] keyword got executed 
      
        # function1 starting...
        # function2 starting...
        # function3 starting...
    

    # 2nd
     # next which ever lines of code which takes less time to resolve will get executed [ that is 2 seconds ]
        # * here i mentioned lines of code not the overall function ( which means all the functions are still in the process of execution which has not finished completely )
        # its because [ function3() ] line of code got executed next those line got printed 
         # if no lines of code comes after this executed lines which means the overall lines of function got resolved so the Function has got completed,
          # This function will come out of Event Loop 
     
        # End of FUNCTION THREE
    
    
    # 3rd 
      # next its line from [ function2() ] which got resolved, that is [ 5 seconds ]
       # if no lines comes next to this line which means the function got completely finished 
    
        # End of FUNCTION TWO
    
    # 4th
      # Finally it is [ function1() ] which took the highest time to execute, that is [ 10 seconds ]
    
        # End of FUNCTION ONE
    

   # Overall Time taken for [ main() ] function to execute is [ 10 seconds ]

    

# ------------------------



# here we have event loop which creates and executes Asynchronous functions
    
asyncio.run( main2() )























