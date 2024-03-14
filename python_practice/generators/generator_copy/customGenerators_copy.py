



# How to create a Custom Generator Function

# Here we have [ Gen ] class
class Gen:

    # [__init__() ] 
     # This is used to initialize and get the Value from the Constructor
    def __init__(self, n):
        self.n = n # [n] is the Variable which can be used to store how many times the values has to be executed
        self.last_currentValue = 0  # [ last_currentValue ] is used to store the current state value. 

    # [ __next__() ]
      # [ __next__() ] will keep executing the program untill it the Iteration count is met, once if every values got iterated finnaly the program ends
         # For each and every iteration this program will not store the Previous values, this method will keep deleting the previous values, it only stores current values in the Memory.
    def __next__(self):
        return self.next()
    
    
    # [next() ] - this is a Custom Method.
    def next(self):
        if self.last_currentValue == self.n:
            # [ StopIteration() ] will stop the iteration, even if we run these [next()] from inside the [for or while ] loop this will stop the iteration
            raise StopIteration()
        rv = self.last_currentValue ** 2 # here we use exponential(power of 2 ) and store the values
        self.last_currentValue += 1 # here we kept incrementing the [ last_currentValue ] value so that it reaches the base case and condition get false that is ( if self.last_currentValue == self.n: )
        
        # Here we have returned [ rv ], here rv value will keep on changing, Here rv will store only the current value which comes from each iteration, it will not store the previous Or Future(next) values in the iteration
         # By doing these we can we keep romoving the previousle Executed values and try to store current values, By this way we can iterate value of any ( reguardless of how big the number is )
         # becuase if each iteration, this program will store only the current values (how much ever current values size is only that much space will be occupied in the RAM memory ) as this method keeps removing the previously executed values.
        #  This Operation is done by [ __next__() Dunder method ].
        return rv 


g = Gen(10)


# Here we have used Loops to Iterate the Generator values 
while True:
    try:

        # [ next(Generator_class_instance) ]
         # Return the next item from the iterator. If default is given and the iterator is exhausted, it is returned instead of raising StopIteration
         # when we calle [next()] method it will go inside [ __next__() ] and starts executing the statements,
         # inside this method we have use custom Methods to modify what has to be done during the iterations 
          # [ next() or __next__() ] methods only job is the execute the statements which is present inside and once it is executed those code or iteration value has to be removed from RAM memory.
        print( next(g) )
    except StopIteration:
        break





# Learnings 
 # we can run the Generator functions Infinitely we will not encounter any Problems
 # We can use the above code to run the code infinetely
    
# What is the better pattern for the above code
    
    # The Better apporach of using Generator function is Defining a custom Function which has [yield] keyword


def generatorFunction(n):
    for i in range(n):
        yield i ** 2

g = generatorFunction(10)

for i in g:
    print(i )




print("""



""")





# -------------------------------------------------------------------------------------------------------------------------------------------------------------
    


# There are 2 Approachs in which we can access the yield values from a Function 
    
    # 1. using [ next(instance_generatorObject) ] 
    # 2. using [ for in ] loops




 # [ Approach 1 ]

    # 1. using [ next(instance_generatorObject) ] 

def generatorNext_method():
    yield 1
    yield [1,2,3,4]
    yield True
    yield "String"
    yield {"key": "values"}


# Here let us have Instance Object 

instance_generatorNext_method = generatorNext_method()

print( next( instance_generatorNext_method ) )
print( next( instance_generatorNext_method ) )
print( next( instance_generatorNext_method ) )


# using [ next() ] we have to manually call [ next() ] Function  for all the [yield] values which is present inside the Yield function
# Python program remembers which "yield" value has been accessed lastly so that when we try to access the "yield" next time somewhere in the program we will get next Yield value which is present inside that specific Instance object (function) 

 # To check for individual values we can use this appraoch 



# --------------------------------------------------------------------------------------------



# [ Approach 2 ]

    # 2. using [ for in ] loops

 # Here we will be using [for in] loop to iterate over the yield values which is inside the Yield Function


def generator_approach2():

    yield 1
    yield [1,2,3,4]
    yield True
    yield "String"
    yield {"key": "values"}
    yield (1,2,3,4)
    yield None
    yield {"set value"}
    yield "wow,string"


# Here let us create an instance object for [ generator_approach2 ] function 
    
instance_generator_approach2 = generator_approach2()


for i in instance_generator_approach2:

    # Based on the Length of the Yield values which is present inside the [yeild function] the values will be returned.
     # Behind the scene python will stop once the Yield values have come to an End, [for in] loop will not go beyond the yield values it will exactly stop at the end of the yield
       # By this way we can easily overcome the [ StopIteration() ] errors.
    print( i )

    # Based on what datatype value does the current Yield has the same datatype will be returned, when we try to use the Yield current occurance of the Yield value will be returned.
    print( type(i) )



# Output :-
    
    # 1
    # [1, 2, 3, 4]
    # True
    # 1
    # <class 'int'>
    # [1, 2, 3, 4]
    # <class 'list'>
    # True
    # <class 'bool'>
    # String
    # <class 'str'>
    # {'key': 'values'}
    # <class 'dict'>
    # (1, 2, 3, 4)
    # <class 'tuple'>
    # None
    # <class 'NoneType'>
    # {'set value'}
    # <class 'set'>
    # wow,string
    # <class 'str'>


# behind the scene python will call [ next(instance_generatorObject) ] for every yield values which are inside the Generator Function
 # loop will automatically iterate the Yield Function and Prints the values
    
 # It will like we using the below lines of code :-
    
# next(instance_generator_approach2)
# next(instance_generator_approach2)
# next(instance_generator_approach2)
# next(instance_generator_approach2)
# next(instance_generator_approach2)
# next(instance_generator_approach2)
# next(instance_generator_approach2)
# next(instance_generator_approach2)
# next(instance_generator_approach2)


print("""



""")






# ---------------------------------------------------------------------------------------------------------------------------------------------------



# What happens when we use [for in] loop inside the Generator Function ?
    
def generatorLoopInside_function():

    for i in range(10):
        yield i


    # what happens when we use [for in] loop and try to use [ yield ] keyword with values inside the loop
        
      # How code will look behind the scene ?
        
        # def generatorLoopInside_function():

        #     yield 1
        #     yield 2
        #     yield 3
        #     yield 4
        #     yield 5
        #     yield 6
        #     yield 7
        #     yield 8
        #     yield 9

    # This is how python will create a [ generatorLoopInside_function()  ] function behind the scene.

    



# instance object for [ generatorLoopInside_function ]
        
instance_generatorLoopInside_function = generatorLoopInside_function()


# Now let us iterate the Yield values

for i in instance_generatorLoopInside_function:
    
    print( i )



# ---------------------------------------------------


# Steps to keep in mind while creating an Yield ?
    
 # 1. Create a Function with any name and use reason parameters
    
 # 2. Use [yield] keyword then next to keyword pass the values
   # a. you can either use [yield] keyword manually 
   # b. we can also use [yield] keyword inside a function
    
 # 3. Create an Instace Object by calling the Generator Function
      # this will return [ Generator ] object, store it inside an instance variable
      # Only when we create an Instace Object we can access the [yield] values which is present inside the [ Yield function ]
    
 # 4. Access the [yield] functions by using instance object
    # There are 2 ways to access
    # 1. using [ next()  ] method 
       # Syntax :- [ next( instanceObject_Generator_Function ) ]
    # 2. using [ for in ] loop
      # use [ for in ] loop and iterate the Yield values which is inside the Function.
       




# ---------------------------------------------------------


# Memory size Check for [ list ] and yield functions
    

import sys
    
listValues = [ i ** 2 for i in range(10000) ]


def generatorSizeCheck(n):
    for i in n:
       yield i



instance_generatorSizeCheck = generatorSizeCheck(10000)


# here let us check [ listValues and instance_generatorSizeCheck ]

# here we checked for [ listValues ] variable 
print( sys.getsizeof( listValues ) )


# here we checked for [ instance_generatorSizeCheck ] generator function
print( sys.getsizeof( instance_generatorSizeCheck ) )


# Output :-

    # 85176
    # 192


# here we can see that the 1st value ( listValues ) have occupied [85176] kb of space, where as ( instance_generatorSizeCheck ) have occupied [ 192 ] kb of space in the RAM which is less 
 # by this we can learn that Generator function will occupy less space in the memory by deleting the previous executed values, other values will get garbage collected
 # By using Generator function we can loop throught the Values which is Infinite , even if we have infinite values we can loop it using generator, where generator will not throw any errors
 # Generator function will not throw any Errors such as [ recurrsiveError, or StopIterationError() ], because there will not be such situation where the RAM is full because generators will execute the code and deletes it from memoery once it got executed
 # By using Generator we will not encouter any error which says Memory is full, memory in RAM is full we cannot able to execute further or next lines of code



# ---------------------------------------------



# Important Points :-
    
 # 1. We can use any datatypes as a Value for [yield], the datatype can  be a [ String, Number, boolean, None, Dictionary, list, sets, tuples, etc  ]
 # 2. [yield] function will only store the Current Value into the memory, but will not store those values which has already been executed
     # a. The values which are already been executed will be garbage collected.
    

































