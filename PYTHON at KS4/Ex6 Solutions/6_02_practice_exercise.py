#2)Without using the sort(), function that is defined on list.
#Write a function called my_sort(), that takes an unsorted list
#and return the sorted list

my_list = [56, 3, 89, 2, 34, 12]

def my_sort(l):
    sorted_list = False
    sorted_pos = len(l)-1
    
    print(l)
    while not sorted_list:
        sorted_list = True
        for index in range(sorted_pos):
            if my_list[index] > my_list[index +1]:
                sorted_list = False
                #Swap values
                my_list[index], my_list[index +1] = my_list[index +1], my_list[index]
                print(l)

my_sort(my_list)
print(my_list)
