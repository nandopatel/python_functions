#6)A word is a palindrome if it reads the same thing in both directions.
#For example “civic”, “radar”, “level”, “redder”, “madam” are all palindrome.
#Write a function called is_palindrome(), that takes a word and return True
#if the word is a palindrome or False otherwise

def is_palindrome(word):
    end_pos = -1
    for index in range(int(len(word)/2)):
        if word[index] != word[end_pos]:
            return False
        else:
            end_pos = end_pos -1
    return True

test_word=input("Enter a word to test: ")
decision = is_palindrome(test_word)

print(decision)
