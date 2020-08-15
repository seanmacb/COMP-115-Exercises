#Program that prompts for a single character string value of a number, returns the int val +5

def num1(val):
    val=ord(val)-48
    return val
def num2(val):
    if val=="0":
        return 0
    elif val=="1":
        return 1
    elif val=="2":
        return 2
    elif val=="3":
        return 3
    elif val=="4":
        return 4
    elif val=="5":
        return 5
    elif val=="6":
        return 6
    elif val=="7":
        return 7
    elif val=="8":
        return 8
    elif val=="9":
        return 9
    
    
def main():
    singval=input("Enter a single character: ")
    numnew1=num1(singval)+5
    numnew2= num2(singval)+5
    print("First function +5 yields",numnew1)
    print("Second function +5 yields", numnew2)
main()