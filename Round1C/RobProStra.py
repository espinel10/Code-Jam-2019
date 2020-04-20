import random
import time
import sys
def battle(N,entrada,case):
    #entrada=[['R','S'],['R','S'],['R','S'],['R','S'],['R','S'],['R','S'],['R','S']]
    #entrada=[['R','S']]
    #entrada=[['R'],['S'],['P']]
    win=0
    k=0
    band=0
    i=0
    mov=[]
    cont=0
    iter=0
    permutacion=[]
    fact=1
    for f in range(1,N+1):
        fact=fact*f
    while win==0 and iter<fact*2:
        iter=iter+1
        orden=orden_entrada(N)
        permutacion.append(orden)
        i=0
        band=0
        while band==0 :
            m=ale_mov()
            if match(m,entrada[orden[0]][i])=='A':
                mov.append(m)
                band=1
            if match(m,entrada[orden[0]][i])=='C':
                mov.append(m)
                i=i+1
            if i==len(entrada[orden[0]]):
                i=0
        cont=0
        if len(mov)>40:
            mov.clear()
            continue

        for j in orden:
             i=0
             k=0
             band=0
             while band==0:
                  if match(mov[i],entrada[j][k])=='A':
                      band=1
                      cont=cont+1
                  else:
                      if match(mov[i],entrada[j][k])=='B':
                          band=2
                      else:
                          i=i+1
                          k=k+1
                  if i==len(mov):
                      if band==1:
                          band=1
                      else:
                          band=2
                  if k==len(entrada[j]):
                      k=0
             if band==2:
                break

        if cont==len(entrada):
            win=1

    if win==1:
        output="".join(mov)
        print("Case #{} : {}".format(case,output))
        sys.stdout.flush()
    else:

        print("Case #{} :  IMPOSIBLE".format(case))
        sys.stdout.flush()
def factorial(n):
    if n>1:
        return n*factorial(n-1)
    else:
        return 1

def match(A,B):
    if A==B:
        return 'C'
    if A=='R' and B=='P':
        return 'B'
    if A=='R' and B=='S':
        return 'A'
    if A=='P' and B=='R':
        return 'A'
    if A=='P' and B=='S':
        return 'B'
    if A=='S' and B=='P':
        return 'A'
    if A=='S' and B=='R':
        return 'B'
def orden_entrada(N):
    list=[]
    while len(list)!=N:
        var=random.randint(0,N-1)
        if list.count(var)==0:
            list.append(var)
    return list

def ale_mov():
    var=random.randint(0,2)
    if var==0:
        return 'P'
    if var==1:
        return 'R'
    if var==2:
        return 'S'


T=int(input())
for i in range(T):
    entrada=[]
    N=int(input())
    for j in range(N):
        string=str(input())
        entrada.append(list(string))
    case=i
    battle(N,entrada,case+1)
