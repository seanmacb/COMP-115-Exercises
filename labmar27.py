'''


#Returns the fibonnaci sequence when prompted for a terms

def fib(a):
    folder=0
    fold=1
    flist=[]
    flist.append(fold)
    for i in range(0,a-1):
        f=fold+folder
        flist.append(f)
        folder=fold
        fold=f
    return flist


#Returns the sum of a fibonnaci sequence with a terms

def fibsum(a):
    folder=0
    fold=1
    flist=[]
    flist.append(fold)
    for i in range(0,a-1):
        f=fold+folder
        flist.append(f)
        folder=fold
        fold=f    
    numsum=sum(flist)
    
    return (numsum)


def main():
    number=int(input("Enter in however many fibonacci numbers you want: "))
    print(fib(number))
    print("The sum of those numbers is",fibsum(number))
main()
'''

#Function that rolls a dice twice in main()

import random

def die():
    a=random.randint(1,6)
    return a

def main():
    a=input("Press enter to roll the die!")
    print(die())
    
    print(die())
main()

