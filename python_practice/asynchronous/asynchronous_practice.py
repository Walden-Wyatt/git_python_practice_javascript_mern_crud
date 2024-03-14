


# Here we will be practising asynchronou Programming


# Think of a Situation where we have 3 asynchronous functions 
  # function1 - takes 5 
  # function2 - takes 10
  # function3 - takes 15

  # main function - where we will wrapping all the above asynchronous functions using tasks 


import asyncio 


async def fun1():
    print("Start Function 1.....")
    await asyncio.sleep(5)
    print("End of Function 1.....")


async def fun2():
    print("Start Function 2.....")
    await asyncio.sleep(10)
    print( "End of Function 2....." )


async def fun3():
    print("Start Function 3....")
    await asyncio.sleep(15)
    print("End of Function 3....")

# Here let us have [ main() ] function
    
async def main():
    print("Main Function")

    # let us create tasks 
    task1 = asyncio.create_task(fun1())
    task2 = asyncio.create_task(fun2())
    task3 = asyncio.create_task(fun3())

    # here let us await [ task2 ] using [ await ] keyword but not for [task1 and task3 ]

    await task2



# here us create event loop
    
# asyncio.run( main() )




# Output :- 

    # Main Function
    # Start Function 1.....
    # Start Function 2.....
    # Start Function 3.... 
    # End of Function 1.....
    # End of Function 2.....


# Here if you see value from [ task3 ----> function3() ] is not getting printed because all the tasks which is inside the [ task3 ----> function3() ]  takes more than 10 seconds to execute

 # if any tasks or code which takes less than 10 seconds to execute inside [ [ task3 ----> function3() ]  ], then those tasks will executed and printed from the above code 




# -----------------------------------------------------------------------------------------------------------------------------------------------------------




# [ Practice 2 ]

# Here we will be writing the same code which we have written above with 1 modification 
 # Inside [ task3 --> function3() ] we will be writing asynchronous codes which takes less than 10 seconds to execute because the maximum time taken by [ task2 ] for which we have used [ await ] 




async def fun1():
    print("Start Function 1.....")
    await asyncio.sleep(5)
    print("End of Function 1.....")


async def fun2():
    print("Start Function 2.....")
    await asyncio.sleep(10)
    print( "End of Function 2....." )


async def fun3():
    print("Start Function 3....")


    # Here we have asychronous codes which takes less than 10 seconds to execute 
    
    await asyncio.sleep( 4 )
    print("task 3 code which took 4 seconds to Execute")

    await asyncio.sleep( 9 )
    print("task 3 code which took 9 seconds to Execute")


    await asyncio.sleep(15)
    print("End of Function 3....")

# Here let us have [ main() ] function
    
async def main():
    print("Main Function")

    # let us create tasks 
    task1 = asyncio.create_task(fun1())
    task2 = asyncio.create_task(fun2())
    task3 = asyncio.create_task(fun3())

    # here let us await [ task2 ] using [ await ] keyword but not for [task1 and task3 ]

    await task2



# here us create event loop
    
asyncio.run( main() )



# Output :-

    # Main Function
    # Start Function 1.....
    # Start Function 2.....
    # Start Function 3.... 
    # task 3 code which took 4 seconds to Execute
    # End of Function 1.....
    # End of Function 2.....


# In the above output if you see code from [task 3 ] got executed 

 # Even though [ task 3 ] overall takes 15 seconds to execute but still some of the codes got executed 
  # This is happening because [ task 3 ] has some of the codes which takes less than 10 seconds ( that is exact time taken by task2 ), because we have awaited [ task2 ] inside [ main() ] which ever tasks inside [ async functions ] code which takes less than 10 seconds all those codes will get executed. 



































