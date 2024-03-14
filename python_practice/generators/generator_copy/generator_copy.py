

# Better Pattern to use Generators 

# Here we will be Creating a Generator Function by using [yield ] keyword


# 



def generatorFunction(n):
    # For each iteration which is done using generator instance, the statements which are present inside the function will get executed.
    for i in range(n):
        yield i ** 2
        print("m")

       
# When we Invoke a Function which has [ yield ] keyword the Instance Object will have a Generator Object (Class)
  # Invocation of any Function which has yield keyword will be a Generator Object
generatorInstance = generatorFunction(5)

print( type(generatorFunction) )

print( type(generatorInstance) )


for i in generatorInstance:
    print(i)



# Output :- 
    # <class 'function'>
    # <class 'generator'>
    # 0
    # m
    # 1
    # m
    # 4
    # m
    # 9
    # m
    # 16
    # m


print("""



""")

# -----------------------------------------------------------------------------------------------------------------
    

def generate():
    yield 10
    yield 20
    yield 30
    yield 40

instanceGenerate = generate()

print( next(instanceGenerate) )
print( next(instanceGenerate) )
print( next(instanceGenerate) )
print( next(instanceGenerate) )

# Error :- [ StopIteration ]
# when we try to call [ next() ] method for where there is no yield value or all the yield values are finished executing and there is no yield to be executed.

# print( next(instanceGenerate) )

# Output :-
    # 10
    # 20
    # 30
    # 40





# Learnings :-
# 1. Here from the above example we can clearly see that the [ yield ] function keeps the track of internal state ( what value has to be printed currently ) untill it hits the next keyword 
# 2. for each [ yield ] keyword we have the program gets paused untill we call the [next()] method next time, For each [ yield ] keywords, we have to call the [ next() ] based on how many yield keyword is present inside the function.
# 3. Generator Functions are Infinite, it keeps running for Infinite times.




print("""


""")


# -----------------------------------------------------------------------------------------------------------------------------------------------------


# Let us check the size of values which is present inside the list and generators 


import sys

def generatorFun(n):
    for i in range(n):
        yield i ** 2

x = [ i ** 2 for i in range(10000)]
g = generatorFun(10000)

print( sys.getsizeof(x) )
print( sys.getsizeof(g) )

# Output :- 
    # 85176
    # 200

# Here we can see that the that the Size of the list [x] is bigger as well as size of gerator [g] is smaller
 # when we try to to printe [x] and [g] it will ultimately print the same values, but when it comes to storage in memory List have stored more memory space
  # generator used less memory space, by this way we can run the generator function for infinite times 




print("""


""")


# -----------------------------------------------------------------------------------------------------------------------------------------------------



# [ Practice ]


def generateFunctions(n):
    for i in range(n):
        yield i

# since this function will return generator class let us store it in a variable
        
instanceGeneratorFunctions = generateFunctions(5)

next(instanceGeneratorFunctions)
next(instanceGeneratorFunctions)

for i in instanceGeneratorFunctions:
    print(i)



print("""



""")




# -----------
    

# generator functions without using loops inside it
    


def generatorWithoutLoop():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    yield 7
    yield 8
    yield 9
    yield 10
    yield 11
    yield 12


# There are 2 ways to access values which is inside [ generatorWithoutLoop ] function
    # 1. [ next(generatorFunction_InstanceObject) ]
    # 2. Using [ for in ] loop



# 1. [ next(generatorFunction_InstanceObject) ]

# print( instance_generatorWithoutLoop )


instance_generatorWithoutLoop = generatorWithoutLoop()

print( next(instance_generatorWithoutLoop) )
print( next(instance_generatorWithoutLoop) )
print( next(instance_generatorWithoutLoop) )

# For each and every [ yield ] value which is present inside the inside the [ Generator Function ] we have keep calling [  next(instance_Generator) ]
 # this is a Lengthy process

# Ouput :- 
    # 1
    # 2
    # 3


print("""



""")


# ----------------------


#  # 2. Using [ for in ] loop 
 
  # What happens when we use [ for in ] loop for generator functions

def generator_loops():
    yield 1
    yield 2
    yield 3
    yield 4
    yield "string"
    yield 6
    yield 7
    yield 8
    yield 9
    yield 10


# let us create an Instance for generator function

instance_generator_loops = generator_loops()    


# Now let us use for loop to print the values inside the generator function
    

for i in instance_generator_loops:

    # Here the datatype of [i] will keep changing based on what value is present inside the specific yield which we called or accessed
    print(type(i))
    print( i )


# When we use [ for in ] loop to print the generator instance values ?
    # When using loops to print the values inside the generator instance object, our python interpreter will goes inside the loop and calls [ next( instance_object ) ] method based on the Length of "yield" values which is present inside the Function 
     # using [for in] loop will call the [ next() ] method behind the scene
    
# Behind the scene how will above [for in ] loop will look ?


# print( next(instance_generatorWithoutLoop) )
# print( next(instance_generatorWithoutLoop) )
# print( next(instance_generatorWithoutLoop) )
# print( next(instance_generatorWithoutLoop) )
# print( next(instance_generatorWithoutLoop) )
# print( next(instance_generatorWithoutLoop) )
# print( next(instance_generatorWithoutLoop) )
# print( next(instance_generatorWithoutLoop) )
# print( next(instance_generatorWithoutLoop) )
# print( next(instance_generatorWithoutLoop) )
























































