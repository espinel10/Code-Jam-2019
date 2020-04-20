import sys
import random
import time
import math
W=0
class SistemaEcuaciones:
    def __init__(self):
        self.Ecua=[]
        self.Respuestas=[]
        self.salida=[]

    def getRespuestas(self):
        #return " ".join(map(str,self.salida))
        return self.Respuestas

    def getSalida(self):
        return " ".join(map(str,self.salida))



    def setEcua(self,sist):
        for ecua in sist:
            if len(ecua)==6:
                menor=ecua[5]
                for i in range(6):
                    ecua[i]=ecua[i]//menor
            if len(ecua)==7:
                menor=ecua[5]
                for i in range(7):
                    ecua[i]=ecua[i]//menor

        self.Respuestas.append(sist[0])
        self.Ecua=sist
        self.hallar()


    def mostrar(self):
        for j in self.Ecua:
            print(j)

    def hallar(self):
        sist=self.Ecua
        band=0
        cont=7
        matris=[]

        for iter in range(2):
            combina=[]
            for i in range(len(sist)):
                for j in range(i+1,len(sist)):
                    if len(sist[i])==len(sist[j]):
                        combina.append([i,j])
            aux=[]
            for k in combina:
                aux2=[]
                for j in range(0,len(sist[k[0]])):
                    aux2.append(abs(sist[k[0]][j]-sist[k[1]][j]))
                mayor=max(aux2)
                if len(aux2)==7:
                    if mayor==aux2[-1]:
                        aux.append(aux2)
                else:
                    if mayor==aux2[0]:
                        aux.append(aux2)

            for g in aux:
                if len(g)<2:
                    continue
                menor=min(g)
                if menor==0:
                    y=g[:]
                    while y.count(0)>0:
                        y.remove(0)
                    if len(y)>0:
                        menor=min(y)
                c=0
                if menor!=0:
                    for j in g:
                        if j%menor==0:
                            c=c+1
                    if c==len(g):
                        for j in range(0,len(g)):
                            g[j]=g[j]//menor

            for i in aux:
                if i.count(0)==1 and self.Respuestas.count(i)==0:
                    self.Respuestas.append(i)
                if i.count(0)==2 and self.Respuestas.count(i)==0:
                    self.Respuestas.append(i)
                if i.count(0)==3 and self.Respuestas.count(i)==0:
                    self.Respuestas.append(i)
                if i.count(0)==4 and self.Respuestas.count(i)==0:
                    self.Respuestas.append(i)
                if i.count(0)==5 and self.Respuestas.count(i)==0:
                    self.Respuestas.append(i)
            sist=aux


    def variables(self):
        salida=[0,0,0,0,0,0]
        aux=[]

        menor=None
        mayor=None
        for i in self.Respuestas:
            if mayor==None and i.count(0)==1 and i[-2]==0:
                mayor=i
            if i.count(0)==3:
                aux.append(i)
        for i in aux:
            if i.count(0)==3:
                if i[5]==0 and i[4]==0 and i[3]==0:
                    menor=i
        for i in range(100):
            for j in range(100):
                for z in range(100):
                    sum=i*menor[0]+j*menor[1]+z*menor[2]
                    if sum==menor[-1]:
                        salida[0]=i
                        salida[1]=j
                        salida[2]=z
                        break
        extra=salida[0]*mayor[0]+salida[1]*mayor[1]+salida[2]*mayor[2]
        for i in range(100):
            for j in range(100):
                sum=extra+i*mayor[3]+j*mayor[4]
                if sum==mayor[-1]:
                    salida[3]=i
                    salida[4]=j
        ecuacion=self.Ecua[0]
        extra=salida[0]*ecuacion[0]+salida[1]*ecuacion[1]+salida[2]*ecuacion[2]+salida[3]*ecuacion[3]+salida[4]*ecuacion[4]
        for i in range(100):
            sum=extra+i*ecuacion[5]
            if sum==ecuacion[-1]:
                salida[5]=i

        for i in salida:
            self.salida.append(i)



    def sumar(self,l):
        sum=0
        for i in l:
            sum=sum+i
        return sum



def func_piso(l,i):
    sum=0
    k=1
    for j in l:
        sum=sum+j*2**(i//k)
        k=k+1
    return sum



def coeficientes(i):
    salida=[]
    for k in range(6):
        salida.append(2**(i//(k+1)))
    return salida


def run():
    ecuaciones=[]
    days=[]
    band=0
    iter=0
    while band==0:
        while len(days)<6:
            day=random.randint(1,500)
            if days.count(day)==0:
                days.append(day)
        days.sort()
        obj=SistemaEcuaciones()
        obj.setEcua([coeficientes(days[0]),coeficientes(days[1]),coeficientes(days[2]),coeficientes(days[3]),coeficientes(days[4]),coeficientes(days[5])])
        k=0
        for i in obj.getRespuestas():
            if i.count(0)==3:
                k=k+1
        if k>4:
            band=1
        else:
            days.clear()
    for i in range(W):
        ecua=[]
        day=days[i]
        print(day)
        sys.stdout.flush()
        entrada=int(input())
        #entrada=func_piso([1,0,3,3,3,3],day)
        #print(entrada)
        ecua+=coeficientes(day)
        ecua.append(entrada)
        ecuaciones.append(ecua)

    obj=SistemaEcuaciones()
    obj.setEcua(ecuaciones)
    obj.variables()
    print(obj.getSalida())
    #sys.stdout.flush()
    #veredict=int(input())




T, W = map(int, input().split())
#T=1
#W=6
for _ in range(T):
    run()
