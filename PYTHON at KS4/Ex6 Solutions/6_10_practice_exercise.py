#10) Define a function called mean_list(), that takes a list as input and returns
#the mean of the list.  The mean is the sum of all the elements divided by the
#number of elements, you can use the function above defined in question 9

z = [1, 3, 5, 7, 9, 10]

def sum_list(l):
    total =0
    for element in l:
        total = total + element
    return total

print(sum_list(z))


def mean_list(l):
    return sum_list(l)/len(l)


print(mean_list(z))
