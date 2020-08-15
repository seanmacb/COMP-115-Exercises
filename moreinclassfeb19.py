#Gives the average of 3 scores in a file

def main():
    infile=open("scoresfeb19.dat","r")
    print("Reading from file...")
    score1=int(infile.readline())
    score2=int(infile.readline())
    score3=int(infile.readline())
    print(score1,score2,score3)
    average=(score1+score2+score3)/3.0
    print("The average is",average)
    infile.close()
main()