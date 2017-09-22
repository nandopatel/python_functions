#9)Write a function called print_upto() that takes a number as input and
#print all the whole numbers from 1 up to and including the given number

def print_upto(number):
    for val in range(1,number+1):
        print(val)

num = int(input("Enter the number to print up to: "))

print(print_upto(num))
