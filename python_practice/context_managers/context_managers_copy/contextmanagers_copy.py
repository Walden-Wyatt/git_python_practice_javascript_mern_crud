


# Context Managers 

# How to use Context Manager in python 


# Differenct ways to use Context Manager

 # 1. how to handle files at the Top Level without using Context Managers [ with ] keyword using [ open() and close() ] methods
 # 2. Context Manager using [ try..except..else...finally] blocks
 # 3. Context Manager using [ with ] keyword
 # 4. Create a our Own Context Managers using [ Classes ] [ __init__(), __enter__(), __exit__() ] dunder methods
 # 5. How to Handle Exections inside the Context Managers [ __exit__() ] method
 # 6. How to create Context Managers using Generators and Decorators by importing [ comtextlib ], decorator [ @contextmanager ]




# -------------------------------------------------------------------------------------------------------------------------------------------------------------------



 # 1. how to handle files at the Top Level without using Context Managers [ with ] keyword

  # Here we will be using [ open() and close() ] built-in functions in Python to perform file operations


file = open("./contentFile.py", "r" )
# between [open() and close() ] functions we can any code which will be displayed in the Terminal 

# here we used [ read() ] method to read the contents of the file
readReturn_value = file.read()
print( readReturn_value, "Read return value" )

# Let us check what will [ file.read() ] method returns

print( readReturn_value )
print( type(readReturn_value) )

# Output :-

    # <class 'str'>

# here we can see that the type of [readReturn_value] is a string because whatever value we read from the file is a string datatype.
 # when we read the file we are ultimately accessing the values which is of String Datatypes.




print("\n\n")
print("Middel line")

file.close()



# Let us check what will [ file ] return 


print(file, "read return value")
print( type(file) )

# Output :-

    # <_io.TextIOWrapper name='./contentFile.py' mode='r' encoding='cp1252'> read return value
    # <class '_io.TextIOWrapper'>

# Here we can see that [ file.read() ] method returns [ _io.TextIOWrapper ] class, this class can be used to perform File Operations





# ------------------------------


# let us write the file 

file = open("./writefile" , "w" )

 # Points :-
  # open() method will accept following arguements [ file_path, mode, buffering, encoding, errors, newline, closefd, opener ]
   # 2 mandatory arguments which we have to use is [ file_path, mode ]
   # open() method will return an Instance object which will have methods which can be used to perform file operations such as [ close(), read(), write(), etc ]
  
  # [ file_path ] - if the file name is not present and file extention is not created in such when using [ read mode ] in such situation, python will create New file without any extentions
     # if you provide file extension in such situation based on the file extension new python file will created.
print("new File")


# here let us use [ write()) ] method and write some content inside the file 
file.write("Here we wrote come content inside [writefile]")

print("\n\n")

# let us check is there any content inside [ writefile]
    # file.read() 
     # Error :- 
        # io.UnsupportedOperation: not readable
        # We get this error because when when we open the file used specified [ "w" ] as 2nd arguement in [open() method ], which means we are allowed to perform only Write operations, when we try to perform other operations other than read we will get the above error.




# When you open a File we have to mandatorily close the files otherwise we will encounter many issues such as  [ Resource Leakage, Data Integrity, Concurrency Issues, Portability Issues, etc ]

 # Here we used [ close() ] method to close the files
file.close()





# ------------------------------


# What happens when we use [write() ] method for the files which has contents already 


contentPresent = open("writefile", "w" )


# file content before writing - [ Here we wrote come content inside [writefile] ]
# file content after writing - [ " New Updated values " ]

  # when we try to write and file which has content already in such situation, previous contents of the File will completely erased [ from 1 and end of the file ], New content will be written from [ line 1 ] to end of the line
writeReturn = contentPresent.write(" New Updated values ")
print( writeReturn, "written value" ) 
# Output :- 20 written value
 # [ contentPresent.write() ] - this method will return the length of Text which we have given inside the [ write() ] arguements



# let us check the type of [ writeReturn ]
print( type(writeReturn) )
# Output :- <class 'int'>
 # becase the [ contentPresent.write() ] returns the length its Datatype will be Integer.




print( type(contentPresent) )

contentPresent.close()


# Let us check what datatype will the [open()] method returns 

print( type(contentPresent) )
print( contentPresent )



# Output :-

    # <class '_io.TextIOWrapper'>
    # <_io.TextIOWrapper name='writefile' mode='w' encoding='cp1252'>

# [ open() ] method will return ( _io.TextIOWrapper ) class which is the class which is ment to handle File Operations in python



print("""



""")



# -----------------------------------------------




 # What happens when we do not pass any options 

file_2 = open("./writefile")
file_2return = file_2.read()
print( file_2return )

# file_2.write("New Datas written inside the file.")
 # Error :- [ io.UnsupportedOperation: not writable ]
  # if we do not pass any Options (2nd arguement ) for [open()] method, it will default to read ("r") 
   # if no 2nd arguement which means by default it is a read operation ("r"), we can only read with the open() instance object but we cannot able to perform any Write operations 
    # if you want to perform [write] operations we have to explicitly pass ["w"] as a 2nd arguement for [ open( )] method

file_2.close()




# --------------




   # let us learn what happens when we get (raise) error before closing




# file_3 = open("./writefile_2.txt")

file_3 = open("./writefile_2.txt", "w" )
 # by default the file operation for [open()] method is "read", so when we try to pass file path as 1st arguement which is not present, in such situati on files will not be read because the file itself is not existing in that path.
 

# file_3 = open("./writefile_2.txt", "w" )
 # New File gets created when we use [ open() ] method by passing in the filename with  ("w") as a 2nd arguement, if not new file will not be created.


# When we use "raise" keyword in the Top level of Nested scope the lines which comes next to it will not be valid, which cannot be accessed so it is of no use writing this codes 
 # We will get this warning [ Code is unreachable ]

# file_3 = open("./writefile_2.txt", "w" )
# raise Exception("There is an Error.")
 # because we use raise keyword the code which creates the file will not written any thing inside it

# file_3.write("Some New Text inside writefile_2")
# Error :- FileNotFoundError: [Errno 2] No such file or directory: './writefile_2.txt'
 # These Exactly occurs when we try to use 2 [opn()] method next to next in a sequence then tring to write the files using [ write() ] method
  
  # In a Sequece we are allowed to use only 1 [open()] method, we are not allowed to use [open()] method immediately next to next,if we do so we will get this type of error.


file_3.close()



print("\n\n")



# ---------------------------------------------------------------------------------------------------------------------------------------------------------



# [ Approach 2 ]

# How to use Context Manager using [ Try...except...else...finally ] block

 # we can even use this appraoch in File Handling 

try:
    file_3 = open("./writefile_4", "w")
    file_3return = file_3.write("Hello Write File 4")
    print( file_3return )
    raise Exception("File Errors ")

except Exception as e:
    print(e)

else:
    # its because we have use [raise ] keyword inside the [ try ] block, if try block does not have any exceptions [ else ] block statement will get executed.
    print("No Exception has occured.")

finally:
    # Now Even though there is some Error inside the [ try ] block, while accessing the File, it will not stop the file from closing it 
     # because we have used [ close() ] method inside the [ finally ] block, even though there is some errors inside the [try] block our file will get closed successfully.
    file_3.close()



print("\n\n")



# ---------------------------------------------------------------------------------------------------------------------------------------------------------



# [ Approach 3 ]

 # the Updated version of [ try...except..else...finally ] block is to use [ with ] keyword statements


with open("./writefile_5", "w") as fileInstance:
    print(fileInstance)
     # Output :- <_io.TextIOWrapper name='./writefile_5' mode='w' encoding='cp1252'>

    fileInstance.close()


   # Let us create a [ try...except...else...finally ] block approach with the above code 

# [ with open("./writefile_5", "w") as fileInstance: ] this line is equivalent to the below line 

try :
    fileInstance = open("./writefile_5", "w")

    # [ print(fileInstance) ] - this line is equivalent to below line 
    print(fileInstance)
    # Output :- <_io.TextIOWrapper name='./writefile_5' mode='w' encoding='cp1252'>


#  [ fileInstance.close() ] - this line is equivalent to below line 
finally:
    fileInstance.close()

    

# -------------------------------------------
    
    # [ with ] keyword statement practice 

with open("./writefile", "r") as fileInstace_2:
    print( fileInstace_2 )

    fileInstace_2.close()

 # By using this syntax even though there is some error in the file it will not stop from closing the file, our file will get closed successfully 
    



print("\n\n")



# ---------------------------------------------------------------------------------------------------------------------------------------------------------



  # How to Create our Own Context managers using Classes 
  # Custom Context Managers 


class CustomContextManager:

    def __init__(self, fileName, optionsType):
        self.file = open(fileName, optionsType)

    
    def __enter__(self):
        print("Enteer")
        return self.file 
    

    def __exit__(self, type, value, traceback ):
        print("Exit")
        self.file.close()


# Now let us create a [ with ] statement using [ CustomContextManager ] class

with CustomContextManager( "./writefile", "w" ) as instanceCustomContextManager :
        print("Middle Value !")
        instanceCustomContextManager.write("This is a Custom Context Manager - MIDDLE")
       



# Output :-
            
    # Enteer
    # Middle Value !
    # Exit

# here we can values from [ __enter__() and __exit__()  ] that is [  Enteer and Exit ] got called and statements inside those method got Executed 
  # Even though we did not called [ __enter__() and __exit__()  ] explicitly, it got called implicitly when we invoke [ CustomContextManager() ] class
    # [ __enter__() ] - this is the First method which will get Executed 
    # [ __exit__() ] - this is the second method which will get Executed



print("\n\n")




# ------------------------
        
  # Understanding the Program flow



# Understanding how [ __enter__()  ] Method works inside the class

class Abc:
    variable_1 = "value 1"
    variable_2 = "Value 2"

    def method_1(self):
        print("Method 1")



class EnterClass:
    def __init__(self):
        # print("Enter init Method")
        self.abc = "abcs"
        self.abc = Abc()

    def __enter__(self):
        print("Hello Enter Method")
        return self.abc
    
    def enterClassMethod(self):
        print("Enter class method")
    
    enterClassVariable = "Enter Class Variable"



# Let us create an Insance Object 
    
instanceEnterClass = EnterClass().__enter__()


# to access the [Abc ] class which is inside [ __enter__() ] method we have manually call [ __enter__() ]

 # Here we are accessing the methods and variables which are inside the [ __enter__() ] method
instanceEnterClass.method_1()




 # Here we will be accessing methods and variables which are inside the [ EnterClass() class ]
# instanceEnterClass.enterClassMethod()
  # Error :- AttributeError: 'Abc' object has no attribute 'enterClassMethod' 
   # we cannot able to access methods which are present outside the [ __enter__() ] method scope, that is in the class scope 
   # by this we can learn that we are not allowed to access the methods and variables which are present inside the Class Scope
    # we can only access methods and variables which are present in the [ __enter__() ] methods scope.





 # What happens when we create a Class which has [ __enter__() and __exit__() ] methods but we do not use it inside Context Managers ( with ) statements ?

   # when we use [ __enter__() and __exit__() ] methods outside the Context Managers ( with ) statements, In this case [ __enter__() and __exit__() ] methods will not automatically invoked those statements which are inside these [ __enter__() and __exit__() ] methods  cannot be accessed
   # if you want to access the Statements which are present inside the [ __enter__() and __exit__() ] methods we have Explicitly call this dunder methods 
   # when we call it Explicitly all the statements inside [ [ __enter__() and __exit__() ] methods ] will be un-wrapped and appended in the Outer scope that is inside the class.



# --------------------------------------------




 # What happens when we create a Class which has [ __enter__() and __exit__() ] methods but we  use it inside Context Managers ( with ) statements ?


  # Example Code :-
 
  # with ClassName() as aliasName:
    #  print( aliasName )



class ClassUsedIn__Enter__method:

    enterVar_1 = "Value 1"

    def enterMethod_1(self):
        print("Enter Method 1")

    def enterMethod_2(self):
        print("Enter Method 2")



class MainClass__Enter__method:

    mainVar_1 = "Value 1"

    def mainVarMethod_1(self):
        print("Method 1")

    def __enter__(self):
        print("__enter__ Mthod")
        return ClassUsedIn__Enter__method()
        
    def __exit__(self, type, value, traceback):
        print('Exit Method')
    


# Now let us create a [ with ] statements with above classes
    

    
with MainClass__Enter__method() as instanceMainClass__Enter__method:
    print(instanceMainClass__Enter__method)



    # What happens when we do not use [ __exit__() ] method but we use [ __enter__() ] inside the Class ?

    
# class MainClass__Enter__method:

#     mainVar_1 = "Value 1"

#     def mainVarMethod_1(self):
#         print("Method 1")

#     def __enter__(self):
#         print("__enter__ Mthod")
#         return ClassUsedIn__Enter__method()
    


# Error :- TypeError: 'MainClass__Enter__method' object does not support the context manager protocol (missed __exit__ method)
    # Why do we get this Error ?
    # we get this Error because when we use Custom Classes in the Context Manager those CustomClasses must include 2 Mandatory Methods 
      # 1. [ __enter__() ] and [ __exit__() ] method, 
    
    


# --------------------------
    


# What happens when you do not use [ __enter__() ] where you only use [ __exit__() ] method ?
    
    

# **** JUST UNCOMMENT AND TRY TO USE :-
    

# class MainClass__Enter__method:

#     mainVar_1 = "Value 1"

#     def mainVarMethod_1(self):
#         print("Method 1")

#     # def __enter__(self):
#     #     print("__enter__ Mthod")
#     #     return ClassUsedIn__Enter__method()
        
#     def __exit__(self, type, value, traceback):
#         print('Exit Method')
    


    # TypeError: 'MainClass__Enter__method' object does not support the context manager protocol
     # This error occurs when we do not use [ __enter__() ] method but we used [ __exit__() ] method




    

# with MainClass__Enter__method() as instanceMainClass__Enter__method:
    
    # Let us try to access the [ methods and variables ] which are inside the [  ClassUsedIn__Enter__method ] ultimately this class has been invoked in the [ __enter__() ] method of [ MainClass__Enter__method ] class

    # instanceMainClass__Enter__method.enterMethod_1()


# 
















# --------------------------------------------




# # here let us Create a Custom Context manager class



# class CustomContextManager_2:

#     def __init__(self, fileName, readOrWrite ):
#         # inside the [ __init__() ] method we have opened the file
#         self.file = open(fileName, readOrWrite)        
        
#         # [file] - this variable has the Instance of [open()] method 
#          # by using [ file ] we have access all the methods which are associated with [open()], such as[ close(), read(), write]
        
#     def __enter__(self):
#         print("Enter")
#         # when we return some 
#         return self.file



print("\n\n\n")



# --------------------------------------------------------------------------
    


    
class ClassUsedIn__Enter__method:

    enterVar_1 = "Value Enter 1"

    def enterMethod_1(self):
        print("Enter Method 1")

    def enterMethod_2(self):
        print("Enter Method 2")



class MainClass__Enter__method:

    mainVar_1 = "Value Main 1"

    def mainVarMethod_1(self):
        print("Method 1")

    def __enter__(self):
        print("__enter__ Mthod")
        ownEnter_var = "Own enter method variables."
        return ClassUsedIn__Enter__method()
        
    def __exit__(self, type, value, traceback):
        print( type, value, traceback )
        # here [ type, value, tracebac ] are values which we can look for 
         # only when we get some error we can see this values
          # [ traceback ] this can be used to look for the Errors

        print('Exit Method')
    


# Now let us create a [ with ] statements with above classes
    

    
with MainClass__Enter__method() as instanceMainClass__Enter__method:
    print(instanceMainClass__Enter__method)

    # Now let us try to access [ ClassUsedIn__Enter__method  ] class which has been used inside [  __enter__ ] method of [ MainClass__Enter__method ] class ?

    print( instanceMainClass__Enter__method.enterVar_1 )
    instanceMainClass__Enter__method.enterMethod_1()
    instanceMainClass__Enter__method.enterMethod_2()


    # Let us try to access the variables and methods which are defined inside the [ __enter__() ] method ?
       # Error :- AttributeError: 'ClassUsedIn__Enter__method' object has no attribute 'ownEnter_var'
     # we are not allowed to access, Those [ methods and variables ] which are defined inside the [ __enter__() ] method
    # the only [ methods and variables ] we are allowed to access is those object which are present inside [ __enter__() ] methods (return) statements.

    # print( instanceMainClass__Enter__method.ownEnter_var )




    # Now let us try to access [ MainClass__Enter__method  ] class 

    # print( instanceMainClass__Enter__method.mainVar_1 )
    # Error :- [ AttributeError: 'ClassUsedIn__Enter__method' object has no attribute 'mainVar_1' ]
      # When we try to access the [ methods, attributes and variables ] from [ MainClass__Enter__method ] that is the class for which we have used [ with ] statements we are getting error 
        # we are not allowed to access any [ methods, attributes and variables ] which are present inside the class, where the same class will be used inside the [ with ] statement Context managers
    
    # instanceMainClass__Enter__method.mainVarMethod_1()


   # Suppose [ __enter__() ] method does not return or do not have ( return ) statement ?
      # Even in this Situation we cannot access the [ Methods, variables and Attributes ] which are inside the Class which we have used in Context Manager [ with ] statement





# Output :- 
    
        
    # __enter__ Mthod
    # <__main__.ClassUsedIn__Enter__method object at 0x000001EB188FE270>
    # Value Enter 1
    # Enter Method 1
    # Enter Method 2
    # None None None
    # Exit Method










# ----------------------------------------
    


    # [ ***  ] Learnings :-
     # In Context Manager by using [ Custom Classes ] we are allowed to [ Methods, properties and Attributes ] which are present inside the [ __enter__() ] methods "return" statements 
      # Those [ methods, variables and attributes ] which are present inside the the Class ( Custom_Context_Class ) which we are using for context manager [with] statement, we are not allowed to access. Those are attirbutes are not accessiable by the [ with ] statements instanceVariables
      # Those [ methods and Variables ] which we define inside the [ __enter__() ] methods ---> which is present inside ( Custom_Context_Class ) which we are using for context manager [with] statement, Even those [methods and variables] cannot be accessed inside the scope of [ with ] statements.
    


print("\n\n\n")
      


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    

from contextlib import contextmanager
# How to Create a Context Managers using [ Generator and Decorator ] syntax 
     # Here we will import [ from contextlib import contextmanager ], here [ contextmanager ] is a decorator 




# here we will create a Function for which we will be using [ @contextmanager ] decorator 

@contextmanager
def fileGenerator(filename, method):
    print("Enter...")

    # 1st open the file 
    file = open(filename, method)
    # next we use yield keyword and call [file],
     # yield keyword will perform [ read or write ] operations and removes those datas (which came from file) from the Memory RAM
    yield file 

    # next let us call [ close() ]method 
     # once file operation is done and cleared from the memeory,let us close the file 
    file.close()
    print("End......")



# Now let us create a Context Manager using [ with ] statement 

with fileGenerator("./generator_File.txt", "w") as instanceFileGenerator:
    print("Middle Operations.....")
    instanceFileGenerator.write("This is a Generator file")
    




# Output :-
        
    # Enter...
    # Middle Operations.....
    # End......


# Here we got Output without any error Which means we have successfully used [ Generator and Decorator ] syntax to create Context managers using [ with ] keyword statement















