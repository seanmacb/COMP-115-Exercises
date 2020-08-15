import random as rand

class Tictactoe:
    def __init__(self):
        self.list=[[" "for i in range(3)] for j in range (3)]
    def printBoard(self):
        for i in range(3):
            for j in range (3):
                print(self.list[i][j], end="")
                if j<2:
                    print("|", end="")
            print()
            if i<2:
                print("-+-+-")
    def setBoard(self, row,column):
        self.list[row][column]="X"
    def computerTurn(self):
        row=rand.randint(0,2)
        column=rand.randint(0,2)
        while "X" in self.list[row][column]:
            row=rand.randint(0,2)
            column=rand.randint(0,2)
        self.list[row][column]="O"
    #def checkWin(self):
        

def main():
    ttt = Tictactoe ()
    ttt.printBoard()
    win = False
    numTurns = 0
    while not win:
        r,c = eval(input ("Enter row, col:"))
        numTurns = numTurns + 1
        ttt.setBoard (r, c)
        ttt.printBoard()
        if ttt.checkWin() == True:
            print ("Player wins!")
            win = True
        elif numTurns == 9:
            print ("Tie!")
            win = True
        else:
            ttt.computerTurn ()
            numTurns = numTurns + 1
            ttt.printBoard()
            if ttt.checkWin() == True:
                print ("Computer wins!")
                win = True   
    print ("Thanks for playing!")
main()