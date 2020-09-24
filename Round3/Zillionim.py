import sys
import random

class Bot:
    def __init__(self):
        self.movAI=[]
        self.lastMov=0
    def setMov(self,p):
        self.movAI.append([p,p+10**10])
        self.lastMov=p

    def getLanzar(self):
        prueba=self.lastMov+2*10**10
        cont=0
        return prueba


def run():
    band=0
    bot=Bot()
    cont=0

    while band==0:
        cont=cont+1
        if cont%2==0:
            p=int(input())
            bot.setMov(p)
            if p==-1 or p==-2 or p==-3:
                if p==-1:
                    exit()
                band=1
        else:
            lanzar=bot.getLanzar()
            print(lanzar)
            sys.stdout.flush()





t,w = map(int, input().split())
for _ in range(t):
    run()
