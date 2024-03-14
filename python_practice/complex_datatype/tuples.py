


# Tuples 

 # Tuples is a Datatype where Duplicate Values will not be Stored


# There are 2 ways to create a Tuples Datatype 

# 1. Constructor Syntax

# 2. Literal Syntax



# Methods and Properties are Classified into 2 Types
    
    # Instance Methods and Properties 
      # This are those methods and properties which we access by Invoking Class Constructor to an Instance Variable
      # For all the Instance Methods we will not be passing the Instance object of that specific datatype, instaed we will directly pass the Necessary arguement for that Specific methods.


    # Static Methods and Properties
      # This are those methods and properties which we access directly using Class Constructor

      # To access the Values of a Methods or Property
      # For all the Static Methods we will pass The instance object of that specific datatype,from 2nd arguement we will be passing other necessary arguements for that specific methods




# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# 1. Constructor Syntax 


tuple_constructor = tuple([1,2,3,4,5])
print( tuple_constructor )

tuple_constructor = tuple(("a", "b", "c", "d", "e"))
print( tuple_constructor )





# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# Tuple Literal Syntax






tuples = (1, 2, 3, 4 )
print( tuples )

tuples = (1,2,3,4, 10, 2, 3, 11, 12, 8, 9)
print( tuples )
# Output :- (1, 2, 3, 4, 10, 2, 3, 11, 12, 8, 9)
 # Here we can see that Duplicate values are removed from the tuples.



# There are 2 ways in which we perform CRUD operation in Tuples


# 1. Index Position

tupless = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print( tupless )

tupless_indexPosition = tupless[1]
print( tupless_indexPosition )
# Output :- 2


# tuples[3] = "Replaced Value"
# Error :- TypeError: 'tuple' object does not support item assignment
 # This Error occurs when we try to Assign a Value for a variable using Index Position
print( tupless )


tupless_indexPosition




# ---------------------------------------------------------------------------------------



# 2. Built-in Methods 



tuple_builtIn_method = (1,2,3,4,5,6,2, 3, 2)

print( tuple_builtIn_method )


# [ count(value) ] - this method will return the number of occurance of the Value which we have passed as an Arguement
tuple_count =  tuple_builtIn_method.count(2)
print( tuple_count )


# [ index() ] = this method will return the index value of the Arguement which we pass
tuple_index = tuple_builtIn_method.index(3)

# Error :- ValueError: tuple.index(x): x not in tuple
 # This error occurs when we pass the value which is not inside the Tuples
# tuple_index = tuple_builtIn_method.index( 10 )
print( tuple_index )



print("""




Practise 2




""")


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# [ Practise 2 ]


# Tuple Constructor Syntax 

tuples_2 = tuple("Hello man")
# Even String is an Iterable Object
# Output :- ('H', 'e', 'l', 'l', 'o', ' ', 'm', 'a', 'n')

print( tuples_2 )



# ---------------------------------------------------------------------------


# Tuple Literal Syntax 


tuple_literalSyntax = (1,2,3,4,5,5,4,3,2,1)

print( tuple_literalSyntax )

tuple_count = tuple_literalSyntax.count(3)
print( tuple_count )


tuple_index = tuple_literalSyntax.index(4)
print( tuple_index )





# -----------------------------------------------------------------------------


# Sometime elements inside the Tuple gets rearragned


tuple_rearranged = (1, 2, 3, True, "String", 4, 5)

print( tuple_rearranged )




# -----------------------------------------------


# Tuple remembering methods and properties 

# [ ci ]



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Static Methods and Properties

 # For all Static Methods we will be passing the Instance Object as a First Arguement then we will be passing other necessary arguements


tuple_instance = (1,2,3,1,2,5)

# [ count( instance_object, value) ]
 # this method will accept 2 arguement, this method will return the number of occurance of the Value which we passed as a 2nd arguement.
tuple_count = tuple.count(tuple_instance, 1)
# tuple_count = tuple.count(1)  # Error :- TypeError: descriptor 'count' for 'tuple' objects doesn't apply to a 'int' object

print( tuple_count ) 





# -------------------------------------------------------------------

# [ index( instance_object, value, start_position_to_search, stop_positon_of_search ) ]
 # this method accepts 4 argements based on the arguement values this method will return the index position of the Value which we have passed.

tuple_index = tuple.index(tuple_instance, 2)
print( tuple_index )


# [ mro() ]
 # this method will not accept any arguement, this method will return a List in which we can see how the Method got resolved
  # Mudule resolution means python will search for the Specific method starting from the Derived( child ) class to Base ( parent ) class ---> the End class is Object Class.
tuple_mro = tuple.mro()
print( tuple_mro  )




# Accessing Methods from Tuples Constructor Function

# When you use [ Tuples ] Methods from Set Constructor Object, The First Arguement for all the  Methods should be Tuples Instance Object so that the Method will perform appropriate Operations which the tuple method has to perform.



















