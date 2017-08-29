
"""
bank_holidays_in_month = [1,0,1,1,2,0,0,1,0,0,0,2]
bank_holidays= lambda x: print(bank_holidays_in_month[x-1])
bank_holidays(5)


sortme_list = sortme = [1,23,23,54,32,3.4,23,4,2352,34,2,34,234,6,23,4,231,232,35,37,34,5,31,342345,6]
sorted_list = []

while sortme_list:
    item = sortme_list[0]
    for x in sortme_list:
        if x < item:
            item = x
    sorted_list.append(item)
    sortme_list.remove(item)

print(sorted_list)


lst1 = []
add_hello= lambda x: x.append("hello")
add_hello(lst1)
print(lst1)


lst2 = [1.2,45.6,34.3,3.5,80.76,34.333]
def discount_ten(lst):
    lst=[x*0.9 for x in lst]
    print(lst)
discount_ten(lst2)


lst3 = [5,5,5,5,5,5,2,3,4,5]
remove_five = list(filter(lambda a: a != 5, lst3))
print(remove_five)


str1="chiuihu99c"
is_palindrome = lambda str: print(True) if str == str[::-1] else print(False)
is_palindrome(str1)


lst4 = [12,1,1,1,1,1,1,1,23,2,3,1,2,341,23,12,3,123,123]vvvvvvvvvv
unique_elements = lambda x: print(set(list(x)))
unique_elements(lst4)


lst5 = [436,54.56,.34,53,45]
backways = lambda x: print(x[::-1])
backways(lst5)
v

lst6 = [34,34,3,4,34,3,4,3,43,4,3,4,34,34]
sum_list = lambda x: print(sum(x))
sum_list(lst6)


lst7 = [23,23,23,34,34,34,34,45,45,45,45,56,56,56,56,56,34,3,4,34,34,34,34,34,3,4,10]
mean_list = lambda x: print(sum(x)/len(x))
mean_list(lst7)


lst8 = [34,45,65]
def deviation(lst_of_numbers):
    mean = sum(lst_of_numbers) / len(lst_of_numbers)
    print(mean)
    for x in lst_of_numbers:
        print(x)
        print("deviance from mean: ", x-mean)
deviation(lst8)



from math import sqrt
lst9 = [1,2,3,4,5]

def standard_deviation(lst_of_numbers):
    deviations = []
    mean = sum(lst_of_numbers) / len(lst_of_numbers)
    for x in lst_of_numbers:
        sqrs_of_deviation = (x - mean) **2
        deviations.append(sqrs_of_deviation)
    std_deviation = sqrt(sum(deviations) / len(lst_of_numbers )- 1)
    print (std_deviation)
standard_deviation(lst9)


f = open("UKPrimeMinisters.txt", "r")
print(f.read())
f.close()

file_name = "my_quote.txt"
new_file = open(file_name, "w+")
new_file.close

def update_file(file_name,quote):
    new_file = open(file_name, "a")
    new_file.write("This is an update\n")
    new_file.write(quote)
    new_file.write("\n\n")
    new_file.close()
for index in range(0,3):
    quote = input("Enter favourite quote: ")
    update_file(file_name,quote)
print(new_file.read())
new_file.close()"""