

# Multiple 

 # Here we will be Learning on how Multiple Inheritance works

 # when One Derived Class inherits nore than 1 Base class which means its a Multiply Inheritance 

class Base_1:

    props1 = "Property 1"

    def methods1(self):
        print("Method Multiple Value")

    
class Base_2:

    props2 = "Property 2"

    def method2(self):
        print( "method value" )


# Here inside [ DerivedClass ] when we Inherit more than 1 Class it means its as Multiple Inheritance.
    # Here now [ DerivedClass() ] class ecome[ multiple Inheritance]
class DerivedClass( Base_1, Base_2 ):
    propsDerived = "Property 2"

    def methodDerived (self):
        print( "method value" )


# -------
        

# create Instance and Access the [  DerivedClass  ] 
        
instance_DerivedClass = DerivedClass()

# Here we accessed [ current object ] properties and Methods
print( instance_DerivedClass )
print( instance_DerivedClass.propsDerived )
instance_DerivedClass.methodDerived()

# here we accessed [ Base_1 ] class
print( instance_DerivedClass.props1)
instance_DerivedClass.methods1() 


# here we accessed [ Base_2  ] properties and methods
print( instance_DerivedClass.props2 )
instance_DerivedClass.method2()



# Output :-

    # <__main__.DerivedClass object at 0x000002D15CA7A750>
    # Property 2
    # method value
    # Property 1
    # Method Multiple Value
    # Property 2
    # method value


# Here we did not encouter any Error which means we have successfull Implemented Multiple Inheritance.











