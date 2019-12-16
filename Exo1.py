from point import point
from boule import boule
from PdistL import PdistL
from operator import itemgetter
import random
from math import sqrt

pc=point(0,0,'1')
b1 = boule(pc, 20)
b2 = boule(pc, 40)
test = []

def distP(p11, p22):
    d = 0.0
    d = (p11.x - p22.x) ** 2 + (p11.y - p22.y) ** 2
    return sqrt(d)

def takeSec(elem):
    return elem.d

def DistsKNN(t,bo1,bo2):
    for ppp in t:
       for i in bo1.PList:
          dist=PdistL(i,distP(ppp,i))
          ppp.distances.append(dist)
       for j in bo2.PList:
          dist=PdistL(j,distP(ppp,j))
          ppp.distances.append(dist)
       ppp.distances.sort(key=takeSec)

    return t

def KNN(k,t):
    for p in t:
        kn = 0
        c1 = 0
        c2 = 0
        for dd in p.distances:
            if(kn<k):
                if(dd.p.classe=="1"):
                    c1=c1+1
                elif(dd.p.classe=="2"):
                    c2=c2+1
                kn=kn+1
        if(c2>c1):
            p.classe = "2"
        elif(c1>c2):
            p.classe = "1"
    return t

#print(len(b1.PList))
while len(b1.PList)<10:
    p=point(random.randint(0,70),random.randint(0, 70), "1")
    if (b1.PList.count(p) == 0) and (distP(p,b1.pC))<=b1.r:
        b1.PList.append(p)

#print("boule1:","point de centre:",b1.pC.x,b1.pC.y,"rayon:",b1.r,"longueur de list des points:",len(b1.PList))

b2.PList=[]
while len(b2.PList)<10:
    p=point(random.randint(0,70),random.randint(0, 70), '2')
    if (b2.PList.count(p) == 0) and (distP(p,b2.pC))>=b2.r:
        b2.PList.append(p)

#print("boule2:","point de centre:",b2.pC.x,b2.pC.y,"rayon:",b2.r,"longueur de list des points:",len(b2.PList))

while len(test)<5:
    p3=point(random.randint(0,70),random.randint(0, 70), '0')
    if(distP(p3,b1.pC))>b1.r and (distP(p3,b2.pC))<b2.r and test.count(p3)==0:
        test.append(p3)

#print("longueur de liste des points de test:",len(test))
for t in test:
    t.distances=[]


d=DistsKNN(test,b1,b2)
KNN(5,d)

for pointT in test:
    print(pointT.x,pointT.y)
    i = 0
    for de in pointT.distances:
        if(i==5):
            break
        print(de.p.classe,"distance:",de.d)
        i=i+1
    print("donc la classe de cette point est :",pointT.classe)

