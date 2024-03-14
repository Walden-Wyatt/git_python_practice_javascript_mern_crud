
# Access Modifiers 

# Access modifiers means how do we access the Class Variables and Modify or change it

# 3 things to keep in Mind when it comes to Acces Modifiers 
 # 1. weather the [ Methods and class variables ] can be accessed within the class [ ex: private variables ]
 # 2. weahter the [ Methods and class variables ] can be accessed within the class and inside the Derived ( Base class)
 # 3. weather the [ Methods and class variables ] can be accessed within the class, inside the Derived ( Base class ) and inside the Instance Objects

#############

# [ Public Access Modifiers ]

#############


# Class which has Public Methods and class variables( properties, attributes )
 # by default all the Methods and class variables which is inside the class is Public access modifiers 


# [ Within Class Scope ]

# Check weather public class can be accessed [ within the class ]


class Public_class:

    public_variable = "Public Class Variable"

    def publicMethod(self):
        return "Public Method"
    
   # Check weather public class can be accessed within the class
    
    def accessPublicMethodsVariables(self):
        print( self.public_variable )
        print( self.publicMethod() )



# -----------------------------------------
        

###### [ Derived Class ]

# check weather the class methods and variables can be accessed within the [ derived Class ]

class Derived_Public_Class(Public_class):

    def accessPublicClasses( self ):
        
        print( self.public_variable )
        print( self.publicMethod() )
        print( self.accessPublicMethodsVariables )

    def derivedMethod(self):
        return "Derived Method"


 # Instance of Derived Public Class
    
instance_Derived_Public_Class = Derived_Public_Class()

print( instance_Derived_Public_Class )

print( instance_Derived_Public_Class.accessPublicClasses() )





# -------------------------------



# Instance Method 
        
instancePublic_class = Public_class()

instancePublic_class.accessPublicMethodsVariables()


# Output :-

    # <__main__.Derived_Public_Class object at 0x0000017DBBABA720>
    # Public Class Variable
    # Public Method
    # <bound method Public_class.accessPublicMethodsVariables of <__main__.Derived_Public_Class object at 0x0000017DBBABA720>>
    # None


# Since there is no Error we are allowed to access the Public Methods and class variables from inside the [ Derived Class ]




# -------------------------------

###### [ Instance Object ]


# check weather the class methods and variables can be accessed within the  [ Instance Object ]

print(instancePublic_class.public_variable )

print( instancePublic_class.publicMethod() )






# Output :-

# py accessModifier.py
# Public Class Variable
# Public Method
    

# Since there is no Error we can able to access [ Public Access Modifier ] within the class.


# ----------------------------------


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------




print("""



Protected Methods and Properties




""")




# [ Protected Methods and Properties ]

# Protected methods and properties are those methods and properties which can be accessed within the Class as well as Inside the Derived Class.


class Protected_Class:

    def __init__(self):
        print("Protected class constructor")

        self.attribute1 = "Attribute 1 value"

    def protectedMethod(self):
        print("Protected Method")

    protectedVariables = "Protected Variables"



class Derived_Protected_Class(Protected_Class):

    def __init__(self):
        super().__init__()
        print( "Derived_Protected_Class ")
        self._attributeDerived = "Attribute Value"

    def _derivedProtectedMethod(self):
        print("Derived Protected Method")

    _derivedProtectedVariable = "Derived Protected Variable"


   # Here we accessed the Base class ( Parent class ) methods and Properties from inside the Derived ( Child class), we did not encountered any Errors in the code.
    def accessProtectedMethodsVariables( self ):
        print( self.attribute1 )
        print( self.protectedVariables )
        self.protectedMethod()



instance_Derived_Protected_Class = Derived_Protected_Class()

print( instance_Derived_Protected_Class )

instance_Derived_Protected_Class.accessProtectedMethodsVariables()


# Accessing Protected Methods and Class Variales  using Instance Object

 # Here even though we can able to access the Protected Methods and Class Variables using Instance Object but we are not allowed to do that as a Good Developer
  # Once if you see [ _ ] underscore preceeded before any Methods, class variables, or attributes(instance variables ) we have to understand it is Protected method or property so we should not access it with the Instance Variables.
  # we have to access protected Methods and Properties only within the Class Scope and Derived Class Scope

print( instance_Derived_Protected_Class._attributeDerived )

print( instance_Derived_Protected_Class._derivedProtectedVariable )

instance_Derived_Protected_Class._derivedProtectedMethod()




# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------




# Private Access Modifier

 # Private Access Modifiers are those Methods and Properties which can be accessed only within the Class Scope
 # Private Access Modifiers cannot be accessed inside the Derived Class scope or using Instance Objects
 # This concept can also be called as Encapsulations

 # we can able to access Class variables from inside the Derived/child class scope without any errors


print("""




Private Access Modifier
      



""")



# [ BASE CLASS ]
class Private_Base_Class:

    def __init__(self):
        print("Private Base Class")

        self.__privateBaseAttribute = "Private Attribute Value"

    def __privateBaseMethod(self):
        print("Private Method")

    __privateBaseClassVariable = "Private Class Variable Value"



# [ DERIVED CLASS ]
class Private_Derived_Class( Private_Base_Class ):

    def __init__(self):
        print("Private Derived Class")

        self.__privateDerivedAttribute = "Private Base Class Attribute Value"


          # super() function - here we used [ super() ] function
        # super().__init__()

          # Explicit Calling - here we use Explicit calling 
        Private_Base_Class.__init__(self)

    def __privateDerivedClassMethod(self):
        print("Private Base Class Method")

    __privateDerivedClassVariable = "Private Base Class Variable Value"


    # Here let us try to access the Parent or Base class (i.e, Private_Base_Class) methods and properties from inside Base Class ( i.e., Private_Derived_Class )

    def accessPrivateMethodsVariables_baseClass( self ):

        # Below we have accessed all the [ Methods and Class Variables ] which is inside the [ Private_Base_Class ] class

        # print( self.__privateBaseAttribute  )

        # print( self.__privateBaseClassVariable )

        # self.__privateBaseMethod()

        print("Method which has all invocation of the Base/Parent class privated methods and properties")



    def accessPrivateMethodsVariables_derivedClass( self ):

        print( self.__privateDerivedAttribute )

        print( self.__privateDerivedClassVariable )

        self.__privateDerivedClassMethod()






# Instance of [ Private_Derived_Class ] class
        
instance_Base_Private_Class = Private_Base_Class()


instance_Derived_Private_Class = Private_Derived_Class()


# Here we tried to access the Derived class by loading all the Privated Methods and Properties inside the public method called [ accessPrivateMethodsVariables_derivedClass ]
instance_Derived_Private_Class.accessPrivateMethodsVariables_derivedClass( )



# Here we tried to access Private methods and class instances from the Derived class ( Child class), then tried to print the derived class
print( instance_Derived_Private_Class.accessPrivateMethodsVariables_baseClass() )


 # Errors :-

 # [  AttributeError: 'Private_Derived_Class' object has no attribute '_Private_Derived_Class__privateBaseAttribute'. Did you mean: '_Private_Base_Class__privateBaseAttribute'?       ]
 # [  AttributeError: 'Private_Derived_Class' object has no attribute '_Private_Derived_Class__privateBaseClassVariable'. Did you mean: '_Private_Base_Class__privateBaseClassVariable'? ]
 # [  AttributeError: 'Private_Derived_Class' object has no attribute '_Private_Derived_Class__privateBaseMethod'. Did you mean: '_Private_Base_Class__privateBaseMethod'?  ]

# The above error occured when we tried to access Private Methods and Properties which is present inside [ Private_Derived_Class  ] from inside [ Private_Base_Class ] ( which has a public method called [ accessPrivateMethodsVariables_baseClass ] )
 



# ------------------------------------------

# print( instance_Derived_Private_Class.__privateBaseAttribute )
# Error :- [  AttributeError: 'Private_Derived_Class' object has no attribute '__privateBaseAttribute'   ]

# print( instance_Base_Private_Class.__privateBaseClassVariable )
# Error :- [ AttributeError: 'Private_Base_Class' object has no attribute '__privateBaseClassVariable' ]

# instance_Base_Private_Class.__privateBaseMethod()
 # Error :- [ AttributeError: 'Private_Base_Class' object has no attribute '__privateBaseMethod' ]


# Error :-
    #  print( instance_Derived_Private_Class.__privateBaseAttribute )
    #            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # AttributeError: 'Private_Derived_Class' object has no attribute '__privateBaseAttribute'


# -------------------

 # From this we got to know that Protected Methods and class variables (attributes) cannot be accessed through Instance Object.


# ------------------------------------------------



# Public Methods and Properties 
 # we are allowed to access Public Methods and Properties within the class, from inside the Derived Class and Through the Instance Object.


# Protected Methods and Properties
 # we are allowed to access protected methods and Properties within the class, from the derived class
 # we are not allowed to access protected methods and properties from the Instance object
  # though protected methods and properties can be accessed within the Insntace object we are not allowed to do it, because its a bad practice.


# Private Methods and Properties 
 # We are not allowed to access Private Methods and Properties inside the Derived Class as well as from the Instance Object.
 # we can access it from within the Class [ Base or Parent ] class














