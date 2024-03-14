


# Here we have Import variables 

# Here we have Loaded The [ export_file.py ] files code 

# [ __pycache__ ]
 # when you you use import keyword and imported any modue inside any of the file, then when you try to run the program, this folder [ __pycache__ ] will get installed into the Current Folder.

import export_file

import pandas




 # How will the above code behind the scene looks like 
 # When we import some module using [import] keyword all the codes which are present inside the Module (file) will get loaded inside this current file
  # The location of loading this files are important, code will get loaded in the specific Line where you use [ Import ] keyword

   # when we Import Modules (Files) inside the any of the files (current file), Its like we are writing the Entire code once again inside the [ Import File ] which is there inside [ Export File ] 
    # The code which we imported will be wrapped inside the Class, The name of the Class will be the [ File Name ]. so when we want to access any of the Methods, properties, Variables, Class, objects, etc we have to use [ Dot Notation (.) ]


       # When to Use [ Dot Notation ] ?
        # when you want to access Objects with [ Named Attributes, Clases, Modules, Object Methods, etc ]


       # When to use [ Bracket Notation ] ?
        # when we want to access Methoda and Attributes(properties) of Iterable Objects or Sequeces such as [ Lists, Tuples, Sets, Strings, etc ]
        # When a Class does not Support [ Dot Notation ] to access the Values, ex: Dictionary, etc, to access the Methods and Properties of Dictionary we have to use Bracket Notation only.




        # CODE WHEN GETS LOADED INSIDE THE CURRENT FILE OR IMPORT FILE

        # --------------------------------------------------------------------

           # class export_file:

                # export_variable = "Export Variable"

                # def export_Function(param1):
                #     print("Export Function")

                # class Export_class:
                #     def __init__(self) -> None:
                #         pass
                #     def method():
                #         print("Class Method")
                #     porperty = "Class Property"

        # --------------------------------------------------------------------


 




# Below we accessed all the Code ( statements and declarations ) which are inside the [ export_file.py ]

print( export_file )


print( export_file.export_variable )


print( export_file.export_Function( "Arguement 1" ) )


print( export_file.Export_class )



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Practise 2 



# step 1 - Write the code inside the [ export file ]

# step 2 - create a [ import file ]

# step 3 - import the [export file ] using [ import fileName ]

# step 4 - access the Codes ( Methods and Attributes ) which is inside the [ export file ] by using [ dot notation ].

# step 5 - 

# step 6 - 


import export_file

print( export_file )

print( export_file.export_Function("abc") )















































