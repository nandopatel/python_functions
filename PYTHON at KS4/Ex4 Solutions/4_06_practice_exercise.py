#6) Write a program that asks the user for his name.
#The program should then use a function called tail_name(),
#that return the tail of the person’s name where the
#tail of the name is the person’s name without the first character.  
#HINT:   len(<string>) will return the length of a string

def tail_name(word):
    return word[1:len(word)]

name = input("Please enter your name: ")

print(tail_name(name))
