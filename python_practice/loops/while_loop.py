

# While Loop

 # While loop can be used to Iterate over Iterable objects or Sequences ( list, tuples, strings, sets, etc  )
 # While loop can be used to repeatly run a Block of code untill the Specified condition is met

 # While Loop Providing conditions can be Classfied into 3 Types
  # 1. In the While Loop Line 
  # 2. Inside the While Loop as a Base Case
  # 3. Writing conditions in a Variable then using that variable in a [ while ] condition


# Types of While Loop

 # Regular While Loop
  # this is the regular while loop where we will be providing the conditions on the while line itself, This can be used to iterate over Iteraable Objects or Sequences
  # This type of loop can be used to To Iterate over Iterable Objects or Sequences such as [ list, strings, tuples, sets, etc ]

 # Infinite While Loop
   # In this type of loop we will be writing the while codition inside the Loop ( as a Base Case ), so every when we run the loop, while loop checks the conditions which inside the loop based on it loops moves( decides weather to mover or not ) to the Next line
   # This type of loop can be used to Evaluate User Input, and keep running the While loop untill the condition is Met by providing appropriate values.
   

# Keywords :-

 # break
  # when specified condition is met this will break the Loop execution and gets out of the loop from moving further ( repeating the Loop Execution )

 # continue
  # when specified condition is met it will skip only that specific Iteration but starts executing other iterations till the overall condition is satisfied
  # when you use continue, if the condition is met the next line of code will not get executed

 # pass
  # 



# While Loop Syntax :-

# 1. Truthy or Falsy Conditions - while loop checks for Trutiness and Falsiness then starts executing the statements inside the loop
     
 # while Truthy_Falsy_value:

    # statements to be executed

    # Increment and Decrement 


# ----------------------




# 2. While Loop to check conditions using Operators 
   
   # this is also called a While loop which runs pre-defined number of time
 

 # while variable [ Operator ] value_to_check:
     # Statements to be Executed 



# ----------------------



# 3. Direct usage of True keyword or Infinite While Loop 

 # while True :

  # Base Case - which makes the Loop false, Provide Falsy condition [ Ex: Provide Input variable and check for conditions ]

  # Statements to be executed 




# Tips to Write a While Loop

 # 1 Ensure proper exit conditions

 # 2 Initialise the Variable outside the Loop
    # count = 0
    # while count < 5:
    #     print(count)
    #     count += 1


 # 3 Avoid unnessary complex conditions 
   # Example :- [ while x > 0 and y != 5 or z < 10: ]

 # 4 Use "break" and "continue" wisely










# ------------------------------------------------------------------------------------------------------------------------------------



# Problems to Solve 

 #  write while loop using Regular Approach
 #  write while loop using Trutiness and Falsiness
 #  write while loop using True keyword or Infinite while loop 
 #  use break keyword
 #  use continue keyword
 # 


 #  write while loop using Regular Approach

condition = "True"

# the below while loop becomes infinite
# while condition == "True":
#     print("Yeah it is True")

# if a while loop becomes infinite use [ ctrl + c ] to exit the loop


# let us iterate an list
    
lists = [1,2,3,4,5]

lists = [ "apple","mango", "orange", "papaya", "grapes" ]

# here when you checked for length, len() function has returned the length which is a number, because number other 0 is truthy the statement inside the  loop keept on running infinitely
# while len(lists):  
#     print( lists )


# the reason why the below loop has become infinte is because there is no base case for this which will make the condition false
# while len(lists) > 0:
#     print(lists)


# make sure to use [Base case] inside the While loop, the base case should make the condition false.
 # here this will loop checks the condition, It will run for Pre-defined number of Times
while len(lists) > 0 : # this while loop will run the code till the length value of a list
    print(lists[0]) # here it prints the 1st index of the value
    del lists[0] # For each iteration this code will remove the 1st index position value from the list. by this list length keeps decreasing.
     


while len(lists) > 0 : # this while loop will run the code till the length value of a list
    print(lists[0]) # here it prints the 1st index of the value
    del lists[0] # For each iteration this code will remove the 1st index position value from the list. by this list length keeps decreasing.
     


    


# while len(lists) > 0:
#     del lists[0]
#     print( lists[0] )

 # Error :- IndexError: list index out of range
    #  becuase here we try to access index of 0, till the list has single element the list will print the values in the index 0, but once the list is empty then when we try to print the index of 0 we might encouter the error because there is 0th index value in the last iteration of a list
      # make sure to understand the programm and write th code 


    # ===================================


        # Certainly! Let's break down the code:

        # python

        # while len(lists) > 0:
        #     del lists[0]
        #     print(lists[0])

        # Explanation:

        #     while len(lists) > 0::
        #         This line starts a while loop that continues as long as the length of the list lists is greater than 0.
        #         len(lists) returns the number of elements in the list. The loop will continue executing as long as there are elements in the list.

        #     del lists[0]:
        #         Within the loop, the statement del lists[0] deletes the element at index 0 from the list lists.
        #         This effectively removes the first element of the list in each iteration.

        #     print(lists[0]):
        #         After deleting the first element, the code attempts to print the new first element of the list using print(lists[0]).
        #         It's important to note that this line might raise an IndexError if the list is empty after the deletion. This is because attempting to access lists[0] on an empty list results in an error.

        # Overall Flow:

        # The while loop continues to execute as long as there are elements in the lists:

        #     It deletes the first element of the list (del lists[0]).
        #     It then attempts to print the new first element of the list (print(lists[0])).

        # This process repeats until the length of the list becomes 0, at which point the loop exits.
        # Potential Issue:

        # The code might raise an IndexError if the list becomes empty, as attempting to access lists[0] on an empty list is invalid. To avoid this issue, you may want to check if the list is not empty before attempting to access its elements:

        # python

        # while len(lists) > 0:
        #     del lists[0]
        #     if len(lists) > 0:
        #         print(lists[0])

        # This modification ensures that the print statement is only executed when there are still elements in the list after the deletion.


    # ======================================



# -----------------------------------------------------------------------------------------



 # 2. write while loop using Trutiness and Falsiness

# count program
    
count = 1

while count: # step 1 - here while will check for Truthy or Falsy value
    print(count) # step 2 - here while loop will print the current state value of the count, in first iteration [1]
    count += 1 # step 3 - here count value will get increated by 1
    if count > 10: # step - here the if statement will check for condition that is [ count ] is greater than 10, if this condition is true the loop gets into the if block else the loop will not get inside the [ if ] block
     break # step 5 - incase the condition is true this line of code will get executed which will break the while loop.


print("""



""")

# ------------------------------------------------------------------



 # 3.  write while loop using True keyword or Infinite while loop 


count = 10

while True: # step 1 - in this line loop checks for Trutiness and Falsiness, this condition will always be truthy if will not be falsy, to stop the while loop from running infinite times we have to provide false condition inside the while loop statements.
   # base case 
   if count <= 0: # step 2 - base case condition check, loop checks weather the count value is less than 0, if it is true then  if block statements will get executed and breaks the loop, else if block will be skipped and moves to next lines of code 
      break # step 3 - when [if] condition is fullfilled this line of code gets executed and breaks the loop execution
   
   # below we have recursive code, which keeps on executing
   count -= 1 # step 4 - when the above [if] condition fails then this line of code will get executed, this will increament the [ count ] value and the previous count variable with the new values (after incrementing)
   print( count ) # step 5 - here the count value gets printed that the is current/ new value ( value after gettting updated ).



print("""



""")

# ------------------------------------------------------------------



 # 4.  #  use break keyword

 # here we will be learning how to use [ break ] keyword


# user will pass number from 20 - 30 we have check the value and iterate , it the value goes above 30 we have to stop the loop, 

def iterateFunction():
    
   userValue = input("Enter a Number between 20 to 30 ?\n")

   userValue_casted = int(userValue)

   while userValue: # this will check for Truthiness, once if it is true then the code will move while block and executes the statements

     if userValue_casted < 30 and userValue_casted > 20: # this line will check for the condtion that is the values entered must be lesser than 30 and greater than 20, if the condition is true then the program enters inside this block.
        if userValue_casted <= 30:  # in this line the program checks for the condition that is [userValue_casted ] must be lesser than or equal to 30, if it is the program will enter inside the if block else the if block will be skipped and moved to next line of code
            userValue_casted += 1 # once the value is lesser than 30 here in this line the program will increment the [ userValue_casted ] by for each iterations ( that is till the program reaches the number 30 )
            print( userValue_casted ) # here the current/new values (i.e, value after increment) will get printed.
        

     else: # this line will execute if [ if userValue_casted < 30 and userValue_casted > 20:  ] this condition is failed
      print("Enter value between 20 to 30") # this will print the value
      break # Here we used break keyword, this break keyword will make the program to print the value only once then breaks the while loop execution.
        



print("""



""")

# ------------------------------------------------------------------



 # 5.  #  use continue keyword

   # Continue will skip specific Iteration and moves to next lines of Code. if the condition is met that specific iteration will be skipped and moves to next iterations.

# from the list of values remove number characters and display


count = 0

while count < 5:
   count += 1

   if count == 3:  # in this line program will check for the value 3, if it is present then 3 will be skipped and moved to other lines of code
      continue 
   print( count )


































