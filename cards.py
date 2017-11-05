# import modules
import itertools, random

global draw
draw = []   #empty list for the random card draw

def makeDeck():
  global deck 
  deck = list(itertools.product(range(1,14),['Spades','Hearts','Diamonds','Clubs'])) #saves a deck of 52 cards

def shuffleDeck(deck):
  random.shuffle(deck) #shuffles the deck

def drawCards(numOfCards):
  for i in range(numOfCards):
    draw.append((deck[i][0], deck[i][1]))   #appends the cards to the empty 'draw' list

makeDeck()
shuffleDeck(deck)   #these 3 lines calls the functions to make, shuffle and choose 7 cards which is saved to the draw
drawCards(7)

def changeCard():
  print("First card: {}".format(draw[0]))
  resp = input("Change card? [y] or [n]: ")                     #here is to validate the user response and is functionality for the user to change the first 
  if resp == "y":                                               #card if they wish to do so.
    draw[0] = deck[random.randint(1,52)]                        #saves the first card as a random card from the original deck  
    print(draw[0])
  else:
    pass
  
def highOrLow(cardIndex):
  resp = input("[h]igher or [l]ower: ")
  if resp == "h" and draw[cardIndex]>draw[cardIndex+1]:         #LEFT OFF HERE!!! trying to do the conditionals for when the user chooses higher and the next card is higher not sure if the if statement will work as list items are tuples
    draw[0] = deck[random.randint(1,52)]
    print(draw[0])
  #elif: cover the condition if user chooses lower and next card is lower...
  else:
    pass

def playGame():                               
  changeCard()
  

playGame()




#General Public License v3.0 (GNU) to spookiestevie
