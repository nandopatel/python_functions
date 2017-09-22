#9) Define a function called power_value(), that takes two integers
#and return the first raised to the power of the second

def power_value(base, index):
    return base**index

base = float(input("Enter the number for the base: "))
index = float(input("Enter the index: " ))

print("The power is ", power_value(base, index))
