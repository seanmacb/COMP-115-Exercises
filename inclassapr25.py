#wedsgrades.py

def findAve(num,grades):
    tot=0
    for j in range(5):
        tot+=grades[num][j]
    tot=tot/5
    return tot

def main():
    grades=[[0 for i in range(5)] for j in range(25)] #makes a 2d array with 5 columns and 25 rows
    
    for i in range (2):
        print("Put in grades for student", i)
        for j in range(5):
            grades[i][j]=int(input())
    
    studentNum=int(input("Enter student ID to get average "))
    while studentNum>=0:
        oneAverage=findAve(studentNum,grades)
        print("The average for student ",studentNum, " is ", oneAverage)
        studentNum=int(input("Enter student ID to get average: "))
    print("All done!")
main()




'''for i in range(2):
    sum1=0
    for j in range(5):
        sum1+=grades[i][j]
    print("The average for student ",i, " is ",sum1/5, sep="")'''

'''class grades:
    def __init__(self):
        self.average=0
    def averagedisp(self, row):
        for i in range (5):
            self.average+=grades[row][i]
        self.average=self.average/5
        print ("The average of student ",row," is ", self.average, end="")'''