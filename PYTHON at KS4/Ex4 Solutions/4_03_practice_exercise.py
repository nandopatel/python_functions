#3) Define a function called area_of_circle that takes one number as input
#to represent the radius, and return the area of the circle.

def area_of_circle(r):
    return (22/7)*r**2

radius = float( input("Please enter the radius: "))
print("The area is ", area_of_circle(radius))
