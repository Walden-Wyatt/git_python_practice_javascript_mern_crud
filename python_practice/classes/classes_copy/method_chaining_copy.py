

# Method Chaining 

# Here we will be Learning on how Method chaining works
 # method chaining is a Method which returns the same Class using (self) parameter
 # Method chaining means where we keep on calling a Sequences of methods

# Important Points :-
 # Method chaining is Infinite we can keep on chain a Method as well as Properties, If we keep on using [ dot notation ] (.) Methods and Properties which are related to that Specific Datatype will be poped
 # Based on what Datatype value does the Method returns, appropriate Methods and Properties for those Methods will be invoked
   # Those methods which starts and Ends with [ __methodName__() ] are Object Class Methods and properties
   # Those methods which does not start and Ends with [ __methodName__() ]  are Class Specific Methods, those methods and Properties belongs that a Specific Class of the Datatype Value
    # if the datatype value is a String -> then the poped up methods will be from "String" class, if datatype is Number -> then the poped up method will be from Number class, It keeps on going Infinitely based on the Datatype Value.

class Calculator:

    def __init__(self, value):
        self.value = value

    def add(self, x):
        self.value += x # self.value = value + x
        return self 
    
    def multiply(self, y):
        self.value *= y 
        return self 
    

instance_Calculator = Calculator(10)

# Here we used Method chaining 
print( instance_Calculator.add(10).multiply(2).value )


class Example:
    def method1(self):
        print("Method 1")
        return self

    def method2(self):
        print("Method 2")
        return self

instance_Example = Example()


# print( instance_Example.method1().method2().method1().method2().method1().method2().method2().method2().method2().method1().... )
 # Here we started with [ instance_Example ] and kept on chaining the Methods, This chaining will be infine there is not end for this Chaining
 # here we can also observer we have chined same Method Multiple times, we also chained the Method repeatedly in a sequence of Next to Next.
 
 # we can also get some other Datatypes methods by twiking the value in the Sequence 
  # We cannot directly change or use the Literal Values in a Sequence of Chaining
  # We are only allowed to use whatever method is Avialable inside that specific datatype or Which is Poped.

# print( "string".capitalize().11 ) # Error :- [ "(" was not closed  ]
 # here we tried to add a New literal value [ 11 ] in the sequence of method chaining which we are not allowed to do




# --------------------------------------------------------------------------------------------------------------------------------------------------------------



# If you want to Keep on Looping the Methods which is Inside the Current Class then we can use the Below Approach

 # In this looping when we



class LoopCurrentClass:

    # Here is how we can assign the Current class as a Value for the Class Variables 
    classVariable = None  # Here we have Class variables with None value

    def __init__(self):
        self.attribute = self

         # here inside th [__init__() ] method we have re-assigned the [ classVariable ] with [ self ] as a Value
        self.classVariable = self

    def method_1(self):
        print("Hello Method 1")
        return self

    def method_2(self):
        print("Method 2")
        return self
    
    def method_3(self):
        print("Method 3")
        return self
    
    def method_4(self):
        print("Method 4")
        return self
    
    def method_5(self):
        print("Method 5")
        return self
    
    
    


# Let us create an Instance Object and try to loop 

instance_LoopCurrentClass = LoopCurrentClass()

print( instance_LoopCurrentClass )

# Here we will Loop the methods 

instance_LoopCurrentClass.method_1().method_2().method_3().method_4()

# here let us try to method chain [ attribute ] in the sequence 
instance_LoopCurrentClass.method_5().attribute.method_1()
 # here we can see that value of [ attribute ] is not printed because, the value which is present inside [ attribute ] property is the [self, i.e, the current class ]
 # From here we learned that we can method chain Methods as well as Attributes


# here let us try to method chain [ class varialbes ]
instance_LoopCurrentClass.method_1().classVariable.method_1()
 # here we can see that value of [ classVarialbe ] is not printed because, the value which is present inside [ classVarible ] property is the [self, i.e, the current class ]
 # From here we learned that we can method chain Methods as well as Class Variables


# When you stop the Method chaining at some method, whatever values or statements which is present inside the method will be displayed ( i.e, lines of codes which comes before "return" line)



# ----------

# Cases in which Looping of Current Class methods and class variables ends
 
 # 1. when the Current Class Method does not return [self] as a Return value
 # 2. when you try to include a Property in the method chaining using [ dot notation ], where the property have some other datatype value.
 # In the above 2 cases the Method and property chaining of current class will end, to moves to other class methods and properties based on what datatype value does the method or proeprty returned


# Cases where you can keep chaining the Current Class Methods and Properties
 
 # 1. Incase of Methods - when the current class methods returns [self] (i.e, the current class itself ) 
 # 2. Incase of Attribute  - when the current class Attribute has [self] as its value, in such a case we can even perform chaining for those Attributes
 # 3. Incase of Class Variables - in case of we can method chain when the variable has [self] as its value
   # we can acheive this by create a class variable, and re-assigning the value for class variable in the [__init_() ] method because as soon we invoke the Constructor to create Instance Object, Class variable value will get re-assigned (updated). 
   # we can also use this other Methods, but the problem is unless we invoke that specific method the re-assignment will not happen























