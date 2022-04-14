'''
This program is about python grpahical user interface
while calculating and displaying the
amount earned based on the user input for homework 15
Name: Saad
'''
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


root = tk.Tk()
root.withdraw()

name = simpledialog.askstring("Welcome and please type your full name", "Welcome to my program. \nPlease enter your full name:")
result = "Hello, " + name + "\n" + "This program will ask you to enter the hours worked and the rate per hour.The program will calculate and display the amount earned."
messagebox.showinfo("This what the program is about",result)

hours = simpledialog.askfloat("Input number of hours", "Enter number of hours:")
rate = simpledialog.askfloat("Input rate per hour:", "Enter rate per hour:")
sums = hours * rate
result = "You have earned: $" + str(sums)
messagebox.showinfo("Total",result)
goodbye = "Thank you and have a nice day. \nGood bye!"
messagebox.showinfo("Thank you!",goodbye)
