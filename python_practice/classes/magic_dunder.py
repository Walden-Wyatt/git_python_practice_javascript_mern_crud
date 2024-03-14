

# Magic or Dunder Methods 

 # Magic or Dunder Methods are those methods which are Present inside the [ Object ] class which is base or parent class for all the custom classes which we create inside the File

 # Dunder methods has to be used inside the class

 # Dunder methods are called Implicitly we don't need to call Explicily 

 # Dunder methods are set of methods which will will associated with some Built-in funcions and Symbols, if we want to make use of those Dunder methods by our custom Class to displaye some custom value we can use Dunder Methods.

# Make use of Below methods 

 # 1. __str__
 # 2. __len__
 # 3. __add__
 # 4. __sub__
 # 5. __mul__
 # 6. __div__
 # 7. __Mod__


from collections.abc import Iterable
from types import UnionType
from typing import Any


print( object.mro() )

# for x in dir(object):
#     print(x)


class DunderMethods:

    def __init__(self):
        self.attribute_1 = 10
    
    classVariable_1 = 20

    def __str__(self):
        print("String Dunder Method")
        # return ["str" ]
         # Error :- [ TypeError: __str__ returned non-string (type NoneType) ]
          # we get this error when we do not return string value for [ __str__() ] method, if we to return value which is of other datatype or no return statement at all.
        return "String Dunder Method"



instace_Dundermetods = DunderMethods()

print( instace_Dundermetods )




# -----------------------------------------------------------------


# Class which will have all some of the Dunder Methods

class SomeDunderMethods:

    # [ __init__() ] is also a Dunder Method
    def __init__(self):
        self.num_1 = 10

        # return "Init Dunder Methods"
        # Error:- [ TypeError: __init__() should return None, not 'str' ]
         # we get this error when we try to [ return ] same value other than [ None ] datatype or no return statement at all ( if there is no return statement which means return value will be none by default )
         # we are not suppose to return any value from [__init__() ] method other than [ none ]
        
        return None
    


    # what has to be done when an addition operator is used with the instance object this class in either side of the Operand or both the side



# print( len(10) )
# Error :- TypeError: object of type 'int' has no len()
 # this error occurs when we try to pass interger as an Arguement for [ len() ] method, becuase [ int ] Class will not have Dunder method called [len()] 
 # for [ len() ] method we have to pass only Iterable Objects such as List, tuples, strings, etc, we are not allowed to pass other datatype values.


print("""

""")


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------




class Dundermethod:

    # when we invoke [ Dundermethod ] class [__init__()] method will be called behind the scene, This method can be used to create a Constructor.
    def __init__(self):
        print("Dundermethod Constructor")

     # When instance of this class is called suffixing () parenthesis at the end __call__() will get called behind the scene by python
    def __call__(self):
        print("When instance of this class is called suffixing () parenthesis at the end __call__() will get called behind the scene by python")

    # usually when we try to print Instance object we will get the Address where this Instance Object have been stored, by [__str__()] method we can override it and try to display some Custom values.
    def __str__(self):
        print("String Dunder Method")

    # def __delattr__(self):
    #     print("Delete Dunder Method")

    def __del__(self):
        print("Hello, Delete Dunder Method")

    def __add__(self):
        print("Add Dunder Method.")

    def __eq__(self, __value: object) :
        print("Equal to Dunder Method")

    def __ne__(self,  __value: object) :
        print("Not Equal to Dunder Method")


    def customMethod(self):
        print("Custom Method")

    customClassVariable = "Custom Class Variable"




# Instance Object for [ Dundermethod ]
        
instance_Dundermethod = Dundermethod() # Ouput : [ Dundermethod Constructor ], ( __init__() ) method got invoked behind the scene by python

instance_Dundermethod()
# Output :- When instance of this class is called suffixing () parenthesis at the end __call__() will get called behind the scene by python
 # usually when we invoke an Instance Object we will get Error, Now by using [ __call__() ] method, we have overridden the error message and displayed some costom string value.


# Here let us print [ instance_Dundermethod ]
print( instace_Dundermetods )

# Output :- [  String Dunder Method ]
 # now the Address of instance object have been overridden by the custom String value that is [ String Dunder Method ]



# let us try to delete some property or method form [ instance_Dundermethod ]

# del instance_Dundermethod
# Output :- Hello, Delete Dunder Method
 # here we can see that we got this output when we try to use [del] keyword for the [ instance_Dundermethod ] which is an instance of [ Dundermethod ] class


# print( instance_Dundermethod + 10 )


# Equal to dunder method
# print( instance_Dundermethod == "abc" )
# Output :- [ Equal to Dunder Method ]
 # when we use equal to operator [ == ], where either or both the operand has instance object of the Class which has Dunder method  

# When we try to get values from the Dunder Method, make sure you use only the Instance Object, do not try to call any Properties or Methods from the instance object

print( instance_Dundermethod.customClassVariable == "abc" )
# Output :- # False
 # here we tried to call the [ customClassVariable ] property that is the reason we are not getting equal to dunder method values, because at the [ instance_Dundermethod.customClassVariable ] reference position string value will be present which means there is a String value but there is no reference of [ instance_Dundermethod ] object.
 # when we try to access some value from an Object, the that place where we accessed the value whatever the Property or method returns that datatype value will be stored not the reference of the Object from which we accessed
 # in [ instance_Dundermethod.customClassVariable ] place String datatype Value will be stored.



# Let us try to use [ Not equal to Operaor ]
print( instance_Dundermethod != 1234 )
# Output :-
    # Not Equal to Dunder Method
    # None

# Here we used not equal to operator we got return value which we have used inside [ __ne__() ] dunder method.


print("""

Accessing Dunder Methods directly

""")


# ----------------------------------------------------------

# Accessing Dunder Methods Directly from the Instance Object

instance_Dundermethod.__init__()
instance_Dundermethod.__call__()
instace_Dundermetods.__str__()
instance_Dundermethod.__del__()
instance_Dundermethod.__add__()
instance_Dundermethod.__eq__({"key": "value"})
# Error :- [ TypeError: Dundermethod.__ne__() missing 1 required positional argument: '_Dundermethod__value' ]
 # we get this error when we do not pass required positional arguements which we are suppose to pass
instance_Dundermethod.__ne__("random value")



# Output :-

# Dundermethod Constructor
# When instance of this class is called suffixing () parenthesis at the end __call__() will get called behind the scene by python
# String Dunder Method
# Hello, Delete Dunder Method
# Add Dunder Method.
# Equal to Dunder Method
# Not Equal to Dunder Method



# Learnings :- 
 # From here we learnt that we are allowed to access the Dunder Methods directly from the instance Objects
 # while accessing we have make sure we are passing proper positional arguements 






print("""



""")


# ----------------------------------------------------------------------------------------------------------------------------------------------------------




# By using Dunder Method we can have complete control over the Program
# We can even Modify the Implicit Operations of a Class Instance Object by overriding the Default Operations


# [ Practise 2 ]

class OtherDunderMethods:

    def __call__(self):
        print("Call Dunder Method")

    def __dir__(self):
        print("Directory Dunder Method")

    def __or__(self, __value: Any) :
        print("Or Dunder Method")

    def __new__(cls):
        print("New Dunder Method")


    
instance_OtherDunderMethods = OtherDunderMethods()

# dir(instance_OtherDunderMethods)

# print( instance_OtherDunderMethods() )
# Output:  New Dunder Method
# when we use [ __new__() ] dunder method and try to call by using parenthsis we will get the below error 
  # Error :- [  TypeError: 'NoneType' object is not callable ]


print( instance_OtherDunderMethods )
# Output:  New Dunder Method

print( instance_OtherDunderMethods or "abc" )

# --------------------------------------------------
























