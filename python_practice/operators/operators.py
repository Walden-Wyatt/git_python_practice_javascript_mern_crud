

# Operators 

# Here we will be Learning about Operators in Python


# types of operators in python
# ChatGPT

# In Python, operators are special symbols or keywords that are used to perform operations on operands. Here are the main types of operators in Python:
# 1. Arithmetic Operators:

#     + (Addition): Adds two operands.
#     - (Subtraction): Subtracts the right operand from the left operand.
#     * (Multiplication): Multiplies two operands.
#     / (Division): Divides the left operand by the right operand.
#     // (Floor Division): Returns the quotient of the division, rounded down to the nearest integer.
#     % (Modulus): Returns the remainder of the division.

# 2. Comparison Operators:

#     == (Equal to): Returns True if the operands are equal.
#     != (Not equal to): Returns True if the operands are not equal.
#     < (Less than): Returns True if the left operand is less than the right operand.
#     > (Greater than): Returns True if the left operand is greater than the right operand.
#     <= (Less than or equal to): Returns True if the left operand is less than or equal to the right operand.
#     >= (Greater than or equal to): Returns True if the left operand is greater than or equal to the right operand.

# 3. Logical Operators:

#     and (Logical AND): Returns True if both operands are True.
#     or (Logical OR): Returns True if at least one operand is True.
#     not (Logical NOT): Returns True if the operand is False, and vice versa.

# 4. Assignment Operators:

#     = (Assignment): Assigns the value of the right operand to the left operand.
#     += (Add and Assign): Adds the right operand to the left operand and assigns the result to the left operand.
#     -= (Subtract and Assign): Subtracts the right operand from the left operand and assigns the result to the left operand.
#     *= (Multiply and Assign): Multiplies the left operand by the right operand and assigns the result to the left operand.
#     /= (Divide and Assign): Divides the left operand by the right operand and assigns the result to the left operand.

# 5. Bitwise Operators:

#     & (Bitwise AND): Performs a bitwise AND operation.
#     | (Bitwise OR): Performs a bitwise OR operation.
#     ^ (Bitwise XOR): Performs a bitwise XOR (exclusive OR) operation.
#     ~ (Bitwise NOT): Inverts the bits of the operand.
#     << (Left Shift): Shifts the bits of the left operand to the left by the number of positions specified by the right operand.
#     >> (Right Shift): Shifts the bits of the left operand to the right by the number of positions specified by the right operand.

# 6. Membership Operators:

#     in: Returns True if a value is found in the specified sequence.
#     not in: Returns True if a value is not found in the specified sequence.

# 7. Identity Operators:

#     is: Returns True if both operands are the same object.
#     is not: Returns True if both operands are not the same object.

# 8. Unary Operators:

#     + (Unary Plus): Indicates a positive value.
#     - (Unary Minus): Negates a value.

# These operators play a crucial role in various programming tasks, allowing you to perform a wide range of operations on variables and values.






# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






# provide examples for the above content
# ChatGPT

# Certainly! Let's go through examples for each type of operator mentioned:
# 1. Arithmetic Operators:

# python

# a = 10
# b = 3

# print(a + b)    # Output: 13
# print(a - b)    # Output: 7
# print(a * b)    # Output: 30
# print(a / b)    # Output: 3.333...
# print(a // b)   # Output: 3 (floor division)
# print(a % b)    # Output: 1 (modulus)

# 2. Comparison Operators:

# python

# x = 5
# y = 10

# print(x == y)   # Output: False
# print(x != y)   # Output: True
# print(x < y)    # Output: True
# print(x > y)    # Output: False
# print(x <= y)   # Output: True
# print(x >= y)   # Output: False

# 3. Logical Operators:

# python

# a = True
# b = False

# print(a and b)  # Output: False
# print(a or b)   # Output: True
# print(not a)    # Output: False

# 4. Assignment Operators:

# python

# x = 5

# x += 3   # Equivalent to x = x + 3
# print(x)  # Output: 8

# x -= 2   # Equivalent to x = x - 2
# print(x)  # Output: 6

# x *= 4   # Equivalent to x = x * 4
# print(x)  # Output: 24

# x /= 3   # Equivalent to x = x / 3
# print(x)  # Output: 8.0

# 5. Bitwise Operators:

# python

# a = 5
# b = 3

# print(a & b)   # Output: 1 (bitwise AND)
# print(a | b)   # Output: 7 (bitwise OR)
# print(a ^ b)   # Output: 6 (bitwise XOR)
# print(~a)      # Output: -6 (bitwise NOT)
# print(a << 1)  # Output: 10 (left shift by 1)
# print(a >> 1)  # Output: 2 (right shift by 1)

# 6. Membership Operators:

# python

# my_list = [1, 2, 3, 4]

# print(3 in my_list)    # Output: True
# print(5 not in my_list) # Output: True

# 7. Identity Operators:

# python

# x = [1, 2, 3]
# y = [1, 2, 3]
# z = x

# print(x is y)     # Output: False (different objects)
# print(x is not y) # Output: True
# print(x is z)     # Output: True (same object)

# 8. Unary Operators:

# python

# a = 7

# print(+a)  # Output: 7 (unary plus)
# print(-a)  # Output: -7 (unary minus)

# These examples demonstrate the usage of different types of operators in Python.





# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






# How to Practise Operators 

 # 1. Try all the Operators using Number Datatype
 # 2. Use different Datatype as an Operand and try this pattern for all the Operators


# Syntax of Operator 
 # [ Left Operand ] [ Operator ] [ Right Operand ]



print("""



Arithmatic Operators



""")




# Arithmatic Operators 

a = 10
b = 11

# Addition Operator
add = a + b 
print( add ) # 21


# Subtraction Operator
subtract = a - b
print( a - b ) # -1


# Multiplication Operator
multiplication = a * b
print( multiplication ) # 110


# Division Operator
division = a / b
print( division ) # 0.90


# Modulas Operator
# How modulas works 
 # when tring to divide left operand with right operand if the value is lesser than 1 in such situation whatever value is present in the Left operand will be returned else the Reminder after dividing will be returned.
modulas = a % b
print( modulas ) # 10 -> here because when we try to divide 10 with 11 the value will be below 1


print("""



Comparison operators




""")


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# 2. Comparison Operators:
 # This operators will return Boolean Values such as True and False

x = 5
y = 10

# == - Equal to Operator
 # this will check weather the Left Operand is equal to Right Operand if yes returns True else False

# != - Not Equal to Operator
 # this will check weather the Left Operand is Not-equal to Right Operand if yes returns True else False

# < - Less than operator
 # this will check weather the left operand is Lesser than Right Operand, if yes returns True else False.

# > - Greater than operator
 # this will check weather the Right operand is Greater than Right Operand, if yes returns True else Fasle.

# <= - Lesser than or Equal to Operator
 # this will check weather the Left Operand is Lesser than or Equal to Right Operand, if yes returns True else False.

# >= - Greater than or Equal to Operator
 # this will check weather the Left Operand is Greater than or Equal to Right Operand, if yes returns True else False.


# ---------------------

print( x == y ) # False

print( x != y ) # True

print( x < y ) # True

print( x > y ) # False

print( x <= y ) # True

print( x >= y ) # False


print("""



      
Logical Operators
      



""")


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#  3. Logical Operators:

 # Logical Operator will check Operands

# and
 # [ and ] operator will check Left and Right Operands, only when Left and Right Operands are True this will return True
 # if any One Operand that is Left or Right operand is False, then [ and ] operand will return False
 # if both the Operand if False, then [ and ] operator will return False

# or
 # [ or ] operator will check Left and Right Operands, if any of the Operand that is Left or Right Operand is True, [ or ] Operator will return True
 # if both the Operand that is Left or Right Operands are False, then [ or ] operand will return False
 # if both the operand is True, then [ or ] operator will return True


# not

 # [ not ] operator will swap the Values, if the Value if Truthy preceeding (not) will make the Value False or Falsy 
 # if the Value is False or Falsy then this Operator will make the Value True or Truthy.



a = True
b = False


print( a and b ) # False - Because Right Operand is False

print( a or b ) # True - Because Left Operand is True

print( not a ) # False - This will Swap the Values, if True ==> False, if False ==> True



print("""



      
4. Assignment Operators:
      



""")


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# 4. Assignment Operators:


# =  - [ Assignment Operator ]
 # this operator will assign the value to a Variable


# += - [ Addition Assignment Operator ]
 # This operator will add the Left and Right Operand and assign it to a Variable


# -= - [ Subtraction Assignment Operator ]
 # This operator will Subtract the Left and Right Operand and assign it to a Variable


# *= - [ Multiplication Assignment Operator ]
 # This operator will Multiplication the Left and Right Operand and assign it to a Variable


# /= - [ Division Assignment Operator ]
 # This operator will Division the Left and Right Operand and assign it to a Variable


# %= - [ Modulas Assignment Operator ]
 # This operator will Perform modulas operation between the Left and Right Operand and assign it to a Variable





x = 5
print( x ) # 5

x += 3
# The above code is equavalent of writing in the below code
 # x  = x + 3
print( x ) # 8

x -= 4
# The above code is equavalent of writing in the below code
 # x  = x - 3
print( x ) # 4

x *= 10
# The above code is equavalent of writing in the below code
 # x  = x * 3
print( x ) # 40

x /= 2
# The above code is equavalent of writing in the below code
 # x  = x / 3
print( x ) # 20


x %= 3
# The above code is equavalent of writing in the below code
 # x  = x % 3
print( x ) # 2



print("""



      
5. Bitwise Operators:
      



""")


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# 5. Bitwise Operators:

# Bitwise Operator will create the Bit when we convert the bit to a Character this will return the actual character for the Bit, To check for Bit values you can use ASCII


# And - &
 # Conditions 
 # [ 1 and 1 ] - if the bit values are of 1 and 1 in this case the returned value will be [ 1 ]
 # [ 1 and 0, 0 and 1, 0 and 0 ] - if this is the case the Returned bit value will be 0.


# Or - |
 # Conditions 
 # [ 1 and 0, 0 and 1, 1 and 1 ] - if the bit is in this format the returned value will be [ 1 ]
 # [ 0 and 0 ] - if the bit value is in these format the returned value will be 0.


# XOR - ^
  # conditions  
  # [ 1 and 1 = 0, 0 and 0 = 0 ] - wherever it finds 1 and 1 as well as 0 and 0 it will replace those values with 0, where as if the values are 1 and 0  as well as 0 and 1 it will replace the value with 1
  # 1 and 0 = 1, 0 and 1 = 1
 

# Not - ~
 # This will swap the Values, if it finds 1 bitwise NOT will replace it with 0, if it finds 0 bitwise NOT will replace with 1


# Left Shift - <<
 # this will shift the bit towards Left, that is it will add the 0 at the Right side of the Bit, from that output the value will be evaluated


# Right Shift - >>
 # this will shift the bit towards Right, that is it will add the 0 at the Left side of the bit, from that output the value will be evaluated


# ----------------


x = 10
# bitvalue = 1010
y = 3
# bitvalue = 0011


print( x & y ) # 2
# x          1010 
# y          0011
# solution - 0010 = 2


x = 10
y = 3


print( x | y ) # 11
# x          1010 
# y          0011
# solution - 1011 = 11


x = 10
y = 3

print( x ^ y ) # 13
# x          1010
# y          0011
# solution - 1001 = 9

a = 7
b = 9

print( a ^ b ) # 14



x = 10
y = 3

print( ~x ) #  5
# [ ~value ] this will swap 0 with 1 and 1 with 0
# x          1010 
# solution - 0101 = -11


x = 10
y = 3

print( x << 1 ) # 20
# x          01010
# solution - 10100 = 20


x = 10
y = 3

print(x >> 1 ) # 
# x          1010
# solution - 0101 = 5






print("""



      
6. Membership Operators:
      



""")




# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# 6. Membership Operators:

# Membership operators can be used to check weather a Perticular Value is present inside the Object or not, Objects such as [ List, Sets, etc ]

# [ in ] - 
 # this will check weather a Particular value is present inside the Object [ List ],
 # this will return [ True ] if the value is present, False if the value is not Present.

# [ not in ] - 
 # this will check weather a Particular value is present inside the Object [ List ],
 # this will return [ False ] if the value is present, [ True ] if the value is not Present.


my_list = [ 1, 2, 3, 4 ]

print ( 3 in my_list ) # True, because 3 is present inside ( my_list )

print( 7 not in my_list ) # True, because 7 is not present inside ( my_list )

print( 18 in my_list ) # False

print( 3 not in my_list ) # False







print("""



      
7. Identity Operators:
      



""")




# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# 7. Identity Operators:

 # Identity Operator can be used to check weather the Object is a Deep Copy (copied value) or Shallow Copy ( copied reference ).


# [ is ]
 # [is] operator can be used to check weather both the objects reference are same

# [ is not ]
 # [is not ] operator can be used to check weather both the objects reference are not same.


x = [1, 2, 3]
y = [1, 2, 3]
z = x # Here we did shallow copy, when we changes in any one of the Object both the Object will get modified


print( x is y ) # False 
print( x is not y ) # True 

print( x is z ) # True 
print( x is not z ) # False







print("""



      
7. Identity Operators:
      



""")




# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# 8. Unary Operators:

# if you want to perform Arithmath operations by using Single Operand we can use Unary Operators

 # This operator can be used to preceed a number operand with (+) and (-) symbols

 # Unery Plus  - 
  # used to make a number as a Positive integer or Float
 # Unery Minus - 
  # used to preceed a number with (-) minus symbol negative Integer or Float

unery_plus = 10

unery_minus = 12

print( +unery_plus )
print( unery_plus )

print( -unery_minus )
print( unery_minus )



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------




print("""



Using Different Datatypes as Operators




""")


# Using Different datatypes as an Operands 


# String, Int, Float, Boolean, None, List, Dictionary, Tuple, Set

# Operators - + - * / %


stringType = "String"
intType = 1
floatType = 22.55
boolean = True
noneType = None


# String using Addition Operator with other Datatypes


# print( stringType + intType )
# Error :- TypeError: can only concatenate str (not "int") to str 
 # This Error occurs when we try to concatenate String with Number datatype which we are not allowed to do

print( stringType + stringType )
# we are allowed to concatenate String type with other String type



# ---------------------------




# String float

# print( stringType + floatType )
# Error :- TypeError: can only concatenate str (not "float") to str
 # even we are not allowed to concatenate the Float and String values


# ---------------------------



# String boolean

# print( stringType + boolean )
 # TypeError: can only concatenate str (not "bool") to str
  # we are not allowed to concatenate the Boolean and String values


# ---------------------------


# string none

# print( stringType + noneType )
 
  # Error :- TypeError: can only concatenate str (not "bool") to str
   # even we are not allowed to use String and None to concatenate.




# ---------------------------

# ---------------------------


# Boolean and Number type

 # When we use 


intType = 1
floatType = 22.55
boolean = True


print( intType + boolean ) # 3
print( floatType + boolean )  # 23.55


print( intType - boolean )  # 1
print( floatType - boolean)  # 21.55


print( intType * boolean )  # 2
print( floatType * boolean )  # 22.55


print( intType / boolean )  # 2.0
print( floatType / boolean )  # 22.55


print( intType % boolean )  # 0
print( floatType % boolean )  # 0.5500000000000007


print("""


Comparison Operators 


""")


# Comparison Operators 

print ( intType == boolean ) # True

print( intType != boolean ) # False

print( intType < boolean )

print( intType > boolean )

print( intType <= boolean )

print( intType >= boolean )


print("""


assignment operator 


""")


# assignment operator 

intType += boolean
print( intType )

intType -= boolean
print(intType)

intType *= boolean
print( intType )

intType /= boolean
print( intType )

intType %= boolean
print( intType )


print("""


Logical operator 


""")


intType = 1
floatType = 22.55
boolean = True


print( intType and boolean ) # True

print( intType or boolean ) # 1

print( not intType ) # False


# -------------------------------------------


# Using Boolean and Integer or Float as a Left or Right Operand will perform Mathmatical Operations 
 # Boolean and Number Datatype as an Operands can be used for all the Operators





# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





# using Boolean an None

boolean = True
noneType = None


# print( boolean + noneType )
# print( boolean - noneType )
# print( boolean * noneType )
# print( boolean / noneType )
# print( boolean % noneType )

# Error :- TypeError: unsupported operand type(s) for -: 'bool' and 'NoneType'
 # this error occurs when we try to use Boolean and None Datatype as either of the Operands.



print("""



Operators with Complex Datatypes
      


""")




# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Now lets Explore Complex Datatypes 

# String with list


string = "String"
listType = ["hello"]

# print( string + listType )
# Error :- TypeError: can only concatenate str (not "list") to str



# List which as single Number value

list_number = [10]
listType = 30

# print( list_number + listType )

# Error :- TypeError: can only concatenate list (not "int") to list
 # This error message says that we are not allowed to perform addition operations if one of the Operand is of List Datatype.

# If you want to Use List Datatype property make sure to use List Built-in Methods and properties
 # Based on what value does the Otherside the Operand has make sure to use the List methods which returns the same datatype values or datatype value which supports the operations(Ex:- tuples single value, string, number, etc)






# ------------------------



# Tuples and Strings


tupleTypes = ("alphabets")
# tupleTypes = (1)
print( string + tupleTypes )
# Output :- Stringalphabets
# If a Tuple has a Single value which should be a String  in such situation The concatenation might happen
# if a Tuple has more than 1 value or value other than string datatype in such situation TypeError will be thrown


# tupleTypes = ("alphabets", "new String" )
# print( string + tupleTypes )

# # Error :- TypeError: can only concatenate str (not "tuple") to str

# print(string - tupleTypes )
# Error :- TypeError: unsupported operand type(s) for -: 'str' and 'str'
 # this error occurs when we try to use Operators such as [ - * / %, etc]

# In Tuples 
 # we are allowed to use + operator to with string datatype only if a Tuple has a Single Value as well as it must be a String datatype.



print("""


      
 Tuples with Int
      


""")



# ---------------------------------


# Tuples with Int

# When we use Tuples with single value it is as Equal as using the Variable with some datatype value, its like using Primitive datatype

 # tuple = ("hello")
  # Equavalent to =  stringVariable = "hello"

 # tuple = (111)
  # Equavalent to = numberVariable = 111



intType = 10
tuplesType = (1)
# tuplesType = (1, 2)
 # Error :- TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
  # This error occurs when we try to use Operators where the Tuples have more than 1 values.

print(intType + tuplesType )



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Tuples with Single Number or Boolean Datatype value can be used to perfrom all the Operations using all the Operators



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Tuples with set 

setType = {2}
tuple_number = (22)

# print( setType + tuple_number )
# Error :- TypeError: unsupported operand type(s) for +: 'set' and 'int'
 # this error message says that we are not allowed to use [set] and [int]  as an Operand for "+" addition operator.
 # here we passed Tuple but it says int, a Tuple has only one vlaues in such situation whatever value which we pass will be datatype for that value



dictionary = {
    "key": "value",
    "numKey":45
}

# print( dictionary + tuple_number )




# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Dictionaries 



# We are not allowed to use Any other Datatype as an Operands for Dictionary object as one of the Operand as well as with Different Operators ( +,-,*,/,%, etc)


dictionary = {
    "key": "value",
    "key_2": 111
}



# print("String" + dictionary )

# print( "string" - dictionary )  # TypeError: unsupported operand type(s) for +: 'dict' and 'int'
# print( "String " * dictionary )

# print( "string" * dictionary )
# print( "string" / dictionary )

# if we want to access the dictionary we have to use Methods, just do invoke the method with appropriate Datatype value on one side of Opreands

 # By invoking Dictionary methods as one of the Operand, where the other side of the operand is the Datatype which supports the operation


print( "String" + dictionary.get("key") ) # Output :- Stringvalue






# -----------------------------------------------------------------------------------------------------------------------------------------------------------------



# Sets 

set1 = {2}
set2 = {5}
print(type(set1))

# print( set1 + set2 ) 
# Error :- TypeError: unsupported operand type(s) for +: 'set' and 'set'
 # we encounter this error becuase we are not allowed to use Operators for Set Objects



# print( 10 + set1 )
# Error :- TypeError: unsupported operand type(s) for +: 'int' and 'set'
 # we are not allowed to use int and set as an Operand with add operator to perform Operations.



print( set1.pop() + 25 )
# Here we used addition operator for set and int as an Operands


# If we want to use Set as one of the Operand to perform some Operations we have to make use of Appropriate Set methods based on what datatype will the Other Operand will have
 # Make use of Set methods, Make sure to use set methods which returns the Specific datatype which is in the Ohter side of the Operand.  





# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# ChatGPT :-

  # explain me about using Multiple Operands in a Single Line
  # ChatGPT

  # Using multiple operands in a single line typically involves performing multiple operations or combining multiple expressions within a single statement. This can help improve code readability and conciseness. The use of parentheses is crucial to control the order of operations and ensure that expressions are evaluated correctly.

  # Here are some examples illustrating the use of multiple operands in a single line:
  # Example 1: Multiple Arithmetic Operations

  # python

  # # Performing multiple arithmetic operations
  # result = (3 + 5) * 2 - 7 / 4
  # print(result)  # Output: 14.25

  # In this example, the expression (3 + 5) * 2 - 7 / 4 involves addition, multiplication, and division operations. The use of parentheses controls the order of operations.
  # Example 2: Multiple Assignments

  # python

  # # Multiple assignments in a single line
  # a, b, c = 10, 20, 30
  # print(a, b, c)  # Output: 10 20 30

  # This example demonstrates the assignment of values to multiple variables in a single line.
  # Example 3: Combining Operations

  # python

  # # Combining operations in a single line
  # result = (4 + 7) * 3 + 2
  # print(result)  # Output: 29

  # Here, we combine addition and multiplication operations in a single line.
  # Example 4: Multiple Conditions in an if Statement

  # python

  # # Using multiple conditions in a single line
  # x, y = 5, 10
  # if x > 0 and y > 0:
  #     print("Both x and y are positive.")
  # else:
  #     print("At least one of x or y is not positive.")

  # This example demonstrates using multiple conditions in a single if statement.
  # Example 5: List Comprehension

  # python

  # # List comprehension with multiple operations
  # squared_even_numbers = [x**2 for x in range(10) if x % 2 == 0]
  # print(squared_even_numbers)  # Output: [0, 4, 16, 36, 64]

  # In this example, a list comprehension is used to generate a list of squares for even numbers.

  # Using multiple operands in a single line is a common practice in Python programming, especially when expressing concise and readable code. However, it's essential to strike a balance between conciseness and readability to ensure that the code remains understandable and maintainable.





# ----------------------------------------------------------------------------------------------------------------



# Using Multiple Operands in a Single Line


# Multiple Arithmatic operations
# Multiple Assignment Operations
# Combining Operations
# Multiple Conditions in IF statement
# List Comprehensions


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------


# Multiple Arithmatic operations

 # Multipel Arithmatic Operations means where we will be using different Operators in a Single Line of code
  # How the line gets resolve might differ based on the Operators which we use in the line.


Multiple_Arithmatic_operations = 20 + 30 - 35 * 3 / 5
 # if the operator got resolve from left to right the output would have been [9] => 20 + 30 = 50, 50 - 35 = 15, 15 * 3 = 45, 45 / 5 = 9
 
 # How Python acutally evaluates or Resolves the Operations 
 # 1. Multiplication or Division Operators gets Resolved First 
 # 2. Next Addition or Subtraction operation gets resolve  

 # Solution :- 35 * 3 = 105, 105 / 5 = 21, 20 + 30 = 50, 50 - 21 = 29

print( Multiple_Arithmatic_operations ) # Output :- 29.0


Multiple_Arithmatic_operations = 20 + 30 - 35 * 3 / 5 + (50 - 20)
# 50 - 20 = 30, 35 * 3 = 105, 105/5 = 21, 20 + 30 = 50, 50 + 30 = 80, 80 - 21 = 59

print( Multiple_Arithmatic_operations )


Multiple_Arithmatic_operations = 20 + 30 - 35 * 3 / 5 + (50 - 20) % 7
# 50 - 20 = 30, 105, 21, 30 % 7 = 2, 50 + 2 = 52, 52 - 21 = 31

print( Multiple_Arithmatic_operations )


 # How Python acutally evaluates or Resolves the Operations 
 # 1. Brackets get Resolved First
 # 2. Multiplication or Division Operators gets Resolved First 
 # 3. Next Addition or Subtraction operation gets resolve 

# -------------------------------------------------------------------------------------------------------------------------------------------------------


# Multiple Assignements 




variable_1, variable_2, variable_3 = "Value 1", 1000, True

print( variable_1 )
print( variable_2 )
print( variable_3 )




# multiple Funcion assignements

 # Error :- Statements must be separated by newlines or semicolons
  # This error occurs when we try to use multiple functions in a single line which we are not allowed to do.

# def abc(): print("Hello world") def xyz(): 


# multiple Object assignment

 # we are even allowed to assign Multiple Objects (such as List, Dictionary, Tuples, Sets, etc ) to a Multiple Variables in a Single Line.
 # Here the code is messy we cannot able to read the code, This approach might work for Primitive datatypes such as [ string, boolean, number, none, etc ] but for objects this might not work.

 # Here we assigned different objects for a Multiple variables, we can even assigne single datatype of multiple Values for a Multiple Variable.

objectList, objectDictionary, objectTuples, objectSet = [1, True, 'String'], {"key_1": "Value 1", "key_2": 123 }, (100, False, "ABC"), {30, "Hello", True}

print( objectList )
print( objectDictionary )
print( objectTuples )
print( objectSet )

# Output :-
  # [1, True, 'String']
  # {'key_1': 'Value 1', 'key_2': 123}
  # (100, False, 'ABC')
  # {True, 'Hello', 30}



# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# Example 3: Combining Operations

 # here we will be using differen operation, here we will include Grouping Operators also.


# Error :- 
 # combining_operations = 10 + 20 * 15 - 6 (20 * 2) / 50
 #                                           ^^^^^^^^^^
 # TypeError: 'int' object is not callable

# we encounter this error because we did not used any operator between [ 6 and (20*2) ]
# combining_operations = 10 + 20 * 15 - 6 (20 * 2) / 50

combining_operations = 10 + 20 * 15 - 6 + (20 * 2) / 10

# 40, 300, 4 310, 10, 300

print( combining_operations )


print("""





""")

# --------------------------------------------------------------------------------------------------


# Example 4: Multiple Conditions in an if Statement

  # explore Multiple if conditions

  # Write a programm to take part in gaint wheel


a = 10

# here we used 2 conditions in a Single [ if ] statement
if a < 11 and a > 0:
    print("a is Lesser than 11 but greater than 0")
else:
    print("a is not lesser than 11 or greater than 0")




b = 20

# here below we used 3 Conditions in a Single [ if ] statement
if type(b) == int and b < 21 and b > 0:
    print("b is Number datatype, b is lesser than 21 but greater than 0")

else:
    print( "b fails the above conditions" )


# ------------
    
  # Write a programm to take part in gaint wheel
    


def giantFunction():
 
 age = input("Enter your age :- \n")
 age_cast = int(age)

# while loop 
#   when you use while loop inside the if..else statement make sure to check for the condition, if the while loop is falls into infinite loop then make sure to use the while loop outside the if...else statement.


 while True:
    if age_cast < 18:
          parent_permission = input("Do you have parent permission ?, Enter y=yes, n=no")

          if parent_permission == 'y':
                print("You are allowed for the ride")
                break

          elif parent_permission == "n" :
                print("You are not allowed for the Ride")
                break

          else:
                print(f"Make sure you pass either [y] or [n]")

    elif age_cast > 60:
        children_permission = input("Do you have children permission?, Enter y=yes, n=no")

        if children_permission == 'y':
              print('You are allowed for the ride')
              break

        elif children_permission == 'n':
              print("You are not allowed for the ride")
              break

        else:
              print("Enter either [y] for yes , [n] for no")

    elif age_cast > 18 and age_cast < 60:
        print("You are allowed for the ride")
        break
    



# giantFunction()


# ------------------------------------------------------------------------------------------------------------------------------

a = 2

while True:
  if True:
      if a == 1:
            print("A is 1")
            break

      elif a == 2: 
            print("a is 2")
            break

      else:
            print("a is 3")


# ------------------------------------
            

# giantWheel program using recursive function
            

def giantFun():
     
     age = input("Enter the age: \n")
     age_cast = int(age)

     if age_cast < 18:
          parent_permission = input("Do you have parent permission ? [y] for yes, [n] for no")

          if parent_permission == 'y':
               print("You are allowed for the Ride")

          elif parent_permission == 'n':
               print("You are not allowed for the Ride")

          else:
               giantFun()
     elif age_cast > 60:
          
          children_permission = input("Do you have children permisson ? [y] for yes, [n] for no")

          if children_permission == 'y':
               print("Children allowed you for the ride")
            
          elif children_permission == 'n':
               print("Children not allowed you for the ride")

          else:
               giantFun()

     else:
          print("Perfect Age you are allowed for the RIDE")     




# giantFun()




# ----------------------------------------------------------------------------------------------------------------------------------------------------------------


# Example 5: List Comprehension

 # List comprehension means using Loop(for in, etc) or iterating elements inside the List
          

# List Comprehension Syntax 
          
  #  [ new_list = [expression for item in iterable if condition]  ]



squared_number = []

for x in range(5):
    #  x = x * x
    #  squared_number.append(x)
     squared_number.append(x ** 2), # this syntax is a Power of syntax x ** 2

print( squared_number )


# ---------


squaredNumber = [ num ** 2 for num in range(5) ]


# syntax Breakdown
 # num ** 2 
  # here we used power of a Number the above syntax is equavalent to the below codes 
   # num = num * num 
   # num = pow(num, 2)

 # for num in range(5) 
   # This is the for loop,where we will loop over the values

print( squaredNumber )


# ------------------

# when you come across above syntax visualise as if you are using for loop and inside the loop you are appending the values inside the List

list_comprehension = [ num ** 3 for num in range(5) ]
print( list_comprehension )

# how the above code gets resolved

# 1 - A list datatype with empty values will be created with the name called [ list_comprehension ]
list_comprehension = []

# 2 - for..in loop will be created with the range value of 5
for x in range(5):
     # 3 - power of the number will be created
     x ** 2 # equal to x = x * x
       # 1 [ x = 1 * 1 ], 2 [ x = 2 * 2 ], 3 [ x = 3 * 3 ], 4 [ x = 4 * 4 ], 5 [ x = 5 * 5 ], .....

     # 4 - x value will get appened inside the [ list_comprehension ] list, for every run of this loop based on range value.
     list_comprehension.append( x )



# 5 The value will get printed
     
print( list_comprehension )



# Using [ if...else ] statment inside the loop 


 # from 1 to 10 print only odd numbers

# odd_values = [ n for n in range(10) if n % 2 == 0 ]
odd_values = [ n for n in range(10) if n % 2 == 0 ]
# Error :- 
 # "[" was not closed 
  # This error occurs when we fail to use [ n ], which is initialisation of Variable n
 # "[" was not closed 
   # error occurs when we fail to use [for...in loop]

print( odd_values )
# Output :-  [0, 2, 4, 6, 8]


# -------


# Visualisation of the above code 

# 1 Initilisation of List named ( odd_values )
odd_values = []

# 2 use [for...in] loop with the range value of 10
for x in range(10):
     
     # 3. inside the loop use [if..else] conditional statement
     if x % 2 == 0:
          
          # 4. Append the 'x' values which is an odd number inside the [ odd_values ] list
           # odd number - when we divide x with 2 --> the reminder is 0 ---> then those numbers are Odd numbers
          odd_values.append(x)

# 5. finally we printed the value
print( odd_values )

# Output :-  [0, 2, 4, 6, 8]



# -------------------

# There are 3 Types of List Comprehensions 

 # 1. Basic List Comprehension:

 # 2. List Comprehension with Condition:

 # 3. Nested List Comprehension:



  #  Nested List Comprehension:


# 2D matrix transposed using nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = [[row[i] for row in matrix] for i in range(3)]
# Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


print( transposed_matrix )

# --------




# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Here we learnt about what happens when we use Different Datatypes for different operands 




















