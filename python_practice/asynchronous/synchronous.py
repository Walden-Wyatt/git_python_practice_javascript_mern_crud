

# Synchronous 

# what is Synchronous ?
 # When python interpreter executes the code line by line then it called as asynchronous
 # Synchronous Approach of writing codes takes longer time to execute and finish the program 
 # Sequential Execution of Python codes in a file is called as Synchronous Approach of writing Codes 
   # In Python by default, the code will be executed synchronously ( Line by line ) untill the previous line of codes gets executed Python interpreter will not move to the Next line of code for execution

  



# Asynchronous 
 # when python executes the code simultaneously then it is called asynchronous
 # Because Asynchronous Approach  runs the code ( functions ) simultaneously this way of writing codes takes shorter time to execute and finish the program 



 # Every CPU can perform One Task at a Time, CPU cannot perform multiple tasks at the same time, if you want to perform multiple tasks at the same time we have to use Asynchronous operations(codes which are associated with asynchronous operations )






# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Synchronous Approach of writing codes 



print("Hello, I am Synchronous approach")



def synchronousFunction():
    print('Synchronous functions')

synchronousFunction()



for i in range(20):
    print(i)



print("Hello Conditional statements")



if True:
    print("True conditional statements")

else:
    print("False conditional statements")




print("Hello Exceptional handling statements")




try:
    print("Some Error Codes")

except Exception as e:
    print(e)

else:
    print("Everything is right")
finally:
    print("Finally block")




# Output :-
        
    # PS C:\Users\user\Desktop\python_practice\asynchronous> py synchronous.py
    # Hello, I am Synchronous approach
    # Synchronous functions
    # 0 
    # 1 
    # 2 
    # 3 
    # 4 
    # 5 
    # 6 
    # 7 
    # 8 
    # 9 
    # 10
    # 11
    # 12
    # 13
    # 14
    # 15
    # 16
    # 17
    # 18
    # 19
    # Hello Conditional statements
    # True conditional statements
    # Hello Exceptional handling statements
    # Some Error Codes
    # Everything is right
    # Finally block
    # PS C:\Users\user\Desktop\python_practice\asynchronous> 



# Here if you see the above Output we can clearly Observe that the Code has been executed Line  by Line in a Sequence
    
    # Execution breakdown :

    # There are 8 programs which has to be executed in from the above lines of code 


# ------------------


    # 1 First Execution  :- 
    
    # print("Hello, I am Synchronous approach")

      # Output :- # Hello, I am Synchronous approach
    

# ------------------



    # 2nd Execution :- 

      # Code :-
            
        # def synchronousFunction():
        #     print('Synchronous functions')
        # synchronousFunction()
    

       # Output :-  # Synchronous functions


# ------------------


    # 3rd Execution :- 

       # Code :-

        # for i in range(20):
        #     print(i)
    
       # Output :-
            
            # 0 
            # 1 
            # 2 
            # 3 
            # 4 
            # 5 
            # 6 
            # 7 
            # 8 
            # 9 
            # 10
            # 11
            # 12
            # 13
            # 14
            # 15
            # 16
            # 17
            # 18
            # 19


# ------------------
    
      # 4th 
    
       # Code :-
         
        # print("Hello Conditional statements")
    
       # Output :-
     
        # Hello Conditional statements



# ------------------
    
     # 5th 
            
        # if True:
        #     print("True conditional statements")

        # else:
        #     print("False conditional statements")
    
       # Output :-
    
        # True conditional statements



# ------------------
    
    # 6th 

     # code :-
    
        # print("Hello Exceptional handling statements")
    
     # Output :-
    
        # Hello Exceptional handling statements





# ------------------
    
    # 7th 

     # Code :- 
    
        # try:
        #     print("Some Error Codes")
        # except Exception as e:
        #     print(e)
        # else:
        #     print("Everything is right")
        # finally:
        #     print("Finally block")
    

     # Output :-
            
        # Some Error Codes
        # Everything is right
        # Finally block




# ------------------
    
    # Above we have explained the Execution order, on how lines of code executed in Synchronous Approach 
    # from above examples we can clearly see that the Lines of Code Executed in a Sequential Order ( Line by line)



# ------------------













