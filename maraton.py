import random
def run():
    print("escriba el numero de prueba")
    n=input()
    numero=int(n)
    sum_ale(numero)

def sum_ale(numero):
    bandera=0
    cont=cont_dig(numero)
    while bandera==0:
        pass
        A=num_ale(cont)
        B=num_ale(cont)
        if (A+B)==numero:
            bandera=1
    print("la respuesta es {}  +  {}  = {} ".format(A,B,numero))

def num_ale(num):
    list=[]
    j=0
    for i in range(0,num):
        band=0
        while band==0:
            j=random.randint(0, 9)
            if j!=4:
                band=1
        list.append(j)
    j=0
    for i in range(0,num):
        j=j+list[i]*pow(10,i)
    return j
###funcion que me cuenta cuantos digitos tiene para el algoritmo
def cont_dig(n):
    i=0
    x=n
    ##list=[]
    while (int(n/pow(10,i))!=0):
        i=i+1
    return i
if __name__ == '__main__':
    run()
