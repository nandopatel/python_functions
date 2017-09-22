#9)Define a function called sum_list(), that takes a list as input and return
#the sum of all the elements in the list

z = [1, 3, 5, 7, 9, 10]

def sum_list(l):
    total =0
    for element in l:
        total = total + element
    return total

print(sum_list(z))
