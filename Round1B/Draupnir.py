import sys
import random
import time
import os
T=0
W=6

class Days:
    def __init__(self):
        self.max=0
        self.opciones=[]
        self.per=[]

    def setMax(self,max):
        self.max=max
        self.permu()

    def getMax(self):
        return self.max

    def getOpciones(self):
        return self.opciones

    def permu(self):
        cont=0
        aux=[]
        maximo=0
        maxim=[0,0,0,0,0,0]
        nueves=0
        decimal=0
        minim=0
        num=round(self.max/9,1)
        nueves=int(num)
        for i in range(nueves):
            maxim[i]=9
            minim=minim+9*10**i
        y=num-nueves
        if y>0:
            y=round(y*10)
            maxim[nueves]=int(y)
            minim=minim+int(y)*10**maxim.count(9)
        k=0
        for i in maxim:
            maximo=maximo+i*10**(5-k)
            k=k+1

        for j in range(minim,maximo//10):
            var=self.sume_dig(i)
            if var==self.max:
                self.opciones.append(i)
        rango=self.max
        for i in range(100000,maximo):
            var=self.sume_dig(i)
            if var<rango and var>(rango//2)+(rango//4) :
                self.opciones.append(i)


    def sume_dig2(self,num):
        a=num//100000
        num=num-a*(10**5)
        b=num//10000
        num=num-b*(10**4)
        c=num//1000
        num=num-c*(10**3)
        d=num//100
        num=num-d*(10**2)
        e=num//10
        num=num-e*(10**1)
        f=num
        return ([a,b,c,d,e,f])

    def sume_dig(self,num):
        a=num//100000
        num=num-a*(10**5)
        b=num//10000
        num=num-b*(10**4)
        c=num//1000
        num=num-c*(10**3)
        d=num//100
        num=num-d*(10**2)
        e=num//10
        num=num-e*(10**1)
        f=num
        return (a+b+c+d+e+f)


def sumatoria(auxi):
    sum=0
    for i in range(len(auxi)):
        sum=sum+auxi[i]
    return sum

def run():
    day=1
    intentos=[]
    sys.stdout.flush()
    entrada=int(input())
    obj=Days()
    obj.setMax(entrada)
    intentos.append(obj.getOpciones())
    intentos.append(eliminar(intentos[-1],day,entrada))
    for i in range(2,W+1):
        day=random.randint(2,500)
        print(day)
        sys.stdout.flush()
        entrada=int(input())
        intentos.append(eliminar(intentos[-1],day,entrada))
        if len(intentos[-1])==1:
            break

    a=intentos[-1]
    b=str(a)
    output=list(b)
    print(" ".join(output))



def eliminar(aux,dia,entrada):
    auxi=[]
    for i in aux:
        if func_piso(i,dia)==entrada:
            auxi.append(i)
    return auxi


def func_piso(num,i):
    sum=0
    a=num//100000
    num=num-a*(10**5)
    b=num//10000
    num=num-b*(10**4)
    c=num//1000
    num=num-c*(10**3)
    d=num//100
    num=num-d*(10**2)
    e=num//10
    num=num-e*(10**1)
    f=num
    #for j in l:
    #    sum=sum+j*2**(i//k)
    #    k=k+1
    #return sum
    salida=a*2**i+b*2**(i//2)+c*2**(i//3)+d*2**(i//4)+e*2**(i//5)+f*2**(i//6)
    return salida




def coeficientes(i):
    salida=[]
    for k in range(6):
        salida.append(2**(i//(k+1)))
    return salida

T, W = map(int, input().split())

for _ in range(T):
    run()
