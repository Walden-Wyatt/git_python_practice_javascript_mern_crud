


# Immutable 

# Here we will be learning about Mutable Objects Datatype 

# Mutable objects are those Objects which are once Created it's values cannot be changed or modified 
 # Every time you create an Object using Mutaable Datatype there will be New Object gets created in the Memory 
 
# Re-assginment 
 # When you try to re-assign Mutable and Immutable objects a New Object gets created in the Memory.

# Hashable 
 # When you create a Key for a Dictionary it is an Hashable



# ------------------------------------------


# How Immutable Objects works 

# How Mutable Objects word 

# How Mutable and Immutable Objects work when we use it as a Function Parameter 



# -----------------------------------------------------------------------------------------------------------------------------------------------------



# How Immutable Objects works 

# Primitive Types :-
# strings, numbers, booleans, None, 

# Complex Types :-
 # Tuples, frozenset, range(), ENUM




# Let us create an object which has Mutable Values ?

Immutable_string = "Mutable String Value"

print(Immutable_string)

# Here now [ Immutable_string ] variable holds a mutable value
 # python will create a new object in the memory and assigns [ "Mutable String Value" ] as a value for that object


# Here what happens is that we created [ Immutable_string ] and assigned a value, where we also created [ Immutable_string ] above and assigned the values
 # Now what happens is that python will create a New object with the name [ Immutable_string ] and assigned a value, the [ Immutable_string ] object which we created above will be deleted from the Memory by using garbage collection 
  # by doing garbage collection our memory space will be so that we can create new values in the memory.

Immutable_string = "New Modified Values"
print(Immutable_string)



# -------------------------------------

  # what happens when we assign a variable will other variable which has Mutable values 

originalVariable = "Original Variable Mutable values"

newVariable = originalVariable

print( newVariable )


# Now what has happend is that ?
 # python creates 2 new Objects in the Memory that is for [ originalVariable and newVariable ] changes which we make in either of object will not affect other objects
 # When we assign new variable of mutable values to other variables, in this case other variables will be created with new object reference in the Memory



# -------------------------------------


# Mutable Objects with other mutable datatypes

tupleImmutable_object_1 = ( 1, True, "tuple string", [1,2,3], {"key": "value" } )


# here we have re-assigned value for [ tupleMutable_object ], we did not tried bo modify the tuple values
 # In this case Python will create a New Object ---> stores in the Memory ---> previous values with the same variable name will get Deleted ( Garbage Collected )
  # here now the newly assigned values will be mutable string type value
tupleImmutable_object_1 = "New Tuple object value"

print( tupleImmutable_object_1 )



tupleImmutable_object_2 = (1, "string", None,[1, 2, 3] )

# we can access Tuple values by using [ index positions ]


# tupleImmutable_object_2[2] = "New values"

# Error :- 
    # File "C:\Users\user\Desktop\python_practice\mutable_immutable\mutable.py", line 98, in <module>
    #     tupleMutable_object_2[2] = "New values"
    #     ~~~~~~~~~~~~~~~~~~~~~^^^
    # TypeError: 'tuple' object does not support item assignment

# When we get Errors related to [ item assignment ] which means we are tring to modify the [ Immutable Object Datatype values ]
 # because tuple is a mutable object we cannot change individual values inside the tuples sequence
 # if we directly call the tuple variable and change which means we are trying to re-assign the values, when re-assignment out entire Tuple values will get changed as well as when we try to re-assign value are allowed to change the values of the variable 
   # when values are re-assigned which means previous variables instance will get garbage collected ( deleted ).



# -------------------------------------



print("""



""")


# --------------------------------------------------------------------------------------------------------------------------------------------------------


# Mutable Objects 


mutableObject_list = [1, "string", False, [1,2], None ]

print( mutableObject_list )

# Now python will create an new object with the reference name called [ mutableObject_list ] in the Memory

# Let us try to re-assign [ mutableObject_list ] value 


# Here we have re-assigned the Value for [ mutableObject_list ], we did not mutated the values
mutableObject_list = "New MutableObject Re-assigned"
print( mutableObject_list )

 # In the above case what python does is that, it will take the [ mutableObject_list ] variable name and creates New Object in the Memory, the Objects type might differ based on values which we passed. 
  # mutableObject_list = "New MutableObject Re-assigned
  # since we have re-assigned the values of [ mutableObject_list ] previous values of [ mutableObject_list ] will get deleted or garbage collected from the Memory.




# ---------------------------------



mutableObject_list_2 = [ 1, 2, 3, 4, 5 ]


# Here we have mutated the values of [ mutableObject_list_2 ], which means we are tring the get the values from the reference and change it 
 # once the values gets changed python will check in the memory where it has space to store this values, it goes over there and stores the values.
mutableObject_list_2[2] = "New String values"
# even though we have modified the values, we did not got any errors

print( mutableObject_list_2 )


print("""




""")

# ---------------------------------


# Let us create a Mutable Object which will and assign the same to other variables 

mutableObject_list_assignement = [1, 2, 3, 4, 5]

mutableObject_list_reassignement = mutableObject_list_assignement

print( mutableObject_list_assignement )
print( mutableObject_list_reassignement )


# Now let us try to change values of [ mutableObject_list_assignement ] and check what happens in [ mutableObject_list_reassignement ] ?

mutableObject_list_assignement[2] = "String Value"

# now let us print [ mutableObject_list_reassignement, mutableObject_list_assignement ] objects


print( mutableObject_list_assignement )
print( mutableObject_list_reassignement )


# Output :-

    # [1, 2, 'String Value', 4, 5]
    # [1, 2, 'String Value', 4, 5]

 # here if see that we made changes inside [ mutableObject_list_assignement ] but the same changes also happened inside [ mutableObject_list_reassignement ]
  # that is at index [ 2 ] value from [3] got changed to [ "String Value" ]



# Now let us change values in [ mutableObject_list_reassignement ] and check what happens in [ mutableObject_list_assignement ]

mutableObject_list_reassignement[3] = {"key": "values"}


print( mutableObject_list_assignement )
print( mutableObject_list_reassignement )

# Output :-

    # [1, 2, 'String Value', {'key': 'values'}, 5]
    # [1, 2, 'String Value', {'key': 'values'}, 5]


 # here if see that we made changes inside [ mutableObject_list_reassignement ] but the same changes also happened inside [ mutableObject_list_assignement ]
  # that is at index [ 3 ] value from [4] got changed to [  {"key": "values"} ]


# Leanings :-

 # In mutable objects Reference will be stored when we assign it other values in the Memory 
 # when we assign One Mutable value to another variable which means other variable will hold the reference of the previous mutable values

 # What happens when we assign variable which has mutable values to anther variable ?
  # In this case both the variable names will point the same values 
  # Both the variables will have the same reference 
  # When we make any changes in one Variable it also affects the other variables
  




# -------------------------------------------------------------------------------------------------------------------------------------------------------

 # What actually happens in python incase of Mutable and Immutable objects ?


# 1st - creation of variables 
# 2nd - python checks what value is present inside the variable, 
  # if the values are immutable ( string, boolean, tuples, numbers, etc )
  # then python will create a space in the memory and store this values 
   # this values cannot be modified, we can only re-assign this values
  # tring to modify [tuple] will give you an error [ item assigment ]

 # Think suppose we have created a variable[ x ] which has Immutable values, we create New variable [y] and assign this variable[x] what happens in this case ?
  # in this case python will create new object with the variable name called [y], where both the reference(address) will be different
  # the changes which we make on one variable [x or y] will not affect the other variables[ x or y ], because both has unique reference (address)
  # this is Immutable object 



# 3rd - if the values are Mutable [ lists, dictionary, sets, etc ]
  # if the values are Mutable, python will create a space to store values and stores those values
  # Mutable objects are [ sets, dictionaries, lists, etc ]
  # We are allowed to modify the values which are inside Mutable objects 
  
 # Think suppose we have created a variable[ x ] which has Mutable values, we create New variable [y] and assign this variable[x] what happens in this case ?
   # In this case python will not create a New object for variable[ y ] it will
   # Python will only create Alias [Other name ] for those mutable objects, what ever values which are present inside [ x ] will also be present inside [ y ]
    # Think it like a value which has 2 variable names
   # when we try to make changes in either of the Variables it will also applies those changes to the other variables 
    # Ex: changes made inside variable [x] will also makes changes inside variable [y], as well as changes made inside variable [y] will also make changes inside variable [x]



print("""




""")



# -------------------------------------------------------------------------------------------------------------------------------------------------------




# How Mutable and Immutable Objects work when we use it as a Function Parameter 


 # In function also its the same python will check the values which we passed in the parameters, based on what value are there python will decide weather it has to be mutable or not



def mutable(params):

    # behind the scene python will create a variable called [params] and store the parameter values inside this varialbe 
    # this variables are locally scopted which means we are not allowed to access it outside the function

    # here we created [ params_2 ] and stored [ params ] as values
    params_2 = params

    print( params )
    print( params_2 )




# let us invoke the function
    
mutable("string value")

 # what happens for [ params and params_2 ] when we pass string dataype as values ?
  # what python does is that inside the functions local scope python will create a New object for [ params and params_2 ] where both the reference (address) will be unique
  # for [ params ] it will store whatever values which we passed as an arguement 
  # for [ params_2 ] it will take the values from the [ params ] ----> checks weather the values are mutable or not 
   # if the value is mutable it will create an alias name for the value which means there will be only one value but 2 variable, where both the reference will be same
   # when we try to access any of the values from either of the variables python will go to the same reference (address ) gets the values and displays 
   # if we make changes in any of the either of the variables python will go to the same referenc (address ) updates the changes / modifications and stores
   
   # if the values are Immutable 
   # Python will create 2 new object reference that is for [ params and params_2 ] 
   # for [ params ] it will store the values which we passed as an arguement
   # for [ params_2 ] it will store the values which is present inside [ params ]
   # since both the value is Immutable object both the reference will be different 
    # changes made in one variable[params] will not affect other variable[params_2] because both the references are different 
    # we cannot able to directly modify the primitive datatypes,we can only re-assign the values. when we re-assign the values previous instance of variable will get garbage collected.
    # in case of tuples tring to modify by using index position will throw error [ item assignment ]


# in the above function since we passed String value which is an Immutable object there will be 2 new Objects created [ params and params2 ] both the reference (address) will be completely different.
















