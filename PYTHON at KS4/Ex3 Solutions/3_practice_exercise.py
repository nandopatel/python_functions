#1) Write a python program that stores your favourite quotation
#in a variable called quote
quote = "Your favourite quotation"
print(quote)

#2) Define a variable called name that assigns your name to it
name="Patrick"
print(name)

#3)Write a python program that ask the user for three numbers
#and print their sum
number1= int(input("Please enter the first number: "))
number2= int(input("Please enter the second number: "))
number3= int(input("Please enter the third number: "))

total = number1+number2+number3
print("The sum is ", total)

#4) Write a python program that ask the user for their name and age
# and print this back to the screen with a warm message.
name = input("What is your name: ")
age = int( input("How old are you?: "))
print("Hello ", name, ", lease accept this warm message")

#5) What is the data type of x in the code snippet below?
x=34.67
print(type(x))

#6) What letter will be printed on the screen after running the following code?
title="Python for key stage 4"
letter = title[3]
print(letter)

#7) What letter will be printed on the screen after running the following code?
title="Python for key stage 4"
letter = title[-5]
print(letter)

#8) Use the slice operation / sub-sequence to print “key” from the variable title.
title = "Python for key stage 4"
print(title[11:14])


#9) Use the variable below that uses the concatenation operation to print the greetings below.
Name = "Benjamin"
#Greetings to print:  “Hello Benjamin, Python is fun”
print("Hello " + Name + ", Python is fun")


#10) What will the following code produce? 
title= "Python for key stage 4"
for letter in title:
    print(letter)
