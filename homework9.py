'''
Made for homework 9, lets the user input 6 numbers
then takes them as a list to use the power formula
and print them out.

Name: Saad
'''

resistance = [12,16,27,39,56,81]
current = []
power =[]
count = 0
while(count < 6):
    current_number = (eval(input("Enter number value of Current: ")))
    if (current_number <= 0):
        print("Please try Again")
    else:
        current.append(current_number)
        count = count + 1
        

print("Resistance", "Current", "power")

for num1, num2 in zip(current,resistance):
    power.append((num1**2) *num2)

for lst1,lst2,lst3 in zip(resistance,current,power):
    print(lst1,lst2,lst3)    

print("Total:", sum(resistance),sum(current), sum(power))
