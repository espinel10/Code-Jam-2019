import sys
import random
import time
##python interactive_runner.py python testing_tool.py 0 -- python PotteryLottery.py
salida=[]
class Pottery:
    def __init__(self,valores):
        for i in range(len(valores)):
            for j in range(i,len(valores)):
                if valores[i][1]>valores[j][1]:
                    aux=valores[i]
                    valores[i]=valores[j]
                    valores[j]=aux
        self.valores=valores
        auxi=valores[2:7]
        self.iter=[]
        k=0
        while len(self.iter)<14:
            if k==len(auxi):
                k=0
            self.iter.append(auxi[k])
            k=k+1

    def actualizar(self,n,value):
        self.valores[n]=value

    def getIter(self):
        return self.iter

    def getValores(self):
        return self.valores






def run():
    aux=[]
    for i in range(20):
        aux.append([])

    ##60
    k=0
    j=1
    for i in range(60):
        #computadora
        var=random.randint(0,19)
        aux[var].append(j)

        ##yo
        if k>14:
            k=0
        var=random.randint(1,100)
        aux[k].append(var)
        k=k+1
        j=j+1
    valores=[]

    #20
    for i in range(20):
        ##computadora
        var=random.randint(0,19)
        aux[var].append(j)
        j=j+1
        ##consultas
        valores.append([i,len(aux[i])])

    obj=Pottery(valores)

    #14
    for i in obj.getIter():
        ##computadora
        var=random.randint(0,19)
        aux[var].append(j)
        j=j+1
        ##yo
        var=random.randint(1,100)
        aux[i[0]].append(var)

    #2
    #computadora
    var=random.randint(0,19)
    aux[var].append(j)
    j=j+1
    #yo
    auxi=obj.getValores()[:7]
    a=len(aux[auxi[0][0]])
    #computadora
    var=random.randint(0,19)
    aux[var].append(j)
    j=j+1
    #yo
    b=len(aux[auxi[1][0]])

    mayor=1
    menor=0
    if a > b :
        menor=1
        mayor=0

    for i in range(3):
        ##computadora
        var=random.randint(0,19)
        aux[var].append(j)
        j=j+1
        ##yo
        var=random.randint(1,100)
        aux[auxi[mayor][0]].append(var)

    ##100
    aux[auxi[menor][0]].append(100)

    ##jurado
    values=[]
    for i in aux:
        values.append(len(i))

    mini=min(values)

    if values.count(mini)==1:
        ind=values.index(mini)
        if aux[ind].count(100)==1:
            salida.append(ind)




T=250
for _ in range(T):
    run()
print("{}/250".format(len(salida)))
