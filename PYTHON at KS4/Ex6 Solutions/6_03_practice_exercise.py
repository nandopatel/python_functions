#3) Define a function called add_hello(), that takes any list and
#append the word “hello”, to the list.

my_list = [1, 2, 6, 89, 90]

def add_hello(l):
    return l.append("hello")

add_hello(my_list)

print(my_list)
