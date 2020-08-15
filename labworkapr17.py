def lab11_1a():
    list1=[]
    inp=int(input("Enter an integer "))
    while inp!=0:
        list1.append(inp)
        inp=int(input("Enter an integer "))
    for item in list1:
        print(item,end=" ")
    print()
    s=int(input("Enter an s "))
    
    for item in range(0,len(list1),s+1):
        print(list1[item], end=" ")
    
lab11_1a()

def lab11_1c():
    list1=[]
    inp=int(input("Enter an integer "))
    while inp!=0:
        list1.append(inp)
        inp=int(input("Enter an integer "))
    front=0
    back=len(list1)-1
    while front<back:
        print(list1[front], list1[back],end=" ")
        front+=1
        back-=1
#lab11_1c()

def lab11_1d():
    list1=[]
    inp=int(input("Enter an integer "))
    while inp!=0:
        list1.append(inp)
        inp=int(input("Enter an integer "))
    prompt=input("Want to see positive or negative values? (Enter P for positive, N for negative) ")
    list1=list1.reverse()
    length=len(list1)
    if prompt=="P":
        for i in range(0,length):
            if list1[i]>0:
                print(item, end=" ")
    elif prompt=="N":
        for i in range(0,length):
            if list1[i]<0:
                print(item, end=" ")
#lab11_1d() #idk if this works


class myList:
    def __init__ (self):
        self.list1=[]
    def addValue(self, a):
        self.list1.append(a)
    def printList(self):
        for item in self.list1:
            print(item, end=" ")

def lab2():
    lablist=myList()
    num=int(input("Enter an integer: "))
    while num!=0:
        lablist.addValue(num)
        num=int(input("Enter an integer: "))
    lablist.printList()
    print("The end!")
#lab2()