


# Getters and Setters 

# Here we will be learning about Getters and Setters in python 

# getters and setters can also be acheived by using as [ get() ] Method and [ set() ] Method,which will return the value and update the exsiting variables value.

# Keywords :-
 # [ @property ]
  # "@property" will convert a Method into a Property 

 # [ @getterSetterMethod_name.setter]

class Getters_Setters:

    def __init__(self):
        self.value = 0

    @property
    def getterSetter(self):
        return self.value
    
    @getterSetter.setter
    def getterSetter(self, newValue):
        self.value = newValue


instance_getters_setters = Getters_Setters()

print( instance_getters_setters.getterSetter )

instance_getters_setters.getterSetter = "New value"

print( instance_getters_setters.getterSetter )


print("""


""")


# ---------------------------------------------------------------------------------------------------------------------------------------------------------


class SetterGetter:

    def __init__(self):
        self.setget = "Some value"

    
    # [ @property ] 
     # when we use [ @property ] decorator at the Top of the Methods, those methods will be converted or Treated as Class Properties
        # when accessing this methods we should not invoke the by using parenthsis (), we will get error 
        # while updateing we have treat is as if we are updating an Property or class variables, etc [ print( variableName ) ].
        # when we access the method without assigning any value which means we are calling [ getter function ] ( the function which has @property ) decorator.

    @property
    def setterGetter(self):
        return self.setget




    # [ @methodName.setter ]
     #  [ @methodName.setter ] decorator has to be used for those methods when we want to update the Values of Some class Variables or Attributes which is present inside the class
     # when we want to access this method we have to treat it as if we are updating a Property
     # when we access this method and assign some values which means we are calling [ setter function ] ( the function which has @methodname.setter ) 
    @setterGetter.setter
    def setterGetter(self, newValue):
        self.setget = newValue



# Here we have Instance Object 
instance_setterGetter = SetterGetter()


print( instance_setterGetter )

# Here we just accessed [ instance_setterGetter ] without assigning any value which means we have called [ getter function ]
print( instance_setterGetter.setterGetter )

# here we accessed and assigned new value for [ setget ] method which means we have called [ setter function ], here [ setget ] variable might got updated.
instance_setterGetter.setterGetter = "Hello New New New Value"

# here again we tried to access the [ setterGetter ], now [ setget ] variable will have New updated value.
print( instance_setterGetter.setterGetter )



print("""



""")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Setter and Getter Functions can be to Access and update Private Class Variable, Attributes and methods


# let us use Getter and Setter to Update Private Variables 

class SetterGetter:

    def __init__(self):

        self.__privateAttribute = "Original Value"

    __privateClassVariables = "Original Class Variables"

    def __privateMethod(self):
        return "Original Method Value"
    

    # here let us create [ getters and setters ] to update [ Attribute, Class Variables and Methods ].


    # getter and setter to update [ __privateAttribute ]

    @property
    def updateAttribute(self):
        return self.__privateAttribute 
    
    @updateAttribute.setter
    def updateAttribute(self, newValue):
        self.__privateAttribute = newValue



    
    # getter and setter to update [ __privateClassVariables ]

    @property    
    def updateClassVariables(self):
        return self.__privateClassVariables
    
    @updateClassVariables.setter
    def updateClassVariables(self, newValue):
        self.__privateClassVariables = newValue

    



    # getter and setter to update [ __privateClassVariables ]
        
    @property 
    def updateMethod(self):
    #     return self.__privateMethod()
        return self.__privateMethod
    
    
    
    @updateMethod.setter
    def updateMethod(self, newValue):
        # Error :- [  Expression cannot be assignment target  ]
         # we get this error when we try to assign some value to some Expression, ex: invoking a Function and Assigning some values 
        # self.__privateMethod() = newValue

        self.__privateMethod = newValue




# Let us create Instance Object and Try to Access and Update the attributes, Class Variables and Methods
        
instance_SetterGetter_privateVariables = SetterGetter()

print( instance_SetterGetter_privateVariables )


print( instance_SetterGetter_privateVariables.updateAttribute )
instance_SetterGetter_privateVariables.updateAttribute = "New Attribute value"
print( instance_SetterGetter_privateVariables.updateAttribute )


print( instance_SetterGetter_privateVariables.updateClassVariables )
instance_SetterGetter_privateVariables.updateClassVariables = "New Class Variables"
print( instance_SetterGetter_privateVariables.updateClassVariables )


print( instance_SetterGetter_privateVariables.updateMethod )
instance_SetterGetter_privateVariables.updateMethod = "New Method Update"
print( instance_SetterGetter_privateVariables.updateMethod )
# Error :- [  TypeError: 'str' object is not callable  ]
  # Code : [ print( instance_SetterGetter_privateVariables.updateMethod ) ]
 # we get this error because we tried to access the method, 1st time the method has a function defination, so the value which the function returns is displayed
  # Code : [ instance_SetterGetter_privateVariables.updateMethod = "New Method Update" ]
 # next we updated the [ instance_SetterGetter_privateVariables.updateMethod ], the New value will be a String 
  # print( instance_SetterGetter_privateVariables.updateMethod )
 # next when we try to access the [ upddateMethod ] variable we get an Error because new [ __privateMethod ] is not a Function it has a String Value, we have used parenthsis in the [ updateMethod()  ] to update the [ __private ] that is why we get this error

# Solution :-
 # 1. Do not use patenthsis inside [ updateMethod() ] to update the method when we pass as String value
 # 2. when assigning New Value assign a Function defination for the [ __privateMethod ] 





def a():
    return "helo"




















