# listOfRecords.py

# import the student.py module for access to its Student class
from student import *


def makeStudent (infoStr):
    # infoStr is a tab-separated line: lName fName idNo HW1 HW2 HW3 HW4 Hw5
    # returns a corresponding Student object
    
    # make an array of 5 items


    # split up the input at each tab (\t)


    # call constructor from Student class and return result


    
    
def readStudents():
    # creates a list of all the students in the file
    infile = open ("studentData", 'r')

    # make a list of students



    for line in infile:
        students.append (makeStudent (line))
    infile.close()
    return students

def main():
    # allStudents is a list of Student objects!
    allStudents = readStudents()
    
    # let's print each student's info
    print ("Name\t\tID #  HW1 HW2 HW3 HW4 HW5   Ave")
    for oneStudent in allStudents:
        print ("{0}\t{1}".format(oneStudent.getName(), oneStudent.getId()), end="")
        tempGrades = oneStudent.getGrades()
        sum = 0
        for i in range (5):
            oneGrade = int (tempGrades[i])
            sum = sum + oneGrade
            print ("{0:4}".format(oneGrade), end="")
            
        print("{0:6.1f}".format(sum/5))
    
    print ("Done!")
main()