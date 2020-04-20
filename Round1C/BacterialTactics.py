import random
import os
import time
from copy import copy
B=[2,3]
T=[4,5]
winB=0
class Mapa:
    pass
    def __init__(self,mapa,R,C):
         self.mapa=mapa
         self.R=R
         self.C=C
         self.win=''
    def getWin(self):
        return self.win
    def reiniciar(self,menos):
        ##menos es los que no voy a eliminar
        R=self.R
        C=self.C
        for j in range(0,R):
            for i in range(0,C):
                if self.mapa[j][i]!=1 and menos.count([j,i])==1:
                    self.mapa[j][i]=0
    def increment(self):
        R=self.R
        C=self.C
        for j in range(0,R):
            for i in range(0,C):
                if (i>0 and i<C-1) and (j>0 and j<R-1):
                    if self.mapa[j][i]==2 and self.mapa[j][i-1]==1:
                        self.win='T'
                        return
                    if self.mapa[j][i]==2 and self.mapa[j][i+1]==1:
                        self.win='T'
                        return
                    if self.mapa[j][i]==4 and self.mapa[j][i-1]==1:
                        self.win='B'
                        return
                    if self.mapa[j][i]==4 and self.mapa[j][i+1]==1:
                        self.win='B'
                        return
                    if self.mapa[j][i]==3 and self.mapa[j+1][i]==1:
                        self.win='T'
                        return
                    if self.mapa[j][i]==3 and self.mapa[j-1][i]==1:
                        self.win='T'
                        return
                    if self.mapa[j][i]==5 and self.mapa[j+1][i]==1:
                        self.win='B'
                        return
                    if self.mapa[j][i]==5 and self.mapa[j-1][i]==1:
                        self.win='B'
                        return
                    if self.mapa[j][i]==2 and self.mapa[j][i-1]==0:
                        self.mapa[j][i-1]=2
                        break
                    if self.mapa[j][i]==2 and self.mapa[j][i+1]==0:
                        self.mapa[j][i+1]=2
                        break
                    if self.mapa[j][i]==4 and self.mapa[j][i-1]==0:
                        self.mapa[j][i-1]=4
                        break
                    if self.mapa[j][i]==4 and self.mapa[j][i+1]==0:
                        self.mapa[j][i+1]=4
                        break
                    if self.mapa[j][i]==3 and self.mapa[j+1][i]==0:
                        self.mapa[j+1][i]=3
                        break
                    if self.mapa[j][i]==3 and self.mapa[j-1][i]==0:
                        self.mapa[j-1][i]=3
                        break
                    if self.mapa[j][i]==5 and self.mapa[j+1][i]==0:
                        self.mapa[j+1][i]=5
                        break
                    if self.mapa[j][i]==5 and self.mapa[j-1][i]==0:
                        self.mapa[j-1][i]=5
                        break
                else:
                    if self.mapa[j][i]==2 or self.mapa[j][i]==4:
                        if i==0:
                            if self.mapa[j][i]==2 and self.mapa[j][i+1]==1:
                                self.win='T'
                                return
                            if self.mapa[j][i]==4 and self.mapa[j][i+1]==1:
                                self.win='B'
                                return
                            if self.mapa[j][i]==2 and self.mapa[j][i+1]==0:
                                self.mapa[j][i+1]=2
                                break
                            if self.mapa[j][i]==4 and self.mapa[j][i+1]==0:
                                self.mapa[j][i+1]=4
                                break
                        else:
                            if i==C-1:
                                if self.mapa[j][i]==2 and self.mapa[j][i-1]==1:
                                    self.win='T'
                                    return
                                if self.mapa[j][i]==4 and self.mapa[j][i-1]==1:
                                    self.win='B'
                                    return
                                if self.mapa[j][i]==2 and self.mapa[j][i-1]==0:
                                    self.mapa[j][i-1]=2
                                    break
                                if self.mapa[j][i]==4 and self.mapa[j][i-1]==0:
                                    self.mapa[j][i-1]=4
                                    break
                            else:
                                if self.mapa[j][i]==2 and self.mapa[j][i+1]==1:
                                    self.win='T'
                                    return
                                if self.mapa[j][i]==4 and self.mapa[j][i+1]==1:
                                    self.win='B'
                                    return
                                if self.mapa[j][i]==2 and self.mapa[j][i-1]==1:
                                    self.win='T'
                                    return
                                if self.mapa[j][i]==4 and self.mapa[j][i-1]==1:
                                    self.win='B'
                                    return
                                if self.mapa[j][i]==2 and self.mapa[j][i+1]==0:
                                    self.mapa[j][i+1]=2
                                    break
                                if self.mapa[j][i]==4 and self.mapa[j][i+1]==0:
                                    self.mapa[j][i+1]=4
                                    break
                                if self.mapa[j][i]==2 and self.mapa[j][i-1]==0:
                                    self.mapa[j][i-1]=2
                                    break
                                if self.mapa[j][i]==4 and self.mapa[j][i-1]==0:
                                    self.mapa[j][i-1]=4
                                    break



                    if self.mapa[j][i]==3 or self.mapa[j][i]==5:
                        if j==0:
                            if self.mapa[j][i]==3 and self.mapa[j+1][i]==1:
                                self.win='T'
                                return
                            if self.mapa[j][i]==5 and self.mapa[j+1][i]==1:
                                self.win='B'
                                return
                            if self.mapa[j][i]==3 and self.mapa[j+1][i]==0:
                                self.mapa[j+1][i]=3
                                break
                            if self.mapa[j][i]==5 and self.mapa[j+1][i]==0:
                                self.mapa[j+1][i]=5
                                break
                        else:
                            if j==R-1:
                                if self.mapa[j][i]==3 and self.mapa[j-1][i]==1:
                                    self.win='T'
                                    return
                                if self.mapa[j][i]==5 and self.mapa[j-1][i]==1:
                                    self.win='B'
                                    break
                                if self.mapa[j][i]==3 and self.mapa[j-1][i]==0:
                                    self.mapa[j-1][i]=3
                                    break
                                if self.mapa[j][i]==5 and self.mapa[j-1][i]==0:
                                    self.mapa[j-1][i]=5
                                    break
                            else:
                                if self.mapa[j][i]==3 and self.mapa[j-1][i]==1:
                                    self.win='T'
                                    return
                                if self.mapa[j][i]==5 and self.mapa[j-1][i]==1:
                                    self.win='B'
                                    break
                                if self.mapa[j][i]==3 and self.mapa[j-1][i]==1:
                                    self.win='T'
                                    return
                                if self.mapa[j][i]==5 and self.mapa[j-1][i]==1:
                                    self.win='B'
                                    break
                                if self.mapa[j][i]==3 and self.mapa[j-1][i]==0:
                                    self.mapa[j-1][i]=3
                                    break
                                if self.mapa[j][i]==5 and self.mapa[j-1][i]==0:
                                    self.mapa[j-1][i]=5
                                    break
                                if self.mapa[j][i]==3 and self.mapa[j-1][i]==0:
                                    self.mapa[j-1][i]=3
                                    break
                                if self.mapa[j][i]==5 and self.mapa[j-1][i]==0:
                                    self.mapa[j-1][i]=5
                                    break
    def set_Bact(self,y,x,value):
        valores=self.get_mov()
        cont=0
        for linea in valores:
            if x==linea[1] and y==linea[0]:
                cont=1
                break
        if cont==1:
            self.mapa[y][x]=value
    def get_mov(self):
        C=self.C
        R=self.R
        mov=[]
        for j in range(0,R):
            for i in range(0,C):
                if self.mapa[j][i]==0:
                    aux=[j,i]
                    mov.append(aux)
        return mov
    def getMapa(self):
        return self.mapa
    def mostrar(self):
        time.sleep(1)
        os.system('cls')
        mapa=self.mapa
        R=self.R
        C=self.C
        for j in range(0,R):
            for i in range(0,C):
                if mapa[j][i]==0:
                    print(" . ",end="")
                if mapa[j][i]==1:
                    print(" # ",end="")
                if mapa[j][i]==3 or mapa[j][i]==2:
                    print(" B ",end="")
                if mapa[j][i]==5 or mapa[j][i]==4:
                    print(" T ",end="")
            print()


class Game:
    winB=0
    primerWin=[]
    def getWinB(self):
        return self.winB

    def getPrimerWin(self):
        return self.primerWin

    def juego(self,mapa2,cont,pasos):
        steps=copy(pasos)
        mapa=copy(mapa2)
        mapa.increment()
        cont=cont+1
        
        if mapa.getWin()!='':
            if mapa.getWin()=='B':
                if self.primerWin.count(steps[0])==0:
                    self.winB=self.winB+1
                    self.primerWin.append(steps[0])
                return
        if len(mapa.get_mov())==0:
            if cont%2!=0 and self.primerWin.count(steps[0])==0:
                self.winB=self.winB+1
                self.primerWin.append(steps[0])
            return
        if cont%2==0:
            mov=mapa.get_mov()
            for iter in mov:
                for orientacion in B:
                    if cont==2:
                        steps[0]=[iter[0],iter[1],orientacion]
                    mapa.set_Bact(iter[0],iter[1],orientacion)
                    self.juego(mapa,cont,steps)
                    mapa.reiniciar(mov)
        else:
            mov=mapa.get_mov()
            for iter in mov:
                for orientacion in T:
                    mapa.set_Bact(iter[0],iter[1],orientacion)
                    self.juego(mapa,cont,steps)
                    mapa.reiniciar(mov)




def run():
    C=4
    R=3
    mapa=[[1,0,1,1],[0,0,0,0],[1,0,1,1]]
    #C=2
    #R=2
    #mapa=[[0,0],[0,1]]
    m=Mapa(mapa,R,C)
    cont=1
    obj=Game()
    pasos=[[]]
    obj.juego(m,cont,pasos)
    print(obj.winB)
    print(obj.getPrimerWin())





if __name__ == '__main__':
    run()
