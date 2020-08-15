#Sean MacBride
#
#Program: firstprogram.py
#Description: A program where a given number represents feet per minute is changed to miles per hour
#
#Input: a given number in feet per minute
#Output: the equivalent speed in miles per hour

def main():
    num = eval (input ("Enter your number in feet per minute:"))
    mph = num * 60 / 5280
    print("Your MPH is:", mph)
main()