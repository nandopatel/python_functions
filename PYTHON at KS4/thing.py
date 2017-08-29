numerator = int(input("Input the numerator"))
denominator = int(input("Input the denominator"))
print("{} / {}".format(numerator,denominator))          #prints fraction
if numerator > denominator:
	print("Improper fraction")
else:
  	print("Proper fraction")
numerator1 = denominator                                #setting denominator to a new numerator
denominator1 = numerator                                #setting numerator to a new denominator
print("{} / {}".format(numerator1,denominator1))        #prints fraction
if numerator1 > denominator1:
  	print("Improper fraction")
else:
  	print("Proper fraction")v