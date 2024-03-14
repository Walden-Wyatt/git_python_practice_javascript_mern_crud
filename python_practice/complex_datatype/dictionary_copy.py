

# Dictionary 

# Here we will be Learning about Dictionaries

# There are 2 ways to Create a Dictionaries 

 # 1. Constructor Syntax 

 # 2. Literal Syntax 




# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Constructor Syntax 


dictionary_constructor = dict()

# The arguement for [ dict() ] will be a Keyword Arguement, This Keyword arguement will be stored as properties for a Dictionary Object behind the scene
dictionary_constructor = dict( key="value", key2="value 2" )

print( dictionary_constructor )
print( type(dictionary_constructor) )




# ----------------------------------------------------------------------------------------------------



# Dictionary Literal Syntax :-


# We cannot directly create a Method inside the Dictionary but we can create a Function from outside then pass the reference to the Object Properties

dictionary_literal = {

    # Here we can see that the [ Key_Value ] pairs of a Dictionary must be wrapped with String literals, It looks somewhat like a JSON object

    "property_1": "Value 1",
    
}
print( dictionary_literal )




print("""


      

dictionary Method
      



""")




# How to  create a Method inside the Dictionary

# Here we have method which has been defined outside the Dictionary 
def dictionary_method_1():
    return "Dictionary method"



dictionary_method = {

    "property_1": "Value 1",

    # Here we have passed the Reference of the Method to create a method inside the Dictionary.
    "method_1": dictionary_method_1

}

# Accessing Dictionary Values
print( dictionary_method )

# There are 2 Types of Methods and Properties 

 # 1. Built-in Methods and Properties
  # To access Built-in Methods and Properties we can use Dot Notation ( . )

 # 2. Custom Methods and Properties 
  # To accsess Custom Methods and Properties we can use Index Operator ( [] )
print( dictionary_method["property_1"] )

# [ <function dictionary_method_1 at 0x0000023A07A1A2A0> ] = here we have method reference.
print( dictionary_method["method_1"] )


# here we can see at the end of the method we use parenthsis (), this is to invoke the Method 
print( dictionary_method["method_1"]() )





print("""




Built-in Methods and Properties of Dictionary




""")



def dictionary_method():
    return "Dictionary Method"



dictionary_builtIns = {

    "props": "Property value",
    "method": dictionary_method

}


# ---------------------


# Here we have Custom Methods and Properties 

print( dictionary_builtIns )

print( dictionary_builtIns["props"] )

print( dictionary_builtIns["method"]() )



print("""





""")


# ---------------------



# Here we have Built-in Methods and Properties


# [ clear() ] = this method will create all the Methods and properties which are inside the Dictionary Object
  # this method will not return any value
# dictionary_builtIns.clear(), 
print( dictionary_builtIns )




# [ copy() ] - this method will return a dictionary object which will be exactly same as original object
 # this method will not return any value
dictionary_copy = dictionary_builtIns.copy()
print( dictionary_copy )





dictionary_builtIns = {

    "key_1": "Value 1",
    "key_2": "Value 2", 
    "key_3": "value 3",
    "key_4": "value 4"

}

# [ fromKeys(iterable_listOf_keys , FixedValue_for_those_keys )  ]
 # This method will create a new Dictionary from the key list which we have provided, 2nd arguement which we pass will be value for all those keys,if we fail to pass 2nd arguement then None value will be set to all the Keys.
dictionary_fromkeys = dictionary_builtIns.fromkeys(["key_1", "key_3"], ["Fixed Value", 25] ) 
dictionary_fromkeys = dictionary_builtIns.fromkeys(["key_1", "key_3"], "Fixed Value" ) 

print( dictionary_fromkeys )
# Output :- {'key_1': 'Fixed Value', 'key_3': 'Fixed Value'}





dictionary_builtIns = {

    "key_1": "Value 1",
    "key_2": "Value 2", 
    "key_3": "value 3",
    "key_4": "value 4"

}


# [ get() ]
# This method will Return the value for key if key is in the dictionary, else default.
 # this method will accept 1 arguement that is the Key name of the dictionary
dictionary_key = dictionary_builtIns.get("key_1")
print( dictionary_key )






print("""




""")



dictionary_builtIns = {

    "key_1": "Value 1",
    "key_2": "Value 2", 
    "key_3": "value 3",
    "key_4": "value 4"

}



# [ items() ]
 # this method will return a Method call [ dict_items() ] there will be a list of Tuples which will be stored as value
dictionary_items = dictionary_builtIns.items()
print( dictionary_items )
# Output :-  dict_items([('key_1', 'Value 1'), ('key_2', 'Value 2'), ('key_3', 'value 3'), ('key_4', 'value 4')])







print("""




""")



dictionary_builtIns = {

    "key_1": "Value 1",
    "key_2": "Value 2", 
    "key_3": "value 3",
    "key_4": "value 4"

}

# [ keys() ]
 # This method will return a function invokation [ dict_keys() ] where the arguement will be List of keys from the dictionary object all the Keys which are present inside the Dictionary object
dictionary_keys =  dictionary_builtIns.keys()
print( dictionary_keys )






print("""




""")



dictionary_builtIns = {

    "key_1": "Value 1",
    "key_2": "Value 2", 
    "key_3": "value 3",
    "key_4": "value 4"

}

# [ pop() ]
 # this method will remove a specific Property from the Dictionary object based on the Key value which we pass.
#   this method will return the value of the removed item
dictionary_pop = dictionary_builtIns.pop("key_2")
print( dictionary_builtIns )
print( dictionary_pop )






print("""




""")



dictionary_builtIns = {

    "key_1": "Value 1",
    "key_2": "Value 2", 
    "key_3": "value 3",
    "key_4": "value 4"

}


# [ popitem() ]
 # this method will remove the Properties/attributes/key_value pairs from the End of the Dictionary, those removed key_value pairs will be stored inside the Tuples and returned as a value.
dictionary_popitem =  dictionary_builtIns.popitem()
print( dictionary_popitem )  # Output :- ('key_4', 'value 4')
print(  dictionary_builtIns )  # Output :- {'key_1': 'Value 1', 'key_2': 'Value 2', 'key_3': 'value 3'} 






print("""




""")



dictionary_builtIns = {

    "key_1": "Value 1",
    "key_2": "Value 2", 
    "key_3": "value 3",
    "key_4": "value 4"

}



# [ setdefault( Default_key, Default_value ) ]
 # This method will set a Default Key and Value inside the Dictionary, if such method or property is not defined inside the Dictionary in such situation this Default key_value pairs will be inside the Dictionary.
dictionary_builtIns.setdefault("default_key", "Value as Default")
print( dictionary_builtIns )

# Output :-
 # {'key_1': 'Value 1', 'key_2': 'Value 2', 'key_3': 'value 3', 'key_4': 'value 4', 'default_key': 'Value as Default'}
  # inside the original object we cannot able to see [ 'default_key': 'Value as Default' ]






print("""




""")



dictionary_builtIns = {

    "key_1": "Value 1",
    "key_2": "Value 2", 
    "key_3": "value 3",
    "key_4": "value 4"

}



# [ update(Keyword_arguement=updated_value)  ]
 # This method accepts 1 arguement which is a keyword arguement, here we have provide property/attribute/key name as well as Updated value for that specific keys
 # this method will not return any Value, it will return [ None ] value.


dictionary_update = dictionary_builtIns.update(key_2="New value")
dictionary_update = dictionary_builtIns.update(key_3=112334)
# Output :- {'key_1': 'Value 1', 'key_2': 'New value', 'key_3': 112334, 'key_4': 'value 4'}

print( dictionary_builtIns )

print( dictionary_update )






print("""




""")



dictionary_builtIns = {

    "key_1": "Value 1",
    "key_2": "Value 2", 
    "key_3": "value 3",
    "key_4": "value 4"

}


# [ values() ]
 # this method will return a List of Values which is present inside the Dictionary, this will only return the values this will not return any keys
  # if you want to access only Values we can use [values() ] method

dictionary_values = dictionary_builtIns.values()
print( dictionary_values )

# Output :- dict_values(['Value 1', 'Value 2', 'value 3', 'value 4'])




# -------------------------------------



# Other Methods and Properties are inherited from Object Class





# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------





# [ Practise 2 ]



 # Dictionary Constructor Syntax 

def d_method():
    return "Dict method"
dicts = {
    "props": "Value",
    "method": d_method
}

print( dicts )
print( dicts["props"] )
print( dicts["method"]() )



# --------------------------------------------------------------------------------


dictss = {
    "props": "Value"
}


dictss.clear()
print( dictss )

dictss = {
    "props": "Value", 
    "props2": "Value 2", 
    "method": d_method
}

d_copy = dictss.copy()
print( d_copy )



dictss_fromkeys = dictss.fromkeys(["key1","key2", "k3y3"] , "Fixed Value" )
print( dictss_fromkeys )


dictss_get = dictss.get("props")
print(dictss_get)


dictss_item = dictss.items()
print( dictss_item )

dictss_key = dictss.keys()
print( dictss_key )

dictss_pop = dictss.pop("props2")
print( dictss_pop )
print( dictss )


dictss_popitem =dictss.popitem()
print( dictss_popitem )


dictss.setdefault("default key", "default value")
print( dictss )


dictionary_update = dictss.update(props2="####  ---> New Value")
print( dictionary_update )
print( dictss )


dictionary_values = dictss.values( )
print( dictionary_values )
print( dictss )






# ------------------------------------------------------------------------------


# Dictionary Methods and  Properties Remembering

# [ 2cfgik2psuv ]




# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# Dictionary Static Methods

# This method will return the Method resolution order
dict_mro = dict.mro()
print( dict_mro )

# Output :- [<class 'dict'>, <class 'object'>]





# Accessing Methods from List Constructor Function

# When you use [ List ] Methods from Set Constructor Object, The First Arguement for all the  Methods should be List Instance Object so that the Method will perform appropriate Operations which the List method has to perform.












