#Create a myMath library
class myMath:
    def abs(number):
        if number>0:
            return number
        else:
                return number*-1
    def round(number):
        if number>0:
            number=int(number+0.5)
        else:
            number=int(number-0.5)
        return number
    def round1(number):
        if number>0:
            number=int((number+0.05)*10)/10
        else:
            number=int((number-0.05)*10)/10
        return number      
def main():
    m=myMath()
    num=eval(input("Enter a number "))
    print("Rounded, that number is",myMath.round(num))
    print("Rounded to one decimal place, that number is",myMath.round1(num))
    print("The absolute value of that number is", myMath.abs(num))
main()