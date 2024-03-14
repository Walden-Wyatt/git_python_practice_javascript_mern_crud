


# Prerequisite


# First Class Function 

# First class function allows us to treat functions as any other objects, so that we can use them to 
  # pass as an arguement to another function
  # return the function from another function
  # assign a function to a variables 

 # When a Function becomes an Object  ?
  # We use function without invoking it then it becomes an Object 

# example 

def functionObject():
    return "Hell this is a Function treated as Object"

# Here now [ variable_functionObject ] has an Object that is Function reference ( functionObject )
variable_functionObject = functionObject

 # to prove when we print ( variable_functionObject ), if you get the Address of a Function which means we the variable has reference of Function object 

print( variable_functionObject )
# Output :- <function functionObject at 0x000001C6DFE7A2A0>
 # Here we can see [ variable_functionObject  ] has an Object that is Function reference of ( functionObject )
 # In python everthing is an Object, which has Classes behind the scene [ FU]


# ---------------


# Nested Functions 

 # When we create a Function inside another function then it is Nested function

# 1. Function inside other function

def parent():
    
    def nestedFunction():
        print("Hello Nested Child Function")

    # how nested function can be accessed ?
        # Either nested function can be invoked inside the parent function 
        # Nested function can be used as a Return value for the [ parent function ]

    print(nestedFunction)

    return nestedFunction

parentFunction_returns = parent()

parentFunction_returns()


# Output :- 
    # <function functionObject at 0x000001A2F60EA2A0>
    # <function parent.<locals>.nestedFunction at 0x000001A2F63791C0>
    # Hello Nested Child Function

print("""

""")

# ---

# 2. Function as parameters for another function 

def nestedFunction_byParameters(functionParameter):
    print("Function Parameters are Nested Functions" )
    return functionParameter


def arguement_nestedFunction():
    print("Nested Function Arguement")


print( nestedFunction_byParameters(arguement_nestedFunction) )


# Output :-
    # Function Parameters are Nested Functions
    # <function arguement_nestedFunction at 0x000001DA59009300>  




# ----

# Closures 

 # when inner function accesses the Variables or methods of Outer function in such a case Closure gets created, which makes a function closure function




print("""



""")








# ------------------------------------------------------

# Decorator Defination :-

 # A decorator in python is a function that takes another function as its argument, adds some functionality to it and returns yet another function

 # Decorators dynamically alter the functionality of a function, method or class without having to directly use subclasses or change the source code of the function being decorated.


# There are 2 Approach to create a Decorator Function.


 # [ Approach 1 ] 

# here we have decorator function which is an outer function
def my_decorator_function(functionOriginal):

    # here we will have a wrapper function (inner function) which wraps the original function
    def wrapper():
        print("Start")
        functionOriginal()
        print("Some Lines of code within wraper function")

    # here we have to return the wrapper() function from outer function, we should not invoke the [wrapper function]
    return wrapper



#  [ my_decorator_function ] will be a Decorator function for the [ originalFunction ].
def originalFunction():
    print("Hello, I AM A ORIGINAL FUNCTION. ")          



# Let us invoke the [ my_decorator_function ] by passing the [ originalFunction ] as its argument
    
myDecorator_value = my_decorator_function( originalFunction )
# Output :-  <function my_decorator_function.<locals>.wrapper at 0x000001BFC7AF94E0>

print( myDecorator_value )
myDecorator_value()

# Output :- 
    # Start
    # Hello, I AM A ORIGINAL FUNCTION.
    # Some Lines of code within wraper function

# here we can see that the function inside the [ originalFunction() ] is also got printed, that is [ "Hello, I AM A ORIGINAL FUNCTION. " ]
# This One Approach on how to create a Decorator function


print("""


""")



# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# [ Approach 2 ]
 # Using [ @Function_Name ]

# Here we will using [ @Function_Name ] syntax to create a Decorator function


# Here let us create a Decorator function 

def decoratorFunction(functionToDecorate):

    # here we will have a wrapper function which will have values to be passed for the function which gets decorated
    def wrapper():
        print("I am Decorator function")
        functionToDecorate()
        return "wrapper function"

    return wrapper


@decoratorFunction
def childFunction():
    print("I am Function which has to be Decorated")
    return "child function return"




print( childFunction )
print( childFunction() )


# Output :-

    # <function decoratorFunction.<locals>.wrapper at 0x000001DCDAC196C0>
    # I am Decorator function
    # I am Function which has to be Decorated
    # wrapper function



# Points :-

#  Here if you see that [ childFunction() ] has a return value ("child function return")
 # Inner function of [ decoratorFunction ] function that is [ wrapper  ] function has return value ("wrapper function").

 # when we try to invoke [ childFunction() ] ?
  # [ childFunction() ] functions return value is not getting printed by it prints [ wrapper() ] functions return value

 # By this we get to learn that [ wrapper() ] function gets called when we invoke [ childFunction() ] function
# What happens behind the scenes is that when we try to call the Function which has got decorated, from behind the scene it calls the [ Decorator ] function itself 

 # Here in the above case when we call the [ childFunction() ] it ultemately calls the [ decoratorFunction ]


print("""


""")

# -------------------------------



# How Decorator functions code Written behind the scene ?



def decoratorFunctions( funtion_tobe_Decorated ):

    def wrapper():
        print("Wrapper which will be retured as outer functions value, that is for (decoratorFunctions)")
        funtion_tobe_Decorated()
        print("end")

    return wrapper


@decoratorFunctions
def functionToDecorate():
    print("I AM A FUNCTION TO BE DECORATED")


functionToDecorate()




# Step by step explanatinos :-

# 1. when we use decorator for a function ( childFunction )
   # The function ( childFunction ) will be passed as an Arguement for the [ Decorator function ], where the [ Decorator function ] will have 1 parameter
# 2. ( childFunction ) will be wrapped inside the Decorator function( decoratorFunctions )
# 3. ( childFunction ) will be used inside the wrapper function which is present inside the [ decoratorFunctions ] 
# 4. Decorator function [ decoratorFunctions ] will have an Inner Function called ( wrapper Function ), The same ( wrapper function ) will be returned by the [ Decorator Function ] 
   # here ( wrapper function ) should not be invoked, it has to be passed as Function object ( without invoking it )
# 5 When we try to call the ( childFunction ), behind the Scene it calls the [ Decorator Function ], where the [ Decorator Function ] wraps the ( childFunction ) inside it
# 6. Finally program gets executed line by line which is inside the [ Decorator Functions ] [ Wrapper Function ] statements


# Important Points :-

# Decorator function must have 1 mandatory Parameter ( which is used to accept the other functions )
# Decorator function must have Nested function called [ Wrapper Function ], which is actual statements which gets executed when we call [other functions which got decorated ]
# Wrapper functions Defination or as Object ( without invocation ) has to be passed as return value value for decorator function 
# Decorator functions must be used by preceeding [ @ ] 
# Decorator functions can be used to any Custom Functions which we have declared inside the python file.




# Output :- 

    # Wrapper which will be retured as outer functions value, that is for (decoratorFunctions)
    # I AM A FUNCTION TO BE DECORATED
    # end



print("""


""")


# ---------------------------------------------------------------------------------------------------------------------------------------------------



# Decorator Function [ Practice 2 ]


# def yourDecorator(): # if there is no parameter passed we cannot able to access the decorated function ( child function )
def youDecorator(func):

    print("hello decorator")
    
    func()
    # return 'somee value'
   


# youDecorator
    # What happens if we don't use [ @ ] ?
     # if we don't use [ @ ] which means the Child/ function which has to be decorated has not got decorated. 
      # with [ @ ] function will not get decorated
    

@youDecorator
def apple():
    print("I am an apple")

    # Even if (apple()) function has "return" statement it will not be considered
     # once we use Decorator for a Function, the return statement which we use inside this function has no value.
    return "return from apple"
    
     # Error :- TypeError: 'NoneType' object is not callable
      # here you can see that the [ apple() ] has a return value which is of ( string ) type, but the Error message says [ NoneType ] is not callable, Its because Decorator function ( youDecorator ) has a no return value which means it is treated as [ NoneType  ] 


# apple()
# Error:- TypeError: 'str' object is not callable
     # we get this error because we tried to invoke a string value ( that is what we have returned inside the (youDecorator function ))
    
# if we want to access the [ apple function ], we should access it without invoking it
apple



# What happens when we do not use [ Inner / Nested function ]  for Decorators ?
  # 1. we cannot access the [ Child / Decorated ] function using parenthsis [ childFunc() ]
  # 2. if we want to access we have to access it without using [ Parenthsis i.e, () ]   
 # This is the Reason we have to use Inner or Nested Function.


print("""



""")


# -------------------------------------------------------------------



# #################

# 1. Decorator functions without using wrapper Function, Directly returning the Function which has been paased as an Arguement
# 2. Decorator Functions with more than 2 arguements
# 3. Decorator Functions which has 2 levels of Nested functions
# 4. wrapper function has [ *args and **kwargs ], [ wrapper(*args, **kwargs ) ]. 



# -------

# 1. Decorator functions without using wrapper Function, Directly returning the Function which has been paased as an Arguement

 # Here we did not created any Wrapper functions ( Inner or Nested functions) we directly returned the Function which has been paased as an Arguement

def singleDecorator(func):
    print("Single decorator function")
    return func

   # behind the scene the above return will look like below 
    # return def decorateMe():
    # print("Function Decorated by Single Decorator")


@singleDecorator
def decorateMe():
    print("Function Decorated by Single Decorator")


decorateMe()

# Output :-
    # Single decorator function
    # Function Decorated by Single Decorator




# ---------------------



# 2. Decorator Functions with more than 2 arguements

  # how to create a Decorator Functions with more than 2 arguements

 # We are not allowed to use below pattern for Decorator function 
# def twoArguementsDecorator(func, params1):

#     def wrapper():
#         print("wrapper function")
#         func(params1)

#     return wrapper

# @twoArguementsDecorator
# def wrapperTwoArguements():
#     print("Decorator To be wrapped")


# # wrapperTwoArguements()
# # Error : - TypeError: twoArguementsDecorator() missing 1 required positional argument: 'params1'

# wrapperTwoArguements("arguement value 1")


print("""


""")







# ----------------------------------------------------------------------




# 3. Decorator Functions which has 2 levels of Nested functions



def parent( param1, param2, param3 ):

    # Even here the Actual Decorator that is [ decorator ] does not have more than 1 arguements, it has only one arguement.
    def decorator(func):
        def wrapper():
            print("Wrapper with 3 level nesting")
            func()
            print( param1, param2, param3 )
        
        # here we have to return [ wrapper ]
        return wrapper
    # do not invoke the [ decorator ] it will throw error [ TypeError: parent.<locals>.decorator() missing 1 required positional argument: 'func' ]
    return decorator

# Here we a have passed arguements when decorating a function,
 # this can be done only when you have multi level nested functions, make sure the The place where decorators reference comes does not have any arguements.
@parent("Arguement 1", "Arguement 2", "Arguement 3" )
def getDecoratored():
    print(" I WILL GET DECORATED" )

    
getDecoratored()


# Output :-

    # Wrapper with 3 level nesting
    #  I WILL GET DECORATED
    # Arguement 1 Arguement 2 Arguement 3


# This is how we can use 3 level of nested functions with arguements 



print("""


""")



# -------------------------------------------------



# 4. wrapper function has [ *args and **kwargs ], [ wrapper(*args, **kwargs ) ]. 

 # why do we use [ *args and **kwargs ] in decorator functions

def helloDecorator(func):

    # [ *args and **kwargs ] can be used if we want to use any number of arguements and keyword arguements inside the function which gets decorated ( in this case its "baby" )
    def wrapper(*args, **kwargs):

        print("Hello args and kwargs")
        print("End.....")

        # when using the [ *args and **kwargs ] values make sure to assign it to a Variable inside the (wrapper) function
         # here we have invoked [ func(*args, **kwargs) ] which means we are calling [ baby() ] function statements which are inside th[ baby() ] will get loaded over here.
        result = func(*args, **kwargs)
        return result
    return wrapper


@helloDecorator
def baby( a, b, c=0 ):
    return a + b + c


print( baby(10, 20) )



# -------------------------------------------------------------------------------------------------------------------------------------------------------------



# Use Cases :-

    # Logging:
    # Timing:
    # Authentication and Authorization:
    # Caching:
    # Validation:
    # Django Web Framework:

































