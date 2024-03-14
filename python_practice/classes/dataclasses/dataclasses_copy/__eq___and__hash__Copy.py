




# 1. Equality (__eq__):
# 2. Hashing (__hash__):


# Here we will be Learning on how to use [ __eq__ and __hash__() ] dunder methods in python



# 1. Equality (__eq__):
 # when we use Equality (__eq__) operator how the Things has to be compared has to be specified in the [ __eq__() ] method 
 # In Python, the __eq__ method is used to define how instances of a class should be compared for equality. It's a special method that gets called when you use the equality operator (==). By default, if __eq__ is not defined in a class, instances are compared based on their memory address, which means two different instances with the same values are not considered equal.


class Equality:

    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        if isinstance(other, Equality):
            return self.x == other.x # this line which check the condition and return Boolean values 
        return False

# Let us create an Instnce Object for [ Equality ] class :-
    
instanceEquality_1 = Equality(1)
instanceEquality_2 = Equality(1)


print( instanceEquality_1 == instanceEquality_2 )

 # here we use [ == ] equality operator which means [ __eq__() ] dunder method will be invokded 


  # [ def __eq__(self, other): ]
   # Here [ self ] will be associated with [ Left Operands ]
   # [ other ] will be associated with [ Right Operands ]


  # [ if isinstance(other, Equality):
            # return self.x == other.x ]
   # when [__eq__() ] gets invoked the statements which is present it will be executed 
    # [ if isinstance(other, Equality): ] - this will check weather the instance object are created the speciified Class 
     # other - here the instance object will be stored , we have to pass instace - this instance will be present inside [ __eq__(self, other) ]
     # Equality = here the class will be stored , we have to pass Class names 


    #  return False
     # when above condition that is [ if isinstance(other, Equality): fails in such situation this [ return False ] will get executed 




# Here we have Easily costomised the [ __eq__() ] dunder methods.

# When we don't define [ __eq__() ] dunder methods and customise the Equality operators, by default the comparison will be done by using Instance objects Memory Address values 
 # When we create Instance Objects each object will be stored in different Memory Address, Based on it Equality Comparison will happen



print("""



""")





# -------------------------------------------------------------------------------------------------------------------------------------------------




# 2. Hashing (__hash__):

  # The __hash__ method is used to generate a hash value for an object. Hashing is essential for the use of objects in hash-based data structures like dictionaries and sets. Each unique object should have a unique hash value. If __hash__ is not defined, the default hash value is based on the object's memory address.
  # 





class HashClass:

    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __hash__(self):
        return hash((self.x, self.y))
     # This will calculate the Hash values, and those Hash value will be assigned to the specific instance object which we have created using this class 
      # Hash values are like a Address for Each Instance Objects 
     # Hash can be used to compare One Instance object with other Other Instance Objects 
    


# Here let us create Instance Object for [ HashClass ] ?
    
instanceHashClass_1 = HashClass(1, 2)
instanceHashClass_2 = HashClass(1, 2)
instanceHashClass_3 = HashClass(1, 3)


# Here we have Hash all the Instance Objects using [ hash(Instance_Object) ] ?

hash1 = hash(instanceHashClass_1)
print( hash1 )
hash2 = hash(instanceHashClass_2)
print( hash2 )
hash3 = hash(instanceHashClass_3)
print( hash3 )


# Output :-
    # -3550055125485641917
    # -3550055125485641917
    # -1440771752368011620


# When comparing we have to compare with the variables which we have hashed.
print( hash1 == hash2 )
# Output :- True



# what happens when we mix match the value but the total is same ?

    # instanceHashClass_1 = HashClass(1, 2)
    # instanceHashClass_2 = HashClass(3, 0)

   # Output :-
    # False

 # Here total does not matter, The order of arrangements of Values matters, even though total is same but the order is differnt in such situation hash values will be different.



print( hash1 == hash3 )
# False
 # Here we got False because the order and values are different in this instance objects 


# ------------------------------------------------------



# Here let us create Class where we will be passing dictionary as its values  ?


# Create a Class 

class HashClass_Dict:
    def __init__(self, x_dict, y_dict, z ):
        self.x_dict = x_dict
        self.y_dict = y_dict
        self.z = z

    # here let create an [ __hash__() ] and specify how the things has to be hashed 
        
    def __hash__(self):
        return hash((self.x_dict, self.y_dict, self.z))
    

# Let us create Instance object using [ HashClass_Dict ]
    
    # dictionaries 

dict_1 = {"key_1": "value 1", "key_2": 100 }
    
dict_2 = {"key_11": True, "key_22": [1,2] }


instance_HashClass_Dict_1 = HashClass_Dict( dict_1, dict_2, 10 )

instance_HashClass_Dict_2 = HashClass_Dict( dict_2, dict_1, 10 )

instance_HashClass_Dict_3 = HashClass_Dict( dict_1, dict_2, 10 )


# Now let us Hash the Instance Objects using [ hash() ] method 

hash_1 = hash( instance_HashClass_Dict_1 )
hash_2 = hash( instance_HashClass_Dict_2 )
hash_3 = hash( instance_HashClass_Dict_3 )


# Now let us compare [ hash_1, hash_2 and hash_3 ] using Equality operator [ == ]

print( hash_1 == hash_2 )

# Error:- 
  #  eq___and__hash__.py", line 168, in __hash__ 
  #  TypeError: unhashable type: 'dict'

# This error occurs when we try to pass variable which has Dictionary value for [ hash() ] method we will get this error 
  # we are not allowed to use variables which holds un-hashable datatypes such as [ list, set, and dict, Custom Classes without a Properly Defined __hash__ Method:  ].


# ---------------------------


# Hash is nothing but a Sequence of numbers which will be created by python hash algorithms 
 # It is created to Store to Instance Objects, so that when we want to access some Instance object, by using [ hashed ] number we can easily access those objects 
 # Hash is like a Address, it is number which represents specific Instance objects so that we can use those Hashed Instance objects to Compare with other Instance objects try to get Boolean Values.











