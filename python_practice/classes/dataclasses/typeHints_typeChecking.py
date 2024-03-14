

from dataclasses import dataclass




# Type Hints 

 # Type hints are setting up datatype for the variables which are present inside the class

@dataclass 
class TypeHints:
    x: int 
    # Here we can see that we set [ interger ] datatype for variable [ x ] 
    y: str 
    # Here we can see that we set [ string ] datatype for variable [ y ]

    # Here we have explicitly set the Datatype for the Variables 
      # By doing this our program code will be clear on what datatype has to be stored and assigned(received)
    
    # When we create an Instance object we do 2 things ?
     # We can either pass the same datatype values for those Variables - This is the Right Apporach 
     # if we failed to pass same datatype  values, but used some other datatype values in such situations python will accept the values it will not throw any errors 
      # When we pass other datatype values python will automatically change the datatype from what was set to what was passed.


# Instance object 
    
    # Instance object which has Same datatype values which was defined
instance_TypeHints_sameValues = TypeHints(100, "hello")
print( instance_TypeHints_sameValues  )

# Output :- 
  # TypeHints(x=100, y='hello')




   # Instance Object which has different datatype values then what was defined 

instance_TypeHints_differentValue = TypeHints(True, None)
print( instance_TypeHints_differentValue )

# Output :-
  # TypeHints(x=True, y=None)

# Even when we passed different Datatype values, we did not got any errors still the value got assigned into the variables.



# Example: Adding type hints
def add_numbers(a: int, b: int) -> int:
    return a + b



# -----------------------------------------------------------------------


# 2. Type Checking with mypy:

 # mypy is a type checking tool which helps checking the code before it is getting executed 

 # After we install `mypy` into our system
 # when we write the code, we we try to pass wrong datatype values for any variables, functions, function parameters arguements, etc. there will be warning displayed in the Code editor with some swirggly lines
  # when we hover over the warning we will get to know what the error which we made realated to datatypes values






















