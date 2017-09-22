#4)Write a python program that ask the user for a score
#and print a grade based on the following:
#80-100		A
#60 – 79	B
#40 – 59	C
#30 – 39	D
#< 30		U

score = int(input("Please enter your score: "))

if score> 79:
    print("Your grade is A")
else:
    if score>59:
        print("Your grade is B")
    else:
        if score>39:
            print("Your grade is C")
        else:
            if score>29:
                print("Your score is D")
            else:
                print("Your score is U")

