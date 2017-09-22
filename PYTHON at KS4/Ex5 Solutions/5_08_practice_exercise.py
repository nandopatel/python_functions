#8) Define a function called largest() that takes three numbers
#and return the largest of the three.
#HINT: You can write the function from scratch of use the larger() function that was written before

def larger(first, second):
    if first > second:
        return first
    else:
        return second

def largest(first, second, third):
    return larger(larger(first, second), third)

print("The largest of 12, 45, and 90 is ", largest(12,45, 90) )
