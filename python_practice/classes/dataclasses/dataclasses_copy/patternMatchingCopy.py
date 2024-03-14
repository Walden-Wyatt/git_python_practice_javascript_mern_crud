

# Pattern Matching 

# Pattern matching is a Conditional Statements which can be used to check the variables values based on some conditions we can render the values

 # Pattern matching is similar to the JavaScript Switch statement



# --------------------


# Syntax :-

# match variable_name_to_Match:
#     case Variable_value_to_Match:
        # code to be executed when the variable_name_to_Match is equal to the variable_value_to_Match
        # break





# -------------------





day = "Monday"

# Error :- 
 # Match statement must include at least one case statement
 # This error says that when we create a Match statement we have to atleast use 1 [case] statement which is used to render the values 
match day:
    case "Monday":
        print("It's Monday")
    case "Tuesday":
        print("It's Tuesday")
    case "Wednesday":
        print("It's Wednesday")
    case "Thrusday":
        print("It's Thrusday")
    case "Friday":
        print("It's Friday")
    case "Saturday":
        print("It's Saturday")
    case "Sunday":
        print("It's Sunday")



print("""





""")




# --------------------------------------------------------
        


# Pattern Matching using Wildcard 
        

fruits = "apple"


fruits = "something"

match fruits:

    case "apple":
        print("It's apple")
    case "banana":
        print("It's Banana")
    case "papaya":
        print("It's Papaya")
    case "orange":
        print("It's Orange")
    case "kiwi":
        print("It's Kiwi")

    case _:
        print("No value have matched.")


# Output :-
    # No value have matched.
        
# Here the value for the [ fruits ] variable does not match with any of the Conditions which are present inside [ match ] statement that is the reason we are get the wildcard statements value 

 # [case _: ] - Wildcard expression :-
   # here [ _ ] means it's a Wildcard, If any of the Above statements does not match in such situation whatever value which we have provided inside [ case _: ] will get printed 
   # [ _ ] is a wildcard match, if any of the above cases does not match with the above [ case ] statements in such situation, the indended block of statements which is present inside [ case _: ] will get executed   



# -----------------------------
        

        # what happens when we use [ case _: ] statements in the middle of the case statements ?


fruits = "something"

match fruits:

    case "apple":
        print("It's apple")
    case "banana":
        print("It's Banana")
    case "papaya":
        print("It's Papaya")

    # Error :-
     # Irrefutable pattern is allowed only for the last case statementPylance
      # (function) _: Any
        
    # This Error occurs when we try to use [ WildcardPattern - case _: ] statements in the middle of the case statements which we are not allowed to do
     # [ WildcardPattern - case _: ] statements has to be at the End of the list of Case Statements 
        
      # case _:
      #     print("No value have matched.")


    case "orange":
        print("It's Orange")
    case "kiwi":
        print("It's Kiwi")

        # case _:
        #     print("No value have matched.")

        # Error :- 
            # Irrefutable pattern is allowed only for the last case statementPylance
            # (function) _: Any
        # We getting the same Error as before


    case _:
        print("No value have matched.")

# Learnings :-
    # 1. There should be only one [ WildcardPattern = case _: ] pattern in the Match statements 
    # 2. [ WildcardPattern = case _: ] pattern has to be provided at the End of the case statements that is as a Last Case Statement.





# --------------------------------------------------------------------------------------------
        


# Match using [ break ] keyword ?
        

bikes = "bullet"

match bikes:
    case "bullet":
        print("It's a bullet")
        # break
      # Error:- [ "break" can be used only within a loop ]
       # we are not allowed to use [ break ] inside [ match pattern ]

    case "pulsar":
        print("It's a Pulsar")
    case "yamaha":
        print("It's a YAMHA")
    case "ev":
        print("It's an EV")


























