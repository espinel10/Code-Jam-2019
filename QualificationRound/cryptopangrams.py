import random
import os
import time
primos=[];

##A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z


def run():
    mensaje=list("ABCDEFGHIJKLMNOPQRSTUVWXYZILOVETHEPIZZAWITHPINEAPPLE")###SECRETO
    os.system('cls')
    ABC="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
    abc=ABC.split(",")
    N=10000
    prim=list_prim(N)
    #################encripto el mesaje################################################
    ent_tem=semilla(1229)
    encrypt=[]
    entrada=[]
    for i in ent_tem:
            encrypt.append(prim[i])

    dic2=dict(zip(abc,encrypt))
    L2=len(mensaje)-1
    for i in range(0,L2):
        entrada.append(dic2.get(mensaje[i])*dic2.get(mensaje[i+1]))
    cad="".join(mensaje)
    print("el mesaje es ------>{}".format(cad))
    print("diccionario")
    print(dic2)
    print("mensaje encriptado")
    print(entrada)
    print("----------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------")
    time.sleep(5)
    os.system('cls')
    #####prueba###############################################################
    #N=103
    #entrada=[217,1891,4819,2291,2987,3811,1739,2491,4717,445,65,1079,8383,5353,901,187,649,1003,697,3239,7663,291,123,779,1007,3551,1943,2117,1679,989,3053]
    #N=10000
    #entrada=[3292937,175597,18779,50429,375469,1651121,2102,3722,2376497,611683,489059,2328901,3150061,829981,421301,76409,38477,291931,730241,959821,1664197,3057407,4267589,4729181,5335543]
    L=len(entrada)
    output=[]
    salida=[]
    ###############################funcion para generar numeros aleatorios######################################################################
    ##### N  prim_total
    band=0
    var=0
    for x in prim:
        for y in prim:
            if x*y==entrada[0]:
                valor1=entrada[1]/y
                valor=valor1-int(valor1)
                uno=0
                if valor==0:
                    uno=0
                else:
                    uno=1
                if uno==0:
                    var=y
                    salida.append(x)
                    salida.append(y)
                else:
                    var=x
                    salida.append(y)
                    salida.append(x)
                band=1
                break
        if band==1:
            break

    for k in range(1,L):
        for j in prim:
            if entrada[k]==(var*j):
                var=j
                salida.append(var)
                break

    #print(salida)
    aux=salida[:]
    salida.sort()
    prueba=list(set(salida))[:]
    prueba.sort()
    dic=dict(zip(prueba,abc))
    print("----------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------")
    print("el diccionario es")
    print(dic)
    for i in aux:
        output.append(dic.get(i))
    cad2="".join(output)
    print("el mensaje es :{}".format(cad2))####SECRETO REVELADO

   #############funcion para encontrar el primer valor de la primera letra ###########################################

    #dic=dict(zip(prim,abc))
    #print(dic)
    #print(salida)
    #for i in salida:
    #    output.append(dic.get(i))
    #print(output)

####################inicializa la variable lista del .txt######################
def primos_list():
    list=[]
    with open('numeroPrimos.txt') as f:
        for line in f:
            x=line.split("-")
            list+=x
        f.close()
    for i in list:
        if i!='\n':
            num=int(i)
            primos.append(num)



####################crea una lista de solo los primos que son posiblest######################
def list_prim(n):
    aux=[]
    for i in primos:
        if i<=n:
            aux.append(i)
        else:
            break
    return aux

def semilla(b):
    a=0
    aux=[]
    for i in range(0,26):
        band=0
        while band==0:
            var=random.randint(a, b)
            if aux.count(var)==0:
                aux.append(var)
                band=1

    aux.sort()
    return aux




if __name__ == '__main__':
    primos_list()
    run()
