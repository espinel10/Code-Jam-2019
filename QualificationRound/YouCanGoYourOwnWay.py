import os
import time
import random
class Mov:
    def __init__(self):
        self.mov=None
        self.dx=None
        self.dy=None
    def setDx(self,dx):
         self.dx=dx
    def getDx(self):
        return self.dx
    def setDy(self,dy):
         self.dy=dy
    def getDy(self):
        return self.dy

    def getPoint():
        point=[]
        point.append(self.x)
        point.append(self.y)
        return point


    def setMov(self, mov):
        self.mov = mov
    def getMov(self):
        return self.mov
##########################################
def mov_pro(mapa,n):
    os.system('cls')
    for i in range(0,n):
        for j in range(0,n):
            if mapa[j][i]==0:
                print(" # ",end="")
            if mapa[j][i]==1:
                print(" X ",end="")
            if mapa[j][i]==2:
                print(" O ",end="")

        print()
####################################################
def run():
    n=5
    list=['E','E','S','S','S','E','S','E']
    mapa=[]
    for i in range(0,n+1):
        aux=[]
        for j in range(0,n+1):
            aux.append(0)
        mapa.append(aux)
    lydia=[]
    x=0
    y=0
    interval=(2*n)-2
    for i in range(0,interval):
        mov=list[i]
        obj=Mov()
        obj.setMov(mov)
        obj.setDx(x)
        obj.setDy(y)
        lydia.append(obj)
        if mov=='E':
            mapa[x][y]=0
            x=x+1
            mapa[x][y]=1
        if mov=='S':
            mapa[x][y]=0
            y=y+1
            mapa[x][y]=1



    mapa[x][y]=0
    x=0
    y=0
    bandera=0
    output2=[]
    while bandera==0:
        output1=[]
        for i in range(0,interval):
            mov='p'
            k=dev_pos(x,y,lydia)
            if k==99:
                mov=m_alea(None)
            else:
                mov=m_alea(lydia[k])
            output1.append(mov)
            if mov=='E':
                mapa[x][y]=0
                x=x+1
                mapa[x][y]=1
            if mov=='S':
                mapa[x][y]=0
                y=y+1
                mapa[x][y]=1
            mov_pro(mapa,n)
            print(list)
            time.sleep(1)
        if x==(n-1) and y==(n-1):
            bandera=1
            output2=output1
        else:
            mapa[x][y]=0
            x=0
            y=0
    print("#########################################################")
    print(list)
    print(output2)
#####################################################
def dev_pos(x,y,list):
    bandera=0
    i=0
    while bandera==0:
        if list[i].getDx()==x and list[i].getDy()==y:
            bandera=1
        else:
            if i==len(list)-1:
                bandera=1
                i=99
            else:
                i=i+1
    return i
#######################################################
def m_alea(obj):
    mov='p'
    if obj:
        if obj.getMov()=='E':
            mov='S'
        if obj.getMov()=='S':
            mov='E'
    else:
        s=random.randint(0, 1)
        if s==0:
            mov='E'
        else:
            mov='S'
    return mov

if __name__ == '__main__':
    run()
