#6) Define a function called larger(), that takes two integers
#and return the larger of the two

def larger(first, second):
    if first > second:
        return first
    else:
        return second

number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))

print("The larger is ",larger(number1, number2))
