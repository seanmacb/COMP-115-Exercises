#
import math

def main():
    num=eval(input("Enter a number and I will show you the square root of it! "))
    sqrtnum=math.sqrt(num)
    sqrttenth=int(sqrtnum+0.05)
    sqrtint=int((sqrtnum+0.5)*10)/10
    print("The square root of that number is", sqrtnum)
    print("The square root of that number rounded to the nearest tenth is", sqrttenth)
    print("The square root of that number rounded to the nearest integer is", sqrtint)
main()

