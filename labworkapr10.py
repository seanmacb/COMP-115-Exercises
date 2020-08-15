class String:
    def __init__ (self,string):
        self.string=string
        
        
    def display(self):
        print(self.string)
        
    def countLetter(self, letter):
        print("This string has the letter", letter, self.string.count(letter)+self.string.count(letter.capitalize()), "times")

    def compare(self, string):
        if self.string==string.string:
            return True
        else:
            return False

    def sameWord(self, string):
        
        if self.string.upper()==string.string.upper():
            return True
        else:
            return False        

def main():
    str1=String("Hello")
    str1.display()
    str1.countLetter("l")
    str1.countLetter("e")
    
    str2=String("Hello")
    if str1==str2:
        print("The strings are the same")
    else:
        print("The strings are not the same")
        
    if str1.compare(str2)==True:
        print("The strings are the same")
    else:
        print("The strings are not the same")
    
    str3=String("hello")
    if str1.compare(str3)==True:
        print("The strings are the same")
    else:
        print("The strings are not the same")
        
    if str1.sameWord(str3)==True:
        print("The strings are the same")
    else:
        print("The strings are not the same")
main()