import os
import time
Q=10
Q=Q+1
class Per:
    def __init__(self,D,x,y):
        self.D=D
        self.x=x
        self.y=y
        self.mov=[]
        if D=='N':
            for i in range(y,-1,-1):
                aux=[x,i]
                self.mov.append(aux)

        if D=='S':
            for i in range(y,Q):
                aux=[x,i]
                self.mov.append(aux)
        if D=='W':
            for i in range(x,-1,-1):
                aux=[i,y]
                self.mov.append(aux)
        if D=='E':
            for i in range(x,Q):
                aux=[i,y]
                self.mov.append(aux)


    def getMov(self):
        return self.mov


def run():
    mapa=[]

    for i in range(Q):
        row=[]
        for j in range(Q):
            row.append(0)
        mapa.append(row)

    entrada=[]
    entrada.append(Per('S',2,4))
    entrada.append(Per('N',2,6))
    entrada.append(Per('E',1,5))
    entrada.append(Per('W',3,5))
    mayor=-99999
    output=[0,0]
    for i in entrada:
        for j in i.getMov():
            mapa[j[1]][j[0]]=mapa[j[1]][j[0]]+1
            if mapa[j[1]][j[0]]>mayor:

            time.sleep(1)
            mos_map(mapa)






def mos_map(mapa):
    os.system('cls')
    for i in range(0,Q):
        for j in range(0,Q):
            if mapa[i][j]!=0:
                print(" {} ".format(mapa[i][j]),end="")
            if mapa[i][j]==0:
                print(" # ",end="")
        print()

if __name__ == '__main__':
    run()
