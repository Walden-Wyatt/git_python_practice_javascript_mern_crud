


 # Here we will import Attribute from a [ exportFile.py ]


from exportFile import attribute_1

 # Syntax Break down

  # [ from ] 
   # from is a keyword which has to be used as a part of a syntax

  # [ File_Name ]
    # File_Name is the place where we are suppose to provide the Name of the Module File from where we are importing the code

  # [ import ]
    # [ import ] is the keyword which we must use as a part of a Syntax, this is used to Import a Specific [ Namespace ]

  # [ NameSpace ]
    # NameSpace is nothing but the code which we want to import into our current File, The Namespace code can be a [ Function, Class, Objects, Attributes, etc ]



# How the Above Import Statement might Look behind the Scene ?

#  [ Import Statement ] :- from exportFile import attribute_1

# CODE BEHIND THE SCENE 

# -----------------------------------

 # attribute_1 = "Attibute Value"

# -----------------------------------

# here if you see only namespace [ attribute_1 ] have been imported other declarations code which is below is not imported 
    

    # CODE NOT IMPORTED INSIDE THE CURRENT FILE

    # ----------------------------------------------

        # def exportFunction():
        #     print(" Export Function ")
        # class ExportClass:
        #     def classmethod():
        #         print("Class Method")

    # ----------------------------------------------

print( attribute_1 )


# Here let us try to access [  exportFunction and ExportClass ] from [exportFile.py] file 

# Code :-
# print( exportFile.exportFunction() )

# Error :-

    # print( exportFile.exportFunction() )
    #            ^^^^^^^^^^
    # NameError: name 'exportFile' is not defined

 # We get this error when we try to access the [ exportFile ] modules declaration using module name

 # when we use [ Import Specific Items: ] pattern we cannot able to access the Declarations using [ Module or File ] name which we used to import into current files
 # we are allowed to access only the specific Items ( declarations ) which we have imported inside our Current file not other declarations which we have not imported.


# Code :-
# print( exportFile.ExportClass )





# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

































