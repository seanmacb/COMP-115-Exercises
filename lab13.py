class database:
    def __init__ (self):
        self.states = {"Massachusetts":"MA"}
        self.capitals = {"MA":"Boston"}
    
    def displayStates(self):
        for i in self.states:
            print("\n",i)
            
    def addState(self):
        fullname=input("\nWhat is the state's full name? ")
        abbreviation=input("\nWhat is the state's abbreviation? ")
        capital=input("\nWhat is the state's capital? ")
        self.states[fullname]=abbreviation
        self.capitals[abbreviation]=capital
    
    def displayCapital(self):
        inp=input("\nWhat is the two letter abbreviation of the state that you are looking for? ")
        
        local=self.capitals.get(inp,"bad")
        
        while local=="bad":
            print("\nThat input was invalid")
            inp=input("\nWhat is the two letter abbreviation of the state that you are looking for? ")
            local=self.capitals.get(inp,"bad")
        
        print("\n",self.capitals[inp])

    def showMenu(self):
        print("\n1 -- Display the states in the database")
        print("2 -- Add a new state")
        print("3 -- Display state capital")
        print("4 -- Display state abbreviation")
        print("5 -- Quit\n")
        choice=eval(input("What is your choice? "))
        return choice

    def displayAbbrev(self):
        inp=input("\nEnter the state's full name to get its abbreviation: ")
        local=self.states.get(inp,"bad")
        
        while local=="bad":
            print("\nThat input was invalid")
            inp=input("\nWhat is the two letter abbreviation of the state that you are looking for? ")
            local=self.states.get(inp,"bad")
        
        print("\n",self.states[inp])


def main():
    myDB = database()
    
    choice = myDB.showMenu()
    while choice != 5:
        if choice == 1:
            myDB.displayStates()
        elif choice == 2:
            myDB.addState()
        elif choice == 3:
            myDB.displayCapital()
        elif choice == 4:
            myDB.displayAbbrev()

        else:
            print ("Choice is invalid")
        choice = myDB.showMenu()
   
    print ("\nAdios!")
    
    
main()