

# Heirachical Inheritance 

# When One Class has been inherited by multiple classes then it is called a Heirachical


# Here we have [ Base Class ] which will be inherited by many other Derived Classes
class BaseParent:
    baseProperty = "Base Property"

    def baseMethod(self):
        print("Base Method")


# Here we have [ Derived_1 ] class
class Derived_1(BaseParent):
    derived_1_property = "Derived 1 Property"


# Here we have [ Derived_2 ] Class

class Derived_2(BaseParent):
    derived_2_property = "Derived 2 Property"



# Let us create instance object for [ Derived_2  ] and try to access [  BaseParent ] class.
    
instanceDerived_2 = Derived_2()

  # here we will access properties and methods which is within the class
print( instanceDerived_2 )
print( instanceDerived_2.derived_2_property )

  # here we will access Properties and methods which is inside [ Derived_2 ] class

print( instanceDerived_2.baseProperty )
instanceDerived_2.baseMethod()



# Output :-

    # py multiple.py
    # <__main__.DerivedClass object at 0x000001DF7293A750>
    # Property 2
    # method value
    # Property 1
    # Method Multiple Value
    # Property 2
    # method value


# we got output without any error which means we have successfully accessed the Methods and properites of base class from Derived class 2 




















