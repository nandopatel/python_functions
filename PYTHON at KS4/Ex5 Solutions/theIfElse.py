#Control Structure   - The IF ELSE Statement

#  if <condition>:
#       <true_block>
#  else:
#       <false_block>

number1 = 23
number2 = 50

if number1>number2:
    print(number1, " is the larger number ")
else:
    print(number2, " is the larger number")

# Write a python program that will print Pass if grade is
# 50 or above and Fail otherwise

# The solution
grade = 89

if grade > 49:
    print("Pass")
else:
    print("Fail")

# The program should ask the user for a value for grade.
# print Pass if grade is
# 50 or above and Fail otherwise

grade = int(input("Please enter a grade: "))

print(type(grade))

if grade > 49:
    print("Pass")
else:
    print("Fail")
    








