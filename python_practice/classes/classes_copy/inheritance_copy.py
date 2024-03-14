

# Inheritance 


# Here we will be Learning about Inheritance in Python

 # Inheritance means where Child class will get all the features such as ( methods, properties, attributes, constructors ) from the Parent class and makes use of those things


# what is the difference between the below 2 syntax :-

# 1.super().__init__(self,properties)
# 2. ClassName.__init__(self)


# -----------------

 # [ Important ]
  # ** Above both the Methods can be used only to Inherit the Attributes or Instance Variables of the Parent Class
  # ** Even if you do not use above 2 methods, we can able to access the [ Class Methods and Class Variables ] from inside the Child class

# -----------------


  # Think suppose you have inherited more than 1 Parent class inside the Child class 
  # If you want only Specific Parent Class constructor to be used inside the Child class in such situation we can use the below syntax 
   # [ ClassName.__init(self) ] 
 
  # If you want to use all the Parent Constructor which we have inherited inside the Child Class we can use the below syntax 
   # [ super().__init(self) ]



class Parent_class:

    def __init__(self):
        print("Parent Class Constructor")
        self.parentInstanceVariable = "Parent Class Instance Variable."

    def parentMethod(self):
        print("Parent Class Method")

    parentClassVariable = "Parent Class Variable"



class Child_class( Parent_class ):

    def __init__(self):

        Parent_class.__init__(self)

        # super(self, )

        self.child_instanceVariable = "Child Instance Variable"

        print( "Child Class Constructor" )

    def childMethod(self):
        print( "Child Class Method" )

    childClassVariable = "Child Class Variable"


# Instance of [ Child_class ]

instance_Child_class = Child_class()
    

# Accessing [ Child_class ] own methods and properties
    
print( instance_Child_class.child_instanceVariable )

print( instance_Child_class.childClassVariable )

instance_Child_class.childMethod()


#  Accessing [ Child_class ] Parent methods and properties

print( instance_Child_class.parentInstanceVariable )
# Error :- [ AttributeError: 'Child_class' object has no attribute 'parentInstanceVariable'. Did you mean: 'child_instanceVariable'? ]
 # This error occurs when we try to access the Instance Properties of Parent Class from Child Class Instance without calling the Parent Class Constructor inside the Child Class [ __init__() ] function.

print( instance_Child_class.parentClassVariable )

instance_Child_class.parentMethod()


print("""








""")

# -------------------------------------------------------------------------------------------------------------------------------------------



# What happens when we use [ super().__init__(self) ] ?


# class BaseClass:

#     def __init__(self, property_1, property_2 ):
#         print("Base Class")
#         self.attribute_1 = property_1
#         self.attribute_2 = property_2

#     # def baseMethod(self):
#     #     print("Base class Method")

#     # baseProperty = "Base Class Property"


# class BaseClass2:
#     def __init__(self, property2):
#         self.b2attribute = property2

# class DerivedClass( BaseClass, BaseClass2 ):

#     def __init__(self, property_1, property_2, selfProperty, b2property ):
#         self.derivedAttribute = selfProperty
#         super().__init__(property_1, property_2)
#         super().__init(b2property)
#         print( selfProperty )

#     # def derivedMethod(self):
#     #     print( "Derived Class Method" )

#     # derivedProperty = "Derived Class Property"


# instance_DerivedClass = DerivedClass( "parent Arguement 1", "parent Arguement 2", "self Arguement", "b2 arguement"  )


# print( instance_DerivedClass )
# print( instance_DerivedClass.attribute_1 )
# print( instance_DerivedClass.attribute_2 )


# print( instance_DerivedClass.b2attribute )



# --------------------


        # class Parent1:
        #     def __init__(self, attribute1):
        #         self.attribute1 = attribute1

        #     def method1(self):
        #         print("Method from Parent1")

        # class Parent2:
        #     def __init__(self, attribute2):
        #         self.attribute2 = attribute2

        #     def method2(self):
        #         print("Method from Parent2")

        # class Child(Parent1, Parent2):
        #     def __init__(self, attribute1, attribute2, attribute3):


        #         # Here we used 2 [ super() ] function, but this Class will only recognise only the first [ super() ] function, next occurance of [ super() ] function get ignored.
        #         super().__init__(attribute1)
        #         super().__init__(attribute2)  # Use super() for the second parent class
        #         self.attribute3 = attribute3

        #     def display_attributes(self):
        #         print(f"Attribute1: {self.attribute1}")
        #         print(f"Attribute2: {self.attribute2}")
        #         print(f"Attribute3: {self.attribute3}")

        # # Creating an instance of the Child class
        # child_instance = Child(attribute1="A", attribute2="B", attribute3="C")

        # # Accessing attributes and methods from both parent classes
        # child_instance.display_attributes()
        # child_instance.method1()  # Output: Method from Parent1
        # child_instance.method2()  # Output: Method from Parent2


# Error :- 
 # AttributeError: 'Child' object has no attribute 'attribute2'. Did you mean: 'attribute1'?
  # This Error occurs just because we use 2 [ super() ] functions into our child class, where the first [super()] function that is  [  super().__init__(attribute1) ] got recognised 
  # where as the 2nd [ super() ] function that is [  super().__init__(attribute2)  ] is not recognised, because in python each call can have muliple instance of [ super() ] function but only 1st [ super() ] function will be recognised where as others will be ignored that is the reason we got this error.
  # To overcome this Error we can use [ Explicit Calling ] - Calling Specific Parent class Constructor inside the inheriting Child Class.




# -------------------

# { HOW [ super().__init__(self, parametes_sameAs_ParentClass) ] function as [ ClassName().__init__(parametes_sameAs_ParentClass) ] } WORKS Behind the scene
# Refactored version of above Code 

 # There are 2 ways to Resolve this Problem ?

  # Approach 1. Use Only one [ super().__init__() ] function inside the Child Class which will point the First Parent Class Arguement, for rest of the classes use Explicit Calling [ ClassName().__init__(parametes_sameAs_ParentClass ) ] 

  # Approach 2. Do not use [ super().__init__() ] Only use Explicit Classing inside the Child Class [ ClassName.__init__( parametes_sameAs_ParentClass ) ]
    # Here the Numbe of parameter for [ ClassName.__init__() ] must be exaclty same as the number of parameter which we passed inside the Parent Class Constructor.



# [ Approach 1 ]

class Parent1:
    def __init__(self, attribute1):
        self.attribute1 = attribute1
    
    def method2(self):
        print("Hello method")


class Parent2:
    def __init__(self, attribute2):
        self.attribute2 = attribute2

    def method2(self):
        print("Method 2")

class Child(Parent1, Parent2):
    def __init__(self, attribute3, attribute1_args, attribute2_args ):
        self.attribute3 = attribute3


# --------------------------------------
        
        super().__init__(attribute1_args)

        # Parent1.__init__(self, attribute1_args )

        # super().__init__(attribute2_args)
        Parent2.__init__(self, attribute2_args )


        # How the above code will Look like 
          # whatever statements which are present inside the [ Parent1 and Parent2 ] class Constructor [ __init__() ] function or Method will get loaded inside the Child Class constructor [ __init__() ] method.

          # Loaded from [ Parent1 ] class
        #  self.attribute1 = attribute1

        
          # Loaded from [ Parent1 ] class
        # self.attribute2 = attribute2


  # *** By this way we can easily access the Attributes which are present inside any of the Parent(Base Class) from inside Child (Derived Class)

# --------------------------------------
        





    def method3(self):
        print("Method 3")

instance_child = Child("Argument 3", "args 1", "args 2")

print(instance_child.attribute3)
print(instance_child.attribute1)
print( instance_child.attribute2 )


print("""





""")


# --------------------------------------------------------


# [ Approach 2 ]


class Parent1:
    def __init__(self, attributeParent1):
        self.attributeParent1 = attributeParent1

    def parentMethod(self):
        print("Patnet Method")

    classParent1Variable = "Class Parent 1 Variable"


class Parent2:
    def __init__(self, attributeParent2):
        self.attributeParent2 = attributeParent2

    def parent2method(self):
        print("Parent 2 Method")

    classParent2Variable = "Class Parent 2 Variable"



class Child(Parent1, Parent2):
    def __init__(self, attribute, attributeParent1, attributeParent2 ):
        self.attributeChild = attribute

        # Approach 2 
        # Use [ Explicit Calling ] for all the Parent Class which has been Inherited.

        # super().__init__(attributeParent1)

        # Here we have Explicitly Calling [ Parent1 and Parent2] Classes 
         # Do not invoke any of the Classes while using it as a Explicit Calling 
        
         # Here we called [ Parent1 and Parent2 ] classes without invoking it.
        # Parent1().__init__(self, attributeParent1 )
         # Error :- TypeError: Parent1.__init__() missing 1 required positional argument: 'attributeParent1' 
          # This error occurs when we try to invoke the Parent classes from inside Child Class constructor (__init__() method )
        
        Parent1.__init__(self, attributeParent1)

        Parent2.__init__(self, attributeParent2)

    def childMethod(self):
        print("Child Method")

    classChildVariable = "Child Class Variable"



# Here let us Create an Instance Object
    
instance_object = Child( "Child value", "Parent 1 value", "Parent 2 value" )

print( instance_object.attributeParent1 )
print( instance_object.attributeParent2 )
print( instance_object.attributeChild)





# *** The Changes which we make in the Parent or Base Class will also affect the Child / Derived class
  # The Changes made in the Parent/Base Class those changes will also be reflected inside the Child/Derived Class.
















