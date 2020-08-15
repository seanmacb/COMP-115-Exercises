'''
#make a multiplication table
#fuck this

def main():
    print("         1     2     3     4     5     6     7     8     9     10")
    for i in range(1,11):
        for j in range(1,i+1):
            print(i, end="")
            print("{0:>4}".format(i*j), end="  ")
        print()
        
main()

'''
'''
#find the average of a list of numbers in a file

def main():
    filename=input("Enter a file name please: ")
    inFP= open(filename,"r")
    count=0
    summ=0
    for line in inFP:
        data= float(line)
        summ+=data
        count+=1
        
    if count==0:
        print("ERROR!!")
    else:
        print("The average is:", summ/count)
    inFP.close()
main()
'''

def main():
    filename=input("Enter a file name please: ")
    inFP= open(filename,"r")
    count=0
    summ=0
    for line in inFP:
        data= float(line)
        summ+=data
        count+=1
    average=summ/count
    
    if count==0:
        print("ERROR!!")
    else:
        print("The average is:", average)
    inFP.close()
    
    inFP= open(filename,"r")
    newsum=0
    for line in range(0,count):
        data=float(line)
        newsum+=(average-data)**2
        count+=1
        
    print("The variance s^2 is:", newsum/(count-1))
    
    inFP.close()
main()