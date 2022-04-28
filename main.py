#from re import X
from encoder import Encoder
import random
import numpy as np
from GeneticAlgorithm import *

#Initialize a non repeated random population of ten individuals, index0:cromossome

ga = GeneticAlgorithm()

p = ga.randPopulation()
#print(p)

t = 1

#while t < len(p):

#append fitness value to p, index1: fitness
p = ga.fitness(p)
#print(p)

#append ranking and linear ranking values to p, index2: rank, index3: linRank
p = ga.linRank(p)
#print(p)


#Tournament selection, rn: number of random individuals per tournament
rn = 3

pInter = ga.tournSelec(p)

#print(pInter)

#crossover

#probability crossover

ga.crossover(pInter)
#print(pInter)

#mutation

pm =0.02

ga.mutate(pInter)
print(pInter)