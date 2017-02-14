#NOTICE
#One of the first python programs I have made, I come here to entertain myself, I dont even want improve it...
#NOTICE


#This imports the module that the program will need to run
import random

#These are variables, they will be chosen at random
hobbies=["Playing video games","Eating Meat","Fencing","Swimming","Skating"]
adjectives=["awesome","OTT","incredible","alright","above average","awful"]
jobs=["Prime Minister","Footballer","Singer","Major pro player","Chef","Bored guy in an office","Head CEO of Apple"]
kids=["1","2","3","4","5"]
money=["10k","20k","15k","40 big ones","100k","1 mill","450k"]



#This is the introduction 'print' is what displays text on the screen
print("Welcome to LifeInvader")
#This ask for you name for later use in the program
name = raw_input("Please input your name: ")


#This is the actual scripts, they choose at random one of the variables and display them in a reasonable sentance that makes sense
print ("Hello",name,". you are ", random.choice(adjectives),"at",random.choice(hobbies))
print ("You will be an",random.choice(adjectives),"",random.choice(jobs))
print ("You are likely to have",random.choice(kids),"children",)
print ("In a year you will make around",random.choice(money),"a year",)
