

# Implicit Multiplication


 # Here we will be using various combinations on how Multiplication Operator works

# String 
# Number 
# Boolean 
# None 
# List 
# Tuple
# Set
# Dictionary 



# How Python checks weather the syntax is a Dictionary, set, tuple, list etc

 # C++ will use Regular expression and check for following things, why C++ because python is a language which has been written C++

 # For [ List ] :- 
  # it will check weather the start of sequence of character has Opening Square brackets " [ "
  # next it will check the sequence of character has values which is of any datatype, 
  # when python come across comma (,) it will treat the datatype as a Left and Right operand datatype values, all the command seperated values will be treated as a Single values which will be stored in appropriate Index Position.
  # Finally it will also check weather the sequece of Character has closing square brackets "]"

# For Other other programms such as [ Distionary, Tuple, Set, etc ]
# The same process will also be applicable for [ Datatypes, Conditional statements, Loopings, Exception handling statements, etc ].




# -------------------------------------------------------------------------------------------------------------------------------------------------------




# String with other operands using Multiplication Operator




# print( "string" * "string" )
# Error :- TypeError: can't multiply sequence by non-int of type 'str'
 # This error message clearly says that we can't multiply any sequence which does not have Number datatype as operands
# we are not allowed to use [ string and string ] as an operand for Multiplication operator



print( "string " * 10 )
# Output :-
# string string string string string string string string string string
 # When we use [ string and number ] as a Operand, string gets multiplied with number and prints the String value number of time which we passed with number 



print( "string" * True ) # // equal to [ print( "string" * 1 ) ]
# Output :-
# string
 # Behind the scene python will convert boolean values into Number, [ Boolean True = 1 ] [ Boolean False = 0 ]
 # we are allowed to use [ String and Boolean ] as a Operands for Multiplication operator



# print( "string" * None )
# Error :- TypeError: can't multiply sequence by non-int of type 'NoneType'
# we are not allowed to use [ String and None ] as a Operands for Multiplication operator



# print( "String" * [10] )
# Error :-TypeError: can't multiply sequence by non-int of type 'list'
# we are not allowed to use [ String and List ] as a Operands for Multiplication operator



print( "string " * (10) )
# Output :- string string string string string string string string string string
# here we used Tuple syntax but it is Grouping Operator,because it does not have comma or other datatypes 



# print( "string" * (10,) )
# Error :- TypeError: can't multiply sequence by non-int of type 'tuple'
# we are not allowed to use [ String and Tuple ] as a Operands for Multiplication operator



# print( "string" * {10} )
# Error :- TypeError: can't multiply sequence by non-int of type 'set'
# we are not allowed to use [ String and Set ] as a Operands for Multiplication operator



# print( "string" * {"key": 'Dictionary value'} )
# TypeError: can't multiply sequence by non-int of type 'dict'
# we are not allowed to use [ String and Dict ] as a Operands for Multiplication operator



print("""



""")



# -------------------------------------------------------------------------------------------------------------------------------------------------------





# Number with other operands using Multiplication Operator


print( "string " * 10 )
# Output :-
# string string string string string string string string string string
 # When we use [ string and number ] as a Operand, string gets multiplied with number and prints the String value number of time which we passed with number 



print( 10 * 10 )
# Output :- 100
 # we are allowed to use [ Number and Number ] as a Operands for Multiplication operator



print( 10 * True )
# Output :- 10
 # we are allowed to use [ Number and Boolean ] as a Operands for Multiplication operator



# print( 10 * None )
# Error:- TypeError: unsupported operand type(s) for *: 'int' and 'NoneType
# we are not allowed to use [ Number and None ] as a Operands for Multiplication operator



print( 10 * [10] )
# Output :- [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

print( 10 * [10] )
# Output :- [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

print( 10 * [10, 20, True] )
# [10, 20, True, 10, 20, True, 10, 20, True, 10, 20, True, 10, 20, True, 10, 20, True, 10, 20, True, 10, 20, True, 10, 20, True, 10, 20, True]

print( 10 * [10, 20, True, "string"] )
# Output :- [10, 20, True, 'string', 10, 20, True, 'string', 10, 20, True, 'string', 10, 20, True, 'string', 10, 20, True, 'string', 10, 20, True, 'string', 10, 20, True, 'string', 10, 20, True, 'string', 10, 20, True, 'string', 10, 20, True, 'string']

print( 10 * [10, 20, True, "string",{"key":"value"}] )
# Output :- [10, 20, True, 'string', {'key': 'value'}, 10, 20, True, 'string', {'key': 'value'}, 10, 20, True, 'string', {'key': 'value'}, 10, 20, True, 'string', {'key': 'value'}, 10, 20, True, 'string', {'key': 'value'}, 10, 20, True, 'string', {'key': 'value'}, 10, 20, True, 'string', {'key': 'value'}, 10, 20, True, 'string', {'key': 'value'}, 10, 20, True, 'string', {'key': 'value'}, 10, 20, True, 'string', {'key': 'value'}]

print( 10 * [("hello",)] )
# [('hello',), ('hello',), ('hello',), ('hello',), ('hello',), ('hello',), ('hello',), ('hello',), ('hello',), ('hello',)]

# What happens when we use Number with List of any values as an Operands ?
 # Multiplication operator will multiply all the values which is present inside the List based on the specified number value, 
  # Finally it appends the Multiplied values inside the Same list or we can also call in the below manner 
    # Python will multiply all the values which is present inside the List based on the specified number value, then creates New List which will stored Multiple occurrences of the List values in the exact sequences of the Occurencess of Valuse



print( 5 * (10,) )
# Output :- (10, 10, 10, 10, 10)
print( 5 * (10, "string", {"key": "values"}) )
# Output:- (10, 'string', {'key': 'values'}, 10, 'string', {'key': 'values'}, 10, 'string', {'key': 'values'}, 10, 'string', {'key': 'values'}, 10, 'string', {'key': 'values'})


# What happens when we use Number with Tuples of any values as an Operands ?
 # Multiplication operator will multiply all the values which is present inside the Tuples based on the specified number value, 
  # Finally it appends the Multiplied values inside the Same Tuples or we can also call in the below manner 
   # Python will multiply all the values which is present inside the Tuples based on the specified number value, then creates New Tuples which will stored Multiple occurrences of the Tuples values in the exact sequences of the Occurencess of Valuse


# print( 5 * {"set value"} )
# Error :- TypeError: unsupported operand type(s) for *: 'int' and 'set'
# we are not allowed to use [ Number and Set ] as a Operands for Multiplication operator, even if a set object has Single value 


# print( 5 * {"key": "values"} )
# Error :- TypeError: unsupported operand type(s) for *: 'int' and 'dict
# we are not allowed to use [ Number and Dictionary ] as a Operands for Multiplication operator, even if a Dictionary object has Single value 


# Learnings :-
 # if you clearly observe that Multiplication operator can be use in all the Sequence Datatypes such as [ String, Lists, Tuples, etc] as well as Number datatypes.




print("""



""")





# -------------------------------------------------------------------------------------------------------------------------------------------------------



# Boolean with other operands using Multiplication Operator

 # Remember Multiplication operators can be used with all the Sequence Datatypes


print( True * "string" )
# Output :- string
 # Behind the scene python will convert Boolean datatypes to Number, [ Boolean True = 1 ] [ Boolean Fals = 0 ]
print( False * "String" )  # // 0 * "String"
# Ouptut :- empty string 
 # we are allowed to use [ Boolean and String ] as a Operands for Multiplication operator



print( True * 10 ) # // 10
# Output :- 10
 # we are allowed to use [ Boolean and Number ] as a Operands for Multiplication operator



print( True * True ) # 1 
# Output :- 1
print( True * False )  # 0
# Output :- 0
 # we are allowed to use [ Boolean and Boolean ] as a Operands for Multiplication operator



# print( True * None )
# Error :- TypeError: unsupported operand type(s) for *: 'bool' and 'NoneType'
# we are not allowed to use [ Boolean and None ] as a Operands for Multiplication operator



print( True * [10] )  # [10] :-  print( 1 * [10] )
# Output :- [10]
print( True * [ "string", 112, True, {"Key": "Value"}, ["list values", 22] ] )
#  Output :- ['string', 112, True, {'Key': 'Value'}, ['list values', 22]]
 # behind the True will be converted to 1 and multiplies and Prints the Number of occurances
 # we are allowed to use [ Boolean and List ] as a Operands for Multiplication operator, List can have any Datatype values and any number of values



print( True * (10, "String") )
# Output :- (10, 'String')
 # we are allowed to use [ Boolean and Tuple ] as a Operands for Multiplication operator, Tuple can have any Datatype values and any number of values



# print( True * {"set value"} )
# Error :- TypeError: unsupported operand type(s) for *: 'bool' and 'set'
# we are not allowed to use [ Boolean and Set ] as a Operands for Multiplication operator, even if set has single value or multiple values



# print( True * {"key": "Values"} )
# Error :- TypeError: unsupported operand type(s) for *: 'bool' and 'dict'
# we are not allowed to use [ Boolean and Dictionary ] as a Operands for Multiplication operator, even if Dictionary has single value or multiple values




print("""



""")





# -------------------------------------------------------------------------------------------------------------------------------------------------------



# None with other operands using Multiplication Operator

 # None Datatype cannot be used with Multiplication operator, if we use we  will get errors. 



# print( "string" * None )
# Error :- TypeError: can't multiply sequence by non-int of type 'NoneType'
# we are not allowed to use [ String and None ] as a Operands for Multiplication operator



# print( 10 * None )
# Error:- TypeError: unsupported operand type(s) for *: 'int' and 'NoneType
# we are not allowed to use [ Number and None ] as a Operands for Multiplication operator



# print( True * None )
# Error :- TypeError: unsupported operand type(s) for *: 'bool' and 'NoneType'
# we are not allowed to use [ Boolean and None ] as a Operands for Multiplication operator



# print( None * None )
# Error:- TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'
# we are not allowed to use [ None and None ] as a Operands for Multiplication operator


# print( None * [3] )
# Error :- TypeError: can't multiply sequence by non-int of type 'NoneType'
# we are not allowed to use [ None and List ] as a Operands for Multiplication operator, even if the list has single element or multiple elements


# print( None * (2,) )
# Error : TypeError: can't multiply sequence by non-int of type 'NoneType'
 # we are not allowed to use [ None and Tuple ] as a Operands for Multiplication operator, even if the tuple has single element or multiple elements


# print( None * {"set value"} )
# Error :- TypeError: unsupported operand type(s) for *: 'NoneType' and 'set'
 # we are not allowed to use [ None and Set ] as a Operands for Multiplication operator, even if the Dictionary has single element or multiple elements


# print( None * {"key": "Value" } )
# Error :- TypeError: unsupported operand type(s) for *: 'NoneType' and 'dict'
 # we are not allowed to use [ None and Dictionary ] as a Operands for Multiplication operator, even if the Dictionary has single element or multiple elements




print("""



""")






# -------------------------------------------------------------------------------------------------------------------------------------------------------




 
# List with other operands using Multiplication Operator 




# print( "String" * [10] )
# Error :- TypeError: can't multiply sequence by non-int of type 'list'
# we are not allowed to use [ String and List ] as a Operands for Multiplication operator



print( 10 * [10] )
# Output :- [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

print( 10 * [10] )
# Output :- [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

print( 10 * [10, 20, True] )
# [10, 20, True, 10, 20, True, 10, 20, True, 10, 20, True, 10, 20, True, 10, 20, True, 10, 20, True, 10, 20, True, 10, 20, True, 10, 20, True]

print( 10 * [10, 20, True, "string"] )
# Output :- [10, 20, True, 'string', 10, 20, True, 'string', 10, 20, True, 'string', 10, 20, True, 'string', 10, 20, True, 'string', 10, 20, True, 'string', 10, 20, True, 'string', 10, 20, True, 'string', 10, 20, True, 'string', 10, 20, True, 'string']

print( 10 * [10, 20, True, "string",{"key":"value"}] )
# Output :- [10, 20, True, 'string', {'key': 'value'}, 10, 20, True, 'string', {'key': 'value'}, 10, 20, True, 'string', {'key': 'value'}, 10, 20, True, 'string', {'key': 'value'}, 10, 20, True, 'string', {'key': 'value'}, 10, 20, True, 'string', {'key': 'value'}, 10, 20, True, 'string', {'key': 'value'}, 10, 20, True, 'string', {'key': 'value'}, 10, 20, True, 'string', {'key': 'value'}, 10, 20, True, 'string', {'key': 'value'}]

print( 10 * [("hello",)] )
# [('hello',), ('hello',), ('hello',), ('hello',), ('hello',), ('hello',), ('hello',), ('hello',), ('hello',), ('hello',)]

# What happens when we use Number with List of any values as an Operands ?
 # Multiplication operator will multiply all the values which is present inside the List based on the specified number value, 
  # Finally it appends the Multiplied values inside the Same list or we can also call in the below manner 
    # Python will multiply all the values which is present inside the List based on the specified number value, then creates New List which will stored Multiple occurrences of the List values in the exact sequences of the Occurencess of Valuse



print( True * [10] )  # [10] :-  print( 1 * [10] )
# Output :- [10]
print( True * [ "string", 112, True, {"Key": "Value"}, ["list values", 22] ] )
#  Output :- ['string', 112, True, {'Key': 'Value'}, ['list values', 22]]
 # behind the True will be converted to 1 and multiplies and Prints the Number of occurances
 # we are allowed to use [ Boolean and List ] as a Operands for Multiplication operator, List can have any Datatype values and any number of values



# print( None * [3] )
# Error :- TypeError: can't multiply sequence by non-int of type 'NoneType'
# we are not allowed to use [ None and List ] as a Operands for Multiplication operator, even if the list has single element or multiple elements



# print( [12] * [24] )
# Error :- TypeError: can't multiply sequence by non-int of type 'list'
# we are not allowed to use [ List and List ] as a Operands for Multiplication operator, even if the list has single element or multiple elements



print( [12] * (12) )  # [ 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12 ]
# Output :- [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
 # Here we have used Grouping operator, it will get unwrapped once if it resolved the values inside the Grouping operator syntax



# print(  [12] * (10, ) )
# Error :- TypeError: can't multiply sequence by non-int of type 'tuple'
# we are not allowed to use [ List and Tuples ] as a Operands for Multiplication operator, even if the Tuple has single element or multiple elements



# print( [12] * {44} )
# Error :- TypeError: can't multiply sequence by non-int of type 'set'
# we are not allowed to use [ List and Set ] as a Operands for Multiplication operator, even if the Set has single element or multiple elements


# print( [10] * {"key": "Value"} )
# Error :- TypeError: can't multiply sequence by non-int of type 'dict'
# we are not allowed to use [ List and Dictionary ] as a Operands for Multiplication operator, even if the Dictionary has single element or multiple elements
 



print("""



""")






# -------------------------------------------------------------------------------------------------------------------------------------------------------------




 
# Tuple with other operands using Multiplication Operator 



# print( "string" * (10,) )
# Error :- TypeError: can't multiply sequence by non-int of type 'tuple'
# we are not allowed to use [ String and Tuple ] as a Operands for Multiplication operator



print( 5 * (10,) )
# Output :- (10, 10, 10, 10, 10)
print( 5 * (10, "string", {"key": "values"}) )
# Output:- (10, 'string', {'key': 'values'}, 10, 'string', {'key': 'values'}, 10, 'string', {'key': 'values'}, 10, 'string', {'key': 'values'}, 10, 'string', {'key': 'values'})


# What happens when we use Number with Tuples of any values as an Operands ?
 # Multiplication operator will multiply all the values which is present inside the Tuples based on the specified number value, 
  # Finally it appends the Multiplied values inside the Same Tuples or we can also call in the below manner 
   # Python will multiply all the values which is present inside the Tuples based on the specified number value, then creates New Tuples which will stored Multiple occurrences of the Tuples values in the exact sequences of the Occurencess of Valuse



print( True * (10, "String") )
# Output :- (10, 'String')
 # we are allowed to use [ Boolean and Tuple ] as a Operands for Multiplication operator, Tuple can have any Datatype values and any number of values



# print( (2,) * None  )
# Error : TypeError: can't multiply sequence by non-int of type 'NoneType'
 # we are not allowed to use [ None and Tuple ] as a Operands for Multiplication operator, even if the tuple has single element or multiple elements



print( [12] * (12) )  # [ 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12 ]
# Output :- [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
 # Here we have used Grouping operator, it will get unwrapped once if it resolved the values inside the Grouping operator syntax

# print(  [12] * (10, ) )
# Error :- TypeError: can't multiply sequence by non-int of type 'tuple'
# we are not allowed to use [ List and Tuples ] as a Operands for Multiplication operator, even if the Tuple has single element or multiple elements



print( (10, ) * (20) )
# Output :- (10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
print( (10) * (20,) )
# Output :- (20, 20, 20, 20, 20, 20, 20, 20, 20, 20)

# print( (10,) * (20,) )
# Error :- TypeError: can't multiply sequence by non-int of type 'tuple'
 # if there are more than 1 occurrences of Tuple we cannot use Mupltiplication operator 
# we are not allowed to use [ tuple and Tuples ] as a Operands for Multiplication operator, even if the Tuple has single element or multiple elements



# print( (10,) * {202} )
# Error :- TypeError: can't multiply sequence by non-int of type 'set'
# we are not allowed to use [ tuple and set ] as a Operands for Multiplication operator, even if the set has single element or multiple elements



# print( (12,) * {"key": "Value"} )
# Error :- TypeError: can't multiply sequence by non-int of type 'dict'
# we are not allowed to use [ tuple and dictionary ] as a Operands for Multiplication operator, even if the dictionary has single element or multiple elements




print("""



""")





# -------------------------------------------------------------------------------------------------------------------------------------------------------




# Set with other operands using Multiplication Operator 




# print( "string" * {10} )
# Error :- TypeError: can't multiply sequence by non-int of type 'set'
# we are not allowed to use [ String and Set ] as a Operands for Multiplication operator



# print( 5 * {"set value"} )
# Error :- TypeError: unsupported operand type(s) for *: 'int' and 'set'
# we are not allowed to use [ Number and Set ] as a Operands for Multiplication operator, even if a set object has Single value 



# print( True * {"set value"} )
# Error :- TypeError: unsupported operand type(s) for *: 'bool' and 'set'
# we are not allowed to use [ Boolean and Set ] as a Operands for Multiplication operator, even if set has single value or multiple values



# print( None * {"set value"} )
# Error :- TypeError: unsupported operand type(s) for *: 'NoneType' and 'set'
 # we are not allowed to use [ None and Set ] as a Operands for Multiplication operator, even if the Dictionary has single element or multiple elements



# print( [12] * {44} )
# Error :- TypeError: can't multiply sequence by non-int of type 'set'
# we are not allowed to use [ List and Set ] as a Operands for Multiplication operator, even if the Set has single element or multiple elements



# print( (10,) * {202} )
# Error :- TypeError: can't multiply sequence by non-int of type 'set'
# we are not allowed to use [ tuple and set ] as a Operands for Multiplication operator, even if the set has single element or multiple elements




# print( {11} * {12} )
# Error :- TypeError: unsupported operand type(s) for *: 'set' and 'set'
# we are not allowed to use [ set and set ] as a Operands for Multiplication operator, even if the set has single element or multiple elements



# print( {11} * {"key": "value"} )
# Error :- TypeError: unsupported operand type(s) for *: 'set' and 'dict'
# we are not allowed to use [ set and Dictionaries ] as a Operands for Multiplication operator, even if the Dictionaries has single element or multiple elements




print("""



""")





# -------------------------------------------------------------------------------------------------------------------------------------------------------




# Dictionary with other operands using Multiplication Operator



# print( "string" * {"key": 'Dictionary value'} )
# TypeError: can't multiply sequence by non-int of type 'dict'
# we are not allowed to use [ String and Dict ] as a Operands for Multiplication operator



# print( 5 * {"key": "values"} )
# Error :- TypeError: unsupported operand type(s) for *: 'int' and 'dict
# we are not allowed to use [ Number and Dictionary ] as a Operands for Multiplication operator, even if a Dictionary object has Single value 



# print( True * {"key": "Values"} )
# Error :- TypeError: unsupported operand type(s) for *: 'bool' and 'dict'
# we are not allowed to use [ Boolean and Dictionary ] as a Operands for Multiplication operator, even if Dictionary has single value or multiple values



# print( None * {"key": "Value" } )
# Error :- TypeError: unsupported operand type(s) for *: 'NoneType' and 'dict'
 # we are not allowed to use [ None and Dictionary ] as a Operands for Multiplication operator, even if the Dictionary has single element or multiple elements



# print( [10] * {"key": "Value"} )
# Error :- TypeError: can't multiply sequence by non-int of type 'dict'
# we are not allowed to use [ List and Dictionary ] as a Operands for Multiplication operator, even if the Dictionary has single element or multiple elements
 


# print( (12,) * {"key": "Value"} )
# Error :- TypeError: can't multiply sequence by non-int of type 'dict'
# we are not allowed to use [ tuple and dictionary ] as a Operands for Multiplication operator, even if the dictionary has single element or multiple elements



# print( {11} * {"key": "value"} )
# Error :- TypeError: unsupported operand type(s) for *: 'set' and 'dict'
# we are not allowed to use [ set and Dictionaries ] as a Operands for Multiplication operator, even if the Dictionaries has single element or multiple elements



# print( {"key": "Value"} * {"key": 100} )
# Error :- TypeError: unsupported operand type(s) for *: 'dict' and 'dict'
# we are not allowed to use [ Dictionary and Dictionaries ] as a Operands for Multiplication operator, even if the Dictionaries has single element or multiple elements














