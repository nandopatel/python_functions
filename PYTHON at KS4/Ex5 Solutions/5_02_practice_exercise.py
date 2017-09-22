#2) Write a python program that asks the user to enter a score,
#it should print the following message, base on the score of the user: 
#50 and above  -> “Pass”
#0-49          -> “Fail”

score = int( input("Please enter your score: "))

if score>49:
    print("Pass")
else:
    print("Fail")
