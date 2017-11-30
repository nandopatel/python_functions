"""Anand Patel
This program is designed to present the user a menu if they want to: generate
a password, check the strength of a current password or quit from the program

General coding style:
I Anand Patel format my code under the PEP 8 style as this is the
style I always use when coding for clients in the industry. This style is
important because readability counts. Variables will be lowercase with underscores
and function names will also be lowercase with underscores. I will ensure functions are
provided with a docstring describing what it does, the arguments it takes and what it returns.
As this is a timed challenge I will use tabs instead of spaces for indenting as it is more efficient for me.
"""



import string
import random
import re
# Imports ^^^

def menu():
    """
    This is a simple menu simulation function that will ask the user to input the first
    letter of one of the options, if an invalid input is given it will recall this function
    On valid entry the function relevant to that option is called
    ~
    Args: none
    Returns: none
    """
    print("---Menu---")
    print("*Generate new password | g \n*Check password | c \n*Quit | q \n")
    # User inputs a letter. The .lower() method converts the user input to lowercase so uppercase inputs are valid.
    user_input = input("Choose [g], [c] or [q]: ").lower()
    if user_input == 'g':
        generate_password()
        back_to_menu()
    elif user_input == 'c':
        pass
    elif user_input == 'q':
        print("Goodbye! :)")
        pass
    else:
        print("Invalid input!")
        menu()

def back_to_menu():
    """
    This function asks the user if they want to go back to the menu and calls
    the menu() function, if they choose not to the program finishes. If input is
    invalid the function is called again.
    ~
    Args: none
    Returns: none
    """
    user_input = input("Would you like to go back to the menu? [y] or [n]: ").lower()
    if user_input == 'y':
        menu()
    elif user_input == 'n':
        print("See you soon...")
    else:
        print("Invalid input!")
        back_to_menu()


def get_password():
    """
    This is a simple function which asks the user for their password
    ~
    Args: none
    Returns: users' password
    """
    user_pass = input("Enter your password: ")
    return user_pass


def generate_password():
    """
    This function uses the string library to get the sorted list of ascii letters, digits
    from 0-9 and punctuation !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    A random character from the sorted chars is joined to the string. This is repeated
    8-12 times which is the random length of the password
    ~
    Args: none
    Returns: randomly generated password which includes alphanumerics and special characters of length 8-12
    """
    chars = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join((random.choice(chars)) for character in range(random.randint(8, 12)))
    print("Here is your new and secure password: ")
    print(generated_password)
    print("Keep it safe!")
    return generated_password


def check_password(password):




menu()