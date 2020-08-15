'''

#The auxiliary function that will return the larger number to main()
def maxx(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    elif b==a:
        return a
        
#The main() function, which requests two values as an input, and with the maxx() function prints the larger value
def main():
    one, two = eval(input("Enter two values: "))
    print(maxx(one,two), "is the larger value")
main()
'''
'''


#The auxiliary function which returns the completed string with the longer answer prompt
def maxx(a,b,c):
    if a>b:
        c[0]=a
    if b>a:
        c[0]=b
#The 
def main():
    answer=[1]
    one,two=eval(input("Enter two values: "))
    
    maxx(one,two,answer[0])
    print(maxx(answer[0], "is the larger of the two"))
    
main()
'''

'''
#A function that swaps the two values
def swap(a,b):
    return b,a

def main():
    one, two=eval(input("Two values! "))
    one, two=swap(one,two)
    print(one,two)
main()
'''


'''

#A program that models a tv remote

def getbutton():
    newbutton=input()
    while newbutton!="u" and newbutton!="d" and newbutton!="o":
        newbutton=input()
    return newbutton

def nextch(oldchannel,button):
    if button=="u":
        if oldchannel==13:
            return 2
        else:
            return oldchannel+1
    else:
        if oldchannel==2:
            return 13
        else:
            return oldchannel-1
    
    
def main():
    channel=2
    print(channel)
    button=getbutton()
    while button!="o":
        channel=nextch(channel,button)
        print (channel)
        button=getbutton()
    print("Goodbye!")
main()
'''