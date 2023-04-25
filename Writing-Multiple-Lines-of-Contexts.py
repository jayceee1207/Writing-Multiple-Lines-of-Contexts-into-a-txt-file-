#John Carlo Ablay
#BSCPE 1-5
#Assignment 4: Program 3
#April 22, 2023

import pyfiglet
import emoji
import os

print("\u001b[37;1m","*********************************************************")
print("\u001b[33;1m","WRITING MULTIPLE LINES IN A FILE")
print("\u001b[33;1m","Programmed by: John Carlo Ablay")
print("\u001b[37;1m","*********************************************************")

title = pyfiglet.figlet_format("\nWRITING MULTIPLE LINES IN A FILE", font = "digital" )
print(title)

#PSEUDOCODE

#make a function that will make every line and upload to the other file
def lines():
#open file named myfile.txt
    my_file = open("myfile.txt", "w")
    answer = 'y' or 'Y'
            
    #while line is equal to y
    while answer == 'y' or 'Y':
        #   ask the user to input in the line
        command = input('\nEnter line: ')
        command += '\n'
        #   write on the line
        my_file.write(command)
        #   ask the user if they want to add more lines
        answer = input("Are there any more line/s? y or n? ")
        #   if answer is n
        if answer == 'n':
            print("Thank you for using our program!")
            break
    #       stop the code
    my_file.close()
    #close the file

#call the function
lines()

print("\nThank you for using our program!")
print(emoji.emojize('Have a good day! :grinning_face:'))