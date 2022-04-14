'''
This program asks the users name and then displays the rate of shipping costs based
on weight of package, while letting the user enter multiple inputs.
It puts everything into a class and runs it from main().
Made for homework 12.

Name: Saad
'''

class ShippingCharges:
    def __init__(self, userName=None, totalPack=0, totalWeight=0, totalCost=0,compName=None):
        self.__userName = userName
        self.__totalPack = totalPack
        self.__totalWeight = totalWeight
        self.__totalCost = totalCost
        self.__compName = "The Fast Frieght Shipping Company"
    def getuserName(self):
        return self.__userName
    
    def setuserName(self, userName):
        self.__userName = userName
        
    def gettotalPack(self):
        return self.__totalPack
    
    def settotalPack(self, totalPack):
        self.__totalPack = totalPack

    def gettotalWeight(self):
        return self.__totalWeight
    
    def settotalWeight(self, totalWeight):
        self.__totalWeight = totalWeight
        
    def gettotalCost(self):
        return self.__totalCost
    
    def settotalCost(self, totalCost):
        self.__totalCost = totalCost    
        
    def displayShippingCharges(self):
        print(self.__compName,"\nName:", self.__userName, "\nTotal Packges:", self.__totalPack,"\nTotal Weight:", self.__totalWeight,"\nTotal Cost: $",self.__totalCost)

    def PackageChargeGreeting(self):
        print("Hello", self.__userName ,"the program is about the shipping cost for",self.__compName)
#Function getPackageCharge accepts weight as an argument and return the charges
    def getPackageCharge(self):
        more = "y"
        totalcost = []
        while (more == "y"):
            weight = eval(input("Enter weight of package (in pounds): "))
            if (weight >= 0 and weight <= 2):
                cost = weight * 1.10
                print(self.__compName,"cost for Package: $%.2f"%cost)
            elif (weight > 2 and weight <= 6):
                cost = weight * 2.20
                print(self.__compName,"cost for your package is: $%.2f"%cost)
            elif (weight > 6 and weight <= 10):
                cost = weight * 3.70
                print(self.__compName,"cost for your package is: $%.2f"%cost)
            elif (weight > 10):
                cost = weight * 3.80
                print(self.__compName,"cost for your package is: $%.2f"%cost)
            else:
                print("\nPlease try again!")
            more = input("Do you want to enter Another? <y/n>: ")
            print("\n")
            totalcost.append(cost)
        print(self.__compName,"total cost is: $%.2f"% sum(totalcost))

#The driver function that initiates the main program
def main():
    
    firstMethod = ShippingCharges()
    firstMethod.displayShippingCharges()
    
    print (" ")
    secondMethod = ShippingCharges("Jane Doe","4", "34.6","57")
    secondMethod.displayShippingCharges()
    
    print (" ")
    name = input("Please enter your full name: ")
    thirdMethod = ShippingCharges(name)
    thirdMethod.PackageChargeGreeting()
    thirdMethod.getPackageCharge()

#Start the program
main()

