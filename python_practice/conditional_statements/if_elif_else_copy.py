

# Conditional Statements 

# Here we will be learning about conditional statements in python

 # [ if....elif....else ] block can be used to Conditionally render the Values or list of Statements.

# if Block

# elif Block 

# else Block 


# ----------------------

# Syntax 

# if condition :

   # Statements or lines of code to be executed

# elif condition :
  
   # Statements or lines of code to be executed

# elif condition :
  
   # Statements or lines of code to be executed

# else :

   # Statement or lines of code to be executed

# ---------------------



# -------------------------------------------------------------------------------------------------------------------------------------------------------


# ask for the day with the user print some message


# day = input("Type a Day :- \n")


# if day == "monday" | "Monday":
    # Error :- TypeError: unsupported operand type(s) for |: 'str' and 'str'
     # this error occurs because we have used a Wrong Syntax, we are not allowed to use this syntax
    

# if day == ( "monday" | "Monday" ):

#      # Error :- 
#         #   if day == ( "monday" | "Monday" ):
#         #             ~~~~~~~~~^~~~~~~~~~
#         #     TypeError: unsupported operand type(s) for |: 'str' and 'str'
#     # even this is a Wrong syntax
#     print("Hello, Monday !")


# **** Important - do not use [ | ] thinking it is or, it is actaully bitwise or in python, this type of or will work with javascript
 # in python OR means this syntax [ or ]

# ----------------------------

# Sunday - monday programm



# while Loop 
 # There are 2 places where we can make the While condition false 
  # 1. in the Line where [ while ] keyword comes
      # this is regular approach

  # 2. Inside the [ while ] loop 
      # this approach can be used if you want to use [ break ] statement inside the [while] loop.
      # this can also be used as an Alternative for Recursive functions.


def days():

  while True:

    day = input("Enter a Day : \n") # Here this is the Base case, if this value becomes True by satisfing any of below cases then this loop gets terminated, else this loop will keep running.
            
            # [ break ] - here break means condition will become false and program gets terminated.
    
    # here below we have recuressive cases.
    if day == "monday" or day == "Monday":
            print("Monday")
            break

    elif day == "tuesday" or day == "Tuesday":
            print("Tuesday")
            break

    elif day == "wednesday" or  day == "Wednesday":
            print("wednesday")
            break
        
    elif day == "thursday" or  day == "Thursday":
            print("Thursday")
            break
        
    elif day == "friday" or day == "Friday":
            print("Friday")
            break
        
    elif day == "saturday" or  day == "Saturday":
            print("Saturday")
            break
        
    elif day == "sunday" or day == "Sunday":
            print("Sunday")
            break
        
    else:
            print("This day cannot be found enter other day")



# --------------------------------------


# Problem 1: Grade Classification

def gradeClassification():

        student_grade = input("Enter the Percentage to get to know the grade ? \n")
        student_grade_casted = int(student_grade)
        your_grade = "Your grade is : "

        if student_grade_casted >= 90:
         print( f"{your_grade} A" )
        elif student_grade_casted >= 80 and student_grade_casted < 90 :
         print( f"{your_grade} B" )
        elif student_grade_casted >= 70 and student_grade_casted < 80 :
         print(f"{your_grade} C")
        elif student_grade_casted >= 60 and student_grade_casted < 70 :
         print( f"{your_grade} D")
        else:
         print(f"{your_grade} F")




# --------------------------------------


# Problem 2: Even or Odd

# Write a Python program that takes an integer as input and prints whether it is even or odd.

def oddEven():
 try :
        odd_even = input("Enter a Number to check weathet it is Odd or Even ? \n")

        odd_even_cast = int( odd_even )

        condition = odd_even_cast % 2

        if condition == 0:
         print("the number entered is an Even Number")
        elif condition == 1:
         print("This number entered is an Odd Number")
        else :
         print("this is not a Number")

 except:
     print("Please enter a Valid Number")
    



# -------------------------------------------------


# Problem 4: Temperature Converter

# Write a Python program that converts a given temperature in Celsius to Fahrenheit. The formula is: F = (C * 9/5) + 32


def temperature():

 while True:

  try:
        temperature = input("Enter the Temparature ? \n") # here input will wait it will not allow to loop to execute till the user enters the value
         # without the above code, every time while loop will check, since the while codition is True and there is not not statement which can stop the while loop by using break it keeps on executing infinite times.
        
        temperature_casting = float(temperature)

        if temperature_casting >= 1 and temperature_casting <= 100:
         temperature_value = ( temperature_casting * 9/5 ) + 32
         print( temperature_value )
         break
        else:
         print("Please enter range between 1 to 100")
         
  except:
    print("Please enter a Valid Number")





# ------------------------------------------------
    



# Problem 5: Largest of Three Numbers

# Write a Python program that takes three numbers as input and prints the largest among them.


def largestNumber():
 while True:
  try :
 
    
        number_1 = input("Enter the First Number \n")
        number_1_casted = int(number_1)

        number_2 = input("Enter the Second Number \n")
        number_2_casted = int(number_2)

        number_3 = input("Enter the Third Number \n")
        number_3_casted = int(number_3)

        
        if number_1_casted > number_2_casted and number_1_casted > number_3_casted:
         print(f"{ number_1_casted } is Greater than {number_2_casted} and {number_3_casted}")
         break
        elif number_2_casted > number_1_casted and number_2_casted > number_3_casted:
         print(f"{number_2_casted} is Greater than {number_1_casted} and {number_3_casted}")
         break
        elif number_3_casted > number_1_casted and number_3_casted > number_2_casted:
         print(f"{ number_3_casted } is greater than {number_1_casted} and {number_2_casted}")
         break
        

  except:
    print("Please enter Valid Number character")
    continue
    



# ----------------------------------------


# Problem 6: Quadratic Equation Solver

# Write a Python program that takes coefficients (a, b, c) of a quadratic equation (ax^2 + bx + c = 0) as input and prints the solutions.


    



# ----------------------------------------


# Problem 7: Vowel or Consonant

# Write a Python program that takes a single character as input and prints whether it is a vowel or a consonant.


# while True:

def vowelCheck(): 
 while True:   
        
        alphabet = input("Enter an Alphabet \n")

        if len(alphabet) == 1 and alphabet.isalpha():
                # [ string.isalpha() ] - this method can be used if you want to check for Alphabet character and remove other characters such as Number and Symbols.
                # [ string.isdigit() ] - is used to check for digit character
                if alphabet in ["a", "e", "i", "o", "u"]:
                # the value which has been passed in the terminal, if any of the value is matched with the value which is present inside the List the the return value will be a Truthy or True
                # if you want to check for multiple values in a single if condition line you can use [Membership operator ] [ in ]
                
                 print("This is a Vowel")
                #     continue
                
                else:
                 print("This is a consonent")
                break
                
        else:
         print("Please enter a Single character as well as Alphabet character")



# ----------------------------------------------------
   



# Problem 8: Time of the Day

# Write a Python program that takes the current hour as input and prints "Good Morning," "Good Afternoon," or "Good Evening" based on the time.



def time_day():

 while True: 

  time = input("Enter a Valid Number between 0 - 12 \n") # Base Case

  # Below we have recursive case

  if time.isdigit() and time in str( [n for n in range(13)] ):

        # Here we use Nested While loop, understand and the Base case and Recurssive case and use the Nested while loop appropriately
        while True:
         pm_or_am = input("Enter weather it is AM or PM") # Base Case 

         # Below we have Recurssive case. 
         if pm_or_am.isalpha() and pm_or_am.casefold() == "am":
          print("Good Morning")
          break
         elif pm_or_am.isalpha() and time in str([n for n in range(1, 3)]) and pm_or_am.casefold() == "pm":
          print("Good Afternoon")
          break
         elif pm_or_am.isalpha() and time in str([n for n in range(3, 13)]) and pm_or_am.casefold() == "pm":
          print("Good Evening")
          break
         else:
          print("Please Enter PM or AM")

        break
         
  else :
         print("Not a Valid Number")





# ----------------------------------------------------
   
# Problem 9: Positive, Negative, or Zero

# Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.


def positiveNegative():

 checkNumber = input("Enter a Number to check Positive,Negative or Zero \n")

 checkNumber_cast = int( checkNumber )

 print( checkNumber.startswith("-") )




# if checkNumber.index(0) == "-":
#    print("This is a Negative Number")
# elif checkNumber.index(0) == "":
#    print("This is a Positive Number")











# ----------------------------------------------------
   


# Problem 10: Currency Converter

# Write a Python program that takes an amount in a specific currency (e.g., USD, EUR, GBP) as well as the target currency and converts it.






# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------



##########################################

# 1. if Statement:


condition = True

if condition:
   print("This is a Truthy Value")

if condition == True:
   print("This is a Exact Value")

if True:
   print("Wow, This is Truthy Value")

# The below [if] statement is not getting printed because condition which we passed is a Falsy value.
   
if 0:
   print("This value will not be printed because this is a Falsy Value")

 



# ----------------------------------------------------


# 2. if...else Statement:
   
# Here we will be using [if.....else] statement

if_variable = 10

# if not False :
if True:
   print("This value will get printed because this is a Truthy Value")

else:
   # Warning :- Code is unreachable
     # we get this error because the if condition has a Truthy value
   
   # We get this warning only in 2 situations 
     # 1. when we just use [ True ] in the [ if ] block condition
     # 2. when we use [ not False ] in the [if ] block conditons
   print("This value does not have any scope")



# ----
   
   
 # here we will be using conditions to check for the Exact Values

abc = "values"

if abc == "values":
   print("This is a Correct Value") # this block will get printed
else :
   print("This is a Wrong Value")




# ----------------------------------------------------


# 3. if...elif...else Statement:


  # The if...elif...else statement allows you to check multiple conditions sequentially. It executes the block of code corresponding to the first true condition.
   
# here we will be using [ if....else....elif ] statements
   

# three_blocks = "Value"
# three_blocks = "elif_value"
three_blocks = 1

if three_blocks == "Value" :
   print("If block value matched")
elif three_blocks == "elif_value" :
   print("elif block value matched")
else :
   print( "No Value matched so else block printed" )








# ----------------------------------------------------


# 4. Nested if Statements:

   #  You can nest if statements inside other if statements to create more complex conditional structures.


# here we will be learning on how to use nested [ if...elif...else ] blocks
   
condition_1 = "Value 1"

# Outer most [if... else ] statement
if condition_1:
   print("Yeah this is True, Condition 1")
   condition_2 = "value 2"

   # First Level Nested [if....else] statement
   if condition_2:
      print("Condition 2 value")

      condition_3 = "value 3"

      # Second Level Nested [if....else] statement
      if condition_3:
         print("Condition 3 passed")

      else :
         print("Condition 3 failed ")

   else :
      print("Condition 2 failed")

else:
   print("This is Else Block")



print("""




""")

# --------------------------------------


# 5. Ternary Conditional Expression (Conditional Operator):

 # The ternary conditional expression is a concise way to write an if...else statement in a single line.
   

# Syntax :-

 # variable_name = [ Value to Print if Condition is True ] [ "if" block condition ] [else] [ Value to print when if block fails ].

  # Ternary syntax can be breaked into 4 parts 
   # 1. [ Value to Print if Condition is True ]
     # Here we have to provide the value which will be printed if the [if] condition is True or Truthy 
   # 2. [ "if" block condition ]
     # here we have to provide the Condition using [if] block
   # 3. [else]
     # next we have to use [ else ] keyword to represent else block
   # 4. [ Value to print when if block fails ]
     # Here we have to provide the value which has to be printed if the [if] block condition is failed.

 



value_if_true = 15

message = "Greater than 10" if value_if_true > 10 else "Value is lesser than 10"

print( message )



# [ Practise ]

alphabet_value = "abc"

alphabet_result = "Alphabet is present" if alphabet_value else "Alphabet value is not Present"

print( alphabet_result )



# check for age and display the content 


person_age = int( input(f"Enter you age ? \n") ) # we can even directly do casting on the input by wrapping the Input inside the Specific datatype to which we want to cast the data.

content_display = "Content not Displayed" if person_age <= 18 else "Content is Displayed"

print( content_display )





# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------










