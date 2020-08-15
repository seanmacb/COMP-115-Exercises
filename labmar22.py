#lab mar 22
#Manually making the power function

def power(x,y):
    b=1
    if x<0:
        return print("Done")
    else:
        if y>0:
            for i in range(0,y):
                b=b*x
        elif y<0:
            for i in range(0,-y):
                b=b/x
        else:
            b=1
                
        return b

def getvalues():
    a=float(input("Enter your first value here "))
    if a<0:
        return ("Done","")
    else:
        b=int(input("Enter your second value here "))
        return(a,b)


def main():
    
    a,b=getvalues()
    if type (a) is str:
        print("Done")
    else:
        
        print(power(a,b))
main()

'''

def sortem(a,b,c):
    if a>=b>=c:
        return (a,b,c)
    elif a>=c>=b:
        return (a,c,b)
    elif b>=a>=c:
        return (b,a,c)
    elif b>=c>=a:
        return(b,c,a)
    elif c>=a>=b:
        return (c,a,b)
    elif c>=b>=a:
        return (c,b,a)

    
    
def main():
    x=eval(input("Enter your first number here "))
    y=eval(input("Enter your second number here "))
    z=eval(input("Enter your third number here "))
    print(sortem(x,y,z))
main()
'''