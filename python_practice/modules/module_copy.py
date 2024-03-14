

# Module 

# Module is a File which has staements and Declarations



# Concepts to Learn

  # 1. Meaning of Module



  # 2. Types of Imports 

     # a. Regular or Basic Import 
       # [ import FileName.py ]

     # b. Import with Alias  
      # [ import filename as Alias_Name ]

     # c. Import Specific Items
      # [ from fileName import specific_Code ]

     # d. Wild Card Import
       # [ from fileName import * ]

     # e. Conditional Import 
       # if condition:
         # import fileName

     # f. Dynamic Import 
       # imoprt importlib
       # dynamic_Variable = importlib.import_module("filename")



  # 3. Module Content and Namespace 
   # Module Content - module content means the contents which is present inside the File or module.
   # contents such as Functions, Variables, Classes, Objects, etc

   # Namespace 
    # Namespace is nothing but the file which names for all Declarations and statements, such as [ Functions, variables, Classes, Objects, etc ]
    # Namespace in simple term means Names of Functions, Classes, Objects, Variables, etc.



  # 4. Accessing Modules 
   # There are two ways in which we can access the Modules 
    # 1. Accessing Using Dot Notations 
    # 2. Accessing Using Namespace - same as  using Dot Notations



  # 5. Standard Library Modules 
    # Set of Modules or Files which has code related to Specific Classes
    # Ex :- Math, os, sys, random, etc
    # All those Modules which are already present inside the Python Folders as Files or Modules, This files or Modules will have classes which will have static as well as Instance methods which are related to that specific modules



  # 6. Creating Your Own Modules 
    # When you create file with [ .py ] extentions and write some relevant codes then it becomes a Modules 
    # Module is another name for Files, in python specifically Python Files 



  # 7. Script Modules and "__main__()"
     # Script modules or script files are those files which has this method called [ __main__() ] function 
     # when we file has this condtion [ if "__main__" == "__name__" ] which means this is a Python Script Module Files
     # the code which we write inside this condition will get executed only when we try to execute the Current File, 
     # if we import this to another files we cannot abel to access the codes which has been written inside the [ if "__main__" == "__name__" ] condition



# -----------------------------



  # 8.  Packages 
    # Packages are nothing but Folders, when we create a Module (File) and store those files inside a Folder then the Folder will become a Package
    # Another Name for Folder is "Package" or "Directory"
    # Package will have Set of Files or specifically Python Files inside it

  # 9. Importing Package or Folders or Dicrectory from Parent to Child Folders
     # [ from Package_Folder_Directory import Module_File ]
     # This will import the Module or File inside our Current file or Child Module(file), from Parent Module (file) by this inside the child module we can make use of codes which is present inside [ Parent Modules ].

  # 10. sys.path Modification ( Advanced )
     # [ sys.path ] can be used to modify the path of the modules, if the module is not present inside the Specific path we can use other path by using [ sys.path.appen() ] method
 

  # 11. Module Documentation - 'docstrings' :
     # Use docstrings (triple-quoted strings) to document modules, functions, and classes.

  # 12. Built-in dir() Function:
    # [ dir() ] function can be used check what the contents which is present inside the Class or Object
    # contents means codes such as [ Functions, Objects, variables, classes, etc.]
    # when we use dot notation [ . ] to access the Contents inside a File we get to see either Property or Methods which is nothing but [ Variables, Functions, Objects, Classes ] which are present inside the Class. 


  # 13. __init__.py and Initialization:
    # [ __init__.py ] file can be used to initialise the Package ( Directory or Folder ).


  # 14. 

























