

# Global Scope:

# Here we will be Learning on how Global Scope works in Python Programming Language 


global_variable = "Global Variable"

def globalFunction():
    print( "Global Function" )


print( global_variable )
globalFunction()



# Scope Checcking 
 # Python will check from Current Scopes to Upper Scopes 
  # Python will check variables from current Scopes then  Parent Scopes then  Grandparent Scopes etc 
 # Python will not check from Current Scopes to Lower Scopes
  # Python will check check for variable inside the Current scopes then Children scopes then grandChilderen scopes then greatGrandChilds scopes

abc = "Global"

def check():

    def innerFunction():
        abc = "Local"

    innerFunction()

    print( abc )



check()


print("""

""")

# ----------------------------------------------------------------------------------------------------------------------------------------------------



# Global Scopes 



 # Declaration and Access:


global_variable = "Globa variable"

# access in global scope
print( global_variable )


# accessing in the Local Scope (inside the function )

def accessGlobalVariable():
    print( global_variable )

# we are allowed to access Global varaibles inside the Global environment as well as inside the Local Environments 
    


# ----------------------------------------------------------------------------------------------------------------------------------------------------




print("""

""")


# Modification of Global Variables:



# Here let us try to Modify the Global variables 

globalVariable = "Original Value"


# modifing within the Global Environment 
global_variable = "modifing within the Global Environment"
    # when we try to update the [ global_variable ] variable from the Global Environement ---> Then try to update the same [ global_variable ] variable from inside the [ localFunction ], variables inside the [ localFunction ] will not update the [ global_variable ], where as variables updated from the global environment will get updated.


print( global_variable )

# modifing within the Local Environment 
def localFunction():
    # when we try to modify the global variable within the Local Environment we directly we cannot able to modify 
      # global_variable = "Modifing within local environment"

    # Correct way to Modify is by using [ global ] keyword


    global global_variable   # This will say python that i am tring to modify variable which is in the Global Environment, if there is a same variable present within the Local environment then the global environment has no scope.
    global_variable = "Modifing within local environment"   # here we Re-assigned the value for the [  global_variable ] which is present in the Global environment

  
    # Error :- [ "global_variable" is assigned before global declaration ]
    # when we try to create and assign the variable within the local scope, Python thinks that the variable is Local scope variable
     # even though when we have variable with the same name in the Global scope, First preference will be given to those variables which are within the scope, when tring to access within the Scope.


print( global_variable )


# Output :-

    # modifing within the Global Environment
    # modifing within the Global Environment



print("""



""")



        # -----------------------------



  # [ Practise 2 ]


globaalVariable_2 = "old values"


def globalVariableUpdate():
    
    global globaalVariable_2
    globaalVariable_2 = "New Value"

# let us access and check which value got printed 
    
print( globaalVariable_2 )

# Ouput :- 
  # old values


print("""


""")


# -----------------------------------------------------------------------------------------------------------------



# 4. Shadowing:

 # showding is a concept how will the Variables checked, Which variables  have more precedent(priority) when the Same variables are declared in the Global and Local Scope. 
 

 # Here we have [ shawdowing_variable ] in the Global scope as well in the Local Scope
  # when we try to print this variable in the global scope, the variable declared in the Global scope will be printed ( i.e, "Showdow Variable" )
  # when we try to print this variable in the Local scope, the variable declared in the Local Scope will be printed ( i.e, 10 )

shawdowing_variable = "Showdow Variable"

def shadowFunction():
    shawdowing_variable = 10

    print( shawdowing_variable ) # Output : 10
     # because it's been called from the Local Scope.


shadowFunction()

print( shawdowing_variable )  # Output : "Showdow Variable"
 # because it's been called from the Global Scope



print("""


""")


# -----------------------------------------------------------------------------------------------------------------



# 5. Avoiding Global Variables:

    # While global variables provide accessibility, excessive use can lead to code that is hard to understand and maintain.
    # Best practice is to limit the use of global variables and prefer passing values as function parameters



print("""


""")


# -----------------------------------------------------------------------------------------------------------------



# 6. Modules and Global Scope:

 # when we create a global Variables and Functions inside a Module, If we load [ import ] these Module code inside some other module using [ from import syntax ], In this case all the modules which we have Imported will be Global.



print("""


""")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------





# 7. Global Scope Pitfalls:

#     Global variables can be modified from anywhere in the program, leading to potential side effects.
#     It's essential to carefully manage and document the use of global variables to avoid unintended consequences.




# -----------------------------------------------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------------------------------------------



# [ Practice 2 ]

# Here we will use different scopes to access the Glboal variables 
 
  # functions
  # loops
  # if....else statements
  # try....expect block
  #



# Functions

# globalVar = "Global Variables"

# # access within the function and modify the variable

def functionGlobalVar():
    # print( globalVar )
    # Error :- [ SyntaxError: name 'globalVar' is used prior to global declaration  ]
     # This Error occurs when we try to use "globalVar" variable which is global variable inside the function before [ global globalVar ] variable which is used to modify the global variable in the Local environment. 

    global globalVar
    globalVar = "Updated Value"


functionGlobalVar()
print( globalVar )

# Output :-

    # Updated Value 




# --------------------------------



# [ if..else ]

global_If_Else = "Global If Else"

# global global_If_Else
 # Error :- [  "global_If_Else" is assigned before global declaration  ]
  # This error message says that we are not allowed to use [ global ] keyword in the Global Scope

if False:
   print("False")
else:
    # global global_If_Else
    # Error :- [  "global_If_Else" is assigned before global declaration  ]
     # This Error occurs when we try to re-assign the values, based on the condition the [if___else] block will be removed and becomes global, which means we are ultimately accessing it from the Global environment
     # The same error occurs when we try to access in the Global environment
    
    # Based on the Condition [ if or elif or else ] block will unwarpped and becomes and all the statements which present inside the Block will be global variables and functions
    global_If_Else = "New Value"


# Learnings :-
     # we are not allowed to use [ global ] keyword inside the Global environment as well as inside the [ if...elif....else ] block.






# --------------------------------


  # [try...except...else...finally ]

globalTryExcept = "Global Try Except Block"

try:

    # global globalTryExcept
        # Error :- [  "globalTryExcept" is assigned before global declaration  ]
         # Even we are not allowed to access the [ global ] keyword from inside the [ try...except..finally ] block 
        # Even [ try...except..finally ] block  does the same thing what [ if...elif...else  ] block do, it will unwrap the block and make it to be a Global.

    globalTryExcept = "Updated values"

except:
    print("Something went wrong")



# Learnings :-
     # we are not allowed to use [ global ] keyword inside the Global environment as well as inside the [try...except...else...finally ] block.



# --------------------------------
    

    # while loop


globalLoop = "Loop Variable"
nums = 10
while nums > 0:
    nums -= 1

    # global globalLoop
    # Error :- [ "globalLoop" is assigned before global declaration  ]
     # Even we are not allowed to use [ global ] keyword inside the [ loops ]

    globalLoop = nums



# Learnings :-
     # we are not allowed to use [ global ] keyword inside the Global environment as well as inside the [ while loop ] block.



# -----------------------------------------------------------------------------------------------------------------------------------------------------
    
# [ global ] keyword can be used only inside the [ Functions ] and not on any other Statements.








































