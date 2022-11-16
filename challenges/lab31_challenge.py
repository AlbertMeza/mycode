#!/usr/bin/python3
import random

def main():
    wordbank= ["indentation", "spaces"] 
    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 
            'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 
            'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 
            'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

    wordbank.append(4)
    
    studentCount = len(tlgstudents)

    num = int(input("Please enter a student number (0-"+str(studentCount)+") or type -1 for a random selection: "))

    while True:
        if 0 <= num <= studentCount:
            break
        elif num == -1:
            num = random.randint(0,studentCount)
            break
        else:
            num = int(input("Try again, please enter a student number(0-"+str(studentCount)+") or type -1 for a random selection: "))

    selection = tlgstudents[num]
    print()
    print("You have selected, the talented: " + str(selection))
    print()
    print(str(selection) + " always uses " + str(wordbank[-1]) + " " + str(wordbank[1]) + " to indent.")  
main()
