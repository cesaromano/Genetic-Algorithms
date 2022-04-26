from encoder import Encoder
from random import randint
import numpy as np
from GeneticAlgorithm import *

test1 = Encoder()

"""
#Initialize population
p = np.array([[Encoder().binToGray(format(randint(0, 101), 'b'))] for x in range(0, 10)])
#e = np.array([[GeneticAlgorithm().evalFunc(p[int(x),0])] for x in range(0, 10)])

for x in range(0, 10):

    val = [GeneticAlgorithm().evalFunc(p[int(x),0])]
    print(val)
    np.append(val, p[int(x), 0])
    #print(GeneticAlgorithm().evalFunc(p[int(x),0]))

print(p)
#print(e)
"""
#Initialize a random population of ten individuals
p = [[Encoder().binToGray(format(randint(0, 101), 'b'))] for x in range(0, 10)]

#evaluates each individual aptitude and append their result
for x in range(0, 10):

    val = GeneticAlgorithm().evalFunc(p[x][0])
    #print(val)
    p[x].append(val)

#space ranking aptitude

print(p)