

# Implicit Division Operators 

# Here we will be learning on how Divivision Operator will work with Different Datatypes


# String 
# Number
# Boolean 
# None
# List 
# Tuples
# Set
# Dictionary 
# 



# ------------------------------------------------------------------------------------------------------------------------------------------------------



# String with other operands using Division Operator


# print( "string" / "string" )
# Error :- TypeError: unsupported operand type(s) for /: 'str' and 'str'
# we are not allowed to use [ string and string ] as an operands for Division operator



# print( "string" / 10 )
# Error :- TypeError: unsupported operand type(s) for /: 'str' and 'int'
# we are not allowed to use [ string and Number ] as an operands for Division operator



# print( "string" / True )
# Error :- TypeError: unsupported operand type(s) for /: 'str' and 'bool'
# we are not allowed to use [ string and Boolean ] as an operands for Division operator



# print( "string" / None )
# Error :- TypeError: unsupported operand type(s) for /: 'str' and 'NoneType'
# we are not allowed to use [ string and None ] as an operands for Division operator



# print( "string" / [10] )
# Error :- TypeError: unsupported operand type(s) for /: 'str' and 'list'
# we are not allowed to use [ string and List ] as an operands for Division operator, even if List has single value or multiple values



# print( "string" / (10,) )
# Error :- TypeError: unsupported operand type(s) for /: 'str' and 'tuple'
# we are not allowed to use [ string and Tuple ] as an operands for Division operator, even if tuple has single value or multiple values



# print( "string" / {"set value"} )
# Error :- TypeError: unsupported operand type(s) for /: 'str' and 'set'
# we are not allowed to use [ string and Set ] as an operands for Division operator, even if Set has single value or multiple values 



# print( "string" / {"Key": "value"} )
# Error :- TypeError: unsupported operand type(s) for /: 'str' and 'dict'
# we are not allowed to use [ string and Dictionary ] as an operands for Division operator, even if Dictionary has single value or multiple values





print("""



""")





# -------------------------------------------------------------------------------------------------------------------------------------------------------




# Number with other operands using Division Operator



# print( "string" / 10 )
# Error :- TypeError: unsupported operand type(s) for /: 'str' and 'int'
# we are not allowed to use [ string and Number ] as an operands for Division operator


print( 10 / 5 )
# Output :- 2.0
# here we get Float values, because when we divide Numerator with denominator there is changes that we might get value with decimal point
# we are allowed to use [ Number and Number ] as an operands for Division operator



print( 10 / True )  # print( 10 / 1 )
# Output :- 10.0

# print( 10 / False ) # print( 10 / 0 )
# print( "abc" / False ) # print( 10 / 0 )
# Error :- ZeroDivisionError: division by zero , here we are dividing by zero, when we divide any datatype by zero we will get this error.
# we are allowed to use [ Number and Boolean ] as an operands for Division operator



# print ( 10 / None ) 
# Error : -TypeError: unsupported operand type(s) for /: 'int' and 'NoneType' 
# we are allowed to use [ Number and None ] as an operands for Division operator



# print( 10 / [10] )
# Error :- TypeError: unsupported operand type(s) for /: 'int' and 'list'
# we are allowed to use [ Number and List ] as an operands for Division operator, weather a list has single element or multiple elements



# print( 10 / (10,) )
# Error :- TypeError: unsupported operand type(s) for /: 'int' and 'tuple'
# we are allowed to use [ Number and tuple ] as an operands for Division operator, weather a tuple has single element or multiple elements



# print( 10 / {20} )
# Error :- TypeError: unsupported operand type(s) for /: 'int' and 'set'
# we are allowed to use [ Number and Set ] as an operands for Division operator, weather a Set has single element or multiple elements


# print( 10 / {"key": 10} )
# Output :- TypeError: unsupported operand type(s) for /: 'int' and 'dict'
# we are allowed to use [ Number and Dictionary ] as an operands for Division operator, weather a Dictionary has single element or multiple elements





print("""



""")





# -------------------------------------------------------------------------------------------------------------------------------------------------------




# Boolean with other operands using Division Operator




# print( "string" / True )
# Error :- TypeError: unsupported operand type(s) for /: 'str' and 'bool'
# we are not allowed to use [ string and Boolean ] as an operands for Division operator



print( 10 / True )  # print( 10 / 1 )
# Output :- 10.0

# print( 10 / False ) # print( 10 / 0 )
# print( "abc" / False ) # print( 10 / 0 )
# Error :- ZeroDivisionError: division by zero , here we are dividing by zero, when we divide any datatype by zero we will get this error.
# we are allowed to use [ Number and Boolean ] as an operands for Division operator



print( True / True )
# Output :- 1.0
# print( True / False)
# Error :- ZeroDivisionError: division by zero
# When we divide any datatype by zero we will get this error.
# we are allowed to use [ Number and Boolean ] as an operands for Division operator only when all the operands have [True] as a Value.



# print( True / None )
# Error :- TypeError: unsupported operand type(s) for /: 'bool' and 'NoneType'
# we are not allowed to use [ Boolean and None ] as an operands for Division operator



# print( True / [10] )
# Error :- TypeError: unsupported operand type(s) for /: 'bool' and 'list'
# we are not allowed to use [ Boolean and List ] as an operands for Division operator, weather a list has single element or multiple elements


print( True / (10) )
# Output :- 0.1, Here we used Grouping operator which looks like Tuple syntax

# print( True / (10, ) )
# Error :- TypeError: unsupported operand type(s) for /: 'bool' and 'tuple'
# we are not allowed to use [ Boolean and tuple ] as an operands for Division operator, weather a tuple has single element or multiple elements




# print( True / {33} )
# Error :- TypeError: unsupported operand type(s) for /: 'bool' and 'set'
# we are not allowed to use [ Boolean and Set ] as an operands for Division operator, weather a Set has single element or multiple elements



# print( True / {"Key": 30} )
# Error :- TypeError: unsupported operand type(s) for /: 'bool' and 'dict'
# we are not allowed to use [ Boolean and dict ] as an operands for Division operator, weather a dict has single element or multiple elements






print("""



""")





# -------------------------------------------------------------------------------------------------------------------------------------------------------




# None with other operands using Division Operator



# print( "string" / None )
# Error :- TypeError: unsupported operand type(s) for /: 'str' and 'NoneType'
# we are not allowed to use [ string and None ] as an operands for Division operator



# print ( 10 / None ) 
# Error : -TypeError: unsupported operand type(s) for /: 'int' and 'NoneType' 
# we are allowed to use [ Number and None ] as an operands for Division operator



# print( True / None )
# Error :- TypeError: unsupported operand type(s) for /: 'bool' and 'NoneType'
# we are not allowed to use [ Boolean and None ] as an operands for Division operator



# print( None / None )
# Error :- TypeError: unsupported operand type(s) for /: 'NoneType' and 'NoneType'
# we are not allowed to use [ None and None ] as an operands for Division operator



# print( None / [10] )
# Error :- TypeError: unsupported operand type(s) for /: 'NoneType' and 'list'
# we are not allowed to use [ None and List ] as an operands for Division operator, weather a list has single element or multiple elements



# print( None / (10, ) )
# Error :- TypeError: unsupported operand type(s) for /: 'NoneType' and 'tuple'
# we are not allowed to use [ None and tuple ] as an operands for Division operator, weather a tuple has single element or multiple elements



# print( None / {"Set value"} )
# Error :- TypeError: unsupported operand type(s) for /: 'NoneType' and 'set'
# we are not allowed to use [ None and set ] as an operands for Division operator, weather a set has single element or multiple elements



# print( None / {"key": "value"} )
# Error :- TypeError: unsupported operand type(s) for /: 'NoneType' and 'dict'
# we are not allowed to use [ None and dict ] as an operands for Division operator, weather a dict has single element or multiple elements






print("""



""")





# -------------------------------------------------------------------------------------------------------------------------------------------------------





# List with other operands using Division Operator


# print( "string" / [10] )
# Error :- TypeError: unsupported operand type(s) for /: 'str' and 'list'
# we are not allowed to use [ string and List ] as an operands for Division operator, even if List has single value or multiple values



# print( 10 / [10] )
# Error :- TypeError: unsupported operand type(s) for /: 'int' and 'list'
# we are allowed to use [ Number and List ] as an operands for Division operator, weather a list has single element or multiple elements



# print( True / [10] )
# Error :- TypeError: unsupported operand type(s) for /: 'bool' and 'list'
# we are not allowed to use [ Boolean and List ] as an operands for Division operator, weather a list has single element or multiple elements



# print( None / [10] )
# Error :- TypeError: unsupported operand type(s) for /: 'NoneType' and 'list'
# we are not allowed to use [ None and List ] as an operands for Division operator, weather a list has single element or multiple elements



# print([10] / [5] )
# Error :- TypeError: unsupported operand type(s) for /: 'list' and 'list'
# we are not allowed to use [ List and List ] as an operands for Division operator, weather a list has single element or multiple elements



# print( [10] / (2) )
# print( [10] / (2,) )
# Error :- TypeError: unsupported operand type(s) for /: 'list' and 'int'
# Error :- TypeError: unsupported operand type(s) for /: 'list' and 'tuple'
# we are not allowed to use [ List and Tuple ] as an operands for Division operator, weather a Tuple has single element or multiple elements



# print( [10] / {2} )
# Error :- TypeError: unsupported operand type(s) for /: 'list' and 'set'
# we are not allowed to use [ List and Set ] as an operands for Division operator, weather a Set has single element or multiple elements



# print( [10] / {"key": 22} )
# Error :- TypeError: unsupported operand type(s) for /: 'list' and 'dict'
# we are not allowed to use [ List and dict ] as an operands for Division operator, weather a dict has single element or multiple elements






print("""



""")





# -------------------------------------------------------------------------------------------------------------------------------------------------------





# Tuple with other operands using Division Operator



# print( "string" / (10,) )
# Error :- TypeError: unsupported operand type(s) for /: 'str' and 'tuple'
# we are not allowed to use [ string and Tuple ] as an operands for Division operator, even if tuple has single value or multiple values



# print( 10 / (10,) )
# Error :- TypeError: unsupported operand type(s) for /: 'int' and 'tuple'
# we are allowed to use [ Number and tuple ] as an operands for Division operator, weather a tuple has single element or multiple elements



print( True / (10) )
# Output :- 0.1, Here we used Grouping operator which looks like Tuple syntax

# print( True / (10, ) )
# Error :- TypeError: unsupported operand type(s) for /: 'bool' and 'tuple'
# we are not allowed to use [ Boolean and tuple ] as an operands for Division operator, weather a tuple has single element or multiple elements



# print( None / (10, ) )
# Error :- TypeError: unsupported operand type(s) for /: 'NoneType' and 'tuple'
# we are not allowed to use [ None and tuple ] as an operands for Division operator, weather a tuple has single element or multiple elements



# print( [10] / (2) )
# print( [10] / (2,) )
# Error :- TypeError: unsupported operand type(s) for /: 'list' and 'int'
# Error :- TypeError: unsupported operand type(s) for /: 'list' and 'tuple'
# we are not allowed to use [ List and Tuple ] as an operands for Division operator, weather a Tuple has single element or multiple elements


# print( (10, ) / (5, ) )
# Error :- TypeError: unsupported operand type(s) for /: 'tuple' and 'tuple'
# we are not allowed to use [ Tuple and Tuple ] as an operands for Division operator, weather a Tuple has single element or multiple elements



# print( {33} / (330,))
# Error : TypeError: unsupported operand type(s) for /: 'set' and 'tuple'
# we are not allowed to use [ set and tuple ] as an operands for Division operator, weather a tuple has single element or multiple elements



# print( (222, ) / {"keyRight": 2 } )
# Error:- TypeError: unsupported operand type(s) for /: 'tuple' and 'dict'
# we are not allowed to use [ tuple and dict ] as an operands for Division operator, weather a dict has single element or multiple elements







print("""



""")





# -------------------------------------------------------------------------------------------------------------------------------------------------------





# set with other operands using Division Operator




# print( "string" / {"set value"} )
# Error :- TypeError: unsupported operand type(s) for /: 'str' and 'set'
# we are not allowed to use [ string and Set ] as an operands for Division operator, even if Set has single value or multiple values 



# print( 10 / {20} )
# Error :- TypeError: unsupported operand type(s) for /: 'int' and 'set'
# we are allowed to use [ Number and Set ] as an operands for Division operator, weather a Set has single element or multiple elements



# print( True / {33} )
# Error :- TypeError: unsupported operand type(s) for /: 'bool' and 'set'
# we are not allowed to use [ Boolean and Set ] as an operands for Division operator, weather a Set has single element or multiple elements



# print( None / {"Set value"} )
# Error :- TypeError: unsupported operand type(s) for /: 'NoneType' and 'set'
# we are not allowed to use [ None and set ] as an operands for Division operator, weather a set has single element or multiple elements



# print( [10] / {2} )
# Error :- TypeError: unsupported operand type(s) for /: 'list' and 'set'
# we are not allowed to use [ List and Set ] as an operands for Division operator, weather a Set has single element or multiple elements


# print( {33} / (330,))
# Error : TypeError: unsupported operand type(s) for /: 'set' and 'tuple'
# we are not allowed to use [ set and tuple ] as an operands for Division operator, weather a tuple has single element or multiple elements




# print( {100} / {10} )
# Error :- TypeError: unsupported operand type(s) for /: 'set' and 'set'
# we are not allowed to use [ set and Set ] as an operands for Division operator, weather a Set has single element or multiple elements



# print( {1000} / {"key": 10} )
# Error :- TypeError: unsupported operand type(s) for /: 'set' and 'dict'
# we are not allowed to use [ set and dict ] as an operands for Division operator, weather a dict has single element or multiple elements








print("""



""")





# -------------------------------------------------------------------------------------------------------------------------------------------------------





# dictionary with other operands using Division Operator







# print( "string" / {"Key": "value"} )
# Error :- TypeError: unsupported operand type(s) for /: 'str' and 'dict'
# we are not allowed to use [ string and Dictionary ] as an operands for Division operator, even if Dictionary has single value or multiple values



# print( 10 / {"key": 10} )
# Output :- TypeError: unsupported operand type(s) for /: 'int' and 'dict'
# we are allowed to use [ Number and Dictionary ] as an operands for Division operator, weather a Dictionary has single element or multiple elements



# print( True / {"Key": 30} )
# Error :- TypeError: unsupported operand type(s) for /: 'bool' and 'dict'
# we are not allowed to use [ Boolean and dict ] as an operands for Division operator, weather a dict has single element or multiple elements



# print( None / {"key": "value"} )
# Error :- TypeError: unsupported operand type(s) for /: 'NoneType' and 'dict'
# we are not allowed to use [ None and dict ] as an operands for Division operator, weather a dict has single element or multiple elements



# print( [10] / {"key": 22} )
# Error :- TypeError: unsupported operand type(s) for /: 'list' and 'dict'
# we are not allowed to use [ List and dict ] as an operands for Division operator, weather a dict has single element or multiple elements




# print( (222, ) / {"keyRight": 2 } )
# Error:- TypeError: unsupported operand type(s) for /: 'tuple' and 'dict'
# we are not allowed to use [ tuple and dict ] as an operands for Division operator, weather a dict has single element or multiple elements



# print( {1000} / {"key": 10} )
# Error :- TypeError: unsupported operand type(s) for /: 'set' and 'dict'
# we are not allowed to use [ set and dict ] as an operands for Division operator, weather a dict has single element or multiple elements



# print( {"key": 222} / {"keyRight": 22} )
# Error :- TypeError: unsupported operand type(s) for /: 'dict' and 'dict'
# we are not allowed to use [ dict and dict ] as an operands for Division operator, weather a dict has single element or multiple elements



























