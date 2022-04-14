'''
This program will calculate and displays the
amount earned based on the user input for homework 2

Name: Saad
'''
print ("Welcome to my program.")
name = input("Please enter your full name: ")
print("Hello,",name)
print("This program will ask you to enter the hours worked and the rate per hour. The program will calculate and display the amount earned.")

hour = eval(input("Enter number of hours: "))
rate = eval(input("Enter rate per hour: "))
sum = hour * rate
print("You have earned: $",sum)
print("Thank you and have a nice day.")
print ("Good bye!")
