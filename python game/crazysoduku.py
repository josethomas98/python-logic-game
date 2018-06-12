from graphics import *
import random, time
import sys
import os
from subprocess import *
def second():
    out = GraphWin("input", 400, 400)
    out.setBackground("white")
    testText = Text(Point(200,80),'TRIAL SPACE')
    testText.setStyle('bold')
    testText.setTextColor('green')
    testText.draw(out)
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    inEntry = Entry(Point(125,225),10)
    inEntry.draw(out)
    sol=Text(Point(290,175),'obtain 1 U L 1100');
    sol.draw(out)
    rect=Rectangle(Point(248,331), Point(383,373))
    rect.setOutline('black')
    rect.setWidth(3)
    rect.draw(out)
    flowerImage = Image(Point(320,350), "submit.png")
    flowerImage.draw(out)
    flowerImage = Image(Point(120,350), "exit.png")
    flowerImage.draw(out)
    recta=Rectangle(Point(38,320), Point(202,378))
    recta.setOutline('black')
    recta.setWidth(3)
    recta.draw(out)
    while True:
        mouse=out.getMouse()
        if rect.p1.x<mouse.x<rect.p2.x and rect.p1.y<mouse.y<rect.p2.y :
            break
        if recta.p1.x<mouse.x<recta.p2.x and recta.p1.y<mouse.y<recta.p2.y :
            out.close()
            return 0
    
    text = inEntry.getText()
    if(len(text)!=4 or text.isdigit()!=1):
        testText = Text(Point(250,280),'invalid entry')
        testText.draw(out)
        time.sleep(1)
        out.close()
        return -1
    w=str(int(text[0])**2)
    x=alpha[13+int(text[1])]
    y=alpha[13-int(text[2])]
    if((int(text[3])+3)<=3):
        z=bin(int(text[3])+3).replace("0b","00")
    elif((int(text[3])+3)<8):
        z=bin(int(text[3])+3).replace("0b","0")
    else:
        z=bin(int(text[3])+3).replace("0b","")
    outentry = Entry(Point(290,225),10)
    outentry.setText(w+" "+x+" "+y+" "+z)
    outentry.draw(out)
    if(int(text)==1729):
        testText = Text(Point(200,280),'CONGRATS TO FIND THE RAMANUJAN NUMBER')
        testText.setStyle('bold')
        testText.setTextColor('RED')
        testText.draw(out)
        time.sleep(1)
        out.close()
        return 1
    time.sleep(3)
    out.close()

def main():    
    win = GraphWin("Enigma", 600, 600)
    win.setBackground("yellow")
    s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key="LOGIC"
    lab = Text(Point(300,50),'FIND THE HIDDEN WORD')
    lab.draw(win)
    for i in range(0,len(key)):
        p=random.randrange(0,5)
        for j in range(0,p):
            label = Text(Point(300, 300),s[random.randrange(0,25)])
            u=['red','black']
            label.setTextColor(u[random.randrange(0,2)])
            label.setStyle('bold')
            label.setSize(30)
            label.draw(win)
            time.sleep(2)
            label.undraw()
        label = Text(Point(300, 300),key[i])
        label.setTextColor('green')
        label.setStyle('bold')
        label.setSize(30)
        label.draw(win)
        time.sleep(1)
        label.undraw()
    textEntry = Entry(Point(233,200),50)
    textEntry.draw(win)
    rect=Rectangle(Point(380,331), Point(513,373))
    rect.setOutline('black')
    rect.setWidth(3)
    rect.draw(win)
    flowerImage = Image(Point(450,350), "submit.png")
    flowerImage.draw(win)
    flowerImage = Image(Point(120,350), "exit.png")
    flowerImage.draw(win)
    recta=Rectangle(Point(38,320), Point(202,378))
    recta.setOutline('black')
    recta.setWidth(3)
    recta.draw(win)
    while True:
        mouse=win.getMouse()
        if rect.p1.x<mouse.x<rect.p2.x and rect.p1.y<mouse.y<rect.p2.y :
            break
        if recta.p1.x<mouse.x<recta.p2.x and recta.p1.y<mouse.y<recta.p2.y :
            win.close()
            return 0
    text = textEntry.getText()
    if(text=='LOGIC'):
        testText = Text(Point(350,500),'CONGRATS')
        testText.setStyle('bold')
        testText.draw(win)
        time.sleep(2)
        win.close()
        return 1
        
    else:
        testText = Text(Point(350,500),'TRY AGAIN')
        testText.setStyle('bold')
        testText.draw(win)
        time.sleep(2)
        win.close()
        return -1
def timer():
    win = GraphWin("timer", 200, 200)
    win.setBackground("white")
    c=Circle(Point(100,100),50)
    c.setFill(color_rgb(255, 0, 0))
    c.draw(win)
    for i in range(0,20):
        label = Text(Point(100, 100),str(i))
        label.setStyle('bold')
        label.setSize(30)
        label.draw(win)
        if(i%3==0):
            stat=open("status.txt","r")
            val=stat.read()
            if(val=='1'):  #check if soduku is quited properly and stop timer
                break
            if(val=='3'):
                break
            stat.close()
        time.sleep(1)
        label.undraw()
    stat=open("status.txt","w")
    stat.write("1")
    stat.close()
    win.close()
def sodoku(a,o,score):
    win = GraphWin("sudoku", 1200, 700)
    win.setBackground("white")
    p=650
    message=Text(Point(340,10),"sudoku")
    message.draw(win)
    for i in range(0,6):   #creating table
        rect=Rectangle(Point(50,50), Point(p,650))
        if(i==3):
            rect.setOutline("red")
        rect.draw(win)
        
        rect.setWidth(3)
        rect=Rectangle(Point(50,50), Point(650,p))
        if(i%2==0):
            rect.setOutline("red")
        rect.setWidth(3)
        rect.draw(win)
        p=p-100
    rect=Rectangle(Point(50,50), Point(650,650))
    rect.setWidth(3)
    rect.draw(win)  #end of table
    q=[]
    s=[]
    if(a==1):
        q=[2,3,5,6,1,4,1,4,6,5,2,3,6,1,2,4,3,5,3,5,4,2,6,1,5,2,3,1,4,6,4,6,1,3,5,2]
        s=[3,5,6,1,1,3,2,3,5,4,2,6,5,2,4,6,6,1,3,5]
        print(len(s))
    elif(a==2):
        q=[5,3,1,2,6,4,2,4,6,1,5,3,1,6,3,5,4,2,4,5,2,3,1,6,3,1,4,6,2,5,2,6,5,4,3,1]
        s=[3,1,2,6,2,3,3,4,5,2,3,1,3,1,2,5,6,5,4,3]
        print(len(s))
    elif(a==3):
        q=[1,2,3,4,5,6,3,6,2,5,1,4,4,3,6,2,5,1,2,5,4,1,3,6,6,1,5,3,4,2,5,4,1,6,2,3]
        s=[2,3,4,5,3,4,6,5,5,4,1,3,6,1,4,2,4,1,6,2]
    elif(a==4):
        q=[5,2,4,6,1,3,1,3,6,4,5,2,2,6,1,5,3,4,3,4,5,2,6,1,6,1,2,3,4,5,4,5,3,1,2,6]
        s=[2,4,6,1,1,2,1,3,4,5,2,6,6,1,4,5,5,3,1,2]
    pos=[0,5,7,8,9,10,12,13,15,17,18,23,26,27,30,35]
    message=Text(Point(100,100),str(q[pos[0]]))
    message.setSize(30)
    message.draw(win)
    message=Text(Point(100*6,100),str(q[pos[1]]))
    message.setSize(30)
    message.draw(win)
    message=Text(Point(100*2,100*2),str(q[pos[2]]))
    message.setSize(30)
    message.draw(win)        
    message=Text(Point(100*3,100*2),str(q[pos[3]]))
    message.setSize(30)
    message.draw(win)
    message=Text(Point(100*4,100*2),str(q[pos[4]]))
    message.setSize(30)
    message.draw(win)
    message=Text(Point(100*5,100*2),str(q[pos[5]]))
    message.setSize(30)
    message.draw(win)
    message=Text(Point(100,100*3),str(q[pos[6]]))
    message.setSize(30)
    message.draw(win)
    message=Text(Point(100*2,100*3),str(q[pos[7]]))
    message.setSize(30)
    message.draw(win)
    message=Text(Point(100*4,100*3),str(q[pos[8]]))
    message.setSize(30)
    message.draw(win)
    message=Text(Point(100*6,100*3),str(q[pos[9]]))
    message.setSize(30)
    message.draw(win)
    message=Text(Point(100*1,100*4),str(q[pos[10]]))
    message.setSize(30)
    message.draw(win)
    message=Text(Point(100*6,100*4),str(q[pos[11]]))
    message.setSize(30)
    message.draw(win)
    message=Text(Point(100*3,100*5),str(q[pos[12]]))
    message.setSize(30)
    message.draw(win)
    message=Text(Point(100*4,100*5),str(q[pos[13]]))
    message.setSize(30)
    message.draw(win)
    message=Text(Point(100*1,100*6),str(q[pos[14]]))
    message.setSize(30)
    message.draw(win)
    message=Text(Point(100*6,100*6),str(q[pos[15]]))
    message.setSize(30)
    message.draw(win)
    textEntry1 = Entry(Point(100*2,100),2)
    textEntry1.setSize(27)
    textEntry1.draw(win)
    textEntry2= Entry(Point(100*3,100),2)
    textEntry2.setSize(27)
    textEntry2.draw(win)
    textEntry3 = Entry(Point(100*4,100),2)
    textEntry3.setSize(27)
    textEntry3.draw(win)
    textEntry4 = Entry(Point(100*5,100),2)
    textEntry4.setSize(27)
    textEntry4.draw(win)
    textEntry5 = Entry(Point(100*1,100*2),2)
    textEntry5.setSize(27)
    textEntry5.draw(win)
    textEntry6 = Entry(Point(100*6,100*2),2)
    textEntry6.setSize(27)
    textEntry6.draw(win)
    textEntry7 = Entry(Point(100*3,100*3),2)
    textEntry7.setSize(27)
    textEntry7.draw(win)
    textEntry8 = Entry(Point(100*5,100*3),2)
    textEntry8.setSize(27)
    textEntry8.draw(win)
    textEntry9 = Entry(Point(100*2,100*4),2)
    textEntry9.setSize(27)
    textEntry9.draw(win)
    textEntry10= Entry(Point(100*3,100*4),2)
    textEntry10.setSize(27)
    textEntry10.draw(win)
    textEntry11 = Entry(Point(100*4,100*4),2)
    textEntry11.setSize(27)
    textEntry11.draw(win)
    textEntry12 = Entry(Point(100*5,100*4),2)
    textEntry12.setSize(27)
    textEntry12.draw(win)
    textEntry13= Entry(Point(100*1,100*5),2)
    textEntry13.setSize(27)
    textEntry13.draw(win)
    textEntry14= Entry(Point(100*2,100*5),2)
    textEntry14.setSize(27)
    textEntry14.draw(win)
    textEntry15 = Entry(Point(100*5,100*5),2)
    textEntry15.setSize(27)
    textEntry15.draw(win)
    textEntry16 = Entry(Point(100*6,100*5),2)
    textEntry16.setSize(27)
    textEntry16.draw(win)
    textEntry17 = Entry(Point(100*2,100*6),2)
    textEntry17.setSize(27)
    textEntry17.draw(win)
    textEntry18 = Entry(Point(100*3,100*6),2)
    textEntry18.setSize(27)
    textEntry18.draw(win)
    textEntry19 = Entry(Point(100*4,100*6),2)
    textEntry19.setSize(27)
    textEntry19.draw(win)
    textEntry20 = Entry(Point(100*5,100*6),2)
    textEntry20.setSize(27)
    textEntry20.draw(win)
    rect=Rectangle(Point(882,331), Point(1013,373))
    rect.setOutline('black')
    rect.setWidth(3)
    rect.draw(win)
    flowerImage = Image(Point(950,350), "submit.png")
    flowerImage.draw(win)
    flowerImage = Image(Point(120,350), "exit.png")
    flowerImage.draw(win)
    recta=Rectangle(Point(38,320), Point(202,378))
    recta.setOutline('black')
    recta.setWidth(3)
    recta.draw(win)
    while True:
        mouse=win.getMouse()
        if rect.p1.x<mouse.x<rect.p2.x and rect.p1.y<mouse.y<rect.p2.y :
            break
        if recta.p1.x<mouse.x<recta.p2.x and recta.p1.y<mouse.y<recta.p2.y :
            win.close()
            return 0
    v=[]
    v.append(textEntry1.getText())
    v.append(textEntry2.getText())
    v.append(textEntry3.getText())
    v.append(textEntry4.getText())
    v.append(textEntry5.getText())
    v.append(textEntry6.getText())
    v.append(textEntry7.getText())
    v.append(textEntry8.getText())
    v.append(textEntry9.getText())
    v.append(textEntry10.getText())
    v.append(textEntry11.getText())
    v.append(textEntry12.getText())
    v.append(textEntry13.getText())
    v.append(textEntry14.getText())
    v.append(textEntry15.getText())
    v.append(textEntry16.getText())
    v.append(textEntry17.getText())
    v.append(textEntry18.getText())
    v.append(textEntry19.getText())
    v.append(textEntry20.getText())
    point=0
    for i in range(0,20):
        if(v[i].isdigit()!=1):
            continue
        elif(int(v[i])==s[i]):
            point=point+1
    message=Text(Point(100*9,500),'POINTS SCORED : '+str(point*5)+'\n chance left: '+str(2-o))
    message.setSize(30)
    point=point*5
    message.setTextColor("green")
    message.draw(win)
    time.sleep(1.7)
    win.close()
    if point>=score:
        return point
    else:
        return score
while(1):
    password=GraphWin("secure", 400, 200)
    password.setBackground("black")
    p3=Text(Point(180,40),'PASSWORD')
    p3.setSize(15)
    p3.setTextColor("white")
    p3.draw(password)
    t1 = Entry(Point(180,100),15)
    t1.setSize(15)
    t1.draw(password)
    password.getMouse()
    stat=open("status.txt","w")
    stat.write('0')#writing status to 0
    stat.close()
    if(t1.getText()=='locker'):
        password.close()
        file1=open("level1.txt","w")
        file2=open("level2.txt","w")
        file3=open("level3.txt","w")
        file1.write('0')
        file2.write('0')
        file3.write('0')
        file1.close()
        file2.close()
        file3.close()
        temp=open("temp.txt","w")
        temp.write('0')
        temp.close()
        break
    elif(t1.getText()=='continue'):
        password.close()
        file1=open("level1.txt","r")
        temp=open("temp.txt","w")
        temp.write(file1.read())
        temp.close()
        file1.close()
        break
    else:
        password.close()
file1=open("level1.txt","r")
file2=open("level2.txt","r")
file3=open("level3.txt","r")
stat=open("status.txt","w")
stat.write('0')#writing status to 0
stat.close()
menu= GraphWin("main menu", 600, 600)
flowerImag = Image(Point(300,80), "enigma.png")
flowerImag.draw(menu)
flowerImag = Image(Point(300,240), "level1.png")
flowerImag.draw(menu)
flowerImag = Image(Point(300,360), "level2.png")
flowerImag.draw(menu)
flowerImag = Image(Point(300,480), "level3.png")
flowerImag.draw(menu)
rect1=Rectangle(Point(199,206), Point(401,279))
rect1.setOutline('black')
rect1.draw(menu)
p1=Text(Point(500,243),file1.read()+'/100')
p1.setSize(30)
p1.draw(menu)
rect2=Rectangle(Point(200,325), Point(400,396))
rect2.setOutline('black')
rect2.draw(menu)
p2=Text(Point(500,357),file2.read()+'/50')
p2.setSize(30)
p2.draw(menu)
rect3=Rectangle(Point(201,446), Point(401,518))
rect3.setOutline('black')
rect3.draw(menu)
p3=Text(Point(500,490),file3.read()+'/100')
p3.setSize(30)
p3.draw(menu)
score=0
while(1):
    mouse=menu.getMouse()
    if rect1.p1.x<mouse.x<rect1.p2.x and rect1.p1.y<mouse.y<rect1.p2.y :
        stat=open("status.txt","w")
        stat.write('0')#writing status to 0
        stat.close()
        j=Popen("timer.py",shell=True)
        timer()
        file1=open("level1.txt","w")
        temp=open("temp.txt","r")
        lo=temp.read()
        file1.write(lo)
        temp.close()
        file1.close()
        file1=open("level1.txt","r")
        p1.undraw()
        p1=Text(Point(500,243),file1.read()+'/100')
        p1.setSize(30)
        p1.draw(menu)
        file1.close()   
    if rect2.p1.x<mouse.x<rect2.p2.x and rect2.p1.y<mouse.y<rect2.p2.y :
        while(1):
            l=main()
            if(l==1):
                p2.undraw()
                p2=Text(Point(500,357),'50/50')
                file2=open("level2.txt","w")
                file2.write('50')
                file2.close()
                p2.setSize(30)
                p2.draw(menu)
                score=score+20
                break
            if(l==0):
                break
    
    if rect3.p1.x<mouse.x<rect3.p2.x and rect3.p1.y<mouse.y<rect3.p2.y :
        while(1):
            l=second()
            if(l==1):
                p3.undraw()
                p3=Text(Point(500,490),'100/100')
                p3.setSize(30)
                p3.draw(menu)
                file3=open("level3.txt","w")
                file3.write('100')
                file3.close()
                break
            if(l==0):
                break
