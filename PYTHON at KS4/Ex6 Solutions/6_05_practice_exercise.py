#5)Define a function called remove_five(), that takes a list as input and
#remove all occurrence of 5 in the list.  Write the function in such a way
#that you will not receive an error if there is no 5s in the list

my_list = [12, 4,5, 3, 5, 34]

def remove_five(l):
    while 5 in l:
        l.remove(5)

remove_five(my_list)

print(my_list)
