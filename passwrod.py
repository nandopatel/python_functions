
import string
import random
from time import sleep
import re
# Imports ^^^


string1 = "qwertyuiop"

def menu():
    """
    This is a simple menu simulation function that will ask the user to input the first
    letter of one of the options, if an invalid input is given it will recall this function
    On valid entry the function relevant to that option is called
    ~
    Args: none
    Returns: none
    """
    score = 0
    print("---Menu---")
    print("*Generate new password | g \n*Check password | c \n*Quit | q \n")
    # User inputs a letter. The .lower() method converts the user input to lowercase so uppercase inputs are valid.
    user_input = input("Choose [g], [c] or [q]: ").lower()
    if user_input == 'g':
        generate_password()
        back_to_menu()
    elif user_input == 'c':
        user_pass = get_password()
        sleep(0.5)
        # print(score)
        score += password_list_search(user_pass)
        sleep(0.5)
        # print(score)
        score += largest_substring_match(string1, user_pass)
        sleep(0.5)
        # print(score)
        score += length_check(user_pass)
        sleep(0.5)
        # print(score)
        return ""

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


def get_password():
    """
    This function assigns a score value based on how strong the password is
    ~
    Args: none
    Returns: passwords strength score
    """
    user_pass = input("Enter your password: ")
    #password_list_search(user_pass)
    return user_pass


def password_list_search(user_pass):
    """
    This function checks the password against a 10000 most common password list
    ~
    Args: password, score
    Returns: score
    """
    f = open("/home/anand/Desktop/10k_most_common.txt")
    password_list = [x.strip() for x in f.readlines()]
    for i in password_list:
        if i == user_pass:
            print("Found your password in a public passwords list!!! , -25")
            return -25
            break
    print("Your password was not found, +5")
    return 5


def largest_substring_match(string1, string2):
    """
    This function checks the password against a 10000 most common password list
    ~
    Args: password, score
    Returns: score
    """
    match = ''

    lst = []
    for indx, letter in enumerate(string1):
        match += letter
        if match in string2:
            lst.append(match)

        else:
            lst.append('')

            match = ''
    if len(max(lst, key=len)) >= 3:
        print("Contains key row substring matched on: {}, -5".format(max(lst, key=len)))
        return -5
    else:
        print("Does not contain key row substring, +10")
        return 10


def length_check(user_pass):
    """
    This function checks the password against a 10000 most common password list
    ~
    Args: password, score
    Returns: score
    """
    if len(user_pass) < 8:
        print("Password length is less than 8 characters, -5")
        return -5
    elif 12 >= len(user_pass) >= 8:
        print("Password length is between 8 and 12 characters, +5")
        return 5
    else:
        print("Password length is longer than 12 characters, +10")
        return 10


menu() 
























