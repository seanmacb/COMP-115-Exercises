from graphics import *

def main():
    
    biglength=eval(input("What do you want the length of the big square to be? "))
    smalllength=0.5*biglength
    win=GraphWin("Just a couple of squares man",800,800)
    rect1=Rectangle(Point((800-biglength)/2,(800-biglength)/2),Point((800+biglength)/2,(800+biglength)/2))
    rect2=Rectangle(Point((800-smalllength)/2,(800-smalllength)/2),Point((800+smalllength)/2,(800+smalllength)/2))
    rect1.draw(win)
    rect2.draw(win)
    rect1.setFill("blue")
    rect2.setFill("yellow")
    win.close()
main()