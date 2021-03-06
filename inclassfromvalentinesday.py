from graphics import *

anum=eval(input("How many A's were in this class? "))
bnum=eval(input("How many B's were in this class? "))
cnum=eval(input("How many C's were in this class? "))
dnum=eval(input("How many D's were in this class? "))
fnum=eval(input("How many F's were in this class? "))

def main():
    
    win=GraphWin("Grades",800,800)
    
    arect=Rectangle(Point(50,750),Point(190,750-7*anum))
    arect.setFill("red")
    arect.draw(win)
    brect=Rectangle(Point(190,750),Point(330,750-7*bnum))
    brect.setFill("blue")
    brect.draw(win)
    crect=Rectangle(Point(330,750),Point(470,750-7*cnum))
    crect.setFill("yellow")
    crect.draw(win)
    drect=Rectangle(Point(470,750),Point(610,750-7*dnum))
    drect.setFill("green")
    drect.draw(win)
    frect=Rectangle(Point(610,750),Point(750,750-7*fnum))
    frect.setFill("purple")
    frect.draw(win)
    yaxis=Line(Point(50,50),Point(50,750))
    xaxis=Line(Point(50,750),Point(750,750))
    xaxis.draw(win)
    yaxis.draw(win)
    atext=Text(Point(120,775),"A's")
    atext.draw(win)
    btext=Text(Point(260,775),"B's")
    btext.draw(win)
    ctext=Text(Point(400,775),"C's")
    ctext.draw(win)
    dtext=Text(Point(540,775),"D's")
    dtext.draw(win)
    ftext=Text(Point(680,775),"F's")
    ftext.draw(win)
    input("Press <enter> to continue...")
    
    win.close()
    
main()