


# Multilevel Inheritance 

# Multilevel Inheritance means where One Class Inherits Other class, Other class inherits next others, it keeps on going this is called as Multilevel inheritance


# Let us create Inheritance from GrandParent to GrandChild


class GrandParent:
    grandParent_variable = "Grand Parent"

    def grandParent_method(self):
        print("Grand Parent Method")


class Parent(GrandParent):
    parentVariable = "Parent Variable"

    def parent_method(self):
        print("Parent Method")


class Child( Parent ):
    childVariable = "Child Variable"

    def child_method(self):
        print("Child Method")

class GrandCild( Child ):

    grandChildVariable = "Grand Child Variable"

    def grandChild_Method(self):
        print( "Grand Child Method" )


# Now let us create Instance object for [ GrandCild ] and try to access the methods and variables which are present inside the [ Child, Parent, GrandParent ]
        
    
instance_Grand_child = GrandCild()

print( instance_Grand_child )


# here let us access [ Child ] Class 
print( instance_Grand_child.childVariable )
instance_Grand_child.child_method()


# here let us access [ Parent ] class
print(instance_Grand_child.parentVariable )
instance_Grand_child.parent_method() 


# here let us access [ GrandParent ] class

print( instance_Grand_child.grandParent_variable )
instance_Grand_child.grandParent_method()



# Output :-

    # <__main__.GrandCild object at 0x000001AFD332A6C0>
    # Child Variable     
    # Child Method       
    # Parent Variable    
    # Parent Method      
    # Grand Parent       
    # Grand Parent Method



# Here we did not had any Error which means we have successfully used [ Multilevel inheriance ]








