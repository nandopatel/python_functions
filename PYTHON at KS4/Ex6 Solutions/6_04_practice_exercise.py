#4)Define a function called discount_ten(), that takes a list of floating point
#number and return a list with each element having a ten percent discount

my_list = [150, 46, 69, 120, 36]

def discount_ten(l):
    for index in range(len(l)):
        l[index] = l[index]*1.1
        

discount_ten(my_list)
print(my_list)
    
