



# Script Module 


# Here we will be Learning about Script Module



if __name__ == "__main__":
    print("Hello World, from Script Module")


# Output :-
    
# PS C:\Users\user\Desktop\python_practice\modules\script_module> py import_file.py
    # here when we run [ import_file.py ] we did not got any output from [ script_module.py ] file, even though we had imported [ scipt_module.py ] file inside [ import_file.py ] file
     # this is because we used [ if __name__ == "__main__" ] statement which will restrict importing files from executing this codes 
    

# PS C:\Users\user\Desktop\python_practice\modules\script_module> py script_module.py
# Hello World, from Script Module
    
    # when we run [ py script_module.py ] file we got the output [ Hello World, from Script Module ]
    

# PS C:\Users\user\Desktop\python_practice\modules\script_module> 





print( __name__ )

print( "__main__" )



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    print("hello")


# Syntax Breakdown :-
    
  # if __name__ == "__main__":
        
    # 1. [ if ]
      # "if" is the keyword which we must use as a part of conditional statements
        
    # 2. [ __name__ ]
      # [__name__ ] will have to name of the file, how this works
       # when you execute the Original File ( the which in which we have "__name__" variable ) in this case - the value for [ __name__ ] will be [ __main__ ]
       # when you execute the Import file ( that is the file which has imported the Original file which has "__name__" variable  ) in this case - The value of the [ __name__ ] will be [ FileName ] which we executed in the Terminal.
        # that is reason we check for String ["__main__"]
        # [ __name__ ] will have String value  either [ "__main__" or "FileName" ]

    # 3. [ == ]
      #  [==] This is a Equal to Operator which we can use to check for the value
        
    # 4. [ "__main__" ]
        # "__main__" is the String which is used to check weather the [__name__ ] variable has the same value, Which is used to decide which file has accessed this variable
        


# Important Points :-
    
    # 1. If you want Certain codes to be Executed Only the Main Or Original file ( i.e, the file which has to Original code ) in such situation we can use [ if __name__ == "__main__" ]
    # 2. if you want the code to be accessed by all the Files which imports the Original File in such cases we dont need to write the code inside [ if __name__ == "__main__" ]



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------



# [ Practise 2 ]


if __name__ == "__main__":

    variable = "Variable Value"

    def mainFunction():
        print("This is Main Function")

    print("This can Only be accessed by [__main__] file")
























