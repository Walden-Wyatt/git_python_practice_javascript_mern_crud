

# Dataclasses 

# Here we will be learning Dataclasses in Python 




string_type = "Old string value"

print(string_type)

string_type = "New value"

print(string_type)




# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# Dataclasses 

# Here we will be Learning on what is dataclasses in Python 

from dataclasses import dataclass 


# Error:-
    #  from dataclasses import dataclass
    #     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # ImportError: cannot import name 'dataclass' from partially initialized module 'dataclasses' (most likely due to a circular import) (C:\Users\user\Desktop\python_practice\classes\dataclasses\dataclasses.py)

 # When we try to Import dataclasses Module from inside [ dataclasses.py ] file we will get this error
  # when you are tring to import dataclasses module do not use [ dataclasses.py ] as a File name because it will have clash with the Original [ dataclass ] module
  # when you are tring to use any Module inside the file, make sure you do not use same Module Name as a File Name if you use you will get the above error.



@dataclass
class Point:
    x: int
    y: int 


instance_point = Point(x=1, y=2)

print( instance_point )


# 1. [ init() ] - Initializes the object and  assigns the Provided values to the attributes
# 2. [ repr() ] - Provides a string representation of the object 
# 3. [ eq() ] - Implements equality comparison between two objects of the class based on their attributes 



print("""




""")

# ---------------------------------------------





class Person:

    def __init__(self, name:str, age):
        self.name = name 
        self.age = age 


person_1 = Person("John", 33)

print( person_1 )





print("""




""")

# ---------------------------------------------



# How to Create a Class by setting up Datatype for constructor Parameters 


class ClassWith_Datatype:
    def __init__(self, paramStr: str, paramInt: int):
        self.paramStr = paramStr 
        self.paramInt = paramInt


# now let us Create an instance object for [ ClassWith_Datatype ]
        
instanceClassWith_Datatype = ClassWith_Datatype("string value", 100)
print( instanceClassWith_Datatype )


# Output :-
 # <__main__.ClassWith_Datatype object at 0x000002A4E00FAFF0>
 # Here we have created a class by setting up Datatype for Class Constructor Parameters 


# What happens when we pass Arguement values which is of other datatype than what we have specified ?

instanceClassWith_Datatype_otherValues = ClassWith_Datatype([1,2,3], 100)
print( instanceClassWith_Datatype_otherValues )

  # Here when we pass other datatype values than what we have specified, in such situation still the class instance will get created and we can even access the values 
   # There will not be any errors, we can access all the [ attributes, variables and Methods ] of the Class 

print( instanceClassWith_Datatype_otherValues.paramInt, instanceClassWith_Datatype_otherValues.paramStr )





print("""




""")


# ---------------------------------------------


# Actual Dataclass practice 


# dataclass which has parameter with default values 


# dataclass with Immutable Variables, Making a class immutable using [ Frozen=True ]


# Dataclass with Inheritance, just inheriting the parent class


# Nested Dataclasses, we can use One dataclass inside other dataclass 




# -----------------------------------------------------------------


from dataclasses import dataclass



@dataclass
class HelloWorld:

    # Error :- "attribute_param_1" is not defined
     # This error occurs when we try to create an attribute without specifing Datatype for the attribute 
    
    # attribute_param_1

    attribut_param_1: str
    attribut_param_2: int


# Let us create an Instance for [ HelloWorld ] class :- 

 # The Arguement value for [HelloWorld() ] class must be the Attributes which we have specified inside the [ HelloWorld ] class.
    # The value for this must match with the datatype which we have specified for the attributes, even though if we pass wrong datatype values there will not be any issues or errors 
      # we can able to access those Values from the instance objects.
    # Based on the Order of creation of Attributes, the arguement value which we pass will be assigned.

instance_HelloWorld = HelloWorld( "Arguement 1", 123 )
print( instance_HelloWorld )


# Output :-
 # HelloWorld(attribut_param_1='Arguement 1', attribut_param_2=123)


 # Points :-
 # usually when we try to access the values of the Instance object, we will get the the address where the instance object has been stored 
  # ex :-  <__main__.Person object at 0x000001C3ED3EB080>

# But when we create a Class and access the Instance object we will get object with string version
 # Ex: # HelloWorld(attribut_param_1='Arguement 1', attribut_param_2=123)
 # This is done by python [ @dataclass ] behind the scene by using the dunder method called [ __repr__() ] 

 # Here we can also see even though we did not created a class [ __init__() ] method still we are allowed to call the constructor method, this is because behind the scene this dataclass gets created.



# Other 2 dunder methods features will also be used inside this dataclass by default :-
 # [ __init__() ] - Initializes the object and  assigns the Provided values to the attributes
 # [ __str__() ] - Provides a string representation of the object 
 # [ __eq__() ] - Implements equality comparison between two objects of the class based on their attributes 
 # [ __repr__() ] - Provides a string representation of the object




# -----------------------------------------------------------------



# Mutable Dataclasses 

 # Mutable dataclasses are those class where we can change or Modify the [ variables, methods and attributes ] after the class creation
  # By default all the Classes, custom Instance objects are Mutable where we can change the values of the  [ variables, methods and attributes ]

from dataclasses import dataclass

@dataclass

class Mutable_dataclass:
    x: str 
    y: int
    z: list


# Here let us create the instance of [ Mutable_dataclass ] 
    
instance_Mutable_dataclass = Mutable_dataclass("string value", 100, [1,2,3] )

print( instance_Mutable_dataclass )

# Output :-
 # Mutable_dataclass(x='string value', y=100, z=[1, 2, 3])

# here let us try to change or modify the [ x, y, z ] attributes 

instance_Mutable_dataclass.x = "Modified x value"
instance_Mutable_dataclass.y = "y got changed"
instance_Mutable_dataclass.z = "Modified z"

print( instance_Mutable_dataclass )

# Output :-
 # Mutable_dataclass(x='Modified x value', y='y got changed', z='Modified z')

# From the above 2 instance object we can see that 2 occurance of [ instance_Mutable_dataclass ] variables such as [ x, y, z ] have got changed 
 # From this we can learn that dataclass variables can be changed and mutable 



print("""


""")

# -----------------


# Now let us create Class where the [ variables, attributes and methods ] cannot be changed [ Immutable Dataclass ]

  # @dataclass(frozen=True) 

from dataclasses import dataclass

@dataclass(frozen=True)
 # [ frozen=True ] - when you use (frozen=True) which means the Instance objects which we create from that specific dataclasses we are not allowed to modify or make changes using Instance Objects.
class ImmutableDataclass:
    p: str 
    y: int


# Here let us create the instance of [ ImmutableDataclass ] 
    
instance_ImmutableDataclass = ImmutableDataclass( "String value", 1000 )

print( instance_ImmutableDataclass )


# Here let make some changes inside [ p , y ] varialbes of [ ImmutableDataclass ] using instance object 

# instance_ImmutableDataclass.p = "Modified p"


# -----

# Error :- 

    #  instance_ImmutableDataclass.p = "Modified p"
    #     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #   File "<string>", line 4, in __setattr__
    # dataclasses.FrozenInstanceError: cannot assign to field 'p'

# We got this error, when we try to modify the variables which are present inside the dataclass which as [frozen=True] arguement value which means we are not allowed to modify the variables which are inside the dataclass.
 # [ frozen=True ] attribute will make the dataclass Immutable, trying to modify the variables will throw errors.


# ----



# instance_ImmutableDataclass.y = 123



print("""


""")



# -----------------------------------------------------------------



# 5. Default Values:

from dataclasses import dataclass

@dataclass
class DefaultValue:

    a: str ="String value"
    # Here we can see that we have specified [int] type and assigned string datatype value, we are allowed to do this.
    # x: int = "string"


# -------------
    
    # q: list = [1,2,3]
    # Error:- [ ValueError: mutable default <class 'list'> for field q is not allowed: use default_factory ]

    # q: int = {"key": "values"}
    # Error :- ValueError: mutable default <class 'dict'> for field q is not allowed: use default_factory  

 # We are getting the above errors because when we try to use Mutable datatypes(list, dict, etc ) as a Default values for Class Attributes 
 
 # In attrubtes values are more impotant than what datatype we specify for variables 
  # Example :- # q: int = {"key": "values"} 
  # in the above example we have specified [int] datatype for variable [q] but we used [dict] datatype as a value
     # even though we have set [int] which is immutable type but still we are getting error becuase we used [dict] as a value, from here we can clearly learn that values are more important than what datatype we specify.
    


    # Caution :-
      # Do not use [ Mutable ] dataypes as a Values for [ @dataclass ] attributes.
    
# -------------
    
    q: tuple = (1,) 



# Here let us create the instance of [ DefaultValue ]
    
instance_DefaultValue = DefaultValue()

print( instance_DefaultValue )

# Output :-
 # DefaultValue(a='String value', q=(1,)) 

# Because we did not passed any values for the [ DefaultValue() ] class, the default values has been assigned.


# Let us pass arguement values for [ DefaultValue ] class

instance_DefaultValue_2 = DefaultValue("ABCD" )
print( instance_DefaultValue_2  )

# Output :-
 # DefaultValue(a='ABCD', q=(1,))

# Because we have passed value for the 1 parameter and not for the 2 parameter, only 1 arguements values was overriden by default value, where as 2nd arguements valuse are not overriden.



print("""



""")



# -----------------------



# 6. Custom __repr__ Method:

# Let let us learn on how to customize the Output values which we get when we create an Instance objects.

from dataclasses import dataclass

@dataclass
class Custom_repr:
    a: str = "default string"
    b: int = 12

    # If you want to set datatype for a function use the  below syntax 
     # [ def functionName(self) -> datatype : ]
    def __repr__(self) -> str:
        return f"This is a Custom value"


instance_Custom_repr = Custom_repr()

print( instance_Custom_repr )

# Output :-
 # This is a Custom value

# before using [ __repr__() ] method the function we where getting values that is [attributes ] which we have passed, like below example 
 # Example : Custom_repr(a="default string", b=12)

# After we using [ __repr__() ] method and return some other string values
  # The values which was to returned by [ instance_Custom_repr ] instance object is has changed that is whatever values which we have returned inside the [__repr__()] method has been returned when we invoked the Constructor of [ Custom_repr() ] class


# Learnings :- 
 # By using [ __repr__() ] method we can customize Instance values of class and Dataclass 
  # Instead of Class Instance returning [ Class Address or String object which has variable values ] we can try to return some customized values. 





# ------------------------------------------------------


# 7. Inheritance with Data Classes:

# Here let us learn about Inheritance in Dataclasses 


 # How inheritance will work in general Classes ?

class Parent:
    def __init__(self):
        parentAttr = "attribute value"
    parentVar ="variable value"
    def parentMethod(self):
        return "parent method"


class Child(Parent):
    def __init__(self):
        # super().__init__(self)
           # OR 
        Parent.__init__(self)


# Now let us create instance object with [ Child ] class and try to access [ variables, attributes and methods ] which are inside [ Parent ] class

instance_child = Child()

# accessing parent class [ variables, attributes and methods ] 

print( instance_child.parentVar )
print( instance_child.parentMethod() ) 


print("""



""")




# ----------------


# Now let us use Inheritance in [ Dataclasses ] and check how it works

from dataclasses import dataclass 

@dataclass
class Dataclass_Inheritance_Parent:
    parentVar_1: str 
    parentVar_2: int


@dataclass
class Dataclass_Inheritance_Child( Dataclass_Inheritance_Parent ):
    childVar_1: str
    childVar_2: int



# Now let create Instance object for [ Dataclass_Inheritance_Child ] and try to access [ variables ] which are present inside [ Dataclass_Inheritance_Child and Dataclass_Inheritance_Parent ]
    

# instance_Dataclass_Inheritance_Child = Dataclass_Inheritance_Child( )

# Error :- 
  # [ TypeError: Dataclass_Inheritance_Child.__init__() missing 4 required positional arguments: 'parentVar_1', 'parentVar_2', 'childVar_1', and 'childVar_2' ]
  # We got this Error because we are suppose to pass 4 arguements which we invoke [ Dataclass_Inheritance_Child() ] child, but we failed to pass
  # Look the Order [ parentVar_1', 'parentVar_2', 'childVar_1', and 'childVar_2' ]
   # Fist [ Dataclass_Inheritance_Parent ]
     # the order in which we have arranged the variables inside the [ Dataclass_Inheritance_Parent ], we have pass the values exactly in the same Order, 
   # Finally [ Dataclass_Inheritance_Child ]
     # Next the we have to pass all the variables which are inside [ Dataclass_Inheritance_Child ].

# The order of passing Arguements for the Class will depend on the Inheritance Order of Parent classes which we have used inside the [ Child class ]
 # Example :- 
   #  ChildClass( Parent_1, Parent_2, Parent_3 )
  # Now when we invoke [ ChildClass ] and pass arguements, the arguements must in following order 
    # 1st - Variables, methods which are inside [ Parent_1 ]
    # 2nd - Variables, methods which are inside [ Parent_2 ]
    # 3rd - Variables, methods which are inside [ Parent_3 ]
      # This [Parent] classes might go upto the how many ever parent classes which we use inside the [ ChildClass ] as inheritance.
    # Finally - Variables, methods which are inside [ ChildClass ]


# Important :-
  # If you do not use Default values for the Variables which means we are suppose to pass Arguements mandatorily, if we fail to pass for any of the Non-default values an Error will be thrown by python interpreter.





# instance_Dataclass_Inheritance_Child = Dataclass_Inheritance_Child(  )



# accessing [ Dataclass_Inheritance_Parent  ] class variables 

# print( instance_Dataclass_Inheritance_Child.childVar_1 )
# print( instance_Dataclass_Inheritance_Child.childVar_2 )



# Error :-
 # 1. [ AttributeError: 'Dataclass_Inheritance_Child' object has no attribute 'childVar_1' ]
  # we get this error because we have not decorated the classes with [ @dataclass ]



# ------------


# Let us pass 1 arguement and check for which variable is the arguement is associated
    # let us pass the values based on the order of inheritance 
    
# instance_Dataclass_Inheritance_Child = Dataclass_Inheritance_Child( "Parent args 1", "parent args 2", "child args 1" )

# Error :- 
  # TypeError: Dataclass_Inheritance_Child.__init__() missing 1 required positional argument: 'childVar_2'
  # Because we did not passed one Mandatory arguement that is [ childVar_2 ] we got this error.


instance_Dataclass_Inheritance_Child = Dataclass_Inheritance_Child( "Parent args 1", "parent args 2", "child args 1", "child args 2" )


print( instance_Dataclass_Inheritance_Child.childVar_1 )
print( instance_Dataclass_Inheritance_Child.childVar_2 )
print( instance_Dataclass_Inheritance_Child.parentVar_1 )
print( instance_Dataclass_Inheritance_Child.parentVar_2 )


# Output :-

    # child args 1
    # child args 2
    # Parent args 1
    # parent args 2


# Learnings :-

# Now we have learned how to use Inheritance and Pass arguements for Child/Derived classes.



# -----------------------------------------------------------------




print("""



""")




# -----------------------------------------------------------------



# Nested Dataclasses, we can use One dataclass inside other dataclass 


  # Here let us Learnt on how to use Nested Dataclasses :-

from dataclasses import dataclass 


# [ CODE ] :-
# class NestedParent_dataclass:
#     parentVar_1: str
#     parentVar_2: int

#     nestedDataclass: NestedChild_datacllass

    # Error :-   # "NestedChild_datacllass" is not defined
     # This error occurs because we defined [ "NestedChild_datacllass" ] below [ ""NestedParent_datacllass" ], so when we try to access the [ "NestedChild_dataclass" ] above then where it is defined we are getting this error.
      # Note :- Order of using Classes is Very Important 
       # Order of Classes Flows from Top (starting) of the File (codes which are written at the beginning ) to Bottom (end) of the file (code which are written at the end ) , if we try to mix this order or use opposite to this we will get Errors. 


@dataclass
class NestedChild_datacllass:
    childVar_1: str
    childVar_2: int



@dataclass
class NestedParent_dataclass:
    parentVar_1: str
    parentVar_2: int

    nestedDataclass: NestedChild_datacllass



# Now let us create instance for [ NestedParent_dataclass ] and [ instance_NestedParent_dataclass.nestedDataclass  ]
    

# Instance of [ NestedParent_dataclass ]
    
# instance_NestedParent_dataclass = NestedParent_dataclass("parent_value_1", "parent_value_2")

# Error :- [ TypeError: NestedParent_dataclass.__init__() missing 1 required positional argument: 'nestedDataclass' ]
  # error becuase we did not passed one positonal arguement that is [ nestedDataclass ]
     # The arguement for [ nestedDataclass ] variable must be an Instance object of datatype [ NestedChild_datacllass ] class
    

  
# let us create an instance for [ NestedChild_datacllass ] class ?

instance_NestedChild_dataclass = NestedChild_datacllass("childValue 1", "childValue 2")


    
# instance_NestedParent_dataclass = NestedParent_dataclass("parent_value_1", "parent_value_2", NestedChild_datacllass )

instance_NestedParent_dataclass = NestedParent_dataclass("parent_instance_value_1", "parent_instance_value_2", instance_NestedChild_dataclass )
# here we passed variable [ instance_NestedChild_dataclass ] that is which holds instance of [ NestedChild_datacllass ] class as a 3rd arguement for [ NestedParent_dataclass ] class.


print( instance_NestedParent_dataclass )
print( instance_NestedParent_dataclass.nestedDataclass )

# Output :-

  # NestedParent_dataclass(parentVar_1='parent_instance_value_1', parentVar_2='parent_instance_value_2', nestedDataclass=NestedChild_datacllass(childVar_1='childValue 1', childVar_2='childValue 2'))
  # NestedChild_datacllass(childVar_1='childValue 1', childVar_2='childValue 2')




print("""


""")

  # Error :- [ AttributeError: type object 'NestedChild_datacllass' has no attribute 'childVar_1' ]
  # we got the above error because we did not invoked and passed necessary arguements for [ NestedChild_datacllass ] class, make sure to invoke and pass appropriate arguements.


instance_NestedParent_dataclass = NestedParent_dataclass("parent_value_1", "parent_value_2", NestedChild_datacllass("child_value_1", "child_value_2") )

  # Here we have passed Class itself by invoking it that is [ NestedChild_datacllass() ], which will ultemately create an Instance for that specific class

print( instance_NestedParent_dataclass  )
print( instance_NestedParent_dataclass.parentVar_1 )
print( instance_NestedParent_dataclass.parentVar_2 )

print( instance_NestedParent_dataclass.nestedDataclass )
print( instance_NestedParent_dataclass.nestedDataclass.childVar_1 )
print( instance_NestedParent_dataclass.nestedDataclass.childVar_2 )


# Output :-

  # NestedParent_dataclass(parentVar_1='parent_value_1', parentVar_2='parent_value_2', nestedDataclass=NestedChild_datacllass(childVar_1='child_value_1', childVar_2='child_value_2'))
  # parent_value_1
  # parent_value_2
  # NestedChild_datacllass(childVar_1='child_value_1', childVar_2='child_value_2')
  # child_value_1
  # child_value_2



# Learnings :-
 # we are suppose to pass Instance Object for the Variable_arguement which holds Nested Object as its datatype, There are 2 ways in which we pass this arguement 
  # 1. By creating an Instance object and pass it as an arguement
  # 2. Directly invoking the Appropriate Datatype construtor at the specific arguement position ( the arguement which holds NestedDatatype as its datatype ).



print("""



      
POST INIT
      



""")


# --------------------------------------------------------------



# 8. Post-Init Processing:

# when you want to create any methods and variables inside the dataclass then we can use [ Post-init method ]


from dataclasses import dataclass

@dataclass
class PostInit:
    x: str
    y: int

    def __post_init__(self):
        
        self.z = "some value"
        print("Post Init Value.....")

        
        # Now let us define a Method inside  [ __post_init__() ] method ?
        def postMethod():
            print("Post_init Method")


        # here we create an instance variable and assigned the method reference not the Invocation.
        # do not invoke if you invoke it will be a variable we cannot use parenthsis [()].
        self.postMethods = postMethod


instance_postInit = PostInit("value x", 102)

print( instance_postInit )
print( instance_postInit.x )
print( instance_postInit.y )
print( instance_postInit.z )


# Accessing method which is inside dataclass ?

instance_postInit.postMethods()





# Output :-

 # first values inside [__post_init__() ] method got invoked and displayed print statement
  # Post Init Value.....

 # Next we tried to access the Variables which are inside [ PostInit ] class.
  # PostInit(x='value x', y=102)
  # value x
  # 102
  # some value
  # Post_init Method



# Learnings :-

  # [ __post_init__() ]
  # if you want to Create any Other methods and variables which has hard coded values (not the values which we get from arguements ) those variables can be defined inside the [ __post_init__() ] method.
   # The values for the variables are hard coded not the, values which we get from Arguements.
  # This method gets invoked after [ __init__() ] method 
  # This approach is helpful when you need to perform additional calculations or setup based on the initialized attributes. The __post_init__ method is a convenient way to extend the initialization process of data classes.



print("""



""")




# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# 9. Field Options:

 # Before using [field() ] import it from [ dataclasses ]
  # [ field() ] is a Function which will accept Keyword arguements, ex: [ fun(key=value)]


# 1. default 
# 2. default_factory:
# 3. repr:
# 4. compare:
# 5. hash:
# 6. Customizing Field Behavior:

from dataclasses import dataclass, field

def y_function():
    return "Y function Value."


@dataclass
class DefaultClass:
    x: str = field( default="deafult value" )

    y: str = field( default_factory=y_function )



# -----------------------------------
    

    # z: str = field( repr=False)
    # Error :- TypeError: non-default argument 'z' follows default argument

    # c: int = field( compare=False)
    # Error :- TypeError: non-default argument 'c' follows default argument

    # h: int = field( hash=False )
    # Error:- [ TypeError: non-default argument 'h' follows default argument ]

    # When we use default arguement for a Variable then try to Non-default variables in such situtions we are not allowed to pass values for Variable which comes after Default values
     # ** Do not use Non-default variable after Default variables because when you try to pass some values we will get error which we got above.


# --------------------------------------




# Now let us Create instance object using [ DefaultClass ]
    
# instance_defaultClass = DefaultClass("x value", "y value", "z value", 100, 121 )

# print( instance_defaultClass )
    




# ---------------------------------------------------------------------------------------------------------------
    


# Default Class 
@dataclass
class DefaultClass2:
    x: str = field(default="Default Value")



# Default Factory 

def factoryFunction():
    print('Factory Function')  
    return 10
  
@dataclass
class DefaultFactory:
    y: str = field(default_factory=factoryFunction)

# let us try to create an instance and access [y]
instance_DefaultFactory = DefaultFactory("some value")

print("""




""")

# when we access [ default_factory ] we should not use parenthsis [()]
print(instance_DefaultFactory.y)



@dataclass
class ReprClass:
    z: str = field(repr=False)
    u: str

# let us create an Instance for [ ReprClass ]
instance_ReprClass = ReprClass("z value", "u value")
print( instance_ReprClass )

# Output :-
 # ReprClass(u='u value')
 
 # here we can that variable [z] has not been included inside the String only variable [u] has been included, that is because variable [z] has field value [repr=False] which means those variables will not be included.












































































# -----------


# Learn How Dataclasses are Created behind the scenes, Create a Visualization on how dataclasses might be created behined the scenes.




































































































