

# [ sets ]

# Here we will be Learning about Set Object in Python


# There are 2 Ways to Create a Set Object



# 1. Set Constructor Syntax

# 2. set Literal Syntax



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Set Constructor Syntax

# sets = set(1, 2, 3)
# Error :- TypeError: set expected at most 1 argument, got 3

# sets = set(1)
# Error :- TypeError: 'int' object is not iterable


# set contructor will accept only 1 Arguement and it should be an Iterable Objects such as [ List, tuples, strings, etc].
sets = set([1,2,3,4]) # output :- {1, 2, 3, 4}
sets = set("Hello String")   # output :- {' ', 'l', 't', 'i', 'H', 'n', 'o', 'S', 'g', 'r', 'e'}
sets = set( (1,2,3,4) )   # output :- {1, 2, 3, 4}

print(sets)


print( """





""" )


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Set Literal Syntax


set_literal = { 1, 2, 10, 4, "String", True }

# set_literal = { 1, 2, 10, 4, "String", True, [39, 45] }
# Error :-  set_literal = { 1, 2, 10, 4, "String", True, [39, 45] }
#                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: unhashable type: 'list'

# We are not allowed to pass List Datatype as a Value when we pass we might encouter the above Error.

print( set_literal )


# [ add() ]
 # this method will accept 1 arguement, the arguement value will be added inside the tuple object
 # the element is already present in such situation the new element will not added, because set object will not accept duplicate Element.
set_add = set_literal.add("Add Element")
set_add = set_literal.add(3)
print( set_add )
print( set_literal )

# Output :- {1, 2, 3, 4, 'String', 10, 'Add Element'}
 # here we can see that we added 3 at the end of the Set, but it got inserted at 2nd index position. this is how rearrangement of elements work


# [clear()] -
# this method will clear all the elements which is inside the set object, this method will not return anything.
# set_literal.clear()
print( set_literal )

# copy()
 # Return a shallow copy of a set
set_copy = set_literal.copy()
print( set_copy )


# Original Object value :- {1, 2, 3, 4, 'Add Element', 'String', 10}
# set_copy[7][0] = "Nested Object value"
print(set_copy )





# Shallow Copy
 # Shallow copy will copy will create a New Object, where the New Object will have the values as well as reference of the Nested Objects from Original Object, so whenever we make any changes inside the Copied objects nested object this changes will also be reflected inside the Original Object also.

# Deep Copy 
 # Deep copy will copy will create a New Object, wherethe New Object will have the values but not the reference of the Nested Objects from the Original Object, so whenever we make any changes inside the Copied objects nested object this changes will not be reflected inside the Original Object 




# --------------------------------------------------

# [ difference(iterable_set) ]
 # this method will accept 1 arguement that is the Iterable object specifially "set()" object 

 # this method will compare the Values inside the Arguements set object as well as Original Set object, those values which are Not Similar will be returned where as similar object will not be returned.
# set_difference = set_literal.difference("string") # though it accepts iterable such as String, etc. we are suppose to pass only the Set Object.
set_difference = set_literal.difference([1,2,3,4]) # even if we pass List object, it will work perfectly fine as if we passed a Set object
set_difference = set_literal.difference( {1,2,3,4} )
print( set_difference )

# Output :- {'Add Element', 10, 'String'}




# --------------------------------------------------

# [ difference_update ]
# this method will compare Orignal Set with the set which we passed as an Arguement, those items which are Unique/different will be returned where as similar items will be removed from the Original Set Object

set_difference_update = set_literal.difference_update({1,2,3,4})
print( set_difference_update )

print( set_literal )




# --------------------------------------------------





set_literal = { 1, 2, 10, 4, "String", True }

# [ discard() ]
 # this method will accept 1 arguement that is the Element value which has to be removed from the set, this method will return None
 # if the element present inside the Set object then those element will get removed, if element is not present in such situation the element will not get remove as well as not exceptions will be raised.
 # Remove an element from a set if it is a member. Unlike set.remove(), the discard() method does not raise an exception when an element is missing from the set

set_remove = set_literal.discard(2)
print( set_remove )

set_remove = set_literal.discard(29) # here the element is not present still this method did not raised any error
print( set_literal )



print("""



""")
set_literal = { 1, 2, 10, 4, "String", True }
set_1 = { 1, 2, 3, 4, 5, 6, 7, 8, "String", True }
set_2 = {11, 12, 3, 4, 5, "Set 2", False, 5, 6, 7}
set_3 = { 100, 200, "Wow", 3, 4, 5, 6, 7, 8, 1, 2 }

# [ intersection() ] 
 # this method will compare the Orinal set object with all the Set objects which we passed as an Arguement for [ intersection() ] method, from those object the values which are similar in all the Object will inserted inside the New Set object and the New Set object will be returned.
 # if no values are similar in all the Set Object in such situation [ set() ] constructor will be returned.

set_intersection = set_literal.intersection( set_1, set_2, set_3 ) 
# set_intersection = set_literal.intersection( "string value" )
print( set_literal )
print( set_intersection ) # output :- {4}







# --------------------------------------------------



set_literal = { 1, 2, 10, 4, "String", True }
set_1 = { 1, 2, 3, 4, 5, 6, 7, 8, "String", True }
set_2 = {11, 12, 3, 4, 5, "Set 2", False, 5, 6, 7}
set_3 = { 100, 200, "Wow", 3, 4, 5, 6, 7, 8, 1, 2 }


# [ intersection_update() ] 
 # this method will accept any number of Iterables as an Arguements, this method will compare the Original Set object will set object passed as an Arguement, from those object The Items/elements which are common/same in all the Object will be overriden by the Original Object
 # This method will override the Original set object with the values by the intersected values. 

set_insertion_update = set_literal.intersection_update( set_1, set_2, set_3 )
print( set_insertion_update ) # None
print( set_literal )  # {4}







# --------------------------------------------------


set_literal = { 1, 2, 10, 4, "String", True }
set_1 = { 1, 2, 3, 4, 5, 6, 7, 8, "String", True }
set_2 = {700, 800}


# [isdisjoint( iterable_set )]
 # this method will accept only 1 arguement which is an iterable object set, it will compare both the set object if the set object has similar value in such situation it will return "False", if the set object does not have similar value in such situation this method will return "true".
 # Return True if two sets have a null intersection.

set_isdisjoint = set_literal.isdisjoint( set_1 )
print( set_isdisjoint ) # Output :- False, because 4 is common in both the set

set_isdisjoint = set_literal.isdisjoint( set_2 )
print( set_isdisjoint ) # Output:- True

# Error :- TypeError: set.isdisjoint() takes exactly one argument (2 given)
 # this error occurs which we pass more than 2 arguements for [ isdisjoint() ] method







# --------------------------------------------------


set_literal = { 1,2,3,4 }
set_1 = { 1, 2, 3, 4, 5, 6, 7, 8 }


# [ issubset( iterable_set ) ]
 # this method will compare both the method where original Object will be treated as Child method and arguement object will be treated as Parent object
  # the comparison will be done on the following bases
    # The elements which are present inside the Parent object all the elements should be present inside the child object, the order can be mixed but all the elements must be present, if any element is not present inside the child(original) object in such situation it will return [False] else it will return [ True ]
    # The child object can have more elements/items than parent but all the parent element must be present, but if parent has more element/items than child which means the child is not the subset of parent.

set_issubset = set_literal.issubset( set_1 )
print( set_issubset )  # Output :- True


set_literal = { 1, 2, 3, 4, 5, 6, 7, 8 }
set_1 = { 1,2,3,4 }


# Error :- TypeError: set.issubset() takes exactly one argument (2 given)
 # this error occurs when we try to pass more than 2 arguements for [issubset() ] method, where this method accepts only 1 arguement
# set_issubset = set_literal.issubset( set_1, set_2 )
print( set_issubset )   # Output :- False







# --------------------------------------------------


set_literal = { 1, 2, 3, 4, 5, 6, 7, 8 }
set_1 = { 1,2,3,4 }


# [ issuperset( iterable_set ) ]
 # This method will accept exactly 1 arguement that is an iterable object, here Original object will be the Parent Object, Arguement object will be Child Object
  # it will compare the Parent object with Child object, if the Parent object has all the Elements/items which is present inside the Child object in such situatuion Parent object will be superset of Child Object else not 
  # this method will return Boolean Values True and False.
  # The Parent object can have more elements/items than Child but all the Child element must be present, but if Child has more element/items than child which means the Parent is not the Superset of Child.
  # Report whether this set contains another set.

set_issuperset = set_literal.issuperset(set_1)
print(set_issuperset)   # Output :- True





set_literal = { 1,2,3,4 }
set_1 = { 1, 2, 3, 4, 5, 6, 7, 8 }

set_issuperset = set_literal.issuperset(set_1)
print( set_issuperset)  # Output :- False







# --------------------------------------------------


set_literal = { 1,2,3,4, 1, 2, 3, 4, 5, 6, 7, 8 }

# [pop()]
 # this method will not accept any arguement,This method will remove the element/item from the First from the Original Set Object, The removed element/item will be returned by this method
 # the original set object will have a New Set object after removing the value

set_pop = set_literal.pop()
print( set_pop )  # Output :- 1
set_pop = set_literal.pop()
print( set_pop )  # Output :- 2
set_pop = set_literal.pop()
print( set_pop )  # Output :- 3

print( set_literal )
# Output :- {4, 5, 6, 7, 8}



print("""





""")




# --------------------------------------------------


set_literal = { 1,2,3,4, 1, 2, 3, 4, 5, 6, 7, 8 }

# [ remove( element_value ) ]
 # Remove an element from a set; it must be a member. If the element is not a member, raise a KeyError.
  # this method accept exactly 1 arguement which is the value which has to be removed, if the value is present those value will get removed, if not present we get the error called [ KeyError: 12 ]

# set_remove = set_literal.remove( 12 )   # Error :- KeyError: 12
set_remove = set_literal.remove( 2 )
print( set_remove )
print( set_literal )
 # Output :-  {1, 3, 4, 5, 6, 7, 8}







# --------------------------------------------------


set_literal = { 1,2,3,4, 2, 3, 4, 5, 6, 7, 8 }
set_1 = { 1, 2, 3, 4, 5, 6, 7, 8, "String", True }
# [ symmetric_difference ]
 # Return the symmetric difference of two sets as a new set. (i.e. all elements that are in exactly one of the sets.)
 # This will return a New Set Object which will have Unique values by comparing it with all the Set Objects

set_symmetric_difference = set_literal.symmetric_difference( set_1 )
print( set_symmetric_difference )

# Output :- {'String'}
 # though True is unique in both the set object but still it did not got printed that's because [ True is treated as 1 ]  [ False is treated as 0 ] so if [ 0 or 1 , False or True ] is present in any of the set those both values are considerted to be Similar or same. that is the reason True is not getting printed because 1 is present.


set_literal = { 1,2,3,4, 2, 3, 4, 5, 6, 7, 8 }
set_1 = { 1, 2, 3, 4, 5, 6, 7, 8, "String", True }
set_2 = {11, 12, 3, 4, 5, "Set 2", False, 5, 6, 7}
set_3 = { 100, 200, "Wow", 3, 4, 5, 6, 7, 8, 1, 2 }


# set_symmetric_difference = set_literal.symmetric_difference( set_1, set_2 )
# Error :- TypeError: set.symmetric_difference() takes exactly one argument (2 given)
 # We encounter this error because we are not allowed to pass more than 1 arguement for [symmetric_difference()] method, we have to exactly pass 1 arguement which is Set object
print( set_symmetric_difference )







# --------------------------------------------------


set_literal = { 1,2,3,4, 2, 3, 4, 5, 6, 7, 8 }
set_1 = { 1, 2, 3, 4, 5, 6, 7, 8, "String", True }
set_2 = {11, 12, 3, 4, 5, "Set 2", False, 5, 6, 7}
set_3 = { 100, 200, "Wow", 3, 4, 5, 6, 7, 8, 1, 2 }


# [ union( any_Number_of_set_object ) ]
 # This method will accept more than 1 set objects as an arguement, This method will compare Original set object with Arguement set objects, it will merge all the values removes the duplicates ( multiple occurance of a single value ) and returns a New Set value which which has unique values ( single occurances ). 
 # Return the union of sets as a new set. (i.e. all elements that are in either set.)

set_union = set_literal.union( set_1 )
set_union = set_literal.union( set_1, set_2, set_3 )
print( set_literal )
print( set_union )

# Output :- {False, 1, 2, 3, 4, 5, 6, 7, 8, 200, 11, 12, 100, 'String', 'Wow', 'Set 2'}
 








# --------------------------------------------------


set_literal = { 1,2,3,4, 2, 3, 4, 5, 6, 7, 8 }
set_1 = { 1, 2, 3, 4, 5, 6, 7, 8, "String", True }
set_2 = {11, 12, 3, 4, 5, "Set 2", False, 5, 6, 7}
set_3 = { 100, 200, "Wow", 3, 4, 5, 6, 7, 8, 1, 2 }


# [ update() ]
 # Update a set with the union of itself and others.
 # This Method will accept any number of arguements, It will merge all the values from Original set object as well as Arguements Set objects, it will remove the Duplicate values ( all the multiple occurances ) after merging the values, Now there will be New set with unique values, This New set will be overridden by the Original Set
 # Now the original set will have completely new values.

set_update = set_literal.update( set_1 )
set_update = set_literal.update( set_1, set_2, set_3 )
print( set_update )
print( set_literal )

# Output :- {False, 1, 2, 3, 4, 5, 6, 7, 8, 200, 11, 12, 100, 'String', 'Set 2', 'Wow'}
 



print("""




""")



# --------------------------------------------------



# Other Methods and properties of the Set are From Object Class which is the parent class for all the Built-in and Custom Classes which are present in the program.




# How to Remember Set method and properties 

#  [ a2c3d5ipr2s2u ]


 

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Static Methods and Properties 


# [ mro() ]
 # This method can be used to track how the Modules gets resolved, the Searching order of the Class, it will start from Current Class, then keep moving to the Parent Class it will search till the Ancestor class.
set_mro = set.mro()
print( set_mro )

# Output :-
# [<class 'set'>, <class 'object'>]


# Accessing Methods from Set Constructor Function

# When you use [ Set ] Methods from Set Constructor Object, The First Arguement for all the  Methods should be Set Instance Object so that the Method will perform appropriate Operations which the set method has to perform.





















