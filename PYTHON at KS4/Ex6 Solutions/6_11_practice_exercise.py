#11)Define a function called list_of_deviation(), that takes list as input
#and return a list that represent how much each element deviate from the mean


z = [1, 3, 5, 7, 9, 10]

def sum_list(l):
    total =0
    for element in l:
        total = total + element
    return total



def mean_list(l):
    return sum_list(l)/len(l)

mean=mean_list(z)

def list_of_deviation(l):
    for index in range(len(l)):
        z[index] = z[index]- mean
        
list_of_deviation(z)

print(z)
