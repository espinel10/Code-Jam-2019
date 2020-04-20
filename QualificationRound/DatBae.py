import random
import sys
def run(N,B,F):
    enteros=[]
    employer=[]
    dif=[]
    ind=[]
    for i in range(N):
        employer.append(dev_bit(i+1,N))
        enteros.append(i+1)
    for i in range(N-B):
        aux=[]
        dif.append(aux)

    for t in range(F):
        prueba=[]
        for j in employer:
            prueba.append(j[t])
        if dev_ent(prueba)==0:
            break
        output="".join(map(str,prueba))
        print(output)
        sys.stdout.flush()
        s = input()
        entrada=list(map(int,s))
        cont=0
        for linea in dif:
            linea.append(entrada[cont])
            cont=cont+1

    entra_int=list(map(dev_ent,dif))
    #print(entra_int)
    #print(enteros)
    aux=[]
    for linea in enteros:
        if entra_int.count(linea)==0:
            aux.append(enteros.index(linea))
    aux.sort()
    salida=" ".join(map(str,aux))
    print(salida)
    sys.stdout.flush()
    veredict=input()


def dev_bit(n,N):
    salida=[]
    while n>0:
        if n%2==0:
            salida.append(0)
        else:
            salida.append(1)
        n=n//2
    if len(salida)<N:
        for i in range(N-len(salida)):
            salida.append(0)
    return salida

def dev_ent(bit):
    cont=0
    salida=0
    for i in bit:
        if i==1:
            salida=salida+2**cont
        cont=cont+1
    return salida

T= int(input())
for _ in range(T):
    N,B,F=map(int,input().split())
    run(N,B,F)
