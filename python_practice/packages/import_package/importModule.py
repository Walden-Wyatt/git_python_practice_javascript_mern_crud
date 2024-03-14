


# Import File


# import export_package.export
# print( export_package.export.export_variable )



# -------------------------------


# [ sys Syntax ].

import sys  # Step 1 - [ Import sys module ]
sys.path.append( "../" ) # Step 2 - [ Append the sys path, provide appropriate path so that Modules can be imported from that specific path. ]
# The above Provided path will point to [ packages ]

# from ..export_package import exportModule
# Error :-
 # when we use above import statement we get the below error.
 # ImportError: attempted relative import with no known parent package
# print( exportModule )



# The below syntax is not working in Python, please do not use this syntax
# from ..docstrings import docstrings
# print( docstrings )


# ----------------------------------------------------------------------------------------------------------------------------------------------------------



from import_package import importModule

print( importModule )































