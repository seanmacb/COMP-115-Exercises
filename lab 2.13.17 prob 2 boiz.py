num1=eval(input("Give me a big number man! "))
num2=eval(input("Give me a smaller number man! "))
intquot=num1//num2
intrem=num1%num2
intprod=num1*num2

def main():
    print("{0:6}".format(num1))
    print("{0:1}{1:5}".format("x",num2))
    print("{0:6}".format("______"))
    print("{0:6}".format(intprod))
    print()
    print("{0:8}{1:>3}{2:3}".format(intquot,"R",intrem))
    print("{0:>8}".format("_____"))
    print("{0:<3}{1:1}{2:4}".format(num2,")",num1))
main()