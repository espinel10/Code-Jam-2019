import random
import time
import os
R=2
C=5
def run():
    mapa=[]
    aux2=[]
    ind=[]
    cont=0
    for  j in range(0,R):
        aux=[]
        for i in range(0,C):
            ax=[j,i]
            aux2.append(ax)
            ind.append(cont)
            cont=cont+1
            aux.append(0)
            #print(aux[i],end=" ")
        mapa.append(aux)
        #print()
    dic=dict(zip(ind,aux2))
    print(dic)
    band=0
    mov=[]
    cont=cont-1
    var=0
    mov.append(var)
    x=dic.get(var)[1]
    y=dic.get(var)[0]
    print(mov)
    init=[]
    posi=0
    init.append(var)
    while band==0:
        opc=[]
        for k in range(cont+1):
            dx=dic.get(k)[1]
            dy=dic.get(k)[0]
            if k==var:
                continue
            if (dx!=x) and (dy!=y) and mov.count(k)==0:
                if(dx==x-1 and dy==y+1):
                    continue
                if(dx==x-1 and dy==y-1):
                    continue
                if(dx==x+1 and dy==y+1):
                    continue
                if(dx==x+1 and dy==y-1):
                    continue
                opc.append(k)
        if len(opc)==0:
            if len(mov)==cont+1:
                band=1
            else:
                mov.clear()
                var=random.randint(0,cont)
                mov.append(var)
                x=dic.get(var)[1]
                y=dic.get(var)[0]
                if init.count(var)==0:
                    init.append(var)
        else:
            if len(opc)==1:
                var=0
            else:
                var=random.randint(0,len(opc)-1)
            mov.append(opc[var])
            x=dic.get(opc[var])[1]
            y=dic.get(opc[var])[0]

        if len(init)==cont+1:
            posi=1
            band=1

    h=0
    if posi==0:
        for k in mov:
            h=h+1
            time.sleep(1)
            x=dic.get(k)[1]
            y=dic.get(k)[0]
            mapa[y][x]=h
            time.sleep(1)
            mostrar(mapa)
    else:
        time.sleep(1)
        os.system('cls')
        print("IMPOSIBLE")


def mostrar(mapa):
    os.system('cls')
    print("ES POSIBLE")
    dx=0
    dy=0
    for j in range(0,R):
        dx=0
        for i in range(0,C):
            if mapa[j][i]!=0:
                print(" {} ".format(mapa[j][i]),end=" ")
            else:
                print(" # ",end=" ")
        print()

if __name__ == '__main__':
    run()
