

# Advanceed Concepts 


# Create a Class Inside a Class

 # We are allowed to create a Class inside another Class
 # This can be done if we want a Seperate section to hold certain Datas as well as those datas are not used outside the Class.


# When you create a Class inside another class then it becomes a metaclass


# There are 2 ways to Create a Class

 # 1. Using Regular Class Syntax
 # 2. Using [ type("className" , (Inheriting_class), {"key": "values"} ) ] class


 # Meta class is nothing but changing the Structure of a Original Class



# ----------------------------------------------------------------------------------------------------------------------------------------------------




class RegularSyntax:
    def __init__(self):
        return None

print( type(RegularSyntax()) )
print( type(RegularSyntax) )


# Output:-
#  <class '__main__.RegularSyntax'>
#  <class 'type'>

# Class is an Object we can create a Class inside the [ Functions ]
# In class everything is an Object, which is created using some other Object

# print( type(RegularSyntax) )
#  <class 'type'>

 # When we create a Class it is an Object, Since it is an Object The Main class for all the Classes are [ type ]
  # so when we create a Class we are ultimately calling the [ type ] class constructor 
  # Inside the [ type ] class there will be a Method called [ __new__ and __init__ ] which gets invoked 



# How to create a Class Object using type() function which is Ultimate Parent class for all the Classes which we create 

# The below both the Syntax are one and the Same
# class Test:
#     x =  "Value"

Test = type( "Test", (), {"x": "Value"} )

instance_Test_Object = Test()
print( instance_Test_Object )
print( instance_Test_Object.x )


print("""




""")


# ------------------------




# How to do Inheritance using [type()] function ?

class ParentClass:
    def method1(self):
        print("Hello Method")

InheritClass = type( "InheritClass", (ParentClass, ), {"key": "Value"} )


# Instance Object 

instance_InheritClass = InheritClass()

print( instance_InheritClass )
print( instance_InheritClass.key )

# accessing Inherited values [ parent class values ]

instance_InheritClass.method1()


# Output :-

    # <__main__.InheritClass object at 0x0000015E22CFA840>
    # Value
    # Hello Method

# Now we got Proper Output without any Errors.



# -------------------------------------------------------


# How to pass a method inside a Class ?


def classMethod(self):
    print("Class Method Function")


ClassMethod = type( "ClassMethod", (), {"key": "Value", "method": classMethod } )

# create Instance Object 

instance_ClassMethod = ClassMethod()

# access [ instance_ClassMethod ]
print( instance_ClassMethod.key )
instance_ClassMethod.method()


# Output :-

    # Value
    # Class Method Function

# We got proper output without any error.


print("""

""")


# --------------------------------------------------------------------------------------------------------------------------------------------------


# Meta Class 

# Metaclass is Class which is above the Class which we create and Returns the Same class with modified version
# [ type ] 
 # [ type ] is a MetaClass, This is a Built-in Metaclass in Python programming language


class Meta(type):

    # This is first Method which gets called when we create an Instance Object
     # [ __new__() ] method is used to Construct the Object and return the newly constructed object.
    def __new__( self, class_name, bases, attributes ):
        print( class_name )
        print( bases )
        print( attributes )

        return type( class_name, bases, attributes )



class Dog(metaclass=Meta):
    x = 5
    y = 9


# d = Dog()


# even if do not create an Instane the below output will be Printed.

# Output :-
 
    # Dog
    # ()
    # {'__module__': '__main__', '__qualname__': 'Dog', 'x': 5, 'y': 9}




# -------------------------------------------------------------------------------------------------------------------------------------------


# How to Iterate a Dictionary using [ for ] loop ?


dictionary = {
    "key1": "Value 1",
    "key2": "Value 2",
    "key3": "Value 3"
}


print( dictionary )
# print( dir( dictionary ) )

print( dictionary.items() ) # Items will return List of Tuples

# If you want to Iterate List of Tuples we can use the Syntax 
for key, value in dictionary.items():
    print(key, value )

# Syntax Breakdown :
    
 # [ for ] - for is a keyword 
 # [ key ] - key the the key of dictionary, This key will be stored inside the tuples, this will have all the 1st elements of the Tuples 
 # [ value ] - value is the value for the keys inside the dictionary, this value will be stored as a 2nd value for the tuples, value will have all the elemnts of 2nd values of a tuples 
 # [ in ] - in a Keyword which is used to check the values  inside the List
 # [ dictionary.items() ] = [items() ] method will return a list of tuples, which will have all the [ Key, Value ] pairs.


print("""



""")



# --------------------------------------------------------------------------------------------------------------------------------------------------------
    

class MetaClass(type):
    def __new__(self, class_name, bases, attributes):
        print(attributes)

        a = { }

        for key, value in attributes.items():
            if key.startswith("__"):
                a[key] = value
            else:
                a[key.upper()] = value
       # Here we have constructed an object 
        print(a)
        return type(class_name, bases, a )


class ChildMeta(metaclass=MetaClass):
    x = "X Value"
    y = "y Value"

    def method():
        print("Method value")




instance_ChildMeta = ChildMeta()

print( instance_ChildMeta )

# print( instance_ChildMeta.x )
# Error : AttributeError: 'ChildMeta' object has no attribute 'x'. Did you mean: 'X'?
 # this error occurs when we tried to access [ x ] variable which is not present inside the [ instance_ChildMeta ] instance object, now attributes have changed.

print( instance_ChildMeta.X )
print( instance_ChildMeta.Y )

print( type( instance_ChildMeta ) )
print( type( ChildMeta ) )
print( type(MetaClass) )



# Output :-

    # {'__module__': '__main__', '__qualname__': 'ChildMeta', 'x': 'X Value', 'y': 'y Value', 'method': <function ChildMeta.method at 0x000001BD2D1C94E0>}
    # {'__module__': '__main__', '__qualname__': 'ChildMeta', 'X': 'X Value', 'Y': 'y Value', 'METHOD': <function ChildMeta.method at 0x000001BD2D1C94E0>}
    # <__main__.ChildMeta object at 0x000001BD2D1DC710>
    # X Value
    # y Value
    # <class '__main__.ChildMeta'>
    # <class 'type'>
    # <class 'type'>


# Points to Remember ?
 # 1. The custom class ( ex: x_class ) which is used to create Custom Meta class, this custom class type will be [ type ]
 # 2. The custom class ( ex: y_class ) which has [ metaclass ] arguement which defining the Class, This custom class datatype will also be [ type ]
   # when we invoke [ y_class ] and check the Instance Objects type the datatype will point to [ y_class]


print("""



""")




# -----------------------------------------------------------------------------------------------------



# [ Practice 2 ]

# Steps :-

 # 1. create a Class with any name, This clas must Inherit [ type ] class, otherwise it will not be a Custom Metaclass it will be class created from [type] class
 # 2. [ __new__(self, class_name, bases_inheriting_classes, attribute_object_syntax ) ]
    # inside [ __new__() ] method we will be Constructing the New Class 
     # this is the first method which gets invoked when we create and Instance object, This method is also called as "before init method".

    # [ return ] - this method will return a [type() ] by passing appropriate Arguements,  which will then return a Newly Constructed Object
    # we can try to access the folloing variables [ className, bases, attribute_object_syntax ] from inside [ MetaClassCustom ] class.

 # 3. Create another class which will make use of the Custom Metaclass [ ex: y_class]
    # When creating this class use [ metaclass=CustomMetaClass ] as a 1st Arguement
    # you can define Methods and Properties inside this class, based on code which has been used inside the [ __new__() ] method of [ MetaClassCustom ] New Modified Class will be Created

 # 4.  Create an Instance object for [ ex: y_class ]
 # 5. try to access Methods and Attributes of [ ex: y_class ], check weather the returned or printed are right without any error, if there is no error which means everything worked perfectly fine.


class MetaClassCustom(type):

    def __new__(self, className, bases, attribute_object_syntax ):
        print( className )
        print( bases )
        print( attribute_object_syntax )

        return type( className, bases, attribute_object_syntax )


# Now let a Create a Class which will make use of [MetaClassCustom] as a value for [ metaclass ]
    
 # method for [ UseMetaClassCustom ] class 
def methodUseMetaClassCustom(self):
        print("Method Use Meta Class Custom")

    
class UseMetaClassCustom( metaclass=MetaClassCustom ):
    key_property = "Value 1"
    key_property_2 = "Property Value 2"
    key_property_3 = "Property Value 3"
    key_method = methodUseMetaClassCustom



# Let us create an Instance Objecct 
    
instance_UseMetaClassCustom = UseMetaClassCustom()
print( instance_UseMetaClassCustom )
print( instance_UseMetaClassCustom.key_property )
print( instance_UseMetaClassCustom.key_property_2 )
print( instance_UseMetaClassCustom.key_property_3 )
instance_UseMetaClassCustom.key_method()



# Output :-


    # UseMetaClassCustom
    # ()
    # {'__module__': '__main__', '__qualname__': 'UseMetaClassCustom', 'key_property': 'Value 1', 'key_property_2': 'Property Value 2', 'key_property_3': 'Property Value 3', 'key_method': <function methodUseMetaClassCustom at 0x0000016B32B19300>}
    # <__main__.UseMetaClassCustom object at 0x0000016B32B2D010>
    # Value 1
    # Property Value 2
    # Property Value 3
    # Method Use Meta Class Custom




# ------------------------------


# How to Match beweent he Below Syntax ?


# Type_Class = type("Type_Class", (inherit_parents), {"key_Property": "value", "key_method": "function reference" } )

# class Type_Class(inherit_parents):
#     key_Property = "value"
#     key_method = "function reference"



# Here 
 
  # 1. Type_Class -
    # 1st arguement, This is the Name of the class

  # 2. (inherit_parents) 
    # 2nd arguement must be a Tuple where we can pass Inheriting Classes ( Parent classes ), the class has to be used by the Child Class 

  # 3. { "key_Property": "value", "key_method": "function reference" } 
    # 3rd Arguement must be a Dictionary which will, where the key value pairs will be converted as a class variables and methods behind the scene while creating a Class





# --------------------------------------------------


# Point to Remember ?

 # Everytime we Create a Class inside the Python file, Those Class will be Constructed by using the [ __new__() ] method which is present inside [ type ] class
  # what ever rules or construction syntax which has been specified inside the [ __new__() ] method will be used exactly to construct the class.



























