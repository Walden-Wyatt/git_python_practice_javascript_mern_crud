

# Basics 

# Here we will be Learning about Basics in Classes


# How to create a Class

 # Important points 

  # 1. for all the Methods which you create inside the Class must have [ self ] as a 1st Arguement. The name need not be [self] we can even have any custom names.


# 
class ClassName:

    # [ __init__(self) ]
      # Here we have Class Constructor Syntax 
      # The arguement for this parameters has to be passed when Invoking the Class for creating Instance Object.

    def __init__(self, property1, property2):

        # [ Attribute ]
         # here we have Attributes for the class
         # Class Attributes is when we assign a [__init__()] methods arguements to a Variable inside the [ __init__() ] method then it becomes an Attribute.
        
        self.attribute_1 = property1
        self.attribute_2 = property2

    # [ customMethod(self) ]
     # Here we have Custom Method can be accessed through Instance Objects.
        # This Method must mandatorily accept 1 positional Arguement that is [ self ], for every Custom which we create this 1 mandatory positional arguement has to be passed.
    def customMethod(self):
        print("This is a Custom Method.")


    # [ custom_propertyVariable ]
     # Here we have custom property or variable
     # This property can be accesed through Instance Objects.
    custom_propertyVariable = "Property Or Variable Value."
        


# Create an Instance Object

className_instanceObject = ClassName("Arguement 1", "Arguement 2")


# Accesssing Properties, Attributes and Methods of [ ClassName ] class.

print( className_instanceObject )

print( className_instanceObject.attribute_1 )    

print( className_instanceObject.attribute_2 )

print( className_instanceObject.custom_propertyVariable )


# Error :-
 # TypeError: ClassName.customMethod() takes 0 positional arguments but 1 was given     
 # This Error occurs if there is no Minimum 1 parameter which has been passed for the Methods which we create inside the Class
  # For every method which is inside the class must have atleast or minimum One Parameter, else we might encounter this error
 
 # When do we get this error ?
  # we get this Error once we create the Instance of the Object from the class, Then when we try to Invoke the Method only then we get this Error.

className_instanceObject.customMethod()






print("""







""")



# ---------------------------------------------------------------------------------------------------------------------------------------


# 1. Class Constructor 

class ClassConstructor:

    def __init__(self):

        attribute_1 = "Attribute Value"

        print("This is Class Constructor")


# Instance Object 
        
classConstructor_instance = ClassConstructor()






print("""







""")



# ---------------------------------------------------------------------------------------------------------------------------------------


# 2. Attributes and Methods:

class classAttribute_Method:

    def __init__(customName):
        print("1st Arguement with Custom Name.")

        # Here we have Attribute 
        customName.attribute_1 = "Attribute 1"

    # Here we have Method
    def classMethod(self):
        print("This is Class Method")

   # Here we have Property
    property_1 = "Property Value."


# Instance Object 
    
instance_classAttribute_Method = classAttribute_Method()

print( instance_classAttribute_Method )





print("""







""")




# ---------------------------------------------------------------------------------------------------------------------------------------


# 3. Constructors and Destructors:

# constructors and Destructors can be used to Create an Instance Objects and Delete an Instance Objects



class Constructor_Destructor:


  # [ __init__(self) ]
     # Here we have Constructor Function which can be used to create a instance Object.
    def __init__(self):
        print("Constructor Called")
    
    
    # [ __del__(self) ]
        # here we have [__del__() ] function which can be used while deleting the Instance Object created with this Class
        # when we create an Instance Object, when we try to delete the Instance Object using [ del ] keyword what has to be performed has to be given inside the [ __del__() ] function / dunder method.
    def __del__(self):
        print("Destructor Called.")



# Instance Object
        
instance_Constructor_Destructor = Constructor_Destructor()

# Output :-
    # Constructor Called
    # Destructor Called.

# here when we call the Constructor function, both [ __init__() and __del__() ] methods statements gets executed.


# print( instance_Constructor_Destructor )


del instance_Constructor_Destructor


# Tring to access after deleting the [ instance_Constructor_Destructor ]

    # [CODE] :- print( instance_Constructor_Destructor )
    # Error :- NameError: name 'instance_Constructor_Destructor' is not defined. Did you mean: 'Constructor_Destructor'?
     # we get this Error when we try to access the Instance Object after we deleted the Instance Object.





print("""







""")




# ---------------------------------------------------------------------------------------------------------------------------------------


# 4. Instance and Class Variables:

# Instance 
 # Those Properties which we create inside the Class Constructor ( i.e, inside "__init__(self)"  )

# Class Variables
 # This are properties which we create inside the Class Scope but outside the Class Constructor ( i.e, inside "__init__(self)"  )


class Class_Instace_And_Variables:

    # ---------------------------------
     # Here we have [ Class Variables ]
     
    class_variable_1 = "This is class Variable 1"

    class_variable_2 = "Class Variable 2"

    # ---------------------------------



    def __init__(self):
        
    # ---------------------------------
        # Here we have [ Instance Variables ]

        self.instance_variable_1 = "Instance Variable 1"

        self.instance_variable_2 = "Instance Variable 2"
    # ---------------------------------


# Instance Object 
        
instance_Class_Instace_And_Variables = Class_Instace_And_Variables()

print( instance_Class_Instace_And_Variables )



# Here we have invoked [ Class Variables ]

print( instance_Class_Instace_And_Variables.class_variable_1 )

print( instance_Class_Instace_And_Variables.class_variable_2 )



# Here we have invoked [ Instance Variables ]

print( instance_Class_Instace_And_Variables.instance_variable_1 )

print( instance_Class_Instace_And_Variables.instance_variable_2 )



# Output :-

    # <__main__.Class_Instace_And_Variables object at 0x00000262BFCCB0E0>
    # This is class Variable 1
    # Class Variable 2
    # Instance Variable 1
    # Instance Variable 2






