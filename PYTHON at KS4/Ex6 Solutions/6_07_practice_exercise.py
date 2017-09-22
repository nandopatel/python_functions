#7)Define a function called unique_elements() that takes a list and return a list
#that only contain unique elements. The program should take repeated elements
#but only return one value of the element.
#Example in the list [ 1,2,2,3,3,4]  it should return the list [1,2,3,4]

y= [ 1,2,2,3,3,4]

def unique_elements(l):
    x=[]
    for index in range(len(l)):
        test_value = l.pop()
        if test_value not in x:
            x.append(test_value)
    print(x)
        
        
    
unique_elements(y)



