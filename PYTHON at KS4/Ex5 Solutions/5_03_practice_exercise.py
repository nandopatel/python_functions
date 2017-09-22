#3) Develop the program in b) above by using a nested IF statement
#(IF within IF) to give the following additional information:
#50 and above 		-> “Pass”
#	80+		-> ”Well Done”
#0 – 49			-> “Fail”
#	<20		-> “You need to try harder”

score = int( input("Please enter your score: "))

if score>49:
    print("Pass")
    if score>79:
        print("Well Done")
else:
    print("Fail")
    if score <20:
        print("You need to try harder")
