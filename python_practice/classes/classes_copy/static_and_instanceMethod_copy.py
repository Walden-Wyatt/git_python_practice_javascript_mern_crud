

# Static and Instance Methods and Properties


# Here we will be Learning on how to Create a Static and Instance Methods in Python

# instance Methods and Properties



# Decorators 

 # 1. @staticmethod
 # 2. @classmethod
 # 3. @property
 # 4. @methodName.setter
    # this method name should be same as the method which has [ @property ] decorator.





# ----------------------------------------------------------------------------------------------------------------------------------------


# Instance Methods and Properties 

 # Instance Methods and Properties can also be accessed by Instance Object as well as Class Constructors


class InstanceClass:

    def __init__(self):
        self.instanceAttribute = "Instance Attribute Value"


    def instanceMethod(self):
        print( "Instance Method" )

    instanceProperty = "Instance Property"


    # There are Two ways to Define Instance Methods inside the Class
     # 1. Using [ @classmethod ] decorator at the Top of Class. [ Approach 1 ]
        # creating a Method using [ @classmethod ] inside the class is equivalent to creating a Method without using [ @classmethod ] decorator
    
     # 2. without using [ @classmethod ] decorator at the top of the Class. [ Approach 2 ]
        # in this approach we will not be using the [ @classmethod ] decorator at the top of the Methods
    

    # [ Approach 1 ]
    @classmethod
    def usingclasmethod_decorator(cls):
        print("Using Class Method Decorator")

    # [ Approach 2 ]
    def withoutusingclasmethod_decorator(self):
        print("Without using Class Method Decorator")



# Instance Object 
    # Properties and Methods which are inside [ InstanceClass ] can be accessed using "Instance Object"

instance_InstanceClass = InstanceClass()

print( instance_InstanceClass )
print( instance_InstanceClass.instanceAttribute )
print( instance_InstanceClass.instanceProperty )
instance_InstanceClass.instanceMethod()

instance_InstanceClass.usingclasmethod_decorator()
instance_InstanceClass.withoutusingclasmethod_decorator()




print("""





""")


# -----------------------------------------------------------------------


# Static Methods and Properties

 # static methods and Properties can be accessed by Instance Object as well as Class Constructors.
 

class Static_class:

    # Method and Class Variables which we create inside the Class can be accessed by Instance Object as well as Class Constructors.

    def __init__(self):
        # The attributes which we create inside the [ __init__() ] method can be accessed only through Instance Object, it cannot be accessed with Class Constructor.
        self.staticAttribute = "Static Attribute Value"

    @staticmethod
    def staticMethod():
        print("Static Method")

    staticClassVariable = "Static Class Variable"



instaceStatic_class = Static_class()

# print( instaceStatic_class )
# instaceStatic_class.staticMethod()
# instaceStatic_class.classMethod()


Static_class.staticMethod()
print ( Static_class.staticClassVariable )



# Static Methods and Properties 

 # 1. static method 
   # all the Methods which we create by using (@staticmethod) decorator at the top of the Methods are static methods
   # In static methods we need not use 1 mandatory parameter [ self, csl ] ( which will represent the current class )
   # we don't need to use 1 mandatory parameter for all Static methods which we create inside the class
   # Static methods can be accessed by Instance Object as well as Class Constructors

 # 2. static properties
   # all the properties or Class variables which we create at the top of Class Scope are called as static properties, This properties can be accessed by the Class Constructor.
   # all the Properties or Attributes which we create inside the Constructor method ( __init__() ) cannot be accessed by the Class Constructor or class, It can only be accessed by the Instance Object.
   # Except those Properties or Attributes which we define inside [ __init__() ] method, other Static properties ( Class Variables ) can be accessed by Instance Objects as well as Class Constructors


# Instance Methods and Properties 

 # 1. Instance Methods
   # all the methods which we create in the class without using [ @staticmethod ] decorator at the top of the methods can be accessed by the Instance Object
   # The methods which we create by using [ @classmethod ] decorator can also be accessed by the Instance Object.
   # we must use 1 mandatory parameter for all the Instance Methods which we create inside the class, it can be [ cls, self ]
   # Instance Methods can be accessed by Objects as well as Class Constructors


 # 2. Instance Properties
   # all the properties or class variable which we create in the class can be accessed by the Instance Object
   # all the properties or Attributes ( inside __init__() method ) can be accessed only by the Instance Object, it cannot be accessed by Class Constructor
   # Instance Properties can be accessed by Objects as well as Class Constructors

# Very Important :-
    # what happens when we try to access Intance Methods using Class Constructors ?
    #   when we access Instance methods using Class Constructors, we have to passing arguement for all the Parameters which is present inside the Instance Methods ( including "self" parameter which we must use by default for all the Instance methodd ) 
    # we we try access Instance Methods  using Instance Object, we don't need to pass arguement for the first Parameter (self), we whatever arguement we pass will start from 2nd parameter of the Instance Method.
     # mostly the Arguement value will be any Instance Object, so behind the scene python will the Method using the Instance object which we passed. Make sure you pass Instance Object as an Arguement

print("""






""")





# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# [ practice 2 ]

class StaticInstance_class:

    #  here we will have Instance methods and properties 

    def __init__(self):

        self.instanceAttribute = "Instance Attribute"

    
    def instanceMethod(self):
        print("Instance Method")

    @classmethod
    # the methods which we create using [ @classmethod ] decorator we have use 1 mandatory parameters for all the methods which we create.
    def instancMethod_classmethod(cls):
        print("Instance Method classname")

    instanceClassVariable = "Instance Class Variables"


    # -----------------------------------------------


    # Here we will have Static Methods and Properties 

    @staticmethod
    def staticMethod():
        print("Static Method")

    staticClassVariable = "Static Class Variables"



# Accessing the [ StaticInstance_class ] using Instance Object 


instance_StaticInstance_class = StaticInstance_class()

print( instance_StaticInstance_class )
print(  instance_StaticInstance_class.instanceAttribute )
print( instance_StaticInstance_class.instanceClassVariable )
instance_StaticInstance_class.instanceMethod()
instance_StaticInstance_class.instancMethod_classmethod()

print( instance_StaticInstance_class.staticClassVariable )
instance_StaticInstance_class.staticMethod()



print("""

""")


# Accessing the [ StaticInstance_class ] using Class Constructor

# print( StaticInstance_class.instanceAttribute ) 
# Error :- [ AttributeError: type object 'StaticInstance_class' has no attribute 'instanceAttribute' ]
# we get this error when we try to access Attributes which is inside [ __init__() ] method through class constructor ( in a static way ).

print( StaticInstance_class.instanceClassVariable )

StaticInstance_class.instanceMethod("any value")
# [ Code ] :- StaticInstance_class.instanceMethod()
# Error :- [  TypeError: StaticInstance_class.instanceMethod() missing 1 required positional argument: 'self' ]
  # we get this error because we did not pass 1 arguement for [ self parameter ] which has to be passed when accessing from Class Constructor.
StaticInstance_class.instancMethod_classmethod()

print( StaticInstance_class.staticClassVariable )
StaticInstance_class.staticMethod()


# Output :-

   
    # <__main__.StaticInstance_class object at 0x000001F15B08B2F0>
    # Instance Attribute
    # Instance Class Variables
    # Instance Method
    # Instance Method classname
    # Static Class Variables
    # Static Method



    # Instance Class Variables
    # Instance Method
    # Instance Method classname
    # Static Class Variables
    # Static Method
    # PS C:\Users\user\Desktop\python_practice\classes> 




# ------------------------------------------------------------------------------------------------------


# Summary :-

 # 1. Class Attribute properties can be accessed only by the Instance Object
 # 2. when accessing Instance Methods using Class Constructors we have to have pass arguements for all the Parameters including [ "self" ].






























































