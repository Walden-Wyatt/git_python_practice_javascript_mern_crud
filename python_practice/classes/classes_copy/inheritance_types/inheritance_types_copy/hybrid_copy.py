


# Hybrid Inheritance 

# Hybrid Inheritance means where one class might have inherited by multiple classes and later, this current classes will be inherited  Other Function
 # This is infinite we class can inherit antoher multiple classes and this class will be inherited by some ohter person, this process will keep continueing.


class Hybrid_1:
    hybrid_1_classVariable = "Hybrid Class Variable"

    def hybrid_1_method(self):
        print( "Hybrid one method" )


class Hybrid_2:
    hybrid_2_classVariable = "Hybrid 2 Class Variable"

    def hybrid_2_method(self):
        print( "Hybrid 2 method" )


# Here we can see that [ Hybrid_2 ] class have inherited by [ Hybrid_1 and Hybrid_2  ] class
class Hybrid_3( Hybrid_1, Hybrid_2 ):
    hybrid_3_classVariable = "Hybrid 3 Class Variable"

    def hybrid_3_method(self):
        print( "Hybrid 3 method" )


class Hybrid_4( Hybrid_3 ):
    hybrid_4_classVariable = "Hybrid 4 Class Variable"

    def hybrid_4_method(self):
        print( "Hybrid 4 method" )
    

class Hybrid_5(Hybrid_4):
    hybrid_5_classVariable = "Hybrid 5 Variable"

    def hybrid_5_method(self):
        print( "Hybrid 5 method")


# Let us create instance object of [ Hybrid_5 ] and try to access all the Properties and methods which are inside as well as Related to these Object
        
instance_Hybrid_5 = Hybrid_5()

print( instance_Hybrid_5 )

print( instance_Hybrid_5.hybrid_1_classVariable )
instance_Hybrid_5.hybrid_1_method()

print( instance_Hybrid_5.hybrid_2_classVariable )
instance_Hybrid_5.hybrid_2_method()

print( instance_Hybrid_5.hybrid_3_classVariable )
instance_Hybrid_5.hybrid_3_method()

print( instance_Hybrid_5.hybrid_4_classVariable )
instance_Hybrid_5.hybrid_4_method()

print( instance_Hybrid_5.hybrid_5_classVariable )
instance_Hybrid_5.hybrid_5_method()



# Output :-'

        # py hybrid.py
        # <__main__.Hybrid_5 object at 0x000002C80F08A7B0>
        # Hybrid Class Variable  
        # Hybrid one method      
        # Hybrid 2 Class Variable
        # Hybrid 2 method        
        # Hybrid 3 Class Variable
        # Hybrid 3 method        
        # Hybrid 4 Class Variable
        # Hybrid 4 method        
        # Hybrid 5 Variable      
        # Hybrid 5 method        


# Here we have successfully accessed wihtout any, which means we have successfully implemented [ Hybrid class ]















