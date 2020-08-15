class Zork:
    def __init__ (self, num):
        print ("Creating Zork with:", num)
        self.value = 2 * num
    def Zing (self):
        num = self.value * 2
        self.value = self.value + num
        num = num - 2
        print (num, self.value)
'''def main ():
    z = Zork(2) # line X
    z.Zing ()
    z.Zing ()
#main()'''

'''flam = 1
flim = {"two":"flam", "one":2, "three":flam}
for x in ["one", "two", "three", "four"]:
    print (x)
    print (flim.get (x, "Bozo"))'''


class number:
    def __init__(self,num):
        self.base=num
    def pow(self,val):
        return self.base**val
    def print(self):
        print(self.base)

def main():
    tmp = eval (input ("Enter number: "))
    p = eval (input ("Enter a power: "))
    x = number (tmp)
    y = x.pow (p)
    x.print ()
    print (y)
main()