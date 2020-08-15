
#Program that returns the Lastname, Firstinitial

firstname=str(input("What is your first name? "))
lastname=str(input("What is your last name? "))
fullname=str(input("What is your full name? "))
lastnamelen=len(lastname)
def main():
    
    print(lastname+",","{0:1.1}".format(firstname)+".")
    
    
    
main()