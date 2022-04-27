from encoder import Encoder
import random
import numpy as np
from GeneticAlgorithm import *

#Initialize a non repeated random population of ten individuals, index0:cromossome

ga = GeneticAlgorithm()

p = ga.randPopulation()

t = 1

#while t < len(p):

#append fitness value to p, index1: fitness
p = ga.fitness(p)

#append ranking and linear ranking values to p, index2: rank, index3: linRank
p = ga.linRank(p)



#Tournament selection
rn = 3
pInter = []

for x in range(len(p)):
    rInd = random.sample(range(0, 10), rn)
    best = [p[rInd[x]][3] for x in range(len(rInd))]
    i = best.index(max(best))
    pInter.append(p[rInd[i]])

print(rInd)
print(pInter)
print(best, i)



#   t += 1