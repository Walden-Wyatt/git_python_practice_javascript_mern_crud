

# Local Scope 

 # Local Scopes are those Scopes which within the Indented Environment
 # All those Variables and Functions which comes within the Indented Environments are called as Local Scopes




# Local Scope in Python:


# 1. Definition:

#     Local scope in Python refers to the innermost scope of a program, typically within a function or method.
#     Variables declared inside a function or block have a local scope and are accessible only within that specific function or block.



# ----------------------------------------------------------------------------------------------------------------------------------------------



# 2. Declaration and Access:

#     Variables declared within a function are created when the function is called and destroyed when the function exits.
#     They are only accessible within the function in which they are defined.



def localFunction():

    # declaration for Local Variables
    localVariable = "Local Variable Value"

    # access local variables 
    print( localVariable )


localFunction()


# Let us try to access the [ localVariable ] in the Global Environment

# print( localVariable )
# Error :- [ NameError: name 'localVariable' is not defined ]
 # we get this error when we try to access the Local Variable in the Global Environment, which we are not allowed to do


# Learnings :-
 # Local Variables can be accessed only within the Local Environment, it cannot be accessed outside the Local Environment or in the Global Environement



# ----------------------------------------------------------------------------------------------------------------------------------------------



# 3. Function Parameters:

# Function Parameters are Local Variables, which can be accessed only within the Local Environment


def localFunction( parameter1, parameter2 ):

    # here we accessed [ parameter1, parameter2 ] within the Local Environment
      # we did not got any Errors, accessing the Parameters from inside the Function
    print( parameter1 )
    print( parameter2 )


localFunction( "Arguement 1", "Arguement 2" )

# Accessing [  parameter1, parameter2 ] outside the Local environment ( outside the function )

# [ CODE ] :- print( parameter1, parameter2 )
 # Error :- [ NameError: name 'parameter1' is not defined ]
 # we get this error because parameter1 and parameter2 are local variables which has scope within the function body, so Local variables cannot be accessed outside the Local Scope that is in the Global Environment.


print("""


""")


# ----------------------------------------------------------------------------------------------------------------------------------------------



# 4. Local Variable Lifetime:

# Local variables will only be existing till the Function invokation get executed,once the Function execution is done The variables which are presents inside the Function will get Destroyed or garbage collected.

 # Once the Function execution is done the local variables inside the Fuction will get destroyed and its value will not be retained

def localVarLifetime():

    # here we have Local Variables 
    variable1 = "Value 1"
    variable2 = "Value 2"

    # here we printed local variables
    print( variable1, variable2 )

# Here we have invoked the Function 
 # Once the Function execution is done the Local variables will get destroyed, variable such as [ variable1 and variable2 ] value will not be retained.
localVarLifetime()


# Output :- 
  #  Value 1 Value 2


print("""


""")


# ----------------------------------------------------------------------------------------------------------------------------------------------



# 5. Shadowing:

 # Python will decide which value has to be printed based on variables scope
  # if we have same variable name in Global Scope and Local Scope based scope precedence python will print the value

 # ChatGPT explanations :-
    #  Similar to global scope, local scope can also experience variable shadowing.
    # If a local variable has the same name as a variable in an outer scope, the local variable takes precedence within its scope.


globalLocal_variable = "Global First Local Second"

def localScopeFunction():
    globalLocal_variable = "Local First Global Second"

    # access within the local environment 
    print( globalLocal_variable )

print( globalLocal_variable )


# Output :- 
  # Global First Local Second


print("""


""")


# ----------------------------------------------------------------------------------------------------------------------------------------------



# 6. Nested Functions and Local Scope:



def outer_function():
    outerVariable = "Outer Variable"

    def innerFunction():
        # innerVariable = "Inner Variable"
         # here we can see that Inner Function can access the variable which is present in the outer function, that is [ outerVariable ]
        print( outerVariable )

        innerVariable = "Inner Variable Value"

    innerFunction()

    # print( innerVariable )
     # Error :- [ NameError: name 'innerVariable' is not defined ]
     # we cannot able to access the Inner Functions variable from inside the Outer Functions

outer_function()



print("""


""")


# ----------------------------------------------------------------------------------------------------------------------------------------------



# How to  modify outer functions variable from the Inner Function 

def outFunction():
    outVariable = "out value"

    def inFunction():
       inVariable = "In Value"

       global outVariable
       outVariable = "Modified Out Value"

    #    print( outVariable )

    inFunction()

    print( outVariable )
    # Here the value did not got modified even after we changed inside the [inFunction()] function body.

outFunction()






print("""


""")


# ----------------------------------------------------------------------------------------------------------------------------------------------






# 7. Best Practices:

#     Limit the use of global variables to reduce the risk of unintentional side effects and to improve code maintainability.
#     Favor passing values through function parameters rather than relying on global variables.




# ----------------------------------------------------------------------------------------------------------------------------------------------------




# [  Practice 2  ]


def localScope():
    outVariable = "Outer Value"

    def innerScope():
        inVariable = "Inner Value"

        # access localScope variable 
        print( outVariable )

    # access innerScope function variable 
     # Error :- [  NameError: name 'inVariable' is not defined. Did you mean: 'outVariable'?  ]
      # when we try to acces innerScope function in the Outer scope we get this Error.
    # print( inVariable )
    innerScope()

localScope()






# Learnings :-

 # Outer Scopes variables can be accessed from Inside the Inner Scope
 # Inner Scopes variables cannot be accessedd from inside the Outer Scope
  # when it comes to nested function the above 2 points will be same
 # 

































