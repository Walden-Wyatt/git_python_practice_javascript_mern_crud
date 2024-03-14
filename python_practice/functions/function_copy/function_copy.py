


# Functions in Python 

 # Here we will be Learning about Functions in Python Programming Language

 # Function is a block of reuseable which we can use multiple times in multiple places

# Different Types of Functions :-

 # 1. Built-in Functions :
   # This are functions which are already defined in the python programming language


 # 2. User Defined :

  # User defined functions are those functions which we manually define in our Python files, Below we have different ways to define a User Defined Functions.

    # a. Regular Function
     # Regular Functions are basic functions

    # b. Anonymous Function or Lamda functions
     # This are functions which are defined in a single line

    # c. Recursive Function
     # When a function itself then it becomes a Recursive function

    # d. Higher Order Function 
      # when a function accepts another function as Arguement or returns another function or does both the things then it becomes an Higher-Order functions

    # e. First Class Function 
      # this are functions where we can pass the reference to another variable, return the functions from another functions

    # f. Generator Functions 
     # this function uses Yield keyword which will iterate the Sequence or Iterable objects one by one in a Sequence.

    #


 

# def function_Name(parameters):
#     print("Block of statements")

 # Syntax Breakdown :-

 # 1. def 
  # [def] is a keyword which has to be used when defining a function, def keyword indicates that it a funcion

 # 2. Function Name
   # [Function Name] , there must be name for all the functions which we create because name will make the function unique, the code which we write will get stored in an unique reference

 # 3. () 
   # parenthsis has to be successed at the end of the function, parenthsis can be  used to specify Parameters 
   
   # a. Parameters
    # parameters are additional datas which the function accepts to process the result and provide as an output.
 
 # 4 : colen 
    # colen must be used to teminate the function declaration, when we use colen we can provide the block of statements inside the Indended block
    # For all the function which we are create must have indended block so that we can write Function related code inside the function block

 # 5 Intended Block of statements 
   # Intended block of statements are the codes which has to be executed when a Funciton is called
   # Inside this Indended block we can use codes such as :-
     # Datatypes, Loops, Conditional statements, print(), module related code, etc.


 #



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 1.  Built-in Functions:

 # [ print(), min(), etc  ]

print("Value will be printed in the terminal")





# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------


 # 2. User Defined :


    # a. Regular Function

def regularFunction( parameter, arguement ):
    print("Block of statements")
    print( parameter, arguement )


# function call or invocation 
regularFunction( "Parameter value", "Arguement Value" )



# ---------------------------------



# b. Anonymous Function or Lamda functions


 # Syntax :-

   # Function_Name = lambda parameter_1 , parameter_2 : indended Block of Statements 

   # [Function_name] [=] [lambda] [parameter_1, paramter_2] [:] [ indenede block of statements ]

# Syntax Breakdown 

   # 1. Function_Name
    # lambda functionmust have a Function name, this is function initialisation.

   # 2. =
     # after function name you have to use Assignement operator [ = ], so that you can declaration codes

   # 3. lambda
     # lambda is a keyword which has to be used if you want to make a function as a lambda function

   # 4. parameter_1 , parameter_2
     # next to lambda keyword we have to use Parameters, we can use any number of parameters, we can even use [*args and **kwargs]. 
      # Providing parameter is not mandatory we might use or we don't need to use.

   # 5. : [colen]
     # colen has to be used in a Lambda function, the reason we use colen is to provide indended block of statements where we will be writing single or multiple statements which will get executed when we call a Function.

   # 6. indended Block of Statements 
     # indended Block of statements, finally we have provide indended block of statements which will get executed when a function is called.




# Lambda Function with 2 Parameters
lambda_function = lambda parameter, parameter_2 : print(parameter, parameter_2) 


print( lambda_function )


# lambda_function()
# Error :- TypeError: <lambda>() missing 2 required positional arguments: 'parameter' and 'parameter_2' 
 # We encounter this error when we fail to pass required arguements for a function

lambda_function( "Arguement 1", "Arguement 2" )


# Lambda function without any parameters 
lambda_function_noParameter = lambda : print("Lambda function without parameter") 

lambda_function_noParameter()


# Lambda Function with return keyword 
  # Error :- Expected expression
   # this error occurs when we try to use return keyword inside the Lambda Funcion, we are not allowed to use [ return ] keyword inside the Lambda function.
  # lambdaFuntionReturn = lambda params:  return print("Hello")

# Code which is equal to using return keyword 

 # The below code will implicitly use [ return ] and returns the values which we passed inside the Indended block
lambdaFuntionReturn = lambda param1, param2 : param1 + " " + param2

print( lambdaFuntionReturn("return Arguement 1", "return Arguement 2") )



# ---------------------------------

 # c. Recursive Function


def factorial(number):
    if number == 0 or number == 1: # base case
        return 1
    
    # Recursive case
    else:
       return number * factorial(number - 1)  # here we have used Recursive function that is we called a Function inside the same function
print( factorial(4) )


#  --------------------

 # [ Practise 2 ]


def fact(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * fact(number - 1)


print( fact(5) )




print(""""
      

      
        
""")





# ---------------------------------



# 5. Higher-Order Functions:


  # Higher order functions are functions which accepts or returns another function


 # approach 1 - accept other functions

def functionAccepts_otherFunction( otherFunction ):
    print("Hello Accepting Function")


def acceptingFunction():
    print("This is a Accepting Function")


functionAccepts_otherFunction( acceptingFunction )



 # approach 2 - return other functions 


def returnOtherFunction( parameter ):
    return returnOtherFunction()


def returnOtherFunction():
    return "Hello, Returning Function"


print( returnOtherFunction() )



  # approach 3 - function accepts and returns other function


def acceptAndReturnFunction( acceptValue, returnValue ):
    return returnValue()


def acceptReturn_accept():
    print( "Accept Function" )
    return

def acceptReturn_return():
    print("Return Function")
    return


acceptAndReturnFunction( acceptReturn_accept, acceptReturn_return )
 # Output :- Return Function
  # here we can see that the function has returned other function as a return statement for [ acceptAndReturnFunction ]

print( acceptReturn_return() ) # "Return Function", None
print( acceptReturn_accept() ) # "Accept Function" , None






print(""""
      

      
        
""")





# ---------------------------------



# 6. First-Class Functions:

 # This is same as Higher Order Functions


def firstClassFunction(accept, returnFirstclass ):
    print( accept() )
    return returnFirstclass()

def acceptFirstClass():
    print("Accept First Class Function")

def returnFirstClass():
    print("Return First Class Function")


print( firstClassFunction( acceptFirstClass, returnFirstClass) )






print(""""
      

      
        
""")





# ---------------------------------



# 7. Generator Functions:


 # This is a Generator Functions where we will be using Yield keyword

def generatorFunction_2():
    # Here we used "yield" keyword which means program will stop executing at the every yield
     # if we want to access the values of Multiple Yield which is inside the Function, we have to call the Function multiple times, for each function call The appropriate yield value will get executed.
    yield 1
    return "hello"

print( generatorFunction_2() )
print( generatorFunction_2() )

# Output :- <generator object generatorFunction_2 at 0x00000220A4AF4B40>   




 # How python decides  weather a Function is Generator Fuction ?
  # when we use [ Yield ] keyword inside the Function then the Function becomes a Generator Function.


def generatorFunction():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


generatorFunction()
print( generatorFunction() )

print( type( generatorFunction() ) )




# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# [ Practise 2 ]


# 1. Built-in functions
# 2. user defined functions
#  a. Regular function
#  b. Lambda function
#  c. Recursive Function
#  d. Higher order function
#  e. First class Function
#  f. Generator Function
# 



# 1. Built-in functions

print("Hello print built in")

print( min(10, 20) )

print( max( 22, 44) )



print("""



""")


# -----------------------


# User Defined Functions 


# a. Regular function


def functionName(params):
    print("This is a Regular Function")
    print(params)


# function invokation
    
functionName("Arguement Value")



print("""




""")


# -----------------------


# b. Lambda Function



# [CODE ] lambdaFunction = lambda params1, params2 : print(params1 ,params2 ); print(params1); print("Lambda Function"); 
  # Warning :- "params2" is not defined
  # Error :-  lambdaFunction = lambda params1, params2 : print(params1 ,params2 ); print(params1); print("Lambda Function");
#                                                                                ^^^^^^^
           # NameError: name 'params1' is not defined

# We get this error when we try to use lambda functions parameter values from the second [print()] function, becuase the scope of second print function will be Gloabal not Local with the lambda functions indended block.
 # A lambda function will accept only 1 Print() statement as a local scope within indended block when we try to use more than 1 the 2nd occurance of the [ print() ] function will be Globally scoped (i.e, scoped outside the Functions Local Scope).


# lambdaFunction = lambda params1, params2 : print(params1 ,params2 ); print(params1); print("Lambda Function"); 

 # The above code is equal to writing the below code 

 # Equavalent code :-

# lambdaFunction = lambda params1, params2 : print(params1 ,params2 ); 
# print(params1); 
# print("Lambda Function"); 


lambdaFunction = lambda params1, params2 : print(params1 ,params2); 
print("Lambda Function"); 

lambda_function("arguement 1", "arguement 2")
functionName("Arguement Value")



print("""




""")


# -----------------------


# c #  c. Recursive Function

def quitGame():

 value = input("Enter a Value: Play[P] quit[Q]")
 print("Play Game")
 if value.casefold() == "q": # Here we have Base case
     return 
 
 else:
     quitGame() # Here we have Recursive call

# quitGame()





print("""




""")


# -----------------------


#  d. Higher order function


def higerOrderFunction(accept, returnFun):
    print( accept() )
    return returnFun()


def acceptFun():
     print("Accept Function") 
     return "Accept Function"


def returnFun():
     print( "Return function " ) 
     return "Return Function"

print( higerOrderFunction(acceptFun, returnFun) )




# --------------------------------------------------------

 
#  e. First class Function



def firstClassFunction(acceptf, returnf):
    print(acceptf())
    return returnf()

def acceptf():
    return "First Class Accept"

def returnf():
    return "First Class Return"


print( firstClassFunction( acceptf, returnf ) )




# --------------------------------------------------------

#  f. Generator Function



def generatorFunction_practise():
    yield 1
    return "hello"
    yield 2


print( type( generatorFunction_practise ) )


















