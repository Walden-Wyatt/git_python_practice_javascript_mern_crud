


# Conditional Imports :-

 # Here we will be Learning about Conditional Imports 

 # Conditional Imports are nothing but Importing a Module Files based on certain Conditions.


 # Here below we checked for condition if the condition is True or Truthy then the statements which is inside the [ if... ] block will get executed, incase it is false [ if...  ] block statement will not be executed.

if True:
    import conditionalExport

 # Syntax Breakdown :

    # if condition 

     # [ if ]
      # "if" has to be used as a Part of a conditional Syntax
    
     # [ condition ]
      # here we have to provide appropriate conditions, so that when condition is fullfilled the statements which is inside the block gets executed
     
    # import Module_FileName 

      # [ import ]
       # "import" is the keyword which we have to use as a Part of a Syntax when import module files inside the current file

      # [ Module_FileName ]
       # "Module_FileName" is the Name of the Module file which we want to import inside the Current file
    


    # **** Points to Remember :-
     
      # 1. When we import module inside the [ if.... ] block, The Items which is are present in the  Module files can be accessed inside the [ if... ] block within Local Scope, as well as it can also be accessed outside the [if...] block as from the Global scope 
    
      # 2. we can even use other Import syntax such as [ Import with Alias , Import Specific Items, Wild Card Import, Conditional Import, Dynamic Import , etc. ]


      # ** Here we accessed the Module File from inide the [ if.... ] block that is inside the Local Scope
    print( conditionalExport, " " , "This is Inside the If... block" )



# let us try to access [ conditional_imports ] class
    
 # below we have accessed the Items of [ conditionalExport ] from the Global Scope.
 
print( conditionalExport )

print( "Hello" )

print( conditionalExport.ConditionalClass )

print( conditionalExport.conditionalFunction() )

print( conditionalExport.variables_attributes ) 




# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# [ Practise 2 ]


if False:
    # WARNING :-
    # By Default none of the Code is Read because all the code is not reachable,
     # this warning will occur only in 1 situation that is when we directly use [ False ] keyword as condition for [ if... ] block

    import false_conditionalExport

    # let us access within the Local Scope

    print( false_conditionalExport )




# Here let us try to access from the Global Scope
    

# [ Code ] :-
# print( false_conditionalExport )

# Here we Encountered Error because the [ false_conditionalExport ] module file is not import, because we the [ if ] codition is false





# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# [ Practise 3 ]




userData = input( "Should i to import or not, Press [y] for Yes, [n] for No" )


# Here we have conditonally imported the Module files

if userData == "y":
    import conditionalExport3

    print( conditionalExport3.variables_attributes )


print( conditionalExport3.conditionalFunction() )

# when we press [y] we get the below Output ?

    # Conditional Export Attributes
    # Conditional Function



# --------



# when we press [ n ] we get the below output ?

    # File "C:\Users\user\Desktop\python_practice\modules\conditional_imports\conditionalImport.py", line 118, in <module>
    #     print( conditionalExport3.conditionalFunction() )
    #            ^^^^^^^^^^^^^^^^^^
    # NameError: name 'conditionalExport3' is not defined. Did you mean: 'conditionalExport'?





























