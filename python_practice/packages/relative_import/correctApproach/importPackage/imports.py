


# Let us Do Relative Import


  # Steps :-

# 1 - Import [ sys ] module
# 2 - set the Relative path [ sys.path.append( "../Relative/path" ) ]
# 3. use specific Item Syntax to Import the Module Files [ from Package_Name import Module_File ]
# 4. Finally Make use the code which is inside the [ Module_File ] which you have imported.


# Points to Remember :-
 
 # 1. You can Load Folders and Files which is inside the folder path which we have specified inside [ sys.path.append() ] method
  # a. we are not allowed to load Folder which we specified Exactly in the [ sys.path.append() ] method
  # b. we are not allowed to load Folder Whic is One Level Up than what we specified in the [ sys.path.append() ] method.


# # here we have imported the [sys] module
# import sys


# # let us use Relative path to append the Folder path
# sys.path.append(".../")


# from relative_import import ri

# # from packages import abc



# print( ri )

# # print( abc )


# -----------------------------------------------------------------------------------------------------------------------------------------------------------



import sys

sys.path.append( "../" ) # correctApproach
sys.path.append( "../../" ) # relative_import
sys.path.append( "../../../" ) # packages
# sys.path.append( "../../../../" ) # Python_Practice


# Error :- [ ModuleNotFoundError: No module named 'packages' ]
 # we encounter this error because we used wrong pattern to specify the Path, we are not suppose to use this Pattern [ ..../ ], we have to use only [ ../ and ./]
  # [ ./ ] - this will point to Current Folder/Directory/Package
  # [ ../ ] - this will point to Current Folders Parent Director/Folder/Package ( folder 1 level upper ).

# sys.path.append( "...../" ) 

import correctFile

# from correctApproach import correctFile

import ri

print( correctFile )

correctFile.correctFunction()

print(correctFile.correctVariable)  

print( ri )


# --------------------- [ packages ] folder

# import package

from relative_import import ri

print( ri, "This is ri 2" )

print( ri.ri(), "This is ri 2" )



# ------------------------------ [ PYTHON_PRACITCE ]


from packages import package

print( package )

print( package.package_variable )












































