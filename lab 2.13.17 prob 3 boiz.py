firstname=str(input("What is your first name, kind person? "))
lastinitial=str(input("What is your last initial, kind person? "))
length=len(firstname)
othlength=length-2
def main():
    print(firstname)
    print("{0:1}{1:2}{2:1}".format(lastinitial,"",lastinitial))
    print("{0:1}{1:2}{2:1}".format(lastinitial,"",lastinitial))    
    print(firstname)
main()