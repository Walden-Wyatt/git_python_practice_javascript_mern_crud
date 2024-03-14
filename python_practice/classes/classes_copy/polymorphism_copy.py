

# Polymorphism 

 # Here we will be Learning about Polymorphism in python Programming Language

# Code Explanation

# Polymorphism means where there will be only 1 Common Function which will accept different 1 parameter ( the arguement for parameter must be a Instance Object ), the Function will return 1 similar method or class variable which is present inside the all the Classes of Instance Object

 # when we try to Invoke the Common Function by passing different Object instances as Arguements we might get common method or class variable which is present inside all the classes as a Value, where the Value will be different for all the Function calls.

 # Polymorphism allows objects of different classes to be treated as objects of a common base class. It allows a single interface to represent different types of objects.



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Here let us have List of classes


class Class1:
    def commonMethod(self):
        return "Class 1 Common Method"
    
class Class2:
    def commonMethod(self):
        return "Class 2 Common Method"
    
class Class3:
    def commonMethod(self):
        return "Class 3 Common Method"


# Here let us have Polymorphic Method
    
def polymorphicFunction( instanceObject):
    return instanceObject.commonMethod()


# Here let us have Instance Objects for all the Classes


instanceClass1 = Class1()

instanceClass2 = Class2()

instanceClass3 = Class3()

# Now let us invoke the [ polymorphicFunction() ]

print( polymorphicFunction( instanceClass1 ) )

print( polymorphicFunction( instanceClass2 ) )

print( polymorphicFunction( instanceClass3 ) )



# Ouput :-

    # py polymorphism.py
    # Class 1 Common Method
    # Class 2 Common Method
    # Class 3 Common Method
    # PS C:\Users\user\Desktop\python_practice\classes> 




print("""







""")


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------



# [ Practice 2 ]



# Here we have Polymorphism Function
def polymorphismCommonFunction( instanceObject ):
    return instanceObject.commonMethod1()



# Here we are 3 classes

class Poly1:
    def commonMethod1(self):
        return "Poly 1 Comman Method"


class Poly2:
    def commonMethod1(self):
        return "Poly 2 Comman Method"


class Poly3:
    def commonMethod1(self):
        return "Poly 3 Comman Method"


# Here we have Instance Objects
    
instancePoly1 = Poly1()

instancePoly2 = Poly2()

instancePoly3 = Poly3()



# Here let us invoke [ polymorip ]

print( polymorphismCommonFunction( instancePoly1 ) )

print( polymorphismCommonFunction( instancePoly2 ) )

print( polymorphismCommonFunction( instancePoly3 ) )




print("""







""")


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------



# [ Practice 3 ]



# Here let us have Polymorphic Function

def polymorphic_function( instanceObject ):
    return instanceObject.polyMethod()


# here we have 3 classes

class polymorph1:
    def polyMethod(self):
        return "Polymorphic Method 1"
    

class polymorph2:
    def polyMethod(self):
        return "Polymorphic Method 2"
    
    
class polymorph3:
    def polyMethod(self):
        return "Polymorphic Method 3"



# Here let us have Instance Objects
    
instancepolymorph1 = polymorph1()

instancepolymorph2 = polymorph2()

instancepolymorph3 = polymorph3()


# Let us invoke [ polymorphic_function ] function by passing instance objects as arguements

print( polymorphic_function( instancepolymorph1 ) )

print( polymorphic_function( instancepolymorph2 ) )

print( polymorphic_function( instancepolymorph3 ) )




# Output :-

    # Polymorphic Method 1
    # Polymorphic Method 2
    # Polymorphic Method 3





# Example for Polymorphism 

# Inheritance of Class Methods and overridding the Methods of parent class is an example for for polymorphsim
 # Here there is one single Method which is being called by differnt Classes of Class Instance Object 































