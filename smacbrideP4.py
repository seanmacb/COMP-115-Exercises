# Sean MacBride
# Program: smacbrideP4.py
# Description: A program to convert data in a file from base ten to base three, or base 3, based on earlier lines in the program
# Input: The name of the data file
# Output: All of the converted values, with a message for when the program is finished

#Given a number in base 10, prints the equivalent in base 3
def ter(orig):
    #orig is the original input from the data file
    #lenorig is the length of the original data file's integer values only
    #origval is the integer value of the original data point
    #newval is the list with the ternary values
    #finalval is the final integer value of the ternary value, converted from the newval list
    #prints out a statement of the final value in converted form
    origval=eval(orig[0:len(orig)])
    newval=[]
    while origval//3!=0:
        newval.append(origval%3)
        origval=origval//3
    newval.append(origval%3)
    newval=newval[::-1] #Flipping the order of the list so it can be displayed correctly
    finalval=0 #Set finalval as 0 for algorithim in for loop in next line
    for i in range(0,len(newval)):
        finalval+=newval[i]*10**(len(newval)-i-1)
    orig=orig[0:len(orig)-1] #removes the line break that was in orig
    print("The number ",orig," in base 10 is the same as ",finalval, " in base 3.",sep="")
    print()

#Function that takes a ternary number and returns a base 10 number
def int(orig):
    #orig is the original string value
    #origlist is the list containing the original values
    #newtot is the actual integer value in base 10
    #prints out a statement of the final value in converted form
    origlist=orig[0:len(orig)-1]
    origlist=origlist[::-1]
    newtot=0 # Set to 0 for use in the for loop in the next line
    for i in range(0,len(orig)-1):
        newtot+=eval(origlist[i])*3**i
    orig=orig[0:len(orig)-1] #removes the line break that was in orig
    print("The number ",orig, " in base 3 is the same as ",newtot, " in base 10.",sep="")
    print()

#The findfile function directs the correct data to either int() or ter()
def findfile(filename):
    #infile opens the file in read form
    #commandline reads the line that directs
    #valline is the value of the line before conversion
    #this function directs the line data to whichever converter function is necessary
    print()    
    infile=open(filename, "r")
    commandline=infile.readline()
    while eval(commandline)!=3:
        if eval(commandline)==1:
            valline=infile.readline()
            int(valline)
        elif eval(commandline)==2:
            valline=infile.readline()
            ter(valline)
        commandline=infile.readline()
    infile.close()
    print("Finished!")
    

def main():
    filename = input("Enter filename: ") # asking for file name
    findfile(filename) # calls findfile function
    
    #I have abided by the Wheaton honor code in this work
    
main()