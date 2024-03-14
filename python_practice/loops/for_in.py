
# For in Loop 

# There are mainly 2 Types of Loops in Python 

# 1. for..in loop

# 2. while loop


 # Here we will be Learning about [ for..in ] loop


# What is a Sequence ?
 # Sequence is the other name for Iterable Objects or Values,





# Loops are mainly used to Iterate Sequences or Iterable Objects such as [ lists, tuples, strings, range, etc. ]


# for in loop with [ list ]
# for in loop with [ tuples ]
# for in loop with [ strings ]
# for in loop with [ range ]
# for in loop with [ sets ]
# for in loop with [ Custom Objects ]

# Break
  # This will stop the Loop execution at the line / place the [break] keyword,The place where we use [Break] keyword those codes which comes next to the [break] keyword will no be executed. 

# Continue 
  # continues keyword will only th specific value for which we use [continue] which is even present inside the Iterable Objects or Values.



# -----------------------------------



# for..in loop with [ strings ] datatype 

forInString = "This is a For in String"

# The below "while" loop will run for till the end of the strings length,
 # This while loop will even include White space characters also. 
for x in forInString:
    print(x)

# Output :-
    # T
    # h
    # i
    # s
    
    # i
    # s
    
    # a
    
    # W
    # h
    # i
    # l
    # e

    # S
    # t
    # r
    # i
    # n
    # g



print("""




""")

# ------------------------------------------------------------------
    


# for..in loop with [ list ] datatype 

 # here we are allowed to iterate List which has multiple datatype values, if we are able to iterate multiple datatype values we can even iterate Single datatype which has multiple values

list_type = [ 1, "string", False, ["list value"], {"set value"} , {"key": "dictionary value"}, ("Tuple value"), None,  ]



 # here let us use [ for...in ] loop to iterate the values
  # what happens - all the values inside [ list_type ] will be stored inside [ variable_name_to_store_iteratedValue ] , now if we want to modify the [ original list ] we can use [ variable_name_to_store_iteratedValue ] and modify the Original list 
for variable_name_to_store_iteratedValue in list_type:
    print( variable_name_to_store_iteratedValue )


 # Output :-
    
        
    # 1
    # string
    # False
    # ['list value']
    # {'set value'}
    # {'key': 'dictionary value'}
    # Tuple value
    # None






print("""




""")

# ------------------------------------------------------------------


# for..in loop with [ Tuples ] datatype
 
  # we can even use while loop to Iterate (Tuples ) datatypes, even Tuples are Iterable Object

tuple_forin_loop = (1,2,3,4,5)

print( tuple_forin_loop )

 # here we have used [for..in] loop to iterate a [Tuple] datataypes.
for tupleDatas in tuple_forin_loop:
    print( tupleDatas )


# tuples with multiple datatype values

#  tupleMultipleDatatype = ( 1, "string", False, None, [1,2], ("a", 55),  )
 # Error :- Unindent amount does not match previous indent
  # this error occurs when we fail to give proper indendations
    
    
tupleMultipleDatatype = ( 1, "string", False, None, [1,2], ("a", 55), ":--------- Tuples with Multiple values" )

for tupleMultiType in tupleMultipleDatatype:
    print(tupleMultiType)


# Output :-
    
    # 1
    # string
    # False
    # None
    # [1, 2]
    # ('a', 55)
    # :--------- Tuples with Multiple values

# we are even allowed to iterate a Tuple which has multiple datatype values



print("""




""")

# ------------------------------------------------------------------


# for..in loop with [ sets ] datatype

set_forin_type = {"set value", 44, True, ( "I am Tuple", 2) }


# here let us use [ for..in ] to iterate the Sets Element

for setValues in set_forin_type:
    print( setValues )



# set which has [ dictionary, list and nested set ] as its values then let us try to iterate
    
    # If a Set have any of the following Datatype, if we want to iterate the Set in such situation we cannot able to Iterate the values
     # Dictionary
     # Nested Set
     # List
    # if the set which we are tring to iterate has any ofthe above datatype values inside above datat inside the set we cannot able to Iterate the Value, when we try to iterate we might end up getting below errors.

# multiple_setValue = { [1], [2,3, "string Value"], {3}, {4,5, "string"}, {"key": "value"}, {"key1": "Value", "key2": "value 2"} }   # Error :- TypeError: unhashable type: 'list'

# multiple_setValue = {  [2,3, "string Value"], {3}, {4,5, "string"}, {"key": "value"}, {"key1": "Value", "key2": "value 2"} }  # Error :- multiple_setValue = {  [2,3, "string Value"], {3}, {4,5, "string"}, {"key": "value"}, {"key1": "Value", "key2": "value 2"} } , TypeError: unhashable type: 'list' 

# multiple_setValue = { {3}, {4,5, "string"}, {"key": "value"}, {"key1": "Value", "key2": "value 2"} } # { {3}, {4,5, "string"}, {"key": "value"}, {"key1": "Value", "key2": "value 2"} },  TypeError: unhashable type: 'set'

# multiple_setValue = {  {4,5, "string"}, {"key": "value"}, {"key1": "Value", "key2": "value 2"} } # Error :- {  {4,5, "string"}, {"key": "value"}, {"key1": "Value", "key2": "value 2"} },            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   TypeError: unhashable type: 'set'

# multiple_setValue = { {"key": "value"}, {"key1": "Value", "key2": "value 2"} }  # { {"key": "value"}, {"key1": "Value", "key2": "value 2"} }            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  TypeError: unhashable type: 'dict'

# multiple_setValue = { {"key1": "Value", "key2": "value 2"} }  # multiple_setValue = { {"key1": "Value", "key2": "value 2"} }            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ TypeError: unhashable type: 'dict'




# for multiTypeSet in multiple_setValue:
#     print( multiple_setValue )




# -------------------------------------------------------------
    
    # for....in loop used to iterate [ range() ] function values


for rangeForIn in range(10):
    print(rangeForIn)


# Output :-
    
    
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9


# Here we Iterated [ range(10)] function using [ for in loop], range() function will keep executing the value till the End of the Range
    

  # range() with list iterations
    
range_list = [1, False, "hello", None, {}, [], ()]

for rangeIteration in range( len(range_list) ):
    print( rangeIteration )



# for rangeIteration in range( range_list ):
    # Error :- TypeError: 'list' object cannot be interpreted as an integer
      # this error occurs when we try to pass list or other datatype where the expression expects Number datatype, which we are not allowed to do, that is why error has been occured.
    # print( rangeIteration )



# -------------------------------------------------------
    
# Custom Objects (Implementing Iterable or Iterator Protocol):
    
    # Custom Objects means where we will be creating a Custom class and defining [ __iter__() ] function, which decides how the iteration has to happen or perform when we try to use some Iteration from the Instance Objects.


class MyIterable:

    # Here we create a Class constructor which will accept 1 arguement which will be an Iterable object, the variable name is [data]
    def __init__(self, data):
        self.data = data

     # here we defined [ __iter__() ] this function can be used how an iteration has to be performed, when we use Iterations codes such as [for..in, while] loops the code has to be Executed
      # here we try to iterate [ data ] which the value we took as an Arguement.
    def __iter__(self):
        return iter(self.data)

my_iterable = MyIterable([10, 20, 30]) # Here we passed List iterable object as an arguement

# Here we tried to iterate the [my_iterable] which is an instance object of [ MyIterable() ]
for item in my_iterable:
    print(item)



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    

    # ChatGPT 


    #     User
    # python loops
    # ChatGPT

    # In Python, loops are used to repeatedly execute a block of code until a certain condition is met. There are two main types of loops in Python: for loops and while loops.
    # 1. for Loop:

    # The for loop is used for iterating over a sequence (that is either a list, tuple, dictionary, string, or range). Here's the basic syntax:

    # python

    # for variable in sequence:
    #     # code to be executed

    # Example:

    # python

    # fruits = ["apple", "banana", "cherry"]
    # for fruit in fruits:
    #     print(fruit)

    # This will output:

    # apple
    # banana
    # cherry

    # 2. while Loop:

    # The while loop is used to repeatedly execute a block of code as long as the given condition is true. Here's the basic syntax:

    # python

    # while condition:
    #     # code to be executed
    #     # update condition to eventually exit the loop

    # Example:

    # python

    # count = 0
    # while count < 5:
    #     print(count)
    #     count += 1

    # This will output:

    # 0
    # 1
    # 2
    # 3
    # 4

    # break and continue Statements:

    #     break: Terminates the loop and transfers control to the statement immediately following the loop.

    # python

    # for i in range(10):
    #     if i == 5:
    #         break
    #     print(i)

    # This will output:

    # 0
    # 1
    # 2
    # 3
    # 4

    #     continue: Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.

    # python

    # for i in range(5):
    #     if i == 2:
    #         continue
    #     print(i)

    # This will output:

    # 0
    # 1
    # 3
    # 4

    # These are the basics of loops in Python. They are fundamental for controlling the flow of your program and executing repetitive tasks.
    # User
    # what are different types of Loops which are there in Python Programming language
    # ChatGPT

    # In Python, there are mainly two types of loops: for loops and while loops.

    #     for Loop:
    #         The for loop is used to iterate over a sequence (such as a list, tuple, string, range, or other iterable objects).
    #         Syntax:

    #         python

    # for variable in sequence:
    #     # code to be executed

    # Example:

    # python

    # fruits = ["apple", "banana", "cherry"]
    # for fruit in fruits:
    #     print(fruit)

    # Output:

    #     apple
    #     banana
    #     cherry

    # while Loop:

    #     The while loop is used to repeatedly execute a block of code as long as a specified condition is true.
    #     Syntax:

    #     python

    # while condition:
    #     # code to be executed
    #     # update condition to eventually exit the loop

    # Example:

    # python

    # count = 0
    # while count < 5:
    #     print(count)
    #     count += 1

    # Output:

    #         0
    #         1
    #         2
    #         3
    #         4

    # These are the primary types of loops in Python. Additionally, Python also provides control statements like break and continue to modify the behavior of loops:

    #     break Statement:
    #         It terminates the loop and transfers control to the statement immediately following the loop.
    #         Example:

    #         python

    #     for i in range(10):
    #         if i == 5:
    #             break
    #         print(i)

    # continue Statement:

    #     It skips the rest of the code inside the loop for the current iteration and moves to the next iteration.
    #     Example:

    #     python

    #         for i in range(5):
    #             if i == 2:
    #                 continue
    #             print(i)

    # These loops and control statements provide flexibility and control over the flow of your Python programs.
    # User
    # provide list of datatypes in which we can use for and while loops
    # ChatGPT

    # In Python, for and while loops can be used with various data types, including:

    #     Lists:
    #         Example with for loop:

    #         python

    #     fruits = ["apple", "banana", "cherry"]
    #     for fruit in fruits:
    #         print(fruit)

    # Tuples:

    #     Example with for loop:

    #     python

    #     colors = ("red", "green", "blue")
    #     for color in colors:
    #         print(color)

    # Strings:

    #     Example with for loop:

    #     python

    #     message = "Hello, World!"
    #     for char in message:
    #         print(char)

    # Ranges:

    #     Example with for loop:

    #     python

    #     for i in range(5):
    #         print(i)

    # Dictionaries (with keys or values):

    #     Example with for loop:

    #     python

    #     student_grades = {"Alice": 95, "Bob": 87, "Charlie": 92}
    #     for name, grade in student_grades.items():
    #         print(f"{name}: {grade}")

    # Sets:

    #     Example with for loop:

    #     python

    #     numbers = {1, 2, 3, 4, 5}
    #     for number in numbers:
    #         print(number)

    # Custom Objects (Implementing Iterable or Iterator Protocol):

    #     You can create your own classes that implement the iterable or iterator protocol, allowing the use of loops with custom objects.

    # Example with for loop (assuming a custom iterable class MyIterable):

    # python

    # class MyIterable:
    #     def __init__(self, data):
    #         self.data = data

    #     def __iter__(self):
    #         return iter(self.data)

    # my_iterable = MyIterable([10, 20, 30])
    # for item in my_iterable:
    #     print(item)

    # Boolean Data Types (using while loops):

    #     While loops can be used with Boolean conditions, allowing for dynamic iteration until a certain condition is met.

    # Example with while loop:

    # python

    #     count = 0
    #     while count < 5:
    #         print(count)
    #         count += 1

    # These examples showcase the versatility of for and while loops with various data types in Python. The ability to iterate over different types of data structures makes Python a flexible and expressive programming language.

































