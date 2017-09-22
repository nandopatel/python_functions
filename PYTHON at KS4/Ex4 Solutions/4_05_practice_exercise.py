#5) Write a program that requests from the user their name.
#The program should then use a function called head_name(),
#that print the first character from the given name.

def head_name(word):
    return word[0]

name = input("Please enter your name: ")
print("The head of ", name, " is ", head_name(name))
