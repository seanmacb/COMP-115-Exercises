#Gives the square root of a number rounded to 2 dec places

import math
def main():
    num=eval(input("Enter your number here: "))
    sqroot=math.sqrt(num)
    sqroot= int((sqroot + 0.005) * 100) / 100
    print("The square root of",num,"is",sqroot)
main()