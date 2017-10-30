def agecheck(age,lower,upper):
    if age >= lower and age <= upper:
        valid = True
        print('age valid')
    else:
        valid = False
        print('age invalid')

agecheck(12,16,20)
agecheck(16,16,90)
