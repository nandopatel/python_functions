# The for loop iterate over the items in a sequence
#Syntax

# for <variable> in <sequence>:
#   <block>

month = "September"

for letter in month:
    print(letter)


#range(<start>, <end>)

for i in range(0,5):
    print("Hello")

# The Solution

# write a program that will print the square numbers from 0-10
# HINT   number squared --> number*number

for number in range(0,11):
    print(number, "Squared is ", number*number)

# The extended FOR Loop solution

# Ask the user to enter the number to squared upto
#Define a function called squared_upto() that takes an integer
# and print the squared numbers from 0 upto the given number.
# HINT   number squared --> number*number


#define the squared_upto() function
def squared_upto(num):
    for value in range(0,num+1):
        print(value, " Squared is ", value * value)

number = int(input("Please enter a number to square upto: "))

print(squared_upto(number))







































