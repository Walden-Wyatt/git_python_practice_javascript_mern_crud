

# Closures 

# Closures are Functions inside another function 

# In a Function when we try to access the variables of the Outer Scope inside any Indented scope, This Indented scope can be a [ Nested Function, while loop, for loop, if....else, try...except, etc. ]


# When will Closure gets created ?

 # There is Function called [ hello ], This function has 1 variable called [ x ]
 # inside the function there is Nested Local scope, Let us keep another Function (nested function ) called [ nestedHello ]
 # when the Nested Local scope that is [ nestedHello ] function accesses the variables of [ hello ] which is [ x ], Now Closure gets created 
   # Now "x" variable will be retained so that this value can be accesed inside the [ nestedHello ] function 
    # Think of this like as if you are creating a variable in the Global environment and accessing its values inside the Local environement ( functions, try...expect, loops, etc )

 # Usually what happens in Function ?
  # when we create a Function by passing parameters and setting up local variables, All the parameters and local variables will be within the Local Environment 
  # When we we the function, The statements inside the Function gets executed  and prints the values
  # Finally all the values of parameters and local variables values will be destroyed or garbage Collected. We will not have access to those Parameters and Local variables.
 
 # What happens when we a Outer Function has a Nested Function, where the Nested Function has accessed the variables or parameters of the Outer Function 
   # This same situation is applied for not Nested Functions but also for Indented blocks such as [ while loops, for loops, if.....else statements, try....catch, etc. ]

 # When program sees that a Nested Funtion (inner scope ) accessed the variables and parameters of the Outer Function The Lexical Scoping will be created 
   # Lexical Scoping means a Namespace will be created inside the namespace all the variables and parameters value will be stored, This is nothing but an Object will be wrapped above the InnerFunction but not above the Outer Function
   # [ Namespace ] - namespace is nothing but a Wrapper object, 
    # In closure this wrapper object will get created immediately above the scope which has accessed the Outer scopes variables and parameters, Inside the Namespace all the Outer variables which has been accessed inside the inner scope will be stored.
    # Through Namespace outer Scopes ( outer functions ) variables will not get destroyed it will be retained
     # by namespace all the Inner scopes ( such as Functions, loops, if....else, try...except ) indented blocks can access the Values of Outer Scopes Variables and Parameters.
    # This Namespace will get destroyed or garbage collected once the Inner Function execution is finished.

 # This Same Process will be applicable for any Level of Nested Scopes ( functions, loops ) ?
  # If you have 10 levels of nested scopes where in all the 10 levels have accessed the variables or parameters of its previous or parent level ---> In this case there will be 9 Namespace will get created for every level Unless the 10th level function execution is finished the Namespaces will not be Destroyed, once the 10th level execution is finished in that case all the namespces will get destroyed and finally values gets printed in the Terminal. 



# Important Points :-

 # All the Closure Functions will happen only inside the Functions

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------





# Closure Function Examples 


def outerFunction():
    # Here python might have read these line of code, then these line of code will get destroyed once this line gets Executed.
    outVar = "Outer variable"

    # next this line will be executed 
    def innerFunction():
        
        # here [ outVar ] variable has been defined above, where those line of code finished its execution and destroyed the lines, if that is the case then how can we access the [ outVar ] variable below which has already got destroyed.
         # To Resolve this Problem this is python program called [ Lexical Scoping ]
          # Lexical scoping will create a Wrapper namespace for the inner functions, once it finds that the Outer Functions variable has been Accessed inside the InnerFunction
        print( outVar )


    # Here we have Invoked the [innerFunction()]
    innerFunction()

outerFunction()
# Here we called the function, It will keep reading the each and Every lines of Code inside the Function, once it executes those lines of code will be destroyed



# Output :-
  # Outer Value

# Here we can see that the value which is present in the outer function has been accessed by the innerFunction()
  # when we invoke a Function once the function gets executed the Statements which is present inside the Outer Function will also be Destroyed, if the statement gets then how the variable be present


# How the Above code might Look behind the Scene

def outerFunction():
    outVar = "Outer variable"

 # Assume that there is a Wrapper object which has been created for the below function
  


  # ----------------------------------------------
    
  # [ Namespace Object ]
 # { 
  # Inside the Object all those variable whic have been accessed inside the [ innerFunction() ] will be stored 
  # outVar = "Outer variable"
    def innerFunction():
        print( outVar )
    # }
       
  # ----------------------------------------------
     


    # Now when the outer Function codes gets executed and Destroyed, innerFunction can able to access the outer variables because it has been Stored inside the [ Namespace Object ] 
     # This is called as Closure, This is a Program code which is done by Lexical Scoping 
         # Lexical scoping will itentify weather the outer Functions variable has been accessed inside the Inner Function,if yes creates a Namespace objects, else there will not be any Closure created ( Namespace created ).
    innerFunction()

outerFunction()




print("""



""")


# --------------------------------------------------------------------------------------------------------------------------------------------------------------



# Closure Functions [ Practise 2 ]


def parentFunction():
    parentVariable = "Parent Value"

    def childFunction():
        childVariable = "Child Value"
        # Here we have accessed [ parentVariable] which is outerfunction variable, Now closure gets created by the Python Lexical Scoping
        print( parentVariable )
        print( "Hello Parent Function" )

    # here let us invoke [ childFunction ]
    childFunction()

parentFunction()



# Output :-

  # Parent Value
  # Hello Parent Function




print("""



""")


# --------------------------------------------------------------------------------------------------------------------------------------------------------------




# Closures in [ if...elif....else ] statements 

# Code explanation 

# here we have function defination
def ifelseClosure():
    # here we have variable defined in the Outer Scope, 
     # when function is invoked, this line will be evaluated and executed, after execution this line will be destroyed. 
    outVariable = "Out Variable value"

    
    # even the outer Scope variables got desroyed still we can able to access it in the Inner scope of [ if statement ]
     # Here is where closure gets created by using Lexical Scoping
        
        
    if True:
       # [ Namespace  Object ]
        # Namespace object will get created in the Inner Scope.

    # { 
        # inside this object all the variables which has been accessed from the Outer scope will be stored, by this way we Closure function retains the outer Scope values and makes it avialable to be accessed from inside the Inner Scope.
       
        # outVariable = "Out Variable value"
        
        print( outVariable )
    
    # }


    else:
        print("False Value")

    
  
ifelseClosure()



# Output :-
  
  # Out Variable value





print("""



""")


# --------------------------------------------------------------------------------------------------------------------------------------------------------------




# Closures using [ while loop  ]

# Code Explanation 


# Function defination 
def closureLoop():
    
    # Here we have variable declared in the outer scope 
    outerVariable = "outer Loop Variable"
    num = 0

     # Here we have [ while ] loop which will create a Scope within the loop
    while num <= 5:
        # Here we have accessed [ outerVariable ] which has been defined in the outer scope of the while loop ( parent scope of the current scope, while loop )
          # because we have accessed  the outer Variable in the Inner Scope Closure gets created, where lexical scope will identify that the outer function variable has been accessed inside the inner scope.
        
        # [ Namespace object ]
        # { 
        #  Inside this Namespace object outer variables whill be stored so that even the Outer function execution is completed those variables can be accessed inside the Inner Scope
        
          # outerVariable = "outer Loop Variable"
        
        print( outerVariable )
        num += 1

        # } 


closureLoop()



# Output :-

  # outer Loop Variable
  # outer Loop Variable
  # outer Loop Variable
  # outer Loop Variable
  # outer Loop Variable
  # outer Loop Variable





print("""



""")


# --------------------------------------------------------------------------------------------------------------------------------------------------------------



# Closure using [ try...except...else...finally ] block

  # Even in [ try...except...else...finally ] block closure will get created.


# Code breakdown 

# Here we have function defination 
def tryExceptFunction():
    
    # Here we have variable declared in the Outer scope ( local scope )
    outerFuncion_variable = "Outer Function Value"
    
    # Here we have try block, which will create an Inner scope which will again be a Local Scope 
    try:
        
        # [ Namespace Object ]
        # { 

         # Even though the outer function variables have printed and got destroyed when function started to execute even before it comes to [ try ] block, but still we are able to access the Outer Functions variable value this is done by Lexical scoping. 
        # Here we have accessed the [ outerFuncion_variable ] now closure gets created, because we have accessed outer scope variable
        
        #  outerFuncion_variable = "Outer Function Value"
    
        
        print( outerFuncion_variable )

        # }

    except:
        print( "Try Block has same Error." )


tryExceptFunction()



# Output :-

  # Outer Function Value



# ---------------------------------------------------------------------------------------------------------------------------------------------------


# Here we learnt about closure Functions and how the Closure creates a Namespace Object using Lexical scopings































