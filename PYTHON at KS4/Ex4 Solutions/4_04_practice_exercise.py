#4) Define a function called hello_three_times that takes an argument
#called name, and print hello name, three times on the screen

def hello_three_times(name):
    print("hello ", name*3)

person = input("Please enter the person to say hello to: ")

print(hello_three_times(person))
