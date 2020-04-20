import random
import sys
import time
M=0
N=0
holes=18
#####################################################clase blades##############
class Blades:
    def __init__(self,entrada,salida):
        self.entrada=entrada
        self.salida=salida
        self.opciones=[]
        self.permuto=[]

    def gen_opc(self):
        aux=[]
        for i in range(18):
            if self.entrada[i]!=0:
                aux.append(dev_values(self.salida[i],self.entrada[i]))
        cont=0
        self.permu(aux,cont)

        for j in self.permuto:
            sum=0
            for k in j:
                sum=sum+k
            if sum<M:
                if self.opciones.count(sum)==0:
                    self.opciones.append(sum)



    def getPermuto(self):
        return self.permuto

    def GetOpciones(self):
        return self.opciones

    def permu(self,auxi,cont):
        if cont==len(auxi):
            return
        else:
            multi=1
            for j in range(cont+1,len(auxi)):
                multi=multi*len(auxi[j])
            if cont==0:
                k=0
                for i in auxi[cont]:
                    for j in range(multi):
                        self.permuto.append([i])
            else:
                k=0
                indice=0
                axiliar=auxi[cont]
                for i in range(len(self.permuto)):
                    self.permuto[i].append(axiliar[indice])
                    k=k+1
                    if k==multi:
                        k=0
                        indice=indice+1
                    if indice==len(axiliar):
                        indice=0
        self.permu(auxi,cont+1)




############################funcion main#####################################################
def run():
    band=0
    intentos=[]
    respuesta=0
    iter=0
    while band==0 and iter<M:
        iter=iter+1
        salida=dev_wind()
        output=" ".join(map(str,salida))
        ##########outpu#############
        print(output)
        sys.stdout.flush()
        #########input###############
        entrada = list(map(int,input().split()))
        obj=Blades(entrada,salida)
        obj.gen_opc()
        if len(intentos)==0:
            intentos.append(obj.GetOpciones())
        else:
            probar=obj.GetOpciones()
            aux=[]
            for i in probar:
                for j in intentos[-1]:
                    if i==j:
                        aux.append(i)
            intentos.append(aux)

        if len(intentos[-1])==1:
            band=1
            respuesta=intentos[-1][0]
    print(respuesta)
    sys.stdout.flush()
    veredict=int(input())
    if veredict==-1:
        exit()


##0 1 0 1 0 0 1 0 0 1 0 0 0 1 0 0 0 0
# 2 2 2 2 18 3 3 3 3 3 3 4 4 4 4 5 2 2


############################################################################################
def dev_values(blades,n1):
    salida=[]
    z=n1
    salida.append(z)
    while z+blades<M/4:
        salida.append(z+blades)
        z=z+blades
    return salida
#######################################################################################
def dev_wind():
    salida=[]
    for i in range(18):
        var=random.randint(2, 18)
        salida.append(var)
    return salida



t,n,m=map(int,input().split())
N=n
M=m
for _ in range(t):
    run()
