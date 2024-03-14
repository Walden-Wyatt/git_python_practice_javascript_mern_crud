


# Dataclasses Behind the Scenes :-


# How Dataclasses will be Behind the Scenes ?


# let us create a Dataclasses 

from dataclasses import dataclass
from typing import Any

@dataclass
class Dataclass_behindTheScenes:
    x: str
    y: int


instance_Object = Dataclass_behindTheScenes("X Value", 112)

print( instance_Object )


# Output :-

    # Dataclass_behindTheScenes(x='X Value', y=112)




print("""




""")



# here we have How the Dataclasses Gets created Behind the Scenes
 # Here we have Demonstrated using Regular Classes.

# ---------------

class Dataclass_behindTheScenes:

    def __init__(self, x:str, y:int ):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Dataclass_behindTheScenes(x='{self.x}', y={self.y})"
    
    def __eq__(self, other):
        # if isinstance(other, Dataclass_behindTheScenes):
            # return self.x == other.x and self.y == other.y
        # return False
        print("hello")
    
        # return "Helo"
         # when we use "return" statement the value which we give inside the 'return' will get invoked automatically when we create the Constructor and assign it to a Instance Objects.


    def __hash__(self):
        return hash((self.x, self.y))



instance_Dataclass_behindTheScenes = Dataclass_behindTheScenes("x value", 333)

print( instance_Dataclass_behindTheScenes )


# Let us use Equality operator :-

instance_Dataclass_behindTheScenes_2 = Dataclass_behindTheScenes("y value", 221555)

print( instance_Dataclass_behindTheScenes == instance_Dataclass_behindTheScenes_2 )


# Output :-

    # Dataclass_behindTheScenes(x='x value', y=333)
    # False




print("""



""")




# ----------------------------------------------------------------------------------------------------------------------------------



# How to use Other Dunder Methods inside the Dataclasses.


@dataclass
class OtherDunderMethods:
    x: str 
    y: int

 # Here we have used [ __str__() ] dunder method to customize the Dunder method classes.
    def __str__(self) :
        return "Hello String"
    
    # here we used [ __call__() ] dunder method And learnt how to customize the [ @dataclass ]
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return "This is a Call Method."
    
    # we can even customize those dunder methods which are automatically created 
    def __eq__(self, other):
        return "Customized eq dunder method."


instance_OtherDunderMethods = OtherDunderMethods("String", 113344)

# [ __call__() ] method gets invoked when we try to use parenthsis and invoke the Instance object.
print( instance_OtherDunderMethods() )

# Output :- 
    # This is a Call Method.


# [ __eq__() ]
print( instance_OtherDunderMethods == instance_OtherDunderMethods)


# Output :-
    # Customized eq dunder method.


























