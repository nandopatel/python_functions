#NOTICE
#One of the first python programs I have made, I come here to entertain myself, I dont even want improve it... :P
#NOTICE

#This is the Quiz program
score = 0
#This is the introduction
print("Hello there! :)")
name = raw_input("What is your name? ")
print ('Hello',name)
print ('So' ,name)
print ("Welcome to the quiz!")
#This is a question, the user has a choice to input what ever the question asks
answer = raw_input ('What orbits the Earth? ')
#if the user inputs 'moon' they get a print that displays "Good Job! and they get +3 points"
if answer == "moon":


    print ("Good job" ,name)
#Else if the answer is wrong they lose 3 points and have a mean message displayed
else:
    score = score - 3
    print ("Wow, you actually live under a rock")

#this is another question
print ("Welcome to the second quiz!")
answer = raw_input ('What is your favourite colour? ')
if answer == "blue":
    score = score + 10
    print ("Good job, good choice" ,name)
else:
    score = score - 1
    print ("I hope you realise that there are no other cooler colours than blue")

    
print ("Welcome to the third quiz!")
answer = str(raw_input('What does 3+(4+2) equal? '))
if answer == "9":
    score = score + 4
    print ("Good job" ,name)
else:
    score = score - 2
    print ("9, If i can do it, you should be able to. Dumbass!")


print ("Welcome to the fouth quiz!")
answer = raw_input ('What does gravity do? pull or push. ')
if answer == "pull":
    score = score + 4
    print ("Good job soon you will be able to become a phisist" ,name)
else:
    score = score - 2

print ("9, If i can do it, you should be able to. silly!")
#this displays your overall score at the end
print ("Your score = ",score)


