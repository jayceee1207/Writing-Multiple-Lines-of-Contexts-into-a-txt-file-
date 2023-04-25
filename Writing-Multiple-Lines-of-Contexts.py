#John Carlo Ablay
#BSCPE 1-5
#Assignment 4: Program 3
#April 22, 2023

print("*********************************************************")
print("WRITING LINES OF CONTEXTS")
print("Programmed by: John Carlo Ablay")
print("*********************************************************")


#PSEUDOCODE

#make a function that will make every line and upload to the other file
def lines():
#open file named myfile.txt
    my_file = open("myfile.txt", "w")
    line = 'y' or 'Y'
            
    #while line is equal to y
    while line == 'y' or 'Y':
        #   ask the user to input in the line
        command = input('\n Enter line: ')
#   write on the line
#   ask the user if they want to add more lines
#   if answer is n
#       stop the code
#close the file

#call the function