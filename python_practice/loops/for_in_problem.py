

# For in Problem



# Problem 1: Print Numbers

# Write a Python program that prints the numbers from 1 to 10 using a for loop.


for x in range(1,11):
    print(x)




print("""



""")


# Problem 2: Sum of Numbers

# Write a program that calculates and prints the sum of all numbers from 1 to 5

sum_of_numbers = 0

for x in range(1,6):
    sum_of_numbers += x

print( sum_of_numbers )




print("""



""")
    


# Problem 3: Print Squares

# Write a program that prints the squares of the numbers from 1 to 5.



for x in range(1, 6):
    x = x * x 
    print( x )


# Problem 4: List Elements

# Given a list of colors (["red", "green", "blue", "yellow"]), write a program that prints each color using a for loop.


color_list = ["red", "green", "blue", "yellow"]

for x in color_list:
    print( x )



# Problem 5: String Characters

# Given a string ("Python"), write a program that prints each character of the string on a new line using a for loop.


word = "Python"

for x in word:
    print( x )



# Problem 6: Multiplication Table

# Write a program that takes a number as input and prints its multiplication table up to 10.


def multiplication():

 number = input('Enter a Number ? \n')


 if number.isdigit(): 
    
    number_cast = int(number)
    for x in range(1, 11):
     print( f"{number_cast} * {x} = {number_cast * x }")
 else:
    print("Please enter a valid number")



# Problem 7: Counting Even Numbers

# Write a program that counts and prints the number of even numbers from 1 to 10.



for x in range(1,11):
    evenNumber = x % 2
    if evenNumber == 0:
        print(x, "-- This are Even Numbers")



# Problem 8: Factorial

# Write a program to calculate and print the factorial of a given number.


# 4 = 4 * 3 * 2 * 1
        
def factorial():
    userNumber = input("Enter a Number :\n")
    userNumber_cast = int(userNumber)
    factorialValue = 1

    # in factorial there will not be 0
    for x in range(1,userNumber_cast+1):
     factorialValue *= x # factorialValue = factorialValue * x [ 1 * 1, 1 * 2 , 2 * 3, 6 * 4, 24 * 5 ]
    
    print( factorialValue )

print("""




""")


# Problem 9: Reverse a List

# Given a list of numbers ([1, 2, 3, 4, 5]), write a program to print the list in reverse order.



r_list = [1, 2, 3, 4, 5, 8, "helel", "wow","zero"]

reverse_list = []

# print( r_list.pop() )
# print( r_list.pop() )
# print( r_list.pop() )
# print( r_list.pop() )
# print( r_list.pop() )

# for i in range(len(r_list) -1, -1, -1):
#     reverse_list.append(r_list[i])

for i in r_list: # [1, 2, 3, 4, 5, 8, "helel", "wow","zero"]
  lastIndex = r_list[-1]
  reverse_list.append( lastIndex )
  r_list.remove(lastIndex)


print( reverse_list )




