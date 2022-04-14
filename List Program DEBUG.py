#Name: Saad

current = []
power = []
resistance = [16, 27, 39, 56, 81]
currentSum = []
powerSum = []
for i in range(0,5):
    current.append(eval(input("Enter current value: ")))
    power.append(resistance[i] * current[i]**2)
    #print("Resistance /t Current /t Power")

print("Resistance \t Current \t Power")
                  
for lst1,lst2,lst3 in zip(resistance,current,power):
     print(lst1,"\t\t", lst2,"\t\t", lst3)
print("Total:", sum(resistance), "\t", sum(current),"\t\t",sum(power))

'''
Your program output should be as following. Note that the program
output will be different depending on your current input values.

Enter current value: 0.2
Enter current value: 0.4
Enter current value: 0.7
Enter current value: 1.3
Enter current value: 1.5
Resistance          Current          Power
16              0.2             0.6400000000000001
27              0.4             4.320000000000001
39              0.7             19.109999999999996
56              1.3             94.64000000000001
81              1.5             182.25
Total 219       4.1             300.96000000000004

'''
