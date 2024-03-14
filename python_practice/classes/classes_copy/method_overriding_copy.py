


# Method Overriding 

# Here we will be Learning about Method Overriding



class ParentClass:

    def __init__(self):
        print("Parent Constructor")

    def sports(self):
        return "Sport - Cricket"
    

class ChildClass(ParentClass):

    def __init__(self):
        print("Child Constructor")

  # [ accessParentClass ] is used check for the value of [ self.sports() ] method, before updating the [ self.sports() ] methods value
    def accessParentClass(self):
        print(self.sports())

  # here we have overridden [ [ self.sports() ] ] method
    def sports(self):
        return "Overriden Sport - Volly Ball"
    
  # here we have accessed [ self.sports() ] method after overring the [ sports() ] method
    def accesChildClass(self):
        print( self.sports() )



# Let us have Instance Objects
        

# Instance of Parent Class
        
instance_ParentClass = ParentClass()
print( instance_ParentClass.sports() ) # Ouput :- Sport - Cricket
 # here this method returns the value which comes before overriding.




# Instance of Child Class

instance_ChildClass = ChildClass()

# print( instance_ChildClass )

 # here we accessed [ accessParentClass ] method which comes before overridding the [ sports()] method an [ accesChildClass ] after overridding the sports, but both has return the same value that is the Overridden value

  # Here position in where we are updating does not matter, what matters is the wheather you have Overridden the Parent Class method inside the Child class is Important,if you overridden which means the value will be updated else not

instance_ChildClass.accessParentClass()
instance_ChildClass.accesChildClass()



# Output :-

    # PS C:\Users\user\Desktop\python_practice\classes> py method_overriding.py
    # Child Constructor
    # Overriden Sport - Volly Ball
    # Overriden Sport - Volly Ball
    # PS C:\Users\user\Desktop\python_practice\classes> 


print(""""
      
      
      """)



# -----------------------------------------------------------------------------------------------------------------------------------------------------



# Method overriding within the Class

class OverridingWithinClass:

     # First Instance of [ originalMethod ]
    def originalMethod(self):
        return "String valu"
    
    # Second Instance of [ originalMethod ], This is Overridden method
    def originalMethod(self):
        return {
            "key": "Value 1",
            "key_2": 10001,
            "key_3": False
        }


instance_OverridingWithinClass =  OverridingWithinClass()

print( instance_OverridingWithinClass.originalMethod() )

# Ouput :-
# {'key': 'Value 1', 'key_2': 10001, 'key_3': False}

# Here we can see that the value which is present inside 2nd Instance of [ originalMethod ] has been returned, which means First instance of [ originalMethod ] has been overridden by  Second Instance of [ originalMethod ] method
# First Instance [ originalMethod ] will be Garbage collected by the python program


print(""""
      
      
      """)



# -----------------------------------------------------------------------------------------------------------------------------------------------------



# Instance Object 


overrideObject = {

}

# when you use [ {} ] flower brackets, behind the Scene Python will call Object Class, whatever [ variables, methods and attribute ] which we use inside the object python will create a Class and assign this [ class variables, methods and Attributes ]

# behind the scene python will create a Class for [ overriddenObject ] instance

# class Object:



# -----------------------------------------------------------------------------------------------------------------------------------------------------------


  ########### How Python will Create Class for Instace Objects ###########



# Let us create an Instance Object and write how python will create the class behind the scene

def instanceMethod():
    return "instance Method value"

instanceObject = {
    "property1": "Value 1",
    "method_1": instanceMethod,
    "property_object": {'key': "Value", "int": 123 },
    "property_list": [ 1,"string", False, (1,2,3) ]
}

# def instanceMethod():
#     return "instance Method value"
  # Warning :- "instanceMethod" is not definedPylancereportUndefinedVariable
   # This warning will occur when we use or invoke a Method before defining it.


# Accessing the Methods and Properties of [ instanceObject ]

print( instanceObject["property1"] )
print( instanceObject["property_object"] )
print( instanceObject["property_list"] )
print( instanceObject["method_1"]() )




# Output :_

    # Value 1
    # {'key': 'Value', 'int': 123}
    # [1, 'string', False, (1, 2, 3)]
    # instance Method value






# How python will interpret and create a class for [ instanceObject ] ?

class Object:

    property1 = "Value 1"

    def method_1(self):
        return "instance Method value"
    
    property_object = { 'key': "Value", "int": 123 }

    property_list = [ 1,"string", False, (1,2,3) ]





# Let us create an Instance object using [ Object ]

instanceObject_2 = Object()

print( instanceObject_2.property1 )
print( instanceObject_2.property_object )
print( instanceObject_2.property_list )
print( instanceObject_2.method_1() )

# print( Object.property1 )
# print( Object.method_1(instanceObject_2) )


# Output :-

    # Value 1
    # {'key': 'Value', 'int': 123}
    # [1, 'string', False, (1, 2, 3)]
    # instance Method value



# Output :-

# Value 1
# {'key': 'Value', 'int': 123}
# [1, 'string', False, (1, 2, 3)]
# instance Method value
# Value 1
# {'key': 'Value', 'int': 123}
# [1, 'string', False, (1, 2, 3)]
# instance Method value

 # Here we can see that Output from [ instanceObject and instanceObject_2 ] are the same, which means we have properly created how python will interpret and creeate the Class for the Instance Object which we directly create.


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------



# [ Practise 2 ]



def overrideFuncion():
    print("Hello Override Functon")

def newOverrideFunction():
    print(" New and overridden Method")

abc_object = {

"property1": "Value 1",
"method1": overrideFuncion,

# def method1():  # Error : [  Statements must be separated by newlines or semicolons ]--- This Error occurs when we try to use any Function definations ( def fund() ), print() statement etc.
# print()

"method1": newOverrideFunction

}


# Now let us try to access [ method1 ]

abc_object["method1"]()



# Ouput :-
 # New and overridden Method

 # Here we can see that the Overridden method value has been returned




print("""


""")





# --------------------------------------------------------------------------------------------------------------------------------------




# Property Overridding 


class PropertyOverride:

    property_1 = "Value Property 1"

    property_1 = "Overridden Property value"


# instance Object 
    
instance_PropertyOverride = PropertyOverride()

print( instance_PropertyOverride.property_1 )



# Output :-
 # Overridden Property value

# here we can see that the overridden value of [ property_1 ] has been displayed where as [ Value Property 1 ] is not displayed because value got overridden 






























