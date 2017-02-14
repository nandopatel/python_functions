#NOTICE
#One of the first python programs I have made, I come here to entertain myself, I dont even want improve it... :P
#NOTICE


# To Calculate Kinetic Energy
 
print("This program calculates the kinetic energy of a moving object.")
m_string = input("Enter the object's mass in kilograms: ")
m = float(m_string)
v_string = input("Enter the object's speed in meters per second: ")
v = float(v_string)
 
e = 0.5 * m * v * v
print("The object has " + str(e) + " joules of energy.")
