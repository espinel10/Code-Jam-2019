import sys
#M=4
#entrada=[[2,4],[3,4],[2,4],[2,3]]
#pesos=[10,10,10,10]

#M=2
#entrada=[[1,2],[1,2]]
#pesos=[1,0]

#M=2
#entrada=[[1,2],[1,2]]
#pesos=[0,0]


class Nodo:
    def __init__(self,value,ndirigidos):
        self.value=value
        self.ndirigidos=ndirigidos

    def getNDirigidos(self):
        return self.ndirigidos

    def setValue(self,valor):
        self.value=valor
    def getValue(self):
        return self.value

class Grafos:
    def __init__(self,nodos,valores):
        self.nodes=[]
        self.unbounded=0
        #self.trayectorias=[]

        for i in range(len(nodos)):
            obj=Nodo(valores[i],nodos[i])
            self.nodes.append(obj)
        for i in range(len(nodos)):
            self.getCiclo([i])

    def getBandera(self):
        return self.unbounded


    def show(self):
        print("######################")
        print(self.trayectorias)
        print(self.unbounded)
        for i in self.nodes:
            print(i.getValue(),end=" ")

    def getValues(self):
        aux=[]
        for i in self.nodes:
            aux.append(i.getValue())
        return aux


    def getCiclo(self,aux):
        auxi=aux[:]

        if len(auxi)>2:
            if auxi[0]==0 and auxi[-1]==0:
                self.unbounded=1
                return
        for i in auxi:
            if auxi.count(i)>1:
                #self.trayectorias.append(auxi)
                return
        hijos=self.nodes[auxi[-1]].getNDirigidos()
        var=self.nodes[auxi[-1]].getValue()

        if var==0:
            return
        self.nodes[auxi[-1]].setValue(0)
        self.nodes[hijos[0]-1].setValue(self.nodes[hijos[0]-1].getValue()+var)
        self.nodes[hijos[1]-1].setValue(self.nodes[hijos[1]-1].getValue()+var)

        for i in hijos:
            auxi2=auxi[:]
            auxi2.append(i-1)
            self.getCiclo(auxi2)





def run(entrada,pesos,t):
    prueba=[]
    lead=[]
    bandera=0
    band=0
    tusi=pesos
    lead.append(tusi[0])
    while  band==0:
        prueba.append(tusi)
        obj=Grafos(entrada,tusi)
        tusi=obj.getValues()

        if obj.getBandera()==1:
            band=1
            bandera=1
        else:
            lead.append(tusi[0])

        accum=0
        for i in range(1,len(tusi)):
            if tusi[i]==0:
                accum=accum+1
        if accum==len(tusi)-1 or tusi[0]==0:
            band=1

    if bandera==0:
        maxi=max(lead)%1000000007
        print("Case #{}:{}".format(t,maxi))
    else:
        print("Case #{}:UNBOUNDED".format(t))




T=int(input())
for _ in range(T):
    M=int(input())
    entra=[]
    for h in range(M):
        entra.append(list(map(int, input().split())))
    pes=list(map(int, input().split()))
    run(entra,pes,_+1)
