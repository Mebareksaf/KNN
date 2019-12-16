from point import distP
from operator import itemgetter
from PdistL import PdistL
import Exo1

def DistsKNN(t,b1,b2):
    for p in t:
       for i in b1.PList:
          d=PdistL(i,distP(p,i))
          p.distances.append(d)
       for j in b2.PList:
          d=PdistL(j,distP(p,j))
          p.distances.append(d)
       p.distances=sorted(p.distances, key=itemgetter(1))
    return t

def KNN(k,t):
    kn=0
    while(kn<k):
        for p in t:
            print(p.distances.p.classe)
        kn=kn+1
    return t

