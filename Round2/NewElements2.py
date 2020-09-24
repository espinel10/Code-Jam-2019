import sys
import random

class molecula:
    def __init__(self,mol):
        self.mol=mol
        f1=lambda x,y:x*12+y*30
        f2=lambda x,y:x*100+y*5
        self.a=f1(mol[0],mol[1])
        self.b=f2(mol[0],mol[1])
    def getMol(self):
        return self.mol

    def getA(self):
        return self.a

    def getB(self):
        return self.b

class moles:
    def __init__(self,lista):
        self.lista=lista
        self.sum=0
        self.opciones=[]
        auxi=lista[:]
        k=0
        self.permutoA(auxi,k,[])
        self.permutoB(auxi,k,[])

    def permutoB(self,entra,K,salida):
        aux=entra[:]
        steps=salida[:]
        if len(aux)==0:
            if self.opciones.count(salida)==0:
                self.opciones.append(salida)
                self.sum=self.sum+1
            return
        for i in aux:
            aux2=aux[:]
            var=i.getB()
            aux2.remove(i)
            step1=steps[:]
            step1.append([i.getMol()[0],i.getMol()[1]])
            if K<var:
                self.permutoB(aux2,var,step1)


    def permutoA(self,entra,K,salida):
        aux=entra[:]
        steps=salida[:]
        if len(aux)==0:
            if self.opciones.count(salida)==0:
                self.opciones.append(salida)
                self.sum=self.sum+1
            return
        for i in aux:
            aux2=aux[:]
            var=i.getA()
            aux2.remove(i)
            step1=steps[:]
            step1.append([i.getMol()[0],i.getMol()[1]])
            if K<var:
                self.permutoA(aux2,var,step1)

    def show(self,t):
        print("Case #{}: {}".format(t+1,self.sum))


def run(entrada,t):
    lista=[]
    for i in entrada:
        obj=molecula(i)
        lista.append(obj)
    obj=moles(lista)
    obj.show(t)




T=int(input())
for _ in range(T):
    n=int(input())
    entrada=[]
    for i in range(n):
        a,b=map(int, input().split())
        entrada.append([a,b])
    run(entrada,_)
