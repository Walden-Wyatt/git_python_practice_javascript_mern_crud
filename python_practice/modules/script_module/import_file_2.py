




import script_module

# Just when you Load the Import File all the Top Level Print Function statements will get executed 


# Output :-

    # Hello World, from Script Module
    # __main__
    # __main__
    # hello

# print(script_module )

# ----------------------------

# Here let us try to access the [ Practise 2 ] Script module codes 
 # this are the declarations which are present inside it [ variable, mainFunction ]


# Error :- AttributeError: module 'script_module' has no attribute 'variable'
# print( script_module.variable )


# Error :- AttributeError: module 'script_module' has no attribute 'mainFunction'
# print( script_module.mainFunction() )

# we got error when we try to access the Code which is inside the [ if ] condition which checks for ["__main__"] value.
 # From here we got to know that we cannot able to access the [ if __name__ == "__main__" ] conditions code from inside the [ Imported files ].










