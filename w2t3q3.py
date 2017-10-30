global password
def getpw():
    password = str(input('Enter password: '))
    verifpw(password)

def verifpw(password):
    tries = 0
    while tries < 3:
        userinp = str(input('verify password: '))
        if userinp == password:
            print('Welcome')
            break
        else:
            print('incorrect')
            verifpw(password)
            tries + 1
getpw()
