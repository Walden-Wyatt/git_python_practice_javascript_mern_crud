


# Wildcard Import

 # If we want all the Items from the Export file to be imported inside the Current file we can use [ Wildcard Import ]
 
 # This has to be Avoided 

# Problems which we might Encounter :
  # 1. We cannot able to differentiate between The Current File code as well as the Code which we have Imported from Other Export Files 
  # 2. It becomes difficult to keep track of the Current Files code and Imported files code.



# Import File all the codes using [ from ] pattern


from exportFile import *

# Syntax Breakdown :-

 # [ from ]
   # "from" is the keyword which we must use as a part of a syntax

 # [ exportFile ]
   # here we have to provide the Name of the Module file from where we are importing

 # [ import ]
   # "import" is also a Keyword which we must use as a Part of Syntax

 # [ * ] Astrix
   # '*' means we are importing all the Items from the Module files, Items includes [ Functions, Classes, Attributes, objects, etc ]
   # if we want to import all the Items from the Module File we have to use [ * ]






# Now all the Code which is present inside [ exportFile.py ] has been imported here, we can access all the Items which is inside  [ exportFile.py ] from current file
# *** Do not use the [ Module or File ] name while accessing the Items which is present inside the [ exportFile.py ]


# what happens when we access the items using [ exportFile ] which is the module or file name ?


# Code :- print( exportFile ) 


# Error :-

    #  File "C:\Users\user\Desktop\python_practice\modules\wildcard_import\importFile.py", line 14, in <module>
    #     print( exportFile )
    #            ^^^^^^^^^^
    # NameError: name 'exportFile' is not defined

# We encounter this error because we did not loaded Items inside the file as Class 
 # we loaded the content directly inside the File


# print( exportFile.attribute )





 # How will this type of Import look like behind the Scene ?


# -----------------------------------------------------------------

        # CODE BEHIND THE SCENE


        # # Export File

        # attribute = "Attribute Value"
        # def functionDef():
        #     print("Function Defination")
        # class ExportClass:
        #     def classFunction():
        #         print("Class Function")
        #     classAttribute = "Class Attribute"
        # objectExport = { 
        #     "key" : "Value" 
        #     }



# -----------------------------------------------------------------




# we have to access the Items directly using instead of accessing it from a Class 


print( attribute )

functionDef()

print( ExportClass )

print( objectExport )


# Output :-

    # Attribute Value
    # Function Defination
    # <class 'exportFile.ExportClass'>
    # {'key': 'Value'}



print("""




""")



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------



# [ Practise 2 ]


# Here we imported all the items which is present inside [ exportFile ] by using [ from fileName import * ] sytnax
from exportFile import *

print( attribute )

functionDef()

print( ExportClass )

print( objectExport )



print("""




""")



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------



# [ Practise 3 ]


from exportFile import *

print( attribute )

functionDef()

print( ExportClass )

print( objectExport )













































