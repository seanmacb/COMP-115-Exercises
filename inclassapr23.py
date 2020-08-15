#Making a nice litte x o o o x o o o x tic tac toe board

def printer(board):
    for i in range(3):
        for j in range (3):
            print(board[i][j], end="")
            if j<2:
                print(" | ", end="")
        print()
        if i<2:
            print("--+----+--")



def main():
    tictactoe=[[" " for i in range (3)] for j in range (3)]
    for i in range (3):
        for j in range(3):
            if i==j:
                tictactoe[i][j]="X"
            else:
                tictactoe[i][j]="O"
    printer(tictactoe)
            
main()