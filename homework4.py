'''
This program asks displays the rate of shipping costs based
on weight of package, made for hoemwork 4.

Name: Saad
'''
more = "y"
while (more == "y"):
    weight = eval(input("Enter weight of package (in pounds): "))
    if (weight >= 0 and weight <= 2):
        cost = weight * 1.10
        print("The Fast Frieght shipping cost for your package is: $",cost)
    elif (weight > 2 and weight <= 6):
        cost = weight * 2.20
        print("The Fast Frieght shipping cost for your package is: $",cost)
    elif (weight > 6 and weight <= 10):
        cost = weight * 3.70
        print("The Fast Frieght shipping cost for your package is: $",cost)
    elif (weight > 10):
        cost = weight * 3.80
        print("The Fast Frieght shipping cost for your package is: $",cost)
    else:
        print("Please try again!")
        
    more = input("Do you want to enter Another? <y/n>: ")
print("Thank you for using The Fast Frieght Shipping tool!")
    
