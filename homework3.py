'''
This program will preform two tasks of reading a number and converting it
while and then taking the base and height of a triangle and calculating the area
for homeowrk 3.

Name: Saad
'''
feet = eval(input("Enter number of feet: "))
meters = feet * 0.305
print(feet,"feet to meters =",meters, "meters")
base = eval(input("Enter the base of the triangle: "))
height = eval(input("Enter the height of the triangle: "))
area = (base * 0.5) * height
print ("The area of the triangle with base", base, "and height", height, "equals", area)
