# Sean MacBride
#
# Program: smacbrideP1.py
# Description: a program to give you the optimal shipping arrangement for shipping out dooflingies
# Input: Number of dooflingies required to be shipped out
# Output: The number of dooflingies, followed by the number of boxes 
# and prices for the total number of boxes to be sent out

#Notes - as of feb 12, algorithm is correct. Now need the formatting and rounding of numbers
#Notes - as of feb 13, formatting is correct. Want to add a dollar sign in cost column
#Notes - as of feb 13, done, tested, and algorithm working

doofinput= eval(input("How many Dooflingies are you trying to ship out? "))
hugeboxquant=int(doofinput//30)
largeboxquant=int((doofinput%30)//10)
medboxquant=int(((doofinput%30)%10)//5)
smallboxquant=int(((doofinput%30)%10)%5)
hugeboxprice=2.75*hugeboxquant
largeboxprice=1.5*largeboxquant
smallboxprice=0.5*smallboxquant
totalquant=hugeboxquant+largeboxquant+medboxquant+smallboxquant
totalprice=hugeboxprice+largeboxprice+medboxquant+smallboxprice

'''
Naming of variables:
doofinput - the number of dooflingies that you are prompted to be shipped out

hugeboxquant - the total number of huge boxes to be shipped out

largeboxquant - the total number of large boxes to be shipped out

medboxquant - the total number of medium boxes to be shipped out AND the
total price of the medium boxes to be shipped out. This is possible due to
the price of the medium boxes being 1$

smallboxquant - the total number of small boxes to be shipped out

hugeboxprice - the price of shipping out all of the huge boxes

largeboxprice - the price of shipping out all of the large boxes

smallboxprice - the price of shipping out all of the small boxes

totalquant - the total number of boxes being shipped out

totalprice - the total price of shipping all of the boxes out
'''

def main():
    print()
    print("Number of dooflingies: ", doofinput)
    print("{0:>20}{1:>12}".format("Boxes","Cost ($)"))
    print("{0:15}{1:5}{2:12.2f}".format("Huge Boxes:",hugeboxquant,hugeboxprice))
    print("{0:15}{1:5}{2:12.2f}".format("Large Boxes:",largeboxquant,largeboxprice))
    print("{0:15}{1:5}{2:12.2f}".format("Medium Boxes:",medboxquant,medboxquant))
    print("{0:15}{1:5}{2:12.2f}".format("Small Boxes:",smallboxquant,smallboxprice))
    print("{0:15}{1:5}{2:12.2f}".format("Totals:",totalquant,totalprice))
main()

# I have abided by the Wheaton Honor Code in this work