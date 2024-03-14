


# Composition 

# Composition means when you try to Load the Parent Class inside the Child Class without using Inheritance 
# In compostion we will create a class variables or attributes (intance varialbes ) we will invoke [ Parent Class Constructor ] and assign it as a Value for the variable
  # with this variable we can easily access the [ Parent Class methods, attributes and class variables ] from child class Instance Object 

# Important :-

 # 1. The Changes made in the Parent/Base class will not affect the Child/Derived Class.


class Composition_Parent:

    def __init__(self):
        print("Composition_Parent Constructor")

        self.composition_parent_attribute = "Composition Parent Attribute Value"


    def composition_parent_method(self):
        print( "Composition Parent Method" )


    composition_parent_classVariables = "Composition Class Variables"
    


# ----------
    


class Composition_Child:

    def __init__(self):
        print("Composition_Child Constructor")

        self.composition_child_attribute = "Composition Child Attribute Value"

         # Here we have Loaded [ Composition_Parent ] class Explicitly by calling the [ Composition_Parent ] Class Constructor.
          # By using [  composition_parent_classLoaded ] attribute we can access the Methods and Properties which is present inside the Parent/Base class [ Composition_Parent ]
        self.composition_parent_classLoaded = Composition_Parent()

        # why we have Loaded [ Composition_Parent() ] Class inside the [ __init__() ] method and not on any Other Methods ?
          # The reason why we loaded the [ Composition_Parent() ] Class inside the [ __init__() ] method is because, when we create an Instance object [ __init__()] method gets automatically loaded so whatever statements which are present inisde the indentened block gets executed immediately so the Composition_Parent class will also get loaded immmediately
        
        # what happens when we use [ Composition_Parent() ] Class inside the other Method ?
          # when we use [ Composition_Parent() ] Class inside the other Method, untill the Other Method gets invoked there will not be any changes taking place inside the other methods indented block
          # when other method has [ Composition_Parent() ] Class, the [  Composition_Parent() ] class will not get Loaded immediately so it becomes really difficult the access the methods, attributes, class variables which is inside [ Composition_Parent() ] class.



    def composition_child_method(self):
        print("Composition Child Method")

    composition_child_classVariables = "Composition Child Class Variables"


# ---------------
    

# Now let us create an Instance of [ Composition_Child ] and access the methods, attributes and class variable which is inside [ Composition_Child and Composition_Parent ].
    

instance_Composition_Child = Composition_Child()

print( instance_Composition_Child )


  # Accessing [ Composition_Child ] and access the methods, attributes and class variable

print( instance_Composition_Child.composition_child_attribute )
print( instance_Composition_Child.composition_child_classVariables )
instance_Composition_Child.composition_child_method()

# Output :-

    # Composition_Child Constructor
    # Composition_Parent Constructor
    # <__main__.Composition_Child object at 0x0000023DCE15A3F0> 
    # Composition Child Attribute Value
    # Composition Child Class Variables
    # Composition Child Method



# ----------

 # Accessing [ [ Composition_Parent ] and access the methods, attributes and class variable ] from [ Composition_Child ]

  # Here we have accesed methods, attributes and class variable without any Errors.
print( instance_Composition_Child.composition_parent_classLoaded )
print( instance_Composition_Child.composition_parent_classLoaded.composition_parent_attribute )
print( instance_Composition_Child.composition_parent_classLoaded.composition_parent_classVariables )
instance_Composition_Child.composition_parent_classLoaded.composition_parent_method()


# Output :-

    # <__main__.Composition_Parent object at 0x0000023DCE15A420>
    # Composition Parent Attribute Value
    # Composition Class Variables
    # Composition Parent Method



print("""



""")



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------


# Here we used [ Inheritance ]
# Let us create a Inheritance Composition Classes and Try to make changes inside the Parent/Base Class and check weather any changes had happened in the Child/Derived class

class CompositionParent:

    def __init__(self):
        self.CompositionParent_attribute = "CompositionParent Attribute Value"

    def CompositionParent_method(self):
        print( "CompositionParent method" )

    CompositionParent_classVariable = "Composition Parent class Variable"


class CompositionChild(CompositionParent):

    
    def __init__(self):
        # super().__init__()
        CompositionParent.__init__(self)
        self.CompositionChild_attribute = "CompositionParent Attribute Value"

    def CompositionChild_method(self):
        print( "CompositionParent method" )

    CompositionChild_classVariable = "Composition Parent class Variable"



# Instance Objects 

instance_CompositionChild = CompositionChild()
instance_CompositionParent = CompositionParent()


# Accessing the Values 

print( instance_CompositionParent.CompositionParent_attribute )
print( instance_CompositionChild.CompositionParent_attribute )

# Now let us make some Chagnes in [ CompositionParent_attribute ]

instance_CompositionParent.CompositionParent_attribute = "----- New Updated Value ------"

print( instance_CompositionParent.CompositionParent_attribute )
print( instance_CompositionChild.CompositionParent_attribute )


#  Output :-

    # CompositionParent Attribute Value
    # CompositionParent Attribute Value
    # ----- New Updated Value ------
    # CompositionParent Attribute Value

# Here we can clearly observe that the changes which has been made in the [ Parent class Attribute ] will not make any changes inside the [ Child Class Attribute ]




print("""

""")

print( instance_CompositionParent.CompositionParent_classVariable )
print( instance_CompositionChild.CompositionParent_classVariable )

instance_CompositionParent.CompositionParent_classVariable = "--- ABCD New Updated Value ----"



print( instance_CompositionParent.CompositionParent_classVariable )
print( instance_CompositionChild.CompositionParent_classVariable )


# Output :

    # Composition Parent class Variable
    # Composition Parent class Variable
    # --- ABCD New Updated Value ----
    # Composition Parent class Variable


# Here we can clearly observe that the changes which has been made in the [ Parent class class variables ] will not make any changes inside the [ Child Class class variables ]


print("""



""")





# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Composition 

# Let us create a Composition Classes [ Parent and Child ] will make changes inside Parent Class and check weather those changes are reflected inside the Child Class

class CompostionParentClass:

    def __init__(self):
        self.compostionParentClass_attribute = "Composition Parent Class Attribute"

    def compositionParentClass_Method(self):
        print("Composition Parent Method")

    compositionParentClass_classVariable = "composition Parent Class class Variable"



class CompostionChildClass:

    def __init__(self):

        self.compostionChildClass_attribute = "Composition Child Class Attribute"

        # here let us Load the [ CompostionParentClass ] class 
        self.CompostionParentClass_loaded = CompostionParentClass()


    def compositionChildClass_Method(self):
        print("Composition Child Method")

    compositionChildClass_classVariable = "composition Child Class class Variable"



# Let us Create Instance Objects 
    
instance_CompostionParentClass = CompostionParentClass()
instance_CompostionChildClass = CompostionChildClass()



print( instance_CompostionParentClass.compositionParentClass_classVariable )
print( instance_CompostionChildClass.CompostionParentClass_loaded.compositionParentClass_classVariable )


instance_CompostionParentClass.compositionParentClass_classVariable = "----- New Updated Value ------"


print( instance_CompostionParentClass.compositionParentClass_classVariable )
print( instance_CompostionChildClass.CompostionParentClass_loaded.compositionParentClass_classVariable )


# Output :-

    # composition Parent Class class Variable
    # composition Parent Class class Variable
    # ----- New Updated Value ------
    # composition Parent Class class Variable


# Learnings :-

 # The changes which we make inside the Parent Class Instance Object will not reflect or make any changes inside [ Child Class Instance Object ]
  # Here in Composition [  Parent Class Instance Object ] has a unique referenct as well as [ Child Class Instance Object ], so changes made in Parent class will not have any effect inside the Child Class.














