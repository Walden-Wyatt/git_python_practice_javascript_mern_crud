

        # # Abstraction 

        #  # Here we will be Learning about Abstraction in Python
        #  # Abstraction is nothing but where the Method declaration will be given in the Class where as Defination will be given in the Derived( Child ) class


 # What is an Abstract Class ?
  # An Abstract Class is a class where the methods will be declared but the defination ( body with indentation ) is not given, The Class which Inherits ( i.e, parent class ) will create the same method and provide the defination for the Method

 # In Python, an abstract class is a class that cannot be instantiated on its own and is meant to be subclassed by other classes. Abstract classes are typically used to define a common interface or set of methods that must be implemented by any concrete (i.e., non-abstract) subclass. Abstract classes are part of Python's support for abstract base classes (ABCs), which are defined in the abc module.


# Important Points :-

 # 1. we cannot create Instance / Instantiate for those classes which has Abstract Methods
  # a. Even if a Class has 1 abstract method also we cannot able to Create.

 # 2. We can have more than 1 Abstract Methods inside a Single Class.




#-------------------------------


# Steps :-

 # 1. Import "abstractmethod" from "ABC" class [  from abc import ABC, abstractmethod  ]


 # 2. Create a Class [ Abstract_Base_Class  ]
   # The class should have [ ABC ] as a Parent or Base class for the Abstract Class
    # class AbstractClass(ABC):
    # 


 # 3. Inside the Class create an Abstract Method with the below syntax 
        # @abstractmethod 
        # def abstractMethod(self):
        #     pass


 # 4. Create another Class [ Abstract_Dervived_Class ]
      # This is the class which will make use of the "Abstract Methods" which is present inside [ Abstract_Base_Class ]


 # 5. Create Instacne Object only for [ Abstract_Dervived_Class ] not for [ Abstract_Child_Class ]
   # we can create an Instance Object only for [ Abstract_Dervived_Class ] because it does not have any Abstact methods
   # we are not allowed to create Instance Object using [ Abstract_Base_Class ] class because it has abstract Methods







# -------------------------------


# Error :-

# 1.
# from abc import ABC, abstractmethod
 # Error :- NameError: name 'ABC' is not defined
  # This Error occurs when we try to use [ ABC ] class as a Parent/Base Class for [ AbstractBaseClass ] class

# 2.
# Error :- [ IndentationError: expected an indented block after function definition on line 72 ]
 # This Error occurs when we do not use any indented block of statements inside the Abstract Function, we have to mandatory use some statements
 # The statments can be keyword [ pass, return, etc ] or we can also use [ print() function, any variables, etc ], anyhow none of the statements can be used from that method as abstract method cannot be instantiated or created Instance Object.


# 3. 
# Error :- [ TypeError: Can't instantiate abstract class AbstractBaseClass without an implementation for abstract method 'abstractMethod' ]
 # when we try to instantiate or create Instance object from Abstract class ( class which has abstract method ) we encounter this Error





from abc import ABC, abstractmethod

# Here we have an Abstract Class [ Parent or Base ] class
class AbstractBaseClass(ABC):


  # Here we have [ @abstractmethod ] decorator which means we are going to create an Abstract Method under this
    @abstractmethod

    # [ abstractMethod(self) ] this is an Abstract Method, because we used a decorator called [ @abstractmethod ] at the Top of the Method.
    def abstractMethod(self):
        # pass  [ IndentationError: expected an indented block after function definition on line 72 ]
        pass



# [ AbstractDerivedClass ] this is a Child Class which will inherit (AbstractBaseClass) which is Parent Class.
class AbstractDerivedClass(AbstractBaseClass):
    
    # [ abstractMethod() ], this is the Abstract method which is present inside the parent class [ AbstractDerivedClass ]
       # In this method we can provided any number of statements from the Indented Block.
    def abstractMethod(self):
        return "Hello Abstract Methed Derived Class"
    


# Instance Object 
    

# instance_abstractBaseClass = AbstractBaseClass()
 # Error :- [  TypeError: Can't instantiate abstract class AbstractBaseClass without an implementation for abstract method 'abstractMethod'  ]

instance_abstractDerivedClass = AbstractDerivedClass()


# print( instance_abstractBaseClass )

print( instance_abstractDerivedClass )



print("""




""")



# --------------------------------------------------------------------------------------------------------------------------------------------------------


# [ Practice 2 ]


# Two things to make a Class as an Abstract Class
 # 1. Inherit [ ABC ] class inside Abstract_Parent class 
 # 2. Inside the Class use [ @abstractmethod ] decorator at the top of Methods which you want to make as Abstract Method


from abc import ABC, abstractmethod


class AbstractParent(ABC):

    @abstractmethod
    def abstractMethod_1(self):
        return "abc"
    
    @abstractmethod
    def abstractMethod_2(self):
        pass

    @abstractmethod
    def abstractMethod_3(self):
        print("Hello Abstract Method")



# instance_abstractParent = AbstractParent()
# print( instance_abstractParent )

# Error :- [  TypeError: Can't instantiate abstract class AbstractParent without an implementation for abstract methods 'abstractMethod_1', 'abstractMethod_2', 'abstractMethod_3'  ]




# Here let us have Child class which will inherit Parent abstract class

class AbstractChild(AbstractParent):

    def abstractMethod_1(self):
        print("Abstract Method 1")

    def abstractMethod_2(self):
        print("Abstract Method 2")

    def abstractMethod_3(self):
        print("Abstract Method 3")


# create and acces abstract Method from sub class
        

instance_abstractChild = AbstractChild()

print( instance_abstractChild )
instance_abstractChild.abstractMethod_1()
instance_abstractChild.abstractMethod_2()
instance_abstractChild.abstractMethod_3()


