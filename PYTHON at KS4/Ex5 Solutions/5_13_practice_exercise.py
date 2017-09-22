#13)The factorial of a number is the product of all the integers below it.
#For example the factorial of 4 is 4*3*2*1 = 24.  
#a. Write a function called factorial() that returns the factorial of the given number.

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)


number = int (input("Enter the number to find the factorial of: "))

print(factorial(number))
