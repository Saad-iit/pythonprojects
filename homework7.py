'''
This progam asks the user to enter a set of numbers and
loops that many times gathering the information.
It was made for homework 7 for question 2.

Name: Saad
'''

count = 0
contPositive = 0
countNegative = 0
total = 0
count = 0
endgoal = int(input("How many set of numbers would you like to enter:" ))
while (count < endgoal):
    num = eval(input("Enter number:" ))
    if (num > 0):
        contPositive = contPositive + 1
    elif (num < 0):
        countNegative = countNegative + 1
    else:
        count = count - 1
        print("Please retry by entering a number greater than 0")
    total = num + total
    count = 1 + count
    
      
print("The number of positives is", contPositive)
print("The number of negatives is", countNegative)
print("The total is", total)
print("The average is", total/count)
