#Write a function called print_even_upto() that takes a number as input
#and print all the even numbers from 1 up to and including the given number

def print_even_upto(number):
    for val in range(1,number+1):
        if val%2 ==0:
            print(val)

num = int(input("Enter the number to print up to: "))

print(print_even_upto(num))

