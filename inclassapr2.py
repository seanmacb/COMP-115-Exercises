x=2
def getval(one,two):
    two=two*x
    return one+two

def main():
    x=5
    for i in range(5,1,-2):
        i=getval(i,x)+i
        x=x+i
    print(i)
    print(x)
    print(getval(getval(2,1),5))
main()