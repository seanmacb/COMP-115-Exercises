def main():
    value1=eval(input("Enter a value (-999 to end) : "))
    sumaverage=0 #setting as 0 for first value
    count=0
    fulllist=[]
    while value1!=-999:
        sumaverage+=value1
        count+=1
        fulllist.append(value1)
        value1=eval(input("Enter a value (-999 to end) : "))
    average=sumaverage/count
    print("The average is : ",average,sep="")
    print("     <     >=")
    morethan=[]
    lessthan=[]
    if item in fulllist<average:
        lessthan.append(item)
    else:
        morethan.append(item)
    morelength=len(morethan)
    lesslength=len(lessthan)
    if lesslength>=morelength:
        for i in range(0,morelength):
            print("{0:>6},{1:>6}".format(lessthan[i],morethan[i]))
        for item in lessthan:
            print(lessthan[i+morelength])
#main()

class Grades:
    def __init__(self):
        self.listOfGrades=[]
        self.count=0
    def addgrade(self):
        grade=int(input("Enter a grade: "))
        self.listOfGrades.append(grade)
        self.count+=1
    def average(self):
        sumgrades=0
        for grade in self.listOfGrades:
            sumgrades+=grade
        return sumgrades/self.count
        
def main():
    mygrades=Grades()
    mygrades.addgrade()
    stevegrades=Grades()
    stevegrades.addgrade()
    print("Average is: ", mygrades.average())
main()