

# Threading 

# Here we will be learning on what is tread and how to work with Threadings 



# Threads are nothing but Programs which has to be Executed by CPU [ Central Processing Unit ]

 # Based on Number of Cores and Clock speed computers Computational Speed and Computational limit ( number of tasks a CPU can handle ) CPU's Performance will be Determined

 # Core - Core is the Place where we execute out Programs 
    # Programs are files and folders which holds Pieces of Codes written in any Language 
    # Inside this code will be Executing all Codes which we write in python programming language 
    # Python Interpreter and Compiler will convert the Python (High level ) code to Machine level ( 0s and 1s ) or binray codes using this thing called [ core ]
   # Based on Number of Cores which the CPU has , Number of Tasks performed simultaneously will be calculated 
    # If the CPU has More Number of Cores which means CPU can handle More number of tasks simultaneously, if less number of cores then Less number of tasks will be handled


 # Clock Speed 
  # Clock Speed will determine how fast can the Program gets executed 
  # Program gets executed means how fast the CPU coverts the High (Human) readable code to Lower Level code ( Machine Level code  or Binary code or Byte code )
  # Based on the Clock Speed the execution time for Program will be determined
  # High clock speed will execute the Code faster, Low clock speed will execute the Code Slower


# Threads 

 # Thread are nothing but the Code which we write and Load the code inside the CPU Core to be executed
 # Threads in Python means [ Code which is present inside the File ] and [ Code which we write inside the Function, where those function will be assigned to the thread  ] , Where the codes inside the Threads will be assigned to any of the Core and Finally Executes 

 


# ----------------------------------------------------------------------------------------------------------------------------------------------------------


import threading

import time


# When we imoprt [ threading ] inside any file by default python will create 1 thread which is the [ Main ] thread
  # This  [ Main ] thread is responsible for the Codes which are at the Top level of the Files, what are code which write will be handled by [ default Main ] thread 
print( threading.activeCount() ) 
# Ouput :- 1




# This is the Function where we will be assigning it to  a Thread
def threadingFunction():
    print("Function Starts........")
    time.sleep(2)
    print( "Function Ends........" )


# Here we can see that [ threading ] has a nested class called [ Thread ]
firstThread = threading.Thread(target=threadingFunction, args=() )

print( firstThread )
# Output :- <Thread(Thread-1 (threadingFunction), initial)>
 # [ threading.Thread() ] Class will return a nested "Thread" object through which we can access other methods and properties


# To actuall create and run the Newly created thread We have to use [ start() ] method from instance of [ threading.Thread()  ] class

# [ CODE ]
# firstThread.start()
 # when we execute the above funtion, it takes 2 second to execute the codes which comes after [ time.sleep() ] method which is inside [ threadingFunction() ]


print( threading.active_count() )
# Output :- 2


print("""



""")


# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# Threading is some what similar to [ Asynchronous programming ]

# [ Practice 2 ]


import threading
import time


# create a new function 

def functionThread():
    print("Start Function.......")
    time.sleep(2)
    print("End Function......")


# create a Thread 
newThread = threading.Thread( target=functionThread, args=() )

# Syntax breakdown :-
# threading.Thread( target=functionThread, args=() )
 # this is the class which is used to create Thread
 # this class accepts 2 arguements 
  #  target=functionThread - 1st argument must be a Function for which Tread has to be created, here function must not be Invoked we have to pass the Function reference or defination
  # args=() - 2nd argument must be a Tuple inside which we have to pass Arguements for the Function, based on number parameters (positional, **args and **kwargs) we have to pass the values



# start the Thread 
# newThread.start()


# Output :- 

   # Start Function.......
   # End Function......




print("""



""")




# ---------------------------------------------------------------------------------------------------------------------------------------


# Steps in creating a New Thread :-


# 1. Import [ threading ] class 

# 2. Import [ time ] class
# 3. create a Custom Function with any number of paramters including [ *args and **kwargs ]
   # Thread can be created only by using Functions ( Regular or Lambda functions )
   # make sure to use [ time.sleep() ] to simulate Delay in Execution of function lines.

# 4. Create a new Thread and assign it to an instance variable  using 
    # [ instanceObject_thread =  threading.Thread( target=functionName, args=( function_arguement_values ) ) ]

# 5. Start the thread using the [ start() ] which is present inisde the instance of [ threading.Thread() ] class
    # [ instanceObject_thread.start() ]

# 6. Now python behind the scene will create a Thread and Execute the lines of code which is inside the thread function 





# -----------------------------------------------------------------------



import threading
import time


# create a new function
def functionThreading(params1, params2):
    print("Start Threading ..........")
    print( params1, params2 )
    time.sleep(4)
    print( "End Threading...........")


# create a Thread
newFunctionThreading = threading.Thread(target=functionThreading, args=("arguement 1", "arguement 2"))

# start the Thread
# newFunctionThreading.start()


# Output :-

   # Start Threading ..........
   # arguement 1 arguement 2
   # End Function......
   # End Threading...........





print("""



""")




# --------------------------------------------------------------------------------------------------------------------------------------------------


# How to create a Multiple Threads and check the Execution Order 




import threading
import time

def multipleThread_1():
    print("Multiple Threads Starts.........")
    time.sleep(2)
    print("Multiple Threads - Ends..........")


def multipleThread_2():
    print("Multiple Threads 2 Starts.........")
    time.sleep(3)
    print("Multiple Threads 2 - Ends..........")


def multipleThread_3():
    print("Multiple Threads 3 Starts.........")
    time.sleep(1)
    print("Multiple Threads 3 - Ends..........")


   

# Expected Output :
   # "Multiple Threads Starts........."
   # "Multiple Threads 2 Starts........."
   # "Multiple Threads 3 Starts........."
   # "Multiple Threads 3 - Ends.........."
   # "Multiple Threads - Ends.........."
   # "Multiple Threads 2 - Ends.........."


# Let us create a Thread 
   

threadMultiple_1 = threading.Thread(target=multipleThread_1, args=() )
threadMultiple_2 = threading.Thread(target=multipleThread_2, args=() )
threadMultiple_3 = threading.Thread(target=multipleThread_3, args=() )


# let us start all the threads so that it actually creates and runs the code inside the [Tread functions ]

# threadMultiple_1.start()
# threadMultiple_2.start()
# threadMultiple_3.start()


# Actual Output :-


   # Multiple Threads Starts.........
   # Multiple Threads 2 Starts.........
   # Multiple Threads 3 Starts.........
   # Multiple Threads 3 - Ends..........
   # Multiple Threads - Ends..........
   # Multiple Threads 2 - Ends..........


# Both Actual and Expected output are same which means we learned Treading concepts






# --------------------------------------------------------------------------------------------------------------------------------------------------


# How to create Multiple Threads using [for] loop

 # Here to create multiple threads using a single fucntion, the values for sleep time will be taken from the arguements


import threading 
import time 


def loopThreads(num):
    print(f"Single --- Start Thread ........")
    time.sleep( num )
    print( f"Single --- End Thread ......." )


# let us create a for loop which will create 3 threads 
    

# instanceThread = threading.Thread( target = loopThreads, args=(2) )
# Error :- TypeError: __main__.loopThreads() argument after * must be an iterable, not float
 # we get this error because we have used [ args(2) ] as a 2nd parameter for [ threading.Thread() ]
  # if we use [ args(2) ] which means that python will implicitly treat it as a grouping operator and evalutes the expression and returns a [int] datatype values, this will not be treated as a Tuple datatype
  # if we want to treat [ args(2) ] as a Tuple make sure to use comma after tuple values [ args(2,)]
    
for i in range(3):
   instanceThread = threading.Thread( target = loopThreads, args=(2,) )
   # instanceThread.start()


# Output :-
   
   # Single --- Start Thread ........
   # Single --- Start Thread ........
   # Single --- Start Thread ........
   # Single --- End Thread .......
   # Single --- End Thread .......
   # Single --- End Thread .......


# --------------------------------------------------------------------------------------------------------------------------------------------------
   

   # Threads are almost similar to Asynchronous Programming,
    # Threads do same thing what the Asynchronous programming does
   

# Threads will keep on watching lines of codes inside the Main Thread and well as treads which are created inside the Custom Threads which we created manually 
   # Which ever lines of code gets executed first those Values will be printed First --> Then based on the number time taken by other lines of code, code gets printed accordingly, The line of code which takes less time gets printed first then the code which takes more time.


# What happens When 2 or more Executes the code in the same Time ?
    # In this situation based on order or Sequence of code ( Top - Bottom ), The code gets executed, whichever code which we wrote at the top will get executed first, than the code which we wrote next 
     # based on sequence of occurance of of Threads, the threads get executed.
     # based on order or Sequence of [ start() ] method which we passed the threads will get executed




print("""



""")


# --------------------------------------------------------------------------------------------------------------------------------------------------
   


# Thread Synchronization 
   # [ threadInstance.join()  ]
 # if you want to run the thread in a Sequential order based on the Order in which it is created in such situations we can use Thread Sequential using [ join() ] method
   


import threading
import time


def sequence_1():
    print("sequence_1 Start......")
    time.sleep(10)
    print("sequence_1 End......")


instance_sequence_1 = threading.Thread(target=sequence_1, args=() )
instance_sequence_1.start()

# Here we have used [join()] method for [instance_sequence_1] Thread
# This [join()] method will pause the program until the current Thread finishes its Execution, Once the current Thread fininshes the execution the program will be moved in next Aviablable thread in the file
 # wherever and for whatever Threads which we use [join()] progrm gets paused untill the current thread finishes its execution

# The Order of Using [join() ] method is Important 
 # Join() method for Thread has to be used before the occurance of next thread function 

 # here if you see we used [ instance_sequence_1.join() ] before the next function [ sequence_2() ] which is used to create the next Thread
  # This is how [join()] method has to be used.
instance_sequence_1.join()


def sequence_2():
    print("sequence_2 Start......")
    time.sleep(5)
    print("sequence_2 End......")
 


# instance_sequence_1 = threading.Thread(target=sequence_1, args=() )
instance_sequence_2 = threading.Thread(target=sequence_2, args=() )

# instance_sequence_1.start()
instance_sequence_2.start()


instance_sequence_2.join()



# Order before using [ join() ] method

#  Output :-

   # sequence_1 Start......
   # sequence_2 Start......
   # sequence_2 End......
   # sequence_1 End......



# Order after using [ join() ] method

   # sequence_1 Start......
   # sequence_1 End......
   # sequence_2 Start......
   # sequence_2 End......














