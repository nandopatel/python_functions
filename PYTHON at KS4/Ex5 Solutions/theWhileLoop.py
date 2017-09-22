#The While Loop
#Syntax

# while <condition>:
#   <block>

number =1

while number<11:
    print(number)
    number = number+1

while number<11:
    print(number, "Squared is ", number*number)
    number = number +1

# The Solution

# Write a python program that ask the user to enter the number to squared upto
# Define a function called squared_upto() that takes an integer
# use the while loop to print the squared numbers from 0 upto the given number.
# HINT   number squared --> number*number

def squared_upto(num):
    index = 1
    while index<num:
        print(index, "Squared is ", index*index)
        index = index +1

number = int(input("Enter the number to square upto: "))

print(squared_upto(number+1))


# The Break Statement
# Syntax

#   while <condition>:
#       <code>
#       if <BreakTest>:
#           break
#       <code>
#
#   <code after while loop>

#list
z=[2, 4, 6, 10, 7, 9, 23, 50, 12]

def find_seven(p):
    i=0
    while i!=len(p):
        if p[i] ==7:
            print("Breaking out of the while loop ")
            print("Found at position ", i)
            break
        i=i+1
    print("After the while loop")

print(find_seven(z))
















































































