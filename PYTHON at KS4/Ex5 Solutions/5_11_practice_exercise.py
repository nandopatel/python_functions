#11)Write a function called magic_number() that has a variable assigned
#to the value 7,  The user should be prompted to guess the magic number.
#The program should give the user feedback on the guess.
#i.	If the guess is greater than 7, “Too high”
#ii.	If the guess is less than 7, “Too low”
#iii.	If the guess is correct it should print “Well Done”

def magic_number(guess):
    number = 7
    while guess != number:
        if guess== number:
            print("Well done")
        else:
            if guess> number:
                print("Too high")
                guess = int(input("Please enter a guess: "))
            else:
                print("Too low")
                guess = int(input("Please enter a guess: "))
    


guess= int(input("Guess the number: "))

magic_number(guess)
