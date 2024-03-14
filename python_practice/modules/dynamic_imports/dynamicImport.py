

# Dynamic Imports 


# Here we will be Learning about Dynamic Imports in Python

# Dynamic Import happens during the Run time that is when we try to run the specific file our python Interpreter will go to the Specific file location fetches the Specific Statements or Declarations which we have used inside the Current File then displays the Result inside the Terminal

# Other Imports -
 # what happens in other imports is that when we try to import, The Import happens in the Compile Time that is when we load the file inside our current file those, The Export files code will be written inside the Current File as soon as we load so during runtime it need not have to fetch the codes by going to Specific Location.
 # In other files codes will be written immediately once we laod the Module File.


# Benefits of Using Dynamic Imports :-

 # 1. Our application code will be faster
 # 2. our program Folders and File size will not be Large
 # 3. Our file will not Load unnecessary codes which is not used into our File which will also occupy storeage which is not used.
 # 4. overall our application will be faster and Optimised 
 # 5. Try to use Dynamic  Imports as much as Possible
 # 6. by using dynamic Import we can import multiple module files inside our current File, while accessing the code we can accesss those codes or statements or declarations which are necessary for the file 
    # By importing multiple files into a sigle file there, the file size will not be too Large the memory will be consumed only for the code which we have used inside the file, because we have used Dynamic Imports.



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Steps 

 # Step 1 :- import [ importlib ] module 

 # Step 2 :- use [ importlib.import_module("FileName")] 
   # use this method to import the Module file from the python built-in libraries

 # Step 3 :- assign the  [ importlib.import_module("FileName")] to a Variable ( ex: dynamicImport_variable )

 # Step 4 :- by using the variable name that is (  dynamicImport_variable ) try to access the Codes which is present inside the file such as [ Attributes, Functions, Classes, Objects, etc. ]




import importlib

module = importlib.import_module("dynamicExport")

print( module )

# Here in the below syntax only [ variables_attributes ] will get loaded where as other codes will not get loaded into our Current file.
print( module.variables_attributes )


# when we  try to use [ Dot Notaion ] the intillisence is not displaying the [ Statements and Declarations ] which are present inside the [ dynamicExport ] module file.
 # this happens because we have used [ Dynamic Imports ] in our Module file which will Fetch the Code Datas when we run the File not during Compile time ( while write and load the code)
# print( module. )





# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# [ Practise 2 ]


import importlib

dynamicImport_variable = importlib.import_module( "dynamicExport" )



# Below we have accessed Dynamic Import Module files

print( dynamicImport_variable )

print( dynamicImport_variable.variables_attributes )

print( dynamicImport_variable.DynamicFunction() )





# ------------------------------------------------------------------------------------------------------------------------------------------------------



# [ Practise 3 ]


import importlib


# Error :- 
# ModuleNotFoundError: No module named 'dynamicExport.py'; 'dynamicExport' is not a package 
  # we got this Error because we used wrong Module or file name inside the [ import_module() ] function
# [ code ] - dynamicCode = importlib.import_module( "dynamicExport.py" )

dynamicCode = importlib.import_module( "dynamicExport" )

# Error :- AttributeError: module 'dynamicExport' has no attribute 'variable_attribute'. Did you mean: 'variables_attributes'? 
 # we get this error when we use wrong attribute or Property name to access any Property or methods or attributes from a Class or object
# [ code ] -  print( dynamicCode.variable_attribute )

print( dynamicCode.variables_attributes )


# Output :-

        # PS C:\Users\user\Desktop\python_practice\modules\dynamic_imports> py dynamicImport.py
        # <module 'dynamicExport' from 'C:\\Users\\user\\Desktop\\python_practice\\modules\\dynamic_imports\\dynamicExport.py'>
        # Dynamic Export Attributes
        # <module 'dynamicExport' from 'C:\\Users\\user\\Desktop\\python_practice\\modules\\dynamic_imports\\dynamicExport.py'>
        # Dynamic Export Attributes
        # Dynamic Function
        # Dynamic Export Attributes
        # PS C:\Users\user\Desktop\python_practice\modules\dynamic_imports> 

































