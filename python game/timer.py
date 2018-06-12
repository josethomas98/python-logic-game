from graphics import *
import time
import subprocess as sp
import random
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
    flowerImage = Image(Point(950,550), "exit.png")
    flowerImage.draw(win)
    recta=Rectangle(Point(870,522), Point(1030,575))
    recta.setOutline('black')
    recta.setWidth(3)
    recta.draw(win)
    while True:
        stat=open("status.txt","r")
        l=stat.read()
        if(l=="1"):
            win.close()
            stat.close()
            return -1
        stat.close()
        mouse=win.getMouse()
        if rect.p1.x<mouse.x<rect.p2.x and rect.p1.y<mouse.y<rect.p2.y :
            break
        if recta.p1.x<mouse.x<recta.p2.x and recta.p1.y<mouse.y<recta.p2.y :
            win.close()
            return -1
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
    message=Text(Point(100*9,450),'POINTS SCORED : '+str(point*5)+'\n chance left: '+str(2-o))
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
i=random.randrange(1,5)
score=0
while(1):
    for u in range(0,3):
        score=sodoku(i,u,score)
        if(score==-1):
            stat=open("status.txt","w")
            stat.write("1")
            stat.close()
            break
        temp1=open("temp.txt","r")
        if(score>int(temp1.read())):
            temp=open("temp.txt","w")
            temp.write(str(score))
            temp.close()
        temp1.close()
        if(score==100):
            stat=open("status.txt","w")
            stat.write("3")
            stat.close()
            break
    if(score==-1):
        break
    i=i+1
    if(i>4):
        i=random.randrange(0,5)
    if(score==100):
        break
