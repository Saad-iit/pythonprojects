'''
Asks user to input score and avergaes them together.
Made for homework 7 question 1.

Name: Saad
'''
score = 0
total = 0
count = 0
more = "y"
while (more == "y"):
    num = eval(input("Enter a score: " ))
    total = num + total
    count = 1 + count
    more = input("Do you want to enter Another? <y/n>: ")

score = total/count
if (score >= 90):
    print("A")
if(score >= 80)and(score < 90):
    print("B")
if(score >= 70)and(score < 80):
    print("C")
if(score >= 60)and(score < 70):
    print("D")
if(score < 60):
    print("F")
