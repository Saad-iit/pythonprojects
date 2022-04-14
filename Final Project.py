'''
Final project in which there are three classes that find the area
then ask the user which method they would like to print them in.
As part of the classes, they are accessor and mutators as well
and everything is using a private atribute.

Name: Saad
'''
import math
import random
import tkinter as tk
from tkinter import messagebox

class Circle():
    def __init__(self, radius = 5):
        self.__radius = radius
        
    def set_radius(self, radius):
        self.__radius = radius
        
    def get_radius(self):
        return self.__radius
        
    def find_area(self):
        return ((self.__radius * self.__radius) * math.pi)

    def display(self):
        return ("Circle has an area of %.2f" %(self.find_area()))

class Square():
    def __init__(self, side = 4.3):
        self.__side = side
    
    def set_side(self, side):
        self.__side = side

    def get_side(self):
        return self.__side
        
    def find_area(self):
        return (self.__side * self.__side)

    def display(self):
        return ("Square has an area of %.2f" %(self.find_area()))

class Cube():
    def __init__(self, length = 3, width = 3, height = 3):
        self.__length = length
        self.__width = width
        self.__height = height
        
    def set_lenght(self,lenght):
        self.__length = length
    def set_width(self, width):
        self.__width = width
    def set_height(self, height):
        self.__height = height

    def get_lenght(self):
        return self.__length
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height
    
        
    def find_area(self):
        return (6 * (self.__length * self.__width))

    def display(self):
        return ("Cube has a surface area of %.2f" %(self.find_area()))

def main():
    randomshape = []
    choosemethod = 'askagain'
    for numbers in range(10):
        randomnum = random.randint(1,3)

        if (randomnum == 1):
            randomshape.append(Circle())
        elif (randomnum == 2):
            randomshape.append(Square())
        else:
            randomshape.append(Cube())

    while (choosemethod == 'askagain'):
        save = int(input("Enter 1 to save to a file, 2 to print on screen, or 3 for a new window: "))
        if (save == 1):
            filename = input("Please enter a file name to save to: ")
            file = open(filename + ".txt","w")
            for times in randomshape:
                file.write(times.display() + "\n")
            file.close()
            break
        elif (save == 2):
            for times in randomshape:
                print(times.display())
            break
        elif (save == 3):
            root = tk.Tk()
            if root._windowingsystem == 'win32':
                root.attributes('-alpha', 0.0)
            else:
                root.withdraw()
            for times in randomshape:
                if messagebox.askyesno("Results", times.display() + "\n" + "Would you like to see the next reuslt?"):
                    pass
                else:
                    break
            break
        else:
            print("Please try again by choosing one of the numbers")

main()
            
    
    
