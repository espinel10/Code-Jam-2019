import sys
import random
import time
#N=6
#N=2
#N=3
#N=4
def gen_ale():
    salida=[]
    band=0
    while band==0:
        var=random.randint(0, N-1)
        if salida.count(var)==0:
            salida.append(var)
        if len(salida)==N:
            band=1
    return salida

def run():
    #
    #ent=["TARPOL","PROL"]
    #ent=["CODEJAM","JAM","HAM","NALAM","HUM","NOLOM"]
    #ent=["TARPOR","TARPRO","PROL"]
    #ent=["PI","HI","WI","FI"]
    entrada=[]
    for line in ent:
        aux=[]
        aux=list(line)[:]
        aux.reverse()
        entrada.append(aux)
    output=0
    mayor=-99999
    cont=0
    print(entrada)

    bandera=0
    k=0
    while bandera==0:
        rhyme=[]
        orden=gen_ale()

        for i in range(len(orden)//2):
            ind=i*2
            A=entrada[orden[ind]]
            B=entrada[orden[ind+1]]
            j=0
            band=0
            letter=''
            while band==0:
                if j>len(A)-1 or j>len(B)-1:
                    break
                if A[j]==B[j]:
                    if rhyme.count(A[j])==0 and (len(rhyme)<len(entrada)//2):
                        rhyme.append(A[j])
                    else:
                        j=j+1
                else:
                    band=1

        if len(rhyme)==(len(entrada)//2) or k==100:
            bandera=1
        if len(rhyme)>mayor:
            output=len(rhyme)
        k=k+1
    print(output*2)

if __name__ == '__main__':




    run()
