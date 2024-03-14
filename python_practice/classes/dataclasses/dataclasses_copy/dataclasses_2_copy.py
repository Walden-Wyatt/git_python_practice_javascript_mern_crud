

# 9. Field Options:

from dataclasses import dataclass, field


# Default

@dataclass
class DefaultClass:
    x: str = field(default="Default value")
    y: str = field(default='Default Y')


# instance object 

instanceDefaultClass = DefaultClass()

print( instanceDefaultClass )

# Output :-
    # DefaultClass(x='Default value', y='Default Y')

# here we did not passed any arguement for [ DefaultClass ] but still we got the outputs, that is because we used Default Values.



print("""




""")



# ------------------------------------------------------------------------------



# 2. default_factory:
  
  # When you want to use Functions return statement as Default Value we have use [default_factory] Field.

from dataclasses import dataclass, field 

def factoryFunction():
    print("Factory Function")
    return 155



@dataclass 
class DefaultFactory:

    # Error :- [ TypeError: 'int' object is not callable ]
     # we get this error because we try to invoke the Function in [ default_factory ], we are not allowed to invoke we have only pass the Reference of the Function without invoking it.
    # g: str = field(default_factory=factoryFunction() )

    g: str = field(default_factory=factoryFunction )

instanceDefaultFactory = DefaultFactory()
print( instanceDefaultFactory )

# Output :-
    # Factory Function     
    # DefaultFactory(g=155)

  # Here we get the above output because we did not passed any arguements which for [ DefaultFactory() ] which meas default_factory arguement will get invoked that is [ factoryFunction() ]


instanceDefaultFactory = DefaultFactory("Abc")
print( instanceDefaultFactory )


# Output :-
    # DefaultFactory(g='Abc')

 # here we just becuase we have passed arguement for [ DefaultFactory()  ] class what ever is present inside the arguement has been displayed. arguement value has been overriden by [ default_factory ] value.

print( instanceDefaultFactory.g )
# Output :- Abc




print("""




""")



# ------------------------------------------------------------------------------



# 3. repr:

# [ repr ] field option can be used to decide which field has to included and excluded in the Printable object


from dataclasses import dataclass, field 

@dataclass 

class ReprClass:
    x: str = field(repr=True)
    y: int = field(repr=False)
    z: bool = field(repr=True)
    w: float = field(repr=False)

instance_ReprClass = ReprClass("x value", 11, True, 112.224 )

print( instance_ReprClass )


# Output :-
 # ReprClass(x='x value', z=True)

# Here if you see that only [ x and z ] variables are present inside Printable Object, where are [ y and w ] are not present inside the Printable objects
 # This is because when we use [ repr=False ] those variables will not be included in the Printable objects when we try to print the Instance Object.






print("""




""")



# ------------------------------------------------------------------------------


# 4. compare:

 # During comparison what happens ?
 # 1st - Python will check for the 


@dataclass
class Compare_1:
    x: int = field(compare=True)
    y: int = field(compare=False)


@dataclass
class Compare_2:
    x: int = field(compare=True)
    w: int = field(compare=False)

instance_Compare_1 = Compare_1( 11, 12)
instance_Compare_2 = Compare_2( 11, 12)


print( instance_Compare_1 == instance_Compare_2 )


# If the Instance Objects are of completely different Classes which means The Reference of the Objects will be Different and when we use it for comparison, python will return false

 # When creating an Instance Object make sure to create the Instance object from 1 single class


# ------------------------------------------


@dataclass 
class CompareClass:
    x: int = field(compare=True)
    y: int = field(compare=False)


instance_CompareClass_1 = CompareClass( 11, 12 )
instance_CompareClass_2 = CompareClass( 11, 12 )

print( instance_CompareClass_1 == instance_CompareClass_2 )

# Output :- True
 # Because the values for both variables are same, that is variable which has [ compare=True and compare=False ].


# ---


# Now let us try to change the values for variable which has [ compare=False ]

instance_CompareClass_1 = CompareClass(11,12)
instance_CompareClass_2 = CompareClass(11,13)


print( instance_CompareClass_1 == instance_CompareClass_2 )

# Output :- True
  # it returns True that is because the variables for which we had changed the values has [ compare=False ] which means this variables will not be taken for Comparisons.
  # Because those variables are not compared even though we changed its values still python returns True.


# ---


# Now let us try to change the values for variable which has [ compare=False ]

instance_CompareClass_1 = CompareClass(11,12)
instance_CompareClass_2 = CompareClass(112,13)


print( instance_CompareClass_1 == instance_CompareClass_2 )


# Output :- False
 # Now if you see that python returns False, this is because the variable has [compare=True] has a different values
 # instance of [ instance_CompareClass_1 and instance_CompareClass_2 ] --> variables which has [compare=True] has a Different values, which means when we compare it will return False
  # Comparison Operator will only check for values and variable names 


# ------

# what suppose if the variable names are different but the values are same.
  # This can happen only in 1 situation that is when both the instance object of the Class are created with 2 different classe.
  # When the Instance objects are created with different class obiviously they are not Equal, comparison operator will return False.




print("""



""")



# -----------------


 # what suppose if all the Variables has [ compare=False ]

@dataclass
class CompareClassFalse:
    x: int = field(compare=False) 
    y: str = field(compare=False)


instance_CompareClassFalse_1 = CompareClassFalse(112, "string")
instance_CompareClassFalse_2 = CompareClassFalse(33, "Hello")

print( instance_CompareClassFalse_1 == instance_CompareClassFalse_2 )


# Output :-
  # True


# When all the variables inside the dataclass has [ compare=False ] in such situations the instance object which we create Even though the Instance object has differen values for all the Variables python will return [True] when it is compared
 # When there is no variable which has [compare=True] inside the class which means, python assumes all the variables are same there is no need to compare so it returns [True].

 # when there is atleast one variable which has [compare=True] inside the class  in such situation python will check the values of those Variables and return [ True or False ].

# When comparing we have to compare only the instance not the variables which are inside the instance Object 



print("""




""")

# --------------------------------




# Ordering Comparison (__lt__, __le__, __gt__, __ge__):

 # What happens in Ordering Comparison 

@dataclass
class OrderingComparison:
    x: int 
    y: int 


instance_OrderingComparison_1 = OrderingComparison(11, 12)
instance_OrderingComparison_2 = OrderingComparison(12, 13)



# # 11 < 12 
# print( instance_OrderingComparison_1 >= instance_OrderingComparison_2)
# # Output :- True


# # 12 > 13
# print(instance_OrderingComparison_1 <= instance_OrderingComparison_2 )





























