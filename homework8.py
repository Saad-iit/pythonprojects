'''
This program asks the users name and then displays the rate of shipping costs based
on weight of package, while leteting the user enter multiple inputs.
It also puts all of them into functions and runs it from main().
Made for homework 8.

Name: Saad
'''
# Ask user’s full name, greet the user, and explain to the user what the program is all about.
def Greeting():
    name = input("Please enter your full name: ")
    print("Hello", name,"the program is about shipping cost for The Fast Frieght Shipping Company.")
    return(name)

# FunctionPackageCharge accepts weight as an argument and return the charges
def PackageCharge(Weight):
    more = "y"
    totalcost = []
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
        totalcost.append(cost)
    print("Thank you for using The Fast Frieght Shipping tool, your total cost is:" , sum(totalcost))

# the driver function that initiates the main program
def main():
    Greeting()
    PackageCharge('Weight')

main()
    
