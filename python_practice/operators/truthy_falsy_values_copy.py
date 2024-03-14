


# truthy_falsy_values



# ChatGPT Explanations :-


    # comprehensive, in-depth and in-detailed explanations on Truthy value and Falsy values in python programming language
    # ChatGPT

    # Truthy and falsy values in Python refer to the way that values are interpreted in boolean contexts, such as in if statements or boolean operations. Understanding truthy and falsy values is crucial when dealing with conditions and logical expressions. Let's dive into comprehensive explanations:
    # Truthy Values:

    # In Python, a value is considered truthy if it evaluates to True in a boolean context. All values are considered truthy except for a few specific cases. Some common examples of truthy values include:

    #     Non-zero numerical values: Any non-zero number is considered truthy.
    #     Non-empty sequences: Lists, tuples, strings, and other sequence types are truthy if they have at least one element.
    #     Non-empty dictionaries: Dictionaries are truthy if they have at least one key-value pair.
    #     Custom objects: Objects you create can be truthy if they define the __bool__() or __len__() method.

    # python

    # if 42:
    #     print("This is truthy!")

    # Falsy Values:

    # Conversely, a value is considered falsy if it evaluates to False in a boolean context. Common examples of falsy values include:

    #     Zero numerical values: The integer 0, floating-point 0.0, and complex 0j.
    #     Empty sequences: Lists, tuples, strings, and other sequence types are falsy if they are empty.
    #     Empty dictionaries: An empty dictionary is falsy.
    #     Special constants: None is falsy.
    #     Boolean False: The boolean value False is, obviously, falsy.

    # python

    # if 0:
    #     print("This is falsy!")

    # Truthiness in Conditions:

    # In conditional statements like if, while, and or, truthy values are treated as True, and falsy values are treated as False. This allows for concise and expressive code:

    # python

    # value = some_function_returning_a_value()

    # if value:
    #     print("The value is truthy!")
    # else:
    #     print("The value is falsy!")

    # Using Truthy and Falsy in Expressions:

    # Truthy and falsy values are frequently used in concise expressions. For example, using the or operator to provide a default value:

    # python

    # result = user_input or "default_value"

    # If user_input is truthy, result takes that value; otherwise, it defaults to "default_value".

    # Understanding truthy and falsy values is fundamental for writing clean, expressive, and effective Python code, especially when dealing with conditions and logical operations.





 # Here we will be learning about Truthy and Falsy values.

# Truthy Values 

 # 1. Boolean True
 # 2. Non-empty string
 # 3. non-zero number
 # 4. non-empty dictionary
 # 5. custom objects 
 # 6. [ __bool__(), __len__() ] methods
 # 7. not False ( Not False )
 # 8. Negative Number
 # 9. "0" - string with Zero
 # 10. not None



# Falsy values

 # 1. Boolean False
 # 2. 0
 # 3. Empty string
 # 4. empty dictionary
 # 5. not True ( Not True )
 # 6. None
 # 7. Empty Sequences - Lists, Tuples, Strings, and Other Sequence types 




# -----------------------------------------------------------------------------------



# Truthy Values 

# Non-empty string
print( bool( "Non Empty String" ) )

# non-zero number
print( bool( 2 ) )

# print( bool( 1,2,3,4,5,6,7,8,9 ) )
# Error :- when we pass more than 1 arguement for [ bool ]

# boolean True
print( bool( True ) )

# non-empty dictionary
print(  bool( {
    "key": "value",
    "key_2": "value 2"
} ) )

# non-empty List
print ( bool( [1,2,3,4] ) )

# non-empty Tuples
print( bool( (1,2,3, 4) ) )

# non-empty set
print( bool( {"hello", 3} ) )

# Not False
print( bool( not False ) )

print( "The Negative Number", bool(-1) )


print( bool("0") )






# -----------------------------------------------------------------------------------------

print("""


""")

# Falsy Values


# 1. Empty String
# 2. Zero
# 3. Boolean False
# 4. Empty Dictionary 
# 5. Empty List
# 6. Empty Tuples
# 7. Empty Set
# 8. not True (Not true)
# 9. None
# 10. 
#
#




# 1. Empty String
print( bool("") )


# 2. Zero
print(bool(0))

# 3. Boolean False
print(bool(False))

# 4. Empty Dictionary 
print( bool({}) )
print( type({}))
# when you use Flower brackets with any value inside it,it will be treated as a [ Dictionary ], when you use some value based on the value Python will evaluate the Expression weather it is a [ Dictionary or Set ]

# 5. Empty List
print(bool([]))

  # if a list have a single value, where the value is a Falsy value still the Expression is considered as a Truthy Value.
   # below we can see that the list which has 1 value, where the value is a Falsy value
print( bool([0]) )
print( bool([""]) )

# 6. Empty Tuples
print( bool( () ) )

 # Incase of Tuples, when a Tuple have a only one value where that value is a Falsy value in such situation the Expression is considered to  be Falsy Value 
print( bool( (False) ) )
print( bool( (0) )  )

 # if tuple have more than 1 value, where all the values are Falsy values in such situation the Expression is considered to be Falsy value even though the Values inside the Tuple are Falsy values
print( bool( (0, False, ~True, ) ) )

 # When Tuple have Mixture of Truthy and Falsy or just Truthy in both the cases the Tuple Expression is considered as [ Truthy Value ]


# 7. Empty Set
 # Based on what value we pass inside the Flower brackets python will evaluate the Expression, 
   # if we use [ key_value ] pairs inside the Flower brackets then the Expression is evaluated as [ Dictionary ]
   # if we use [ non Key_value ] pairs inside the Flower brackets then the Expression is evaluated as [ Set ]
  # here we used [ non key_value ] pairs that is why the Expression is evaluated as a Set
print(type({1})) 

# when a Set has Empty value, it is evaluated to be Falsy value as well as it is treated a Dictionary.
print( bool( {} ) )

# when we pass a single value for the set where the single value is of Falsy value, the set expression is evaluated as Fasly value, 
 # if the set has more than 1 values where all the values are Falsy in such case set is evaluated as Falsy value only. when set has mixture or all the values to be truthy even in that case Set is evaluated to be Truthy value.
print( bool({False}) ) 
print( bool({False, 0}) ) 


# 8. ~True (Not true)
  # Preceeding [ not ] operator before Boolean True is considered as Falsy value.
print( bool( not True ) )

# 9. None
  # None Datatype is treated as Falsy value in python
print( bool(None) )

# 10. 
#



# -------------------------------------------------------------------------------------------------------------------------------------------------




# What is Negating ?
 # Negating means making a Truthy Values to be Falsy.



# -------------------------------------------------------------------------------------------------------------------------------------------



# Truthy and Falsy values using Conditional Statements 

t_value = True

# The below [if] statement will check for Value, only if the value is matched exactly the statement inside the [if ] block gets printed, else not
if t_value == True:
    print('This will check the Value of the Variable, Weather the Variables values is Exactly Matched.')

# The below [if] statement will check weather the Value of the Variable is Truthy or Falsy, but will not check weather the Exact value by matching each and every character by its sequences.
if t_value:
    print("This will check Truthy or Falsy Value")



# ----
    


# in the below 2 if statement only 2nd if statement value got printed where are 1st if statements are not printed thats because 1st if statement checks for value not the Truthiness
t2_value = 2

if t2_value == True:
    print("This is the Falsy check" )

if t2_value:
    print( "This is the Truthy Check" )





# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


print("""



      
Practise 2 
      



""")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# [ Practise 2 ]
    
    # Truthy Value and Falsy Value


 # Truthy Values 
    
    # 1. string
    # 2. int
    # 3. float
    # 4. boolean True
    # 5. non zero numbers
    # 6. non empty dictionary
    # 7. non empty sequence [ lists, tuples, sets, strings ]
    # 8. not False
    # 9. List with Single value weather it is Truthy or Falsy, Multiple values Truthy or Falsy
    # 10. Tuples with single Truthy value or Multiple values which is Falsy
    # 11. Sets with single Truthy or Falsy as well as Multiple Truthy or Falsy values are considered to be Truthy values.
    # 12. Dictionaries with Non-empty values.
    # 13. Preceeding [ not ] operator before all the Falsy valuse will be Truthy Values.



print( bool( "string" ) )

print( bool( 11 ) )

print( bool( True ) )

print( bool( not None ) )

print( bool( {"key_1": "value 1"} ) )

print( bool( [1] ) )

print( bool( [ 0 ] ) )

print( bool( [1, 2] ) )

print( bool( (1) ) )

print( bool( (0, False) ) )

print( bool( {0} ) )

print( bool( {0, False, not True } ) )

print( bool(not None) )


print("""




""")

# ----------------------------------




# Falsy Values


 # 1. False

 # 2. Preceeding [ not ] operator before Truthy Values 

 # 3. 0

 # 4. Empty String

 # 5. None

 # 6. Empty Dictionary

 # 7. Empty Lists

 # 8. Empty Tuples

 # 9. Empty Sets

 # 10. Empty 

 # 11. Preceeding Double [ not ] operator for [ Falsy ] values

 # 12. 




print( bool( "" ) )

print( bool( 0 ) )

print( bool( 0.0 ) )

print( bool( False ) )

print( bool( None ) )

print( bool( not not None ) )

print( bool( {} ) )

print( bool( [] ) )

print( bool( [] ) )

print( bool( () ) )

print( bool( (0) ) )

# print( bool( (0, False) ) )

print( bool( {} ) )

# print( bool( {0} ) )

print( bool( not True ) )




print("""




""")

# -------------------------------------------------------------------------------------------




data = True

if data == True:
    print("Hello True Variable Value")

if data:
    print( "Truthy Value" )




# The reason why the below 1st if block got printed is because [ False and 0 ] both are same in terms of programming
data = 0


# Now below both the [ if ] block statements will not get printed because both the if block condition is False or Falsy.
data = None

if data == False:
    print("Wow, Value not Same")

if data:
    print("This is Truthy Value")











































