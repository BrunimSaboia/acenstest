#!/usr/bin/python
import random

vetora = []
vetorb = []
vetorc = []

for i in xrange (0,10):
    vetora.insert(i, random.randint(1,100))
    vetorb.insert(i,random.randint(1,100))
for i in xrange (0,20):
    vetorc.append(vetora[i])
    vetorc.append(vetorb[i])
    if i == 9:
        break
    print ("vetor a: %s" %vetora)
    print ("vetor b: %s" %vetorb)
    print ("vetor c: %s" %vetorc)