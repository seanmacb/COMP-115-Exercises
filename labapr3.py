from graphics import *

def myPoint(win,color,x,y):
    p=Point(x,y)
    p.setFill(color)
    p.draw(win)
    input("Press Enter to continue")
    win.close()
    
    
def main():
    x=eval(input("Enter an x value "))
    y=eval(input("Enter a y value "))
    color=input("Enter a color ")
    window=GraphWin("Fractals", 1000, 800)
    
    myPoint(x,y,color,window)
    
    
main()