# Sean MacBride
# Program: smacbrideP3.py
# Description: A pricing program for dooflingies that produces a price slip
# Input: The character price code of the dooflingie, if a discount is applied or not, the discount percentage, and the amount of money the customer is giving
# Output: A sales slip with the price, discount applied (if any, not printed if not applied)


#Defining the price codes of certain dooflingies
codea=24.99
codeb=22.99
codec=20.99
coded=10.99
taxperc=0.0625

'''
NOTES as of 3/5/18: Rounding to nearest tenth is fine, need to print slip at the end with appropriate formatting, need to figure out if inital if can be done with one if or if better to split into 4 if elifs
'''


def main():
    pricecode=input("Enter the price code here! ")
    pricecode=pricecode.capitalize()
    #issues getting the pricecode if statement working... How to get it to recognize A or B or C or D?
    if pricecode == "A" or "B" or "C" or "D":
        ifdiscount=str(input("Is a discount being applied? "))
        ifdiscount=str(ifdiscount.capitalize())
        if ifdiscount== "Y":
            discountval=int(input("How much of a discount would you like applied? "))
        else:
            discountval=0
        customermoney=eval(input("How much money is the customer giving you? "))
        customermoney=int((customermoney+0.005)*100)/100
        if pricecode=="A":
            pricebeforetax=(1-discountval/100)*codea
        elif pricecode=="B":
            pricebeforetax=(1-discountval/100)*codeb
        elif pricecode=="C":
            pricebeforetax=(1-discountval/100)*codec
        elif pricecode=="D":
            pricebeforetax=(1-discountval/100)*coded
        pricebeforetax=int((pricebeforetax+0.005)*100)/100
        priceaftertax=pricebeforetax*(1+taxperc)
        priceaftertax=int((priceaftertax+0.005)*100)/100
        change=customermoney-priceaftertax
        
        #print init price
        #print discount
        #print tax
        #print line break
        #print total
        #print change
        
        
        #print(customermoney, discountval, pricecode, pricebeforetax, priceaftertax)
    else:
        print("Whoops! That code is invalid!")
    
    #I have abided by the Wheaton Honor code in this work
    
main()