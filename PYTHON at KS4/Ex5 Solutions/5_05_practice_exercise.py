#5) Suppose we calculate the vowel worth of a word based on the following rubric:
#a 	5 points
#e 	4 points
#i 	3 points
#o	2 points
#u 	1 points
#Write a python program that ask the user for a word,
#then calculate and print the vowel worth of the word entered.

word = input("Please enter a word to find out the vowel worth: ")

def vowel_worth(word):
    value = 0
    for letter in word:
        if letter =='a':
            value = value + 5
        if letter =='e':
            value == value + 4
        if letter =='i':
            value = value + 3
        if letter =='o':
            value = value + 2
        if letter =='u':
            value = value+ 1
    return value

print("The value worth of ", word, " is ", vowel_worth(word))
