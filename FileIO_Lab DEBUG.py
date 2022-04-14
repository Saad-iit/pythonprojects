    # Name: Saad
        
    # Used data2.txt file as input
import os
def main():
    f1 = input("Enter a filename: ").strip()
    if os.path.isfile(f1):
        infile = open(f1, "r")
        all = infile.read()
        scores = [eval(x) for x in all.split()]

        print("Calculating data from the file.../n")
        print('There are ',len(scores), " scores")
        print("The total is " ,sum(scores))

        mean = sum(scores)/len(scores)
        print("The mean is", mean)
        
        infile.close()
    else:
        print("Failed to open file!")

               
main()               

