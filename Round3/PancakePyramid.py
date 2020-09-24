import sys
import time

class Pancake:
    def __init__(self,stack):
        self.stack=stack
        self.opciones=[]
        self.S=len(stack)
        self.sum=0
        self.posibles()

    def posibles(self):
        result=self.S-3
        xy=[]
        for i in range(result+1):
            for j in range(result-i+1):
                if i+j<=result:
                    xy.append([i,j])
                    


        for i in xy:
            ini=i[0]
            fin=self.S-i[1]
            self.opciones.append(self.stack[ini:fin])


    def suma(self):
        accum=0
        for z in self.opciones:
            menor=9999999999999999999999999999999999999999999999999999999999999999999999999999

            for j in range(0,len(z)):
                i=z[:]


                accum2=0
                ####del pivote hasta 0
                for k in range(j,0,-1):
                    if i[k]==max(i[:k+1]):
                        continue
                    else:
                        dif=max(i[:k])-i[k]
                        i[k]=max(i[:k])
                        accum2=accum2+dif
                ##desde el pivote hasta el final
                for k in range(j,len(z)):
                    if i[k]==max(i[k:]):
                        continue
                    else:
                        dif=max(i[k:])-i[k]
                        i[k]=max(i[k:])
                        accum2=accum2+dif



                if menor>accum2:
                    menor=accum2

            accum=accum+menor

        self.sum=accum%1000000007



    def getOpciones(self):
        return self.opciones

    def getSum(self):
        return self.sum










def run(S,entrada,t):
    obj=Pancake(entrada)
    obj.suma()
    obj.suma()
    print("case #{}:{}".format(t,obj.getSum()))



T=int(input())
for _ in range(T):
    S=int(input())
    entrada=list(map(int,input().split()))
    run(S,entrada,_+1)
