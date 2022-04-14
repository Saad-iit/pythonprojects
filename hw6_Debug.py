'''
This program is to learn how to debug.
The program asks the user for an input, keeps tracks of the numbers
and gives the total vlaue along with the average once 0 is entered. 

Name: Saad
'''

contPositive = 0
countnegative = 0
total = 0
count = 0
num = eval(input("Enter an integer. Enter 0 to end input:" ))
while (num != 0):
    if (num > 0):
        contPositive = contPositive + 1
    elif (num < 0):
        countnegative = countnegative + 1
    total = num + total
    count = 1 + count
      
    '''Read the next number'''
    num = eval(input("Enter an integer. Enter 0 to end input:" ))

if (count == 0):
    print("No numbers are entered except 0")
elif (count != 0):
    print("The number of positives is", contPositive)
    print("The number of negatives is", countnegative)
    print("The total is", total)
    print("The average is", total/count)

'''
Test-run

Enter an integer, the input ends if it is 0: 9
Enter an integer, the input ends if it is 0: -35
Enter an integer, the input ends if it is 0: 13
Enter an integer, the input ends if it is 0: 355
Enter an integer, the input ends if it is 0: -4
Enter an integer, the input ends if it is 0: 290
Enter an integer, the input ends if it is 0: 1
Enter an integer, the input ends if it is 0: 0
The number of positives is 5
The number of negatives is 2
The total is 629
The average is 89.85714285714286
'''

