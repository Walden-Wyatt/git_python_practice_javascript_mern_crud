

# Here we will be Learning about List Datatypes



# There are 2 Syntax to Create a Complex Datatypes

    # List 

    # Constructor Syntax 

    # Literal Syntax 


# Methods and Properties are Classified into 2 Types
    
    # Instance Methods and Properties 
      # This are those methods and properties which we access by Invoking Class Constructor to an Instance Variable


    # Static Methods and Properties
      # This are those methods and properties which we access directly using Class Constructor





# ----------------------------------------------------------------------------------------------------



# List Constructor Syntax 


# list_constructorSyntax = list(1,2,3,4,5)
# Error :-  TypeError: list expected at most 1 argument, got 5 
 # we are suppose to pass only one arguement but we passed more than 1 which we are not allowed to do.


# list_constructorSyntax = list(1)
# Error :- TypeError: 'int' object is not iterable
 # This error occurs because we passed int datatype, we are allowed to pass only iteraable objects such as List, etc


list_constructorSyntax = list([1,2,3,4])

print( list_constructorSyntax )

print( type(list_constructorSyntax) )
# Output :- <class 'list'>

# Using Constructor Syntax we can also use the Built-in methods and properties






print("""



""")


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------



# List Literal Syntax 


list_Type = [ 1, 2, 3, 4, 5, 6 ]

print( list_Type )

# There are 2 ways to Access the Value 

# 1. Index Position


 # Let Us Perform [ CRUD ] Operations

# Here we Accessed the List Value.
index_1 = list_Type[1]
print(index_1)


# Here we override the existing value
list_Type[2] = "New Value"
print( list_Type )


# list_Type[6] = "Adding value"

# Error :- 
 # IndexError: list assignment index out of range
# This Error occurs when we try to add a New Value with the New Index position, which we are not allowed to do, if we want to add a New Value use Built-in Methods.

list_Type[5] = "Adding value"
print(len(list_Type))
print( list_Type )


# Here deleted the value from a Specific Index Position
del list_Type[3]
print( list_Type )


print("""





""")

# --------------------------------------------------------


#. 2. Built-in Methods and Properties 


# CRUD Operation using Built-in Methods

list_built_in_Method = [ 1, 2, 3, 4, 5 ]
print( list_built_in_Method )


list_built_in_Method.append("New Value")
print( list_built_in_Method )


return_index = list_built_in_Method.index(3)
print( return_index )


return_pop = list_built_in_Method.pop()
print( return_pop  )
print( list_built_in_Method )

return_remove = list_built_in_Method.remove(2)
# print( return_remove )
print( list_built_in_Method )


# -----------------------------------------------


 # All List Methods

other_list = [1, 2, 3, 4, 5]
print( other_list )

# Here we can see that we have stored Different Datatypes inside a List

# [append] - this method can be used to insert a Value inside a List
other_list.append("String type")
print( other_list )
other_list.append(False)
print( other_list )


# [ clear() ] - this method will clear the values which inside the list, This will return [None] value
other_list.clear()
print( other_list ) # Output :- [], this is because we have used clear() method which cleared all the values which is inside the list


other_list = [1, 2, 3, 4, 5]

# [ copy() ] = this method will create a New List where all the values will be copied inside the New List
new_list = other_list.copy()
print( other_list )
print( new_list )


other_list = [1, 2, 3, 4, 5, 2, 5, 2, 2, 10, 2]

# [ count() ] - this method will return the Number of Occurance of the value inside the list, count() method will accept 1 arguement that the value which we want to check for
list_count = other_list.count(2)
print( list_count )


other_list = [1, 2, 3, 4, 5, 2, 5, 2, 2, 10, 2]

# [ extend() ] - this method will append the values which we pass inside the list, If you pass a String each and every character will be treated as a Individual Value 
 # the arguement for this method can also be a List Iterable object
other_list.extend("New Extend Value")
# Output :- [1, 2, 3, 4, 5, 2, 5, 2, 2, 10, 2, 'N', 'e', 'w', ' ', 'E', 'x', 't', 'e', 'n', 'd', ' ', 'V', 'a', 'l', 'u', 'e']  
print( other_list )




other_list = [1, 2, 3, 4, 5, 2, 5, 2, 2, 10, 2]


# [ index( search_value, start_value, End_value ) ] - this method will search for the Index Position of the value which we pass, additionally this method also accepts 2 extra arguements where we can specify the start and end index position in a List to Search for the Value.
other_index = other_list.index(5)
# other_index = other_list.index(5, 0, 4)
# Error :- [  ValueError: 5 is not in list  ]
 # This Error occurs if the Value is not Present inside the List.

print( other_index )




other_list = [1, 2, 3, 4, 5, 2, 5, 2, 2, 10, 2]

# [ insert( replace_index_position, New_value ) ] - this method will replace the Existing value with the New value based on the Index position which we give

other_list.insert(2, "Hello")
print( other_list )




other_list = [1, 2, 3, 4, 5, 2, 5, 2, 2, 10, 2]

# [ pop() ] - this method will remove the Value from the List, it will start removing from End of the List.
 # this method will return a value that is a Removed value.
other_pop = other_list.pop()
print( other_pop )
print( other_list )



other_list = [1, 2, 3, 4, 5, 2, 5, 2, 2, 10, 2]

# [ remove( value_toRemove ) ] - this method will remove the value which we specified from the List, this method will not return anything
other_remove = other_list.remove(5)

# Error :- ValueError: list.remove(x): x not in list 
 # This Error occurs because the value which we specified is not present inside the List, if the value specified is not inside the List we might encounter this error, make sure to use the value which is present inside the list.
# other_remove = other_list.remove(11)

print( other_remove )
print( other_list )




other_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# [ reverse() ] - this method will Reverse the values which is inside the List, this method will not take any arguement as well as return any arguement.
other_list.reverse()
print( other_list )



other_list = [ 1, 2, 7, 8, 9, 10, 3, 4, 5, 6, ]

# [ sort() ] - this method will sort the value

other_sort = other_list.sort(key=None, reverse=False )
print( other_sort )
print( other_list )


# When we pass String value which has Alphabetical Characters in such situation, the Values will be sorted based on ASCII Characters
 # It wil check for the each and every sequence of characters based on ascii table, then based on the characters ( i.e, A-Z ) the list gets sorted
other_list = [ "Mango", "Computer", "Phone", "Papaya", "Apple" ]
# other_sort = other_list.sort(key=None, reverse=True )


#     -----

# other_list = [ "Mango", "Computer", "Phone", "Papaya", "Apple", False ]
# # Error :- [   TypeError: '<' not supported between instances of 'int' and 'str'  ]
# other_list = [ "Mango", "Computer", "Phone", "Papaya", "Apple", 1 ]
# # TypeError: '<' not supported between instances of 'bool' and 'str'

#   # The Above 2 error occurs when we try to use Other data types in a List which contains a Value from a Single Datatype which we are not allowed to do.

#     -----

other_list.sort()
print( other_sort )
print( other_list )

# Output :- [  ['Apple', 'Computer', 'Mango', 'Papaya', 'Phone']  ]




# ------------------------------------------------------------------

# Those method which starts and Ends with [ __ ] are the Methods which are inheritated from [ Object ] class



print("""



Practise 2




""")


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------



#  [ Practise 2 ]



list_2 = [ 1,2,3,4,5,6,7,8,9 ]

print( list_2 )


list_2.append("Everyday")
print( list_2 )

list_2_copy = list_2.copy()
print( list_2_copy )

list_count = list_2.count(2)
print( list_count )

list_2.extend([2,True, "Beer"])
print( list_2 )

list_index = list_2.index(2)
print( list_index )

list_insert = list_2.insert(3, "Insterted Value")
print( list_insert )
print( list_2 )


list_pop = list_2.pop()
print( list_pop )
print( list_2 )


list_2.remove("Everyday")
print( list_2 )


list_reverse = list_2.reverse()
print( list_reverse )
print( list_2 )

# for [ sort() ] make sure to use the List of value from a Single Datatype, do not mix match other datatypes.
# list_sort = list_2.sort()
# print( list_sort )






# --------------------------------------------------------------------------------


# List methods and properties remembering

# [a3ce2ip2rs]




# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# Static Methods and Properties 


list_mro = list.mro()
print( list_mro )
# Output :- [<class 'list'>, <class 'object'>]



# list_mro_1 = list.mro( list_2 )
# print( list_mro_1 )
# Error :- [ TypeError: list.mro() takes no arguments (1 given) ]
  # This error occurs when we try to pass arguement for this method, which we are not allowed to do.


# All the Instance Methods and Properties are also Applicable for Static Methods and Properties also





# Accessing Methods from List Constructor Function

# When you use [ List ] Methods from Set Constructor Object, The First Arguement for all the  Methods should be List Instance Object so that the Method will perform appropriate Operations which the List method has to perform.














