'''
This progam asks for a user file,
then takes the number values from the file and reads its contents
to determine different values. Made for homework 10
By: Saad'''

import os
import statistics
def main():
    fileName = input("Please enter a full filename: ").strip()
    if os.path.isfile(fileName):
        inputFile = open(fileName,"r")
        s = inputFile.read()
        scores = [eval(x)for x in s.split()]
        print("The total of the file is", sum(scores))
        print("There mean of the file is:", statistics.mean(scores))
        print("There median of the file is:", statistics.median(scores))
        print("The smallest number of the file is", min(scores))
        print("The largest number of the file is", max(scores))
        inputFile.close()
    else:
        print("Failed to open a file!")

main()
