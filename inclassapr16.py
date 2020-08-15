#prompt for n items
#type in n items
#store in list
#prompt for "interval"
#print out the list by that interval

def main():
    
    itemnumber=int(input("How many items do you want? "))
    list1=[]
    for i in range(0,itemnumber):
        item=input("Enter the item ")
        list1.append(item)
    interval=int(input("What interval do you want? "))
    for i in range(0,itemnumber,interval):
        print(item) #This doesn't work too well
main()