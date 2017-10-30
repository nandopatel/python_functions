global password
def getpw():
    password = str(input('Enter password: '))
    pwlencheck(password)
def pwlencheck(password):
    if len(password) >= 16 or len(password) <= 7:
        print('password must be between 8 - 15 chars')
        getpw()
    else:
        verifpw(password)
def verifpw(password):
    userinp = str(input('verify password: '))
    if userinp == password:
        print('verified')
    else:
        print('incorrect')
        verifpw(password)
getpw()
