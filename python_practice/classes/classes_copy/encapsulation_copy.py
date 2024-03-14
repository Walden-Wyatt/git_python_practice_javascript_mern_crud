




# Encapsulation 

# Encapsulation means making a Class Variable Private and Accessing it from [ getter and setter methods]

 # Encapsulation and Private Methods and Properties are same only the name is different, Encapsulation is done using Private Properties and Methods.


class Encapsulated_parent:
    def __init__(self):
        print("Encapsulated_parent Constructor")

        self.__parentAttribute = "Parent Attribute Value"

    def __parentMethod(self):
        print("Parent Method")

    __parent_classVariable = "Parent Class Variable" 

    # accessing within the class scope

    def accessingWithinClass(self):
        print( self.__parentAttribute )
        print( self.__parent_classVariable )
        self.__parentMethod()



class Encapsulated_child(Encapsulated_parent):

    def __init__(self):
        print("Encapsulated_child Constructor")

        self.__childAttribute = "Child Attribute Value"


    def __childMethod(self):
        print("Child Method")

    __child_classVariable = "Child Class Variable"



  # [ accessingWithinChildClass ]
    def accessingParentProps_methods(self):

        # print( self.__parent_classVariable )
        # Error :- [  AttributeError: 'Encapsulated_child' object has no attribute '_Encapsulated_child__parent_classVariable'. Did you mean: '_Encapsulated_child__child_classVariable'? ]
        
        # print( self.__parentAttribute )
        # Error : [  AttributeError: 'Encapsulated_child' object has no attribute '_Encapsulated_child__parentAttribute'. Did you mean: '_Encapsulated_child__childAttribute'?  ]
        
        # self.__parentMethod()
        # Error :- [  AttributeError: 'Encapsulated_child' object has no attribute '_Encapsulated_child__parentMethod'. Did you mean: '_Encapsulated_child__childMethod'?  ]
    
        print("Method which we used to access Parent Class Methods and properties")

    # accesing 


# Instance Objects
    

instance_Encapsulated_parent = Encapsulated_parent()

instance_Encapsulated_child = Encapsulated_child()


# Here accessed within the class
instance_Encapsulated_parent.accessingWithinClass()


print("""


""")


# Here accesing within child class
instance_Encapsulated_child.accessingParentProps_methods()



# ----------------------

# Output :-

    # Encapsulated_parent Constructor
    # Encapsulated_child Constructor
    # Parent Attribute Value
    # Parent Class Variable
    # Parent Method




    # Method which we used to access Parent Class Methods and properties    






# --------------------------------------------------------------------------------------------------------------------------------------------------------------



print("""




Practice 2
      



""")




class EncapsulatedParent:

    def __init__(self):
        print("Encapsulated Parent Constructor")

        self.__privateParentAttribute = "Private Attribute Value"

    __privateParentClassVariable = "Private Class Variable value"

    def __privateParentMethod(self):
        print("Private Method")






class EncapsulatedChild(EncapsulatedParent):

    def __init__(self):
        print("Encapsulated Child Constructor")

        self.__privateChildAttribute = "Private Child Attribute"

    __privateChildClassVariable = "Private Child class variable"

    def _privateChildMethod(self):
        print( "Private Child Method" )


    # access Parent Class Private Methods and Properties from inside Derived/Child class Method
        
    def accessParentPropertiesMethods(self):

        # print( self.__privateParentAttribute )
         # Error :- [  AttributeError: 'EncapsulatedChild' object has no attribute '_EncapsulatedChild__privateParentAttribute'. Did you mean: '_EncapsulatedChild__privateChildAttribute'?  ]
        # print( self.__privateParentClassVariable )
         # Error :- [ AttributeError: 'EncapsulatedChild' object has no attribute '_EncapsulatedChild__privateParentClassVariable'. Did you mean: '_EncapsulatedChild__privateChildClassVariable'?    ]
        # self.__privateParentMethod()
         # Error :- [ AttributeError: 'EncapsulatedChild' object has no attribute '_EncapsulatedChild__privateParentMethod'. Did you mean: '_EncapsulatedParent__privateParentMethod'? ]
        
        print("Methods and Properties of Parent Class")
 



# ----
        
# Instance Objects 
        

instance_Encapsulated_parent_2 = EncapsulatedParent()

instance_Encapsulated_child_2 = EncapsulatedChild()


# access Parent/Base class methods and properties from Child/Derived class public method [ accessParentPropertiesMethods ]

instance_Encapsulated_child_2.accessParentPropertiesMethods()




# Output :-


    # Encapsulated Parent Constructor
    # Encapsulated Child Constructor
    # Methods and Properties of Parent Class














































