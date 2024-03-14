
# Single Inheritance 

# Single Inheritance means where a One Class will be Inherited by Only One Class


class Parent:

    classVariableParent = "variable"

    def methodParent(self):
        print( "Method Value" )


# Here [ Child ] class have Inherited parent class only once
class Child( Parent ):

    classVar_Child = "Child Variable"

    def methodChild(self):
        print("Method child")



# Instance Object for [ Child ]

instance_child = Child()

print( instance_child )

# Access Child class Variables and methods 

print( instance_child.classVar_Child )
instance_child.methodChild()

print( instance_child.classVariableParent )
instance_child.methodParent()


# Output :-

    # <__main__.Child object at 0x0000023C20A8A540>
    # Child Variable
    # Method child  
    # variable      
    # Method Value  




















