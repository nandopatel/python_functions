"""x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
if x > y:
	print(x)
else:
	print(y)


score = int(input("Enter score: "))
if score >= 80:
	print("Well done")
elif score >= 50:
	print("pass")
elif score < 20:
	print("You need to try harder")
else:
	print("fail")


score = int(input("Enter score: "))
if score >= 80:
	print("Well done")
elif score >= 50:
	print("pass")
elif score < 20:
	print("You need to try harder")
else:
	print("fail")


score = int(input("Enter score: "))
if score >= 80:
	print("A")
elif score >= 60 and score <= 79 :
	print("B")
elif score >= 40 and score <= 59:
	print("C")
elif score >= 30 and score <= 39:
	print("D")
else:
	print("U")


score = 0
word = input("Enter word: ")
for letter in word:
	if 'a' == letter:
		score += 5
	elif 'e' == letter:
		score += 4
	elif 'i' == letter:
		score += 3
	elif 'o' == letter:
		score += 2
	elif 'u' == letter:
		score += 1
print(score)


larger= lambda x,y: print(x) if x > y else print(y)
larger(8,6)


long_name= lambda name: print(True) if len(name) > 14 else print(False)
long_name("Christopher Cillian")"""