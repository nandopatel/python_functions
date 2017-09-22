#7) Define a function called long_name() that take a name is input
#and return a Boolean value (True or False) based on the number of
#characters in the name.  Assume a name is long if it contains more
#than 14 characters

def long_name(name):
    if len(name)>13:
        return True
    else:
        return False


test_name = input("Please enter the name to test: ")

print(long_name(test_name))
