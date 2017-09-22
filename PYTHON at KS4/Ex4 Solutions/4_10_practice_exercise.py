#10) If we had a function called absolute_value(), that takes a number and
#return the positive value of the given number.
#What value will be returned for the following print statements?

#Here I'll define the function absolute --> This is not required for the practice exercise
#When we discuss the IF-ELSE statement in control structure you should be
#able to define the function absolute_value
def absolute_value(num):
    if num<0:
        return -num
    else:
        return num

print(absolute_value(-5))
print(absolute_value(0))
print(-absolute_value(-5))

