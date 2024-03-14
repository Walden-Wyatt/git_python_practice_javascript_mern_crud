

# Implicit Programming 

 # Tips :- press [Tab] if you find the words are correct


# Here we will be leanring about on what happens when we use different datatypes as an Operand for an Operator. 

# Primitive datatypse 
 # Strings
 # Numbers
 # Boolean
 # None 

# Other Dataypes 
 # Lists
 # Tuples
 # Sets
 # Dictionaries

# Here we will be using Different Datatypes as an Operands for a Single Operator


# -----------------------------------------------------------------------------------------------------------------------------------------------------


# Addition Operator 

#  String 

# print( "Hello" + 10 )
# Error :- TypeError: can only concatenate str (not "int") to str
 # we are not allowed to use string with number types for addition operator

print( "string" + "New Other string" )
# Ouput :- stringNew Other string
# when we use String values in both the Operand with addition operator, Python will concatenate the and return the values

# print( "string" + True )
# Error :- TypeError: can only concatenate str (not "bool") to str
# we are not allowed to use [ string and Boolean ] as an operatand for Addition operator


# print( "string" + None )
# Error :- TypeError: can only concatenate str (not "NoneType") to str
# we are not allowed to use [ string and None ] as an operand. Python display the above error


# print( "string" + ["single value"] )
# Error :- [ TypeError: can only concatenate str (not "list") to str ]
# we are not allowed to use [ string and List ] as an operand. Python display the above error


print( "string" + ("single value") )
# print( "string" + (10) )
 # Error :- ypeError: can only concatenate str (not "int") to str

# Output :- stringsingle value
 # when we use String and Tuples with a single value (only 1 value ) where the single value must of String Datatype, in this situation Both the Operands will be concatinted and the value will be returned.

# print( "string" + ("single value", "2 values") )
 # Error :- TypeError: can only concatenate str (not "tuple") to str 
# when we try to pass a Tuple with string dataype values but more than one value, in such situation concatination will not happen, we will end up getting the above error.


# print( "string" + {"value 1"} )
# Error :- TypeError: can only concatenate str (not "set") to str
# we are not allowed to use [ string and set ] datatype with addition operator, even when a set has a Sigle string value


# print( "string" + {"key": "Value"} )
# TypeError: can only concatenate str (not "dict") to str
# we are not allowed to use [ string and dict ] datatype with addition operator,
# 


# Leanings :-
 # Only in 2 situations we can use [ "string" ] with other datatype for Addition operator
  # 1. All the operators for Additon operator must be a String Datatype value
  # 2. The operators must have either string or Tuples with single String values



# ----------------------------------------------------------------------------------------------------------------------------------------------------




# Number dataype with addition operator 

print( 10 + 20 )
# Output :- 30
# when an Operand for Additon operator is a Number Datatype in such situation additon operation will be performed


# print( "Hello" + 10 )
# Error :- TypeError: can only concatenate str (not "int") to str
 # we are not allowed to use [ string with number ] types for addition operator
 

print( 20 + True )
# Output :- 21
# Here python will convert Boolean True to "1" and Boolean False to "0", This Type conversion will happen when we use Boolean datatype as an Operand for any of the Operators
# we are allowed to use [ Number with Boolean ] datatypes


# print( 20 + None )
# Error :- TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
 # we are not allowed to use [ Number with None ] types for addition operator


# print( 20 + [ 2 ])
# TypeError: unsupported operand type(s) for +: 'int' and 'list'
 # we are not allowed to use [ Number with List ] types for addition operator


print(20 + (30))
# Output :- 50
# when we use Tuple with single value which is of Number type, those tuples will not be Treated as Tuple instead it will be Treated as a Value which we pass inside it (ex: when we pass number -> it will be a Number value, string -> string value )
 # Tuples with single value behind the scene python will remove the round brackets and just value will be positioned at that place 
 # How above code will look behind the scene ?
  # print( 20 + 30 )
# we are allowed to use Tuple with single values



print( 20 + (30 + 20 + 40 ) )
print( 20 + (30 + 20 + 40 + ( 30 + ( 55 ) ) ) )
# Output :- 110

# The above code is not a Tuple it is Grouping Operator, which will get resolved first in a Sequence of Operands and Operators
# when we use Tuple wiht multiple values where all the values has a Number Type, in this case Python will perform Addition Operations behind the scene
# We can have any number of values inside the tuples or any level of Nested Tuples with one condition that all the values must of number datatype, in this situation python will perform Addition Operations behind the scene 
  # if a tuple has any one value which is of other datatype then error will be raised 

# behind the scene python will remove the all the round brackets from the nested levels of Tuples and treat it as a single lines value, how above code will look
 # print ( 20 + 30 + 20 + 40 )
 # print( 20 + 30 + 20 + 40 + 30 + 55 )


# print( 20 + ("string") )
# Error :- TypeError: unsupported operand type(s) for +: 'int' and 'str'
# we are not allowed to use [ Number with tuple which has datatype other than Number ]


# print( 20 + {20} )
# Error :- TypeError: unsupported operand type(s) for +: 'int' and 'set'
 # we are not allowed to use [ Number with set datatype ]
 # even if the set has single value or multiple values, Number or Other datatypes,we are not allowed to use to perform operations


# print( 20 + { "key": 20 } )
# Error :- TypeError: unsupported operand type(s) for +: 'int' and 'dict'
 # we are not allowed to use [ Number with dict datatype ] 



# Learnings :-
 # when we can use Number with other operands ?
# we can use Number dataype in 3 situations 
 # 1. Number and all the ohter Operatands is a Number Datatypes 
 # 2. Number and all the ohter Operatands is a Boolean Datatypes
 # 3. Number and Tuples which has values either a Number or Boolean it can be any level of nesteing, this is ultemately called as Grouping Operator.
 # 4. Mixture of above 3 conditons



# -------------------------------------------------------------------------------------------------------------------------------------------

# Boolean with other types using Addition operator


# Boolean with Boolean datatype
print( True + True )
# Boolean with Number datatype
print ( False + 34 )
# Boolean with tuple, can also be called as Grouping Operator
print( True + (30) )
# Boolean with tuple, where the Tuple have only Number dataype value this will perform addition operations
print( True + (30  + 33) )


print( True + (False) )
# Output :- 1 
 # when we use Boolean datatype with any of the Operator behind the scene Boolean datatype values will be converted to Number
  # [ Boolean True = 1 ] [ Boolean False = 0 ]



# -----------------


# Cases where we are not allowed to use Boolean Operand cannot be used with other types using Addition operator


# print( True + "String" )
# Error :- TypeError: unsupported operand type(s) for +: 'bool' and 'str'

# print( True + None )
 # Error :- TypeError: unsupported operand type(s) for +: 'bool' and 'NoneType'

# print( False + [ True ] )
 # Error :- TypeError: unsupported operand type(s) for +: 'bool' and 'list'

# print( True + {False} )
 # Error :- TypeError: unsupported operand type(s) for +: 'bool' and 'set'

# print( True + { "Key": "value"} )
# Error :- [ TypeError: unsupported operand type(s) for +: 'bool' and 'dict' ]


# -------

# Learnings :-

 # Situation where we can use Datatypes Booleand and other datatype but still we will not get the Error.

 # 1. [ Boolean and Boolean values] as left and Right Operand 
 # 2. [ Boolean with number ]
 # 3. [ Boolean with tuples  ] single or Multiple values ( where all the values ar of either Boolean, Number , Nested Tuples of only dataype type values )
 # 4. [ Mixture of above conditons ] just twik the above datatypes which can be accessed.
 # 5.



# -----------------------------------------------------------------------------------------------------------------------------------------------------


# None with other dataypes 


# print( "string" + None )
# Error :- TypeError: can only concatenate str (not "NoneType") to str
# we are not allowed to use [ string and None ] as an operand. Python display the above error
# None with String will give an Error


# None with Boolean will give an Error
# print( True + None )
 # Error :- TypeError: unsupported operand type(s) for +: 'bool' and 'NoneType'


# None with Number  will give an Error
# print( 20 + None )
# Error :- TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
 # we are not allowed to use [ Number with None ] types for addition operator


# None with None will give an Error
# print( None + None )
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# we are not allowed to use [ None with None ] types for addition operator as it will throw an exception( Error )


# print( None + [ None ] )
# Error :- TypeError: unsupported operand type(s) for +: 'NoneType' and 'list'
# we are not allowed to use [ None with List ] types for addition operator as


# print( None + (10) )
# Error :- TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
# print( None + (10 + 30 + 40 + (49 + ( 78 ) )) )
# Error :- TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
 # Here we can clearly see that we have used Tuples but python says that the Right operand is a [int] datatype 
  # by this we leanr that the Tuple which as lef and right operator of number dataype as well as any Level of Nesting This Datatypes will be a [ int ] datatype.

# print( None + {None} )
# Error :- TypeError: unsupported operand type(s) for +: 'NoneType' and 'set'


# print( None + {"key": "Value"} )
# Error :- TypeError: unsupported operand type(s) for +: 'NoneType' and 'dict'


# Learnings :-
 # None datatype cannot be used for either of the Operand ( Left or Right ), if we try to use we will get a TypeError.




# -----------------------------------------------------------------------------------------------------------------------------------------------------





# List with other datatypes using Addition Operators 


# print( "string" + ["single value"] )
# Error :- [ TypeError: can only concatenate str (not "list") to str ]
# we are not allowed to use [ string and List ] as an operand. Python display the above error


# print( 20 + [ 2 ])
# TypeError: unsupported operand type(s) for +: 'int' and 'list'
 # we are not allowed to use [ Number with List ] types for addition operator


# print( False + [ True ] )
 # Error :- TypeError: unsupported operand type(s) for +: 'bool' and 'list'


# print( None + [ None ] )
# Error :- TypeError: unsupported operand type(s) for +: 'NoneType' and 'list'
# we are not allowed to use [ None with List ] types for addition operator as



print( [1, 2, 3] + [ 2, 3, 4])

print( [1, 2, 3] + [ "Hello", 3, 4])

print( [ {"setValue"}, {"key": "Value"}, False ] + [ ["nested List"], ("Tuples"), 30000  ] )

# Output :-
# [1, 2, 3, 2, 3, 4]
# [1, 2, 3, 'Hello', 3, 4]
# [{'setValue'}, {'key': 'Value'}, False, ['nested List'], 'Tuples', 30000]


# When we use list and list datatype to concatenate and create a Single List object which will have all the values includinG Nested values, dicrionaries ex.
 # When a Top level of list has a Multiple Occurrences of the same value ( same value got repeated multiple times or Duplicate values ), in this situation Python will remove the Dkplicate value ( values which occurs multiple times in the list after combining )



# print( [1, 2,3 ] + (4) )
# Error :- TypeError: can only concatenate list (not "int") to list
# we are not allowed to use [ List and Tuple ] datatype, Even if the Tuple datatype has a Single value we will encounter this error 

print( [1, 2,3 ] + ([34, "Nested values", False, 1, 2, 3 ]) )
# Output :- 
 #  [1, 2, 3, 34, 'Nested values', False]
# when the Tuple has single value, where the value is of List datatype ( list has any number of Nested levels as well as any datatype value ), in this situation python will Club all the List values inside the One single List type
 # even if the List has duplicate values,  those values will not be premoved it will be stored exactly in the Index position which we have used.


# print( [1, 2,3 ] + ([34, "Nested values", False, 1, 2, 3 ], [ 2200, 3300 ]) )
 # Error :- TypeError: can only concatenate list (not "tuple") to list


# print( [1, 2, 3] + {"set value"} )
# Error :- TypeError: can only concatenate list (not "set") to list

# print( [ 1, 2, 3] + {[1, 2, 3 ]} )
# Error :- TypeError: unhashable type: 'list'
# even when the set has a single value which is a List datatype still python will not allow to perform addition operation


# print( [1, 2, 3] + {"key": [2, 3, 4]} )
# Error :- TypeError: can only concatenate list (not "dict") to list
# even we not allowed to use [ List and dict ] operands to perform Addition operations



# List with other operands can be used only in 2 situation ?
 # 1. Left and Right Operands are list dataytype
 # 2. List and Tuple as operands, where Tuples must have only 1 value which must be a List Datatype.
 # we cannot use Tuple except for the above situations




# ------------------------------------------------------------------------------------------------------------------------------------------------------


# Tuples with other operands using Addition Operator 


print( "string" + ("single value") )
# print( "string" + (10) )
 # Error :- ypeError: can only concatenate str (not "int") to str

# Output :- stringsingle value
 # when we use String and Tuples with a single value (only 1 value ) where the single value must of String Datatype, in this situation Both the Operands will be concatinted and the value will be returned.

# print( "string" + ("single value", "2 values") )
 # Error :- TypeError: can only concatenate str (not "tuple") to str 
# when we try to pass a Tuple with string dataype values but more than one value, in such situation concatination will not happen, we will end up getting the above error.




print(20 + (30))
# Output :- 50
# when we use Tuple with single value which is of Number type, those tuples will not be Treated as Tuple instead it will be Treated as a Value which we pass inside it (ex: when we pass number -> it will be a Number value, string -> string value )
 # Tuples with single value behind the scene python will remove the round brackets and just value will be positioned at that place 
 # How above code will look behind the scene ?
  # print( 20 + 30 )
# we are allowed to use Tuple with single values



print( 20 + (30 + 20 + 40 ) )
print( 20 + (30 + 20 + 40 + ( 30 + ( 55 ) ) ) )
# Output :- 110

# The above code is not a Tuple it is Grouping Operator, which will get resolved first in a Sequence of Operands and Operators
# when we use Tuple wiht multiple values where all the values has a Number Type, in this case Python will perform Addition Operations behind the scene
# We can have any number of values inside the tuples or any level of Nested Tuples with one condition that all the values must of number datatype, in this situation python will perform Addition Operations behind the scene 
  # if a tuple has any one value which is of other datatype then error will be raised 

# behind the scene python will remove the all the round brackets from the nested levels of Tuples and treat it as a single lines value, how above code will look
 # print ( 20 + 30 + 20 + 40 )
 # print( 20 + 30 + 20 + 40 + 30 + 55 )


# print( 20 + ("string") )
# Error :- TypeError: unsupported operand type(s) for +: 'int' and 'str'
# we are not allowed to use [ Number with tuple which has datatype other than Number ]




# Boolean with tuple, can also be called as Grouping Operator
print( True + ((30)) )
# Boolean with tuple, where the Tuple have only Number dataype value this will perform addition operations
print( True + ((30  + 33)) )


print( True + ((False)) )
# Output :- 1 
 # when we use Boolean datatype with any of the Operator behind the scene Boolean datatype values will be converted to Number
  # [ Boolean True = 1 ] [ Boolean False = 0 ]



# print( None + ((10)) )
# Error :- TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
# print( None + (10 + 30 + 40 + (49 + ( 78 ) )) )
# Error :- TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
 # Here we can clearly see that we have used Tuples but python says that the Right operand is a [int] datatype 
  # by this we leanr that the Tuple which as lef and right operator of number dataype as well as any Level of Nesting This Datatypes will be a [ int ] datatype.




# print( [1, 2,3 ] + (4) )
# Error :- TypeError: can only concatenate list (not "int") to list
# we are not allowed to use [ List and Tuple ] datatype, Even if the Tuple datatype has a Single value we will encounter this error 

print( [1, 2,3 ] + (([34, "Nested values", False, 1, 2, 3 ])) )
# Output :- 
 #  [1, 2, 3, 34, 'Nested values', False]
# when the Tuple has single value, where the value is of List datatype ( list has any number of Nested levels as well as any datatype value ), in this situation python will Club all the List values inside the One single List type
 # even if the List has duplicate values,  those values will not be premoved it will be stored exactly in the Index position which we have used.


# print( [1, 2,3 ] + ([34, "Nested values", False, 1, 2, 3 ], [ 2200, 3300 ]) )
 # Error :- TypeError: can only concatenate list (not "tuple") to list



print( ("string") + ("wow") )
# String with Single values will be treated as not a Tuple but whatever Datatype value which is present insidt the Tuples the same datatype
# Output :- stringwow


# print( ("string") + ("wow", "multiple value") )
# Error :- TypeError: can only concatenate str (not "tuple") to str
# when either side of the Tuple has more than 1 value with where both operands tuple values are of same or different datatype values we will get the above error.
 


# print( (("nested tuples")) + {("set value")}  )
# Error :- TypeError: can only concatenate str (not "set") to str
# when the operands are [ Tuples and set ] python will not perform any addition operation it will return the above error.


# print( ("Tuple value") + {"key": ("Tuple value") } )
# Error :- TypeError: can only concatenate str (not "dict") to str
#  when the operands are of [ Tuple and set ] in this situation python will not perform any Addition operation it will return as Error.





# -----------------------------------------------------------------------------------------------------------------------------------------------------





# Set with other Operands using Addition operators


# print( "string" + {"value 1"} )
# Error :- TypeError: can only concatenate str (not "set") to str
# we are not allowed to use [ string and set ] datatype with addition operator, even when a set has a Sigle string value



# print( 20 + {20} )
# Error :- TypeError: unsupported operand type(s) for +: 'int' and 'set'
 # we are not allowed to use [ Number with set datatype ]
 # even if the set has single value or multiple values, Number or Other datatypes,we are not allowed to use to perform operations


# print( True + {False} )
 # Error :- TypeError: unsupported operand type(s) for +: 'bool' and 'set'



# print( None + {None} )
# Error :- TypeError: unsupported operand type(s) for +: 'NoneType' and 'set'



# print( [1, 2, 3] + {"set value"} )
# Error :- TypeError: can only concatenate list (not "set") to list

# print( [ 1, 2, 3] + {[1, 2, 3 ]} )
# Error :- TypeError: unhashable type: 'list'
# even when the set has a single value which is a List datatype still python will not allow to perform addition operation




# print( (("nested tuples")) + {("set value")}  )
# Error :- TypeError: can only concatenate str (not "set") to str
# when the operands are [ Tuples and set ] python will not perform any addition operation it will return the above error.




# print( {"set value"} + {"set value"} )
# Error :- TypeError: unsupported operand type(s) for +: 'set' and 'set'
 # when we use [ set and set ] operands we will get this error, we are not allowed to use [ set and set ] to perform some operations.



# print( { {"nested set"}} + { 10 } )
# Error :- TypeError: unhashable type: 'set
 # when we use [ set and set ] operands we will get this error, we are not allowed to use [ set and set ] to perform some operations.




# print( {"set value"} + {"key": "set dictionary value"} )
# Error :- TypeError: unsupported operand type(s) for +: 'set' and 'dict'
# we are not allowed to use [ set and dictionary ] or wiseversa as datatype to perfrom addition operations, if we do so we will get the above error








# -----------------------------------------------------------------------------------------------------------------------------------------------------





# Dictionary with other Operands using Addition operators


# print( "string" + {"key": "Value"} )
# TypeError: can only concatenate str (not "dict") to str
# we are not allowed to use [ string and dict ] datatype with addition operator,
# 



# print( 20 + { "key": 20 } )
# Error :- TypeError: unsupported operand type(s) for +: 'int' and 'dict'
 # we are not allowed to use [ Number with dict datatype ] 



# print( True + { "Key": "value"} )
# Error :- [ TypeError: unsupported operand type(s) for +: 'bool' and 'dict' ]



# print( None + {"key": "Value"} )
# Error :- TypeError: unsupported operand type(s) for +: 'NoneType' and 'dict'



# print( [1, 2, 3] + {"key": [2, 3, 4]} )
# Error :- TypeError: can only concatenate list (not "dict") to list
# even we not allowed to use [ List and dict ] operands to perform Addition operations



# print( ("Tuple value") + {"key": ("Tuple value") } )
# Error :- TypeError: can only concatenate str (not "dict") to str
#  when the operands are of [ Tuple and set ] in this situation python will not perform any Addition operation it will return as Error.



# print( {"set value"} + {"key": "set dictionary value"} )
# Error :- TypeError: unsupported operand type(s) for +: 'set' and 'dict'
# we are not allowed to use [ set and dictionary ] or wiseversa as datatype to perfrom addition operations, if we do so we will get the above error




# print( {"key": "dictionary value" } + { "rightKey": "Right Key value" } )
# Error :- TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
 # we are not allwed to use [ Dictionary and Dictionary ] datatype as an Operands to perform Addition Operations, when we use we will get the above error.








# ---------------------------------------------------------------------------------------------------------------------------------------------------


# Here we learnt on how Addition Operator works when we use different datatypes as an Operands.













