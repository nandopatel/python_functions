#2) Define a function called perimeter_of_rectangle that takes two numbers
#to represent the length and width of a rectangle and return
#the perimeter of the rectangle.

def perimeter_of_rectange(length, width):
    return (2*length)+(2*width)


length = float(input("Please enter a length: "))
width = float(input("Please enter a width: "))

print(perimeter_of_rectange(length,width))
