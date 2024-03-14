


# Exceptions 

# Here we will be Learning about Exceptions in Python  Programming Language
# Exceptions are Error which we encouter in python programming language, Exceptions are Set of Rules which we are supppose to follow while writing python code if we fail to Follow those Rules we might encounter Error
 # If we fail to write code in a Spicific Manner we might Encounter Errors in our Programm

# Rules are nothing but Structure or Syntax of the code, if we fail to follow the Structure or Syntax, or Order in which code has to be written we might encounter Errors, which says that we are suppose to follow proper structure or syntax which we have failed.



# Types of Exceptions 


 # Errors can be classified into 2 Types

 # A. Custom Errors 
   # Custom Errors are those errors which we ourself create 
   # We can create Custom Errors using [ raise ] keyword. Using [ raise ] keyword will stop execution of the Program


 # B. Built-in Errors 
  # Below we have some of the Built-in Errors which are there in python Programming Language

 # 1. Syntax Error
    # occurs when we use Wrong structure or syntax in a code

 # 2. Indendation Error 
     # error occurs when we fail to use indendations, space before the block of codes

 # 3. Name Error 
    # error occurs when we try to access variables name which is not inside the Global Scope as well as inside the Local Scopes

 # 4. Type Error
     # Type Error occurs when we try to use Wrong Operands in either side of the operator (i.e, Right or Left Side of the operator )
      # Example :- operands such as [ string and number ], using [ Complex datatype and other datatypes ], using [ boolean and dictionary ]
       # Example :- [ 20 + "string", True - {}, etc ]

 # 5. Value Error
     # Value error occurs when we try to pass wrong value as an arguement of a Function etc.This error occurs mainly in Type casting of Datatypes
     # Example :- tring to pass string of alphabets as an arguement for [int()] object, 
      # [ int("abc") ] - Here string "abc" cannot be converted to Integer type 

 # 6. File Error
     # File Error occurs when we try to access file which is not in that specific location 

 # 7. Index Error
     # Index Error occurs when we try to access values which is not present in that specific index
      # when we use index number more than the value which is present inside the Iterable Object, like a list has 10 values; we are tring to access 20th index value [ list[20] ] in this situation we might encounter this error.

 # 8. Zero Division Error 
     # Zero division error occurs when we try to Divide a Number with zero

 #



# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# Different Ways to Handle Errors 

    #  try.....except......else.....finally Block 


    # try :

    #     #  Statement of code where we Error might occur

    # except ErrorName:

    #     # Here the Error will be caught, The error which occurs inside the [ try ] block will be captured here

    # except ErrorName:

    #     # Here the Error will be caught, The error which occurs inside the [ try ] block will be captured here

    # else:

    #     # If there is not error in the Try Block the statements which we give here will be executed
    #      # when executing this statements the statements which is present inside the [try] block will also be executed

    # finally:

    #     # This block of code gets executed weather we encounter or not
    #     # finally can be used to write code which is related to getting the IP address of the user, getting the scroll position of the user, Providing Subscrition messages 
    #     # By using finally block we seperate the Business Logic code which is written inside [ try ] block as well as Other datas which we are tring to get from the user
    #      # There will not be any confusions between Business Logic code and Other information code, this is the main reason behind finally block





# 1. try

# 2. except 

# 3. else 

#  finally

#  raise
  # this is the keyword which we can use to create our own Custom Errors or Exceptions

#  with
   # [with] keyword can mainly be used to while handling files in our Programs, File handling errors can be handled using [with] keyword 

#  pass
   # This keyword can be used if we dont want our programm to stop if any error occurs, Ignore the error and move on

#  asserts

#  



# -----------------------------------

# ##################################



           ####     [ ChatGPT Explanations]    #####

      # python exceptions
      # ChatGPT

      # In Python, exceptions are events that occur during the execution of a program that disrupt the normal flow of instructions. When an exception occurs, the normal flow of the program is interrupted, and the control is transferred to an appropriate exception-handling block.

      # Here are some common types of exceptions in Python:

      #     SyntaxError:
      #         Occurs when there is a syntax error in your code, preventing it from being parsed correctly.

      #     python

      # # Example SyntaxError
      # print("Hello, world"  # Missing closing parenthesis

      # IndentationError:

      #     Occurs when there is an issue with the indentation of your code.

      # python

      # # Example IndentationError
      # if True:
      # print("Indentation error")  # Missing indentation

      # NameError:

      #     Raised when a local or global name is not found.

      # python

      # # Example NameError
      # print(undefined_variable)

      # TypeError:

      #     Raised when an operation or function is applied to an object of an inappropriate type.

      # python

      # # Example TypeError
      # result = "10" + 5  # Concatenation of string and integer

      # ValueError:

      #     Raised when a function receives an argument of the correct type but with an invalid value.

      # python

      # # Example ValueError
      # number = int("abc")  # Cannot convert "abc" to an integer

      # FileNotFoundError:

      #     Raised when trying to access a file that doesn't exist.

      # python

      # # Example FileNotFoundError
      # with open("nonexistent_file.txt", "r") as file:
      #     content = file.read()

      # IndexError:

      #     Raised when trying to access an index that is outside the bounds of a list or other iterable.

      # python

      # # Example IndexError
      # my_list = [1, 2, 3]
      # print(my_list[5])  # Index 5 is out of range

      # ZeroDivisionError:

      #     Raised when dividing a number by zero.

      # python

      #     # Example ZeroDivisionError
      #     result = 10 / 0

      # To handle exceptions, you can use the try, except, else, and finally blocks. Here's an example:

      # python

      # try:
      #     # Code that might raise an exception
      #     result = 10 / 0
      # except ZeroDivisionError:
      #     # Handling a specific exception
      #     print("Cannot divide by zero!")
      # except Exception as e:
      #     # Handling a generic exception
      #     print(f"An error occurred: {e}")
      # else:
      #     # Code to execute if no exception is raised
      #     print("Division successful!")
      # finally:
      #     # Code that always runs, whether an exception is raised or not
      #     print("Finally block executed.")

      # Remember that it's generally a good practice to catch specific exceptions rather than using a generic except clause, as it helps in better understanding and debugging of the code.
      # User
      # comprehensive, in-depth and in-detailed explanations on different way to Handle Exceptions in Python programming language
      # ChatGPT

      # Certainly! Handling exceptions in Python is a crucial aspect of writing robust and error-tolerant code. There are several ways to handle exceptions in Python, each serving different purposes. Let's explore various approaches:
      # 1. Using try, except, else, and finally Blocks:

      # The most common way to handle exceptions is by using the try and except blocks:

      # python

      # try:
      #     # Code that might raise an exception
      #     result = 10 / 0
      # except ZeroDivisionError:
      #     # Handling a specific exception
      #     print("Cannot divide by zero!")
      # except Exception as e:
      #     # Handling a generic exception
      #     print(f"An error occurred: {e}")
      # else:
      #     # Code to execute if no exception is raised
      #     print("Division successful!")
      # finally:
      #     # Code that always runs, whether an exception is raised or not
      #     print("Finally block executed.")

      #     The try block contains the code that might raise an exception.
      #     The except block catches and handles specific or generic exceptions.
      #     The else block contains code to execute if no exception occurs.
      #     The finally block holds code that always runs, whether an exception is raised or not.

      # 2. Handling Multiple Exceptions:

      # You can handle multiple exceptions in a single except block or use multiple except blocks:

      # python

      # try:
      #     # Code that might raise an exception
      #     result = int("abc")
      # except (ValueError, TypeError) as e:
      #     # Handling multiple exceptions
      #     print(f"Error: {e}")
      # except ZeroDivisionError:
      #     print("Cannot divide by zero!")

      # 3. Using else Block:

      # The else block contains code that runs only if no exception occurs:

      # python

      # try:
      #     # Code that might raise an exception
      #     result = 10 / 2
      # except ZeroDivisionError:
      #     print("Cannot divide by zero!")
      # else:
      #     print(f"Result: {result}")

      # 4. Using finally Block:

      # The finally block contains code that always runs, whether an exception is raised or not. It's often used for cleanup operations:

      # python

      # try:
      #     # Code that might raise an exception
      #     result = 10 / 0
      # except ZeroDivisionError:
      #     print("Cannot divide by zero!")
      # finally:
      #     print("This code always runs.")

      # 5. Raising Exceptions:

      # You can raise exceptions using the raise keyword. This can be useful for creating custom exceptions:

      # python

      # def divide(x, y):
      #     if y == 0:
      #         raise ValueError("Cannot divide by zero!")
      #     return x / y

      # try:
      #     result = divide(10, 0)
      # except ValueError as e:
      #     print(f"Error: {e}")

      # 6. Using assert Statement:

      # The assert statement is used for debugging and testing. It raises an AssertionError if the given expression is False:

      # python

      # x = 10
      # assert x > 0, "x must be positive"

      # 7. Ignoring Exceptions:

      # You can use a bare except block to catch and ignore all exceptions. However, this is generally discouraged as it can hide bugs:

      # python

      # try:
      #     # Code that might raise an exception
      #     result = 10 / 0
      # except:
      #     pass  # Ignoring the exception

      # 8. Using with Statement for Resources:

      # When working with external resources (like files), use the with statement to ensure proper resource management and automatic cleanup:

      # python

      # try:
      #     with open("example.txt", "r") as file:
      #         content = file.read()
      # except FileNotFoundError:
      #     print("File not found!")

      # Handling exceptions properly enhances code reliability and user experience. Choose the approach that fits the specific requirements of your application and promotes clean, readable, and maintainable code.
      # User
      # why this code does not catch indentation error 


      # try :

      #   print("Hello")

      #   for x in range(2):
      #   print("Hello")

      # except IndentationError:
      #  print("You encountered Indentation Error")

      # else:
      #  print("There is no Errors !")

      # finally:
      #  print("Finally Block!")

      # ChatGPT

      # In Python, the try, except, else, and finally blocks are used to handle runtime errors (exceptions) that occur during the execution of the try block. However, IndentationError is a compile-time error and is not caught by the except block. It is not part of the exceptions that can be caught during runtime.

      # In your code, if there is an indentation error in the try block itself, the program won't execute, and you won't reach the except, else, or finally blocks. Indentation errors are detected by the Python interpreter during the parsing (before execution) phase, and they prevent the program from running.

      # To catch IndentationError, you would need to ensure that the indentation in your code is correct before running it. Once the code is free of indentation errors, you can use the try, except, else, and finally blocks to handle other runtime errors that might occur during execution.

      # Here's an example with corrected indentation:

      # python

      # try:
      #     print("Hello")

      #     for x in range(2):
      #         print("Hello")

      # except IndentationError:
      #     print("You encountered Indentation Error")

      # else:
      #     print("There is no Errors !")

      # finally:
      #     print("Finally Block!")

      # In this corrected code, if there are other runtime errors inside the try block, the except block will be executed to handle those errors.
      # 2 / 2
      # User
      # list down all the compile time errors which are there in python programing 
      # ChatGPT

      # Compile-time errors in Python are also known as syntax errors. These errors occur during the parsing phase, before the code is executed. When you run a Python script or try to import a module, the interpreter checks the syntax of the code. If it encounters any syntax errors, it will not generate a compiled version of the code (bytecode), and the program will fail to run.

      # Here are some common syntax errors (compile-time errors) in Python:

      #     SyntaxError: invalid syntax:
      #         Raised when the interpreter encounters code that does not conform to the Python syntax rules.

      #     python

      # # Example SyntaxError: invalid syntax
      # print("Hello"  # Missing closing parenthesis

      # IndentationError:

      #     Raised when there are issues with the indentation of the code, especially in blocks like if, else, for, etc.

      # python

      # # Example IndentationError
      # if True:
      # print("Indentation error")  # Missing indentation

      # TabError: inconsistent use of tabs and spaces:

      #     Raised when there is a mix of tabs and spaces for indentation within the same block.

      # python

      # # Example TabError
      # if True:
      # \tprint("TabError")  # Mix of tabs and spaces

      # SyntaxError: unexpected EOF while parsing:

      #     Raised when the interpreter reaches the end of the file or a block without completing the expected syntax.

      # python

      # # Example SyntaxError: unexpected EOF
      # if True:
      #     print("Incomplete code")

      # SyntaxError: EOL while scanning string literal:

      #     Raised when there is an unterminated string (missing closing quote).

      # python

      # # Example SyntaxError: EOL while scanning string literal
      # print('Unterminated string

      # SyntaxError: invalid token:

      #     Raised when the interpreter encounters an invalid token or character.

      # python

      # # Example SyntaxError: invalid token
      # 123 @ 456  # Invalid character "@"

      # SyntaxError: can't assign to literal:

      #     Raised when trying to assign a value to a literal (immutable object).

      # python

      # # Example SyntaxError: can't assign to literal
      # 42 = x  # Cannot assign value to the integer literal 42

      # SyntaxError: unmatched close parenthesis:

      #     Raised when there is an unmatched closing parenthesis.

      # python

      #     # Example SyntaxError: unmatched close parenthesis
      #     print("Hello"  # Missing closing parenthesis

      # It's important to fix syntax errors before attempting to run the code, as they prevent the interpreter from generating the bytecode necessary for execution.











# -----------------------------------

# ##################################






# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# How to practise 

# Make all the errors which are listed above and handle each and every using [ try..except...else...finally  ] block

# use Multiple [ except ] blocks

# Use [raise] keyword and Create a Custom Exceptions

# use [ with ] keyword to perform file Handling

# use [ pass ] keyword to ignore the errors.



# --------------------------------------------------------




# [ syntax error ]
 

    # try:
    
    #   # Error :- [  Try statement must have at least one except or finally clause  ]
    #    # This error messages says that when we use [ try ] block we must mandatorily use [ except ]

    #  print("Hello"
    #  # Error :- SyntaxError: '(' was never closed
        
    #        # We cannot able to handle Syntax error with [ try...except..finally ] block.

       # The except block executed only when there is Syntax Error inside the [ try ] block Statements.
    # except SyntaxError:
    #     print("This is a Syntax Error")

    # else:
    #   print("This block Executes if there is no Error inside the [try] block")

    # finally:
    #  print("This is Finally Block")




# ---------------------------------------------------------------------------------------------------------------------------------------------------




 # 2. Indendation Error 

  # Because Indendataion Error is a Compile time error this errors will not be caught be Interpretter
  # try..expert block will catch only [ Run Time Errors ] not [ compile time errors ]
  # All the [ Compile time errors ] must be fixed before running the program as the interpreter will stop the execution of the program by not creating a Byte code 

try :

  print("Hello")

  for x in range(2):
   
   # Here we have [ Compile Time Errors ].
# print("Hello")
   
   print("Hello")
except IndentationError:
 print("You encountered Indentation Error")

else:
 print("There is no Errors !")

finally:
 print("Finally Block!")



print("""





""")


# ---------------------------------------------------------------------------------------------------------------------------------------------------



# 3. NameError 
 
 # Error :- [  NameError: name 'WrongVariableName' is not defined ]
  # This error occured because we did not there is no variable in the name [ WrongVariableName ]
#  print(WrongVariableName)\
 
 # Solution for Above Error :-


try:
 
 print(WrongVariableName)

except NameError:
 print("You Encountered Name Error ")

else:
 print("NameError has not occured !")

finally:
 print("Finally block")


# Output :-
    # You Encountered Name Error
    # Finally block

# we got this output because we encountered Name Error.



print("""





""")


# ---------------------------------------------------------------------------------------------------------------------------------------------------



# 4. Type Error 

  # Occurs when we use Wrong datatype value for either of the Operands with a Operator


# print("hello" + 10)
# Error :- TypeError: can only concatenate str (not "int") to str
  # this error occurs when we try to use Operators with wrong datatype as an operand to perform some operations


try:
 
 print( "Hello" + 20 )
 
except TypeError:
 print("TypeError Please check the Datatype of Operand")

else:
 print("NO TypeError")

finally:
 print( "Finally Block !" )


# Output :-
    # TypeError Please check the Datatype
    # Finally Block !



print("""





""")


# ---------------------------------------------------------------------------------------------------------------------------------------------------



# 5. Value Error

 # Value error occurs when we try to pass wrong values but correct datatype as an arguement for functions
 # This error mainly occurs during Type Casting of the Datatypes


# stringType = "Hello"
# # Here let us try to cast String with alphabet characters to int()
# casting = int( stringType )

 # Error :- ValueError: invalid literal for int() with base 10: 'Hello'
  # we encountered value error whenw e tried to type cast String with alphabetical character to Integer


try:

 string = "Hello"
 casting = int( string )

except ValueError:
  print("ValueError - we are not allowed cast Alphabetical String to Int")

else:
 print( "No ValueError" )

finally:
 print("Finally Block !")

# Output :-
    # ValueError - we are not allowed cast Alphabetical String to Int
    # Finally Block !



print("""





""")


# ---------------------------------------------------------------------------------------------------------------------------------------------------



# 6. IndexError 

# lists = [ 1, 2, 3 ]

# print( len( lists ) )  # 3

# print( lists[4] )
# # Error :- [IndexError: list index out of range ]
#  # we encounter this error because we tried to accses tha index value which is not present inside the Iterable Object

try :
 
    lists = [ 1, 2, 3 ]

    print( len( lists ) )  # 3

    print( lists[4] )

except IndexError:
 
 print("IndexError - we encountered IndexError")

else :
 print("No IndexError")

finally:
 print("Finally Block !")


# Output :-
    # IndexError - we encountered IndexError
    # Finally Block !



print("""





""")


# ---------------------------------------------------------------------------------------------------------------------------------------------------



# 7. Zero Division Error 
 
  # we get this error when we try to divide Any number value with 0
    # when we try to divide Other character with 0 we get TypeError

# print( 10 / 0 )
# Error :- ZeroDivisionError: division by zero
 # we encountered this error because we divided a number with zero
 # we get this error only when numerator has some number other than zero where as Denominator has zero value

# print( 0 / 10)   # Output :- 0.0



# Solution :-


try :
 
 print( 100 / 0 )

except ZeroDivisionError:
 print( "ZeroDivisionError - we got ZeroDivisionError ")

else :
 print( "No ZeroDivisionError ")

finally:
 print( "Finally Block !" )


# Output :-
    # ZeroDivisionError - we got ZeroDivisionError
    # Finally Block !



print("""





""")


# ---------------------------------------------------------------------------------------------------------------------------------------------------



# 8. FileError


# open("./abc.txt")
 # Error :- FileNotFoundError: [Errno 2] No such file or directory: './abc.txt'
 # we get this error when we try to access file which is not present inside the specific location




try:
 
 # Here we have code which might have Runtime Error not compile-time error 
 open("./xyz.txt")

except FileNotFoundError:
 
  # here we have except which gets executed when we have atleast one Run-time error inside [ try ] block statements of code
 print("FileNotFoundError - we got FileNotFoundError")

else:
 
 # here we have code which gets executed if there is no Error inside [ try ] block
   # if none of the code throws error inside the [try] block we might get this error.
 print( "No FileNotFoundError" )

finally:
  
   # Here we have Finally block which gets executed weather we have Error inside or not inside [ try ] block
 print( "Finally Block !" )


# Output :-
    # FileNotFoundError - we got FileNotFoundError
    # Finally Block !



print("""


      
#  Use Multiple [ except ] block



""")


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#################
 
 #  Use Multiple [ except ] block


 # use all the 8 errors based on its name and provide the error message, additionally use empty [except] block which does not have any arguements

 # if you have list of error inside the Try block all the errors will not be caught by different [ except ] blocks
  # Python interpretere will resolve the Errors one by one, If there are multiple errors inside the [try], python will stop at the First Occurance of the Error till the First error gets resolved the interpreter will not move the next Line or next [except] block to print the messages.


try :
 
 print("Hello")

 # we cannot use Syntax Error and Indentation Errors

# list of errors 
 
 print(NameNotFound)

 print( 10 * "hello" )

 print( int("abc") )

 lists = [1, 2, 3]
 print( lists[6] )

 print( 100 / 0 )

 open("./abc.txt")



except SyntaxError:
 print ("Encountered - Syntax Error ")

# Code is unreachable
  # we get this Code is unreachable because there is not code inside the [ try ] block which have IndentationError.
except IndentationError:
 print(" Encountered - Indentation Error")


except NameError:
 print("Encoutered - Name Error")

except TypeError:
 print( "Encoutered - Type Error" )

except ValueError:
 print( "Encoutered - Value Error" )

except IndexError:
 print("Encoutered - Index Error")

except ZeroDivisionError:
 print( "Encoutered - ZeroDivisionError Error" )

except FileNotFoundError:
 print("Encoutered - FileNotFoundError Error")

except:
 print("No Errors in the above Except Matched so This Except block will get Executed !")

else:
 print("No Error has Occured inside try block")

finally:
 print("Finally Block !")




# Output :
  # Hello
  # Encoutered - Name Error
  # Finally Block !
 
 # Because untill the First Error gets resolved that is [NameError] python interpreter will not move to next [ except ] block.



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Use [raise] keyword and Create a Custom Exceptions



# raise "Custom Exceptions"
  # Error :- TypeError: exceptions must derive from BaseException
   # we are not suppose to use [ raise ] keyword in the global scope as it is not a Good Practise
 

def divide(x,y):
 if y == 0:
  # here we use [ raise ] keyword to display the error
  raise "cannot divide by 0"
  # raise ValueError( "cannot divide by 0" )
 else:
  return x / y


print( divide(4,2) )

# print( divide( 4, 0 ) )



#  ----------------------------



# How to create a Custom Errors

 # Here we create a Custom Error class which will display [ Custome Error ] message
class CustomError:
 def __init__(self, customError ):
  print(customError)

CustomError("Custome Error")


# now let us have a function which will check the condition and display [ CustomError ] class

def customError(x, y):
 if y == 0:
  raise CustomError
 else:
  return x / y 
 
# print( customError(2, 3) )
# print( customError(2, 0) )


# Error Message :-

  # File "C:\Users\user\Desktop\python_practice\exceptions\exceptions.py", line 620, in customError
  #     raise CustomError
  # TypeError: exceptions must derive from BaseException

#  Here encountered an different errors, we also handled those Errors Gracefully


# ----------------------------------------


# Create a Custom error for value not divisible 0

def denominatorErrorFuntion():
 
 class DenometerNonZero:
  def __init__(self, errorMessage ) :
    print( errorMessage )


def denoNotZero(x, y):
    if y == 0:
      # Here we raised an Exception using [ raise ] keyword.
      raise DenometerNonZero( "Denominater must not be Zero!" )
    else:
      return x / y


# denoNotZero( 10, 22 )

# denoNotZero( 10, 0 )
# Error :-
  # File "C:\Users\user\Desktop\python_practice\exceptions\exceptions.py", line 655, in denoNotZero
  #     raise DenometerNonZero( "Denominater must not be Zero!" )
  # TypeError: exceptions must derive from BaseException

# Here we can see that Our condition is perfecly fine, because wrote the code in such a way the create of the cdoe will not have [error]




# --------------------------------------------------------------------



# use [ pass ] keyword to ignore the errors.

# let us have a [ NameError ] and try to use [ pass ]  keyword


try:

#  print(wow)
 result = 10 / 0

except:

 # Here we used [ pass ] keyword, use [ pass ] keyword the inside the [ except ] block will not make the Program terminate even we have errors 
  # Now even thought above [ try ] block has Error code, those error message has been skiepped because we use [ pass ] keyword inside the [ except ] block 
 pass

else:
 print("Print it no Error inside try")

finally:
  print( "Finally block" )




# ------------------------------------------------------------------------------------------



 # with keyword using inside the [ try block ]



# with open("./abc.txt") as file:
#  content = file.read()

# Error :- FileNotFoundError: [Errno 2] No such file or directory: './abc.txt' 
 

# with syntax 
 
 # [ with ]
  # "with" is a keyword which has to be used to make the with statement 
   # this is mainly used in file handling such as Reading and Writing files
 # open( "file path")
  # open() is the methoch which can be used to check for the file and start reading, writing the file

 # as
  # [as] is the keyword which can be used to same the output into a Variable 
 
 # file
   # here we have to provide the new name for the output value that is to get the file which we specified




# Solution :-
  
try :
 
  with open("./abc.txt") as file:
   content = file.read()

except :
 print("some File error in try block")

# Output :-
  # some File error in try block
# we got this output because we have error code inside the [ try ] block.



# ---------------------------------------------------------------------------------------------


# 6. Using assert Statement:


x = 10
assert x > 0, "x must be positive"




print("""
      
      
      
      
      """)




# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


 # Here We learnt everything which is required to work with Exceptions in python Programming.


# Practise this concepts once again you will master






# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Types of Exceptions :

  # Syntax Error 

  # Indentation Error

  # Name Error 

  # Type error 

  #  value error 

  # Index Error

  # File Error

  # Zero Division Error



# Ways to Handle this Exceptions


  # try 

  # except

  # else

  # finally

  # raise

  # pass

  # with 

  # assertz

  # 

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------



# syntax error

 # print("hello"


# Indentation Error 

 # wrong indentations


# ------------------------------------


# Name  error

try:
 print(wrongName)

except NameError:
 print("Name Error")

else:
 print("If no Error has occured")

finally:
 print("Finally Block!")




print("""




""")



# ------------------------------------


# Type Error
 

print( 10 * "hello" )

# for x in range(10):
#  print(x * "*")

try :
 
 print("a" + True)
# Error :- TypeError: can only concatenate str (not "bool") to str

except TypeError:
 print("Type Error")

else:
 print("No Type Error")

finally:
 print("This is Finally Block")




print("""




""")



# ------------------------------------


# Value Error

try:
 print( int("abc") )
# Error :- ValueError: invalid literal for int() with base 10: 'abc'

except ValueError:
 print("Value Error ")

else:
 print("No Value Error")

finally:
 print("Finally Block!")




print("""




""")



# ------------------------------------


# Index Error

fruits = [ "apple", "mango", "orange", "papaya", "grapes", "kiwi" ]


try:
 print( fruits[10] ) 

  #   print( fruits[10] )
  #            ~~~~~~^^^^
  # IndexError: list index out of range

except IndexError:
 print("IndexError")

else:
 print("No IndexError!")

finally:
 print("Finally Block !")




print("""




""")



# ------------------------------------


# ZeroDivision Error


try:

 print( 10 / 0 )

  #  print( 10 / 0 )
  #            ~~~^~~
  # ZeroDivisionError: division by zero

except ZeroDivisionError:
 print("ZeroDivision Errors !")

else:
 print("No ZeroDivisionError !")

finally:
 print(" Finally Block")




print("""




""")



# ------------------------------------

# FileNotFoundError


try:

  with open("./abc.txt"):
   print("with Keyword")

  # File "C:\Users\user\Desktop\python_practice\exceptions\exceptions.py", line 1402, in <module>
  #     open("./abc.txt")
  # FileNotFoundError: [Errno 2] No such file or directory: './abc.txt'


except FileNotFoundError:
 print("File Not Found Error")

else:
 print("No FileNotFound Error")

finally:
 print("Finally Block !")



# -----------------------------------------------------------
 


 # How to Create a Custom Error using [ raise ] keyword


# when you use [raise] keyword at the Top Level of the file ( that is not inside any Block scope ) our program will stop execution when when we file has any Error code Python Compiler will not create a Byte code, for all the Error files byte code will not be generated.

 # Do not use [ raise ] keyword at the Top Level of the File 
 # [ Code ] 
 #  raise "Custom Error"


# Here we have Custom Error Class
  # This class will accept 1 Arguement that is the Error message which has to be displayed, The parameter value will be displaye be preceeding the value with [ raise ] keyword, This will Create a Custom Error Class.

class Custom_Error_Class:
 def __init__(self, errorMessage):
  raise errorMessage


value = 1

# here we used [if....else] statement to display the Error message.
if value >= 11:
 print( Custom_Error_Class("Value greater than 10"))
else:
 print("No Error has occured !")




# -----------------------------------------------------------
 


 # with keyword
  # with keyword has to be mainly used with file handling, tring to perform CRUD Operations with Files


try:

# FileNotFoundError: [Errno 2] No such file or directory: './abc.txt'
 with open("./abc.txt"):
  print("With Keyword")

except FileNotFoundError:
 print("File Not Found Error")

else:
 print(" No FileNotFoundError Occured !")

finally:
 print("Finally Block !")




print("""



""")

# -----------------------------------------------------------
 


# Pass keyword
 

try:
 print( 10 / 0 )

except:
 
 # inside the [ try ] block we have zeroDivisionError, but just because we used [pass] keyword inside the Except block nothing is printed
 pass


#  print("zero division error")
 # if we give some [ print() ] statements, after using [ pass ] keyword the print function will print the message inside the Terminal

# There Two situations on how to Overcome below Error 
   # [  IndentationError: expected an indented block after 'except' statement on line 1499  ]

# 1. Provide some Indented Block Statements which will print message based on what error has been occured
# 2. [ pass ] keyword = if you don't want any message to printed even after you encounter some error use [ pass ] keyword  which will not print() any message as well as we will not encounter above Error.


else:
 print("There is not ZeroDivisionError !")

finally:
 print("Finally Block !")





# ----------------------------------------------------------------
 
 # Practise 2 is also Done.






















































