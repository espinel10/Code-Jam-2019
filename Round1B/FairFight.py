import sys
import random
import time
#N=4
#k=0
#N=3
#k=0
#N=1
#k=0
#N=5
#k=0
#N=3
#k=0
#N=5
#k=2
def run(N,k,C,D,cont):
    P3=0
    P2=0
#    C=[1,2,3,4,5]
#    D=[5,5,5,5,10]
#    C=[1,0,0]
#    D=[0,1,2]
#    C=[0,8,0,8,0]
#    D=[4,0,4,0,4]
#    C=[3]
#    D=[3]
#    C=[1,1,1,8]
#    D=[8,8,8,8]
#    C=[0,1,1]
#0    D=[1,1,0]

    intervals=intervals_orden(N)
    for subinterval in intervals:
        max=-9999
        if subinterval[0]==subinterval[1]:
            i=subinterval[0]
            max=C[i]
            max2=D[i]
            if max2<=max+k:
                P2=P2+1
            if max2<max-k:
                P3=P3+1
        else:
            for i in range(subinterval[0],subinterval[1]+1):
                if C[i]>max:
                    max=C[i]
            max2=-999999
            for j in range(subinterval[0],subinterval[1]+1):
                if D[j]>max2:
                    max2=D[j]
            if max2<=max+k:
                P2=P2+1
            if max2<max-k:
                P3=P3+1

    y= P2-P3
    print("Case #{}: {}".format(cont,y))


def intervals_orden(N):
    salida=[]
    for i in range(0,N) :
        for j in range(i,N):
            aux=[i,j]
            salida.append(aux)
    return salida

T=int(input())
for _ in range(T):
    N,k = map(int, input().split())
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))
    run(N,k,C,D,_+1)
