

# Import File

# Here we will be having Import code.


# sys.path.append("RELATIVE_PATH")

# What Happens behind the Scene ?

 # when we set the path using [ sys.path.append() ] method, it will allow the Current File to access the Contents which is inside the Parent Folder ( that the path which we set ).
 # [ sys.path.append() ] method will not load the directory but allows access to the Files and Folders which are inside the Specified Folder path
 
 # when we try to access the Folders (packages) or Files( modules ) by loading it using [ import file_name ] or [ from Folder_package import File_Module ] syntax
  # when we do this the contents which is inside the Folder or Package will get loaded inside Class ( where class name will be file name ) or On the Top Level of the File without wrapping inside the class. 





import sys

# set Dynamic Path so that we can access all the Folders and Files which is present in that specific Location

sys.path.append( "../" ) # [ __CorrectApproach ] 
 # this path will point to the [ __CorrectApproach ] folder, when we spicify this Path now we can Load all the Contents which is inside [ ___CorrectApproach ] folder 
  # we are not allowed to use [ __CorrectApproach ] to import some Folders and Files, we can only access Folders and Files which are inside it.

from sysExport import exportFile

print( exportFile )

print( exportFile.exportVariable )



# ----------------------


# here we the sys path points 2 level up from [sysImport] folder
sys.path.append("../../") # packages
# By using the Above path we can Access the Contents which is inside the [ packages ] folder
# we are not allowed to use [ packages ] folder directly, but we can use [ __CorrectApproach, sysImport and sysExport folders as well as files ( Modules ) which is nested inside it ]

from __CorrectApproach import correctApproachFile

print( correctApproachFile )

print( correctApproachFile.correctApproach_Variable )







# ----------------------





# 3 Level up

sys.path.append( "../../../" ) # [ PYTHON_PRATICE ] folder
 # this [ sys path ] will point the [ PYTHON_PRACTICE ] folder, now we can assess Files and Nested Folders_files which is inside the [ PYTHON_PRACTICE ] folder
  # we are not allowed to use [ PYTHON_PRACTICE ] folder while importing content using this path [ sys.path.append( "../../../" ) ]

# here we imported [ package ] file which is inside the [ packages ] folder.
from packages import package

print( package )

# here we accessed [ package_variable ] which is inside [ package ] file
print( package.package_variable )



# ------------------------------


# we can use This syntax as an Alternative for Relative Path






#  Output :-

    # py importFile.py
    # <module 'sysExport.exportFile' from 'C:\\Users\\user\\Desktop\\python_practice\\packages\\__CorrectApproach\\sysImport\\..\\sysExport\\exportFile.py'>
    # Export Variable Value
    # <module '__CorrectApproach.correctApproachFile' from 'C:\\Users\\user\\Desktop\\python_practice\\packages\\__CorrectApproach\\sysImport\\../..\\__CorrectApproach\\correctApproachFile.py'>
    # Correct Approach Variables
    # <module 'packages.package' from 'C:\\Users\\user\\Desktop\\python_practice\\packages\\__CorrectApproach\\sysImport\\../../..\\packages\\package.py'>
    # This is a Package Variable














