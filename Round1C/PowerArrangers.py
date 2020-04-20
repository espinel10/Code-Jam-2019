import sys
import random


class Permutacion:
    def __init__(self):
        self.letters=['A','B','C','D','E']
        aux=self.letters
        self.opciones=[]
        self.pairs=[]
        envio=[]
        self.permu(aux,envio)




    def permu(self,aux,env):
        envio=env[:]
        if len(aux)==1:
            aux2=aux[:]
            aux3=envio[:]
            aux3.append(aux2[0])
            self.opciones.append(aux3)
            return
        else:
            for i in aux:
                aux2=aux[:]
                aux2.remove(i)
                aux3=envio[:]
                aux3.append(i)
                self.permu(aux2,aux3)

    def getOpciones(self):
        return self.opciones


    def setPairs(self,par):
        self.pairs.append(par)

    def getSecuencia(self):
        for i in pairs:
            secu=[]
            ax=self.getPosi(i)
            secu.append(ax)
            for j in pairs:
                axi=self.getPosi(j)
                if axi[0]==ax[0]:
                    secu.append(axi)




    def getPosi(self,par):
        valor=round(par[0]/5,1)
        pos=int(valor)
        porc=round(valor-pos,1)
        posi=None
        if porc==0.2:
            posi=0
        if porc==0.4:
            posi=1
        if porc==0.6:
            posi=2
        if porc==0.8:
            posi=3
        if porc==0.0:
            posi=4
        ###[pos posicion en el orden, posi orden interno,letra]
        return [pos,posi,i[1]]




obj=Permutacion()
print(len(obj.getOpciones()))
cont=0
