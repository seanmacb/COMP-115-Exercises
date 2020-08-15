#Intro to classes
#A fraction class

class Fraction:
    def __init__ (self):
        self.numerator=0
        self.denominator=1
        self.result=0
        self.whole=0
        
    def input(self):
        fract=input()
        slash=fract.find("/")
        self.numerator=int(fract[0:slash])
        self.denominator=int(fract[slash+1:])        
        
    def mult(self, val1,val2):
        self.numerator=val1.numerator * val2.numerator
        self.denominator=val1.denominator * val2.denominator
    
    def display (self) :
        if self.numerator==0:
            print(self.numerator)
        elif self.whole!=0:
            print(self.whole, " ",self.numerator, "/",self.denominator, sep="",end="")
        else:
            print(self.numerator, "/",self.denominator, sep="",end="")
            
    def add (self, val1, val2):
        answer=Fraction()
        answer.denominator=val1.denominator*val2.denominator
        firstvalnum=val1.numerator* (answer.denominator//val1.denominator)
        secondvalnum=val2.numerator* (answer.denominator//val2.denominator)
        answer.numerator=firstvalnum+secondvalnum
        return answer
    def mixed(self):
        self.whole=self.numerator//self.denominator
        self.numerator=self.numerator%self.denominator


def main():
    f1=Fraction()
    f2=Fraction()
    print("The value of f1 is: ", end="")
    f1.display()
    print("Enter a fraction: ",end="")
    f1.input()
    print("Enter another fraction: ", end="")
    f2.input()
    print("The fractions are: ",end="")
    f1.display()
    print(" and ", end="")
    f2.display()
    print()
    f3=Fraction()
    f3.mult(f1,f2)
    print("The product of f1 and f2 is: ", end="")
    f3.display()
    print()
    f4=Fraction()
    f5=Fraction()
    f5=f4.add(f1,f2)
    print("The value of f4 is: ", end="")
    f4.display()
    print("The value of f5 is: ", end="")
    f5.display()
    f5.mixed()
    print()
    print("The mixed value of f5 is: ", end="")
    f5.display()
main()