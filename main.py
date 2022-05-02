import matplotlib.pyplot as plt
from encoder import Encoder
import random
import numpy as np
from GeneticAlgorithm import *

#Initialize a non repeated random population of ten individuals, index0:cromossome
n = 10

ga = GeneticAlgorithm(n)

p = ga.randPopulation()
print(f"init population: {p} \n")

t = 1

while t < 5:

    #append fitness value to p, index1: fitness
    p = ga.fitness(p)
    print(f"first evaluation: {p} \n")

    #append ranking and linear ranking values to p, index2: rank, index3: linRank
    p = ga.linRank(p)
    #print(f"ranking addition: {p} \n")


    #Tournament selection, rn: number of random individuals per tournament
    rn = 8

    pInter = ga.tournSelec(p, rn)

    #print(f"tournament selection: {pInter} \n")

    #crossover

    #probability crossover, must be betwen 0.6 < pc < 1.0
    pc = 0.6

    ga.crossover(pInter, pc)
    #print(f"crossover: {pInter} \n")

    #mutation

    pm =0.02

    #ga.mutate(pInter)

    #print(f"mutation: {pInter} \n")

    #evaluation

    ga.fitness(pInter)

    t += 1

    xcoordinates = [int(Encoder().grayToBin(pInter[x][0]), 2)/100 for x in range(len(pInter))]
    print(xcoordinates)
    ycoordinates = [ga.evalFuncy(pInter[x][0]) for x in range(len(pInter))]
    print(ycoordinates)

    ga.addPointPlot(xcoordinates, ycoordinates)

    plt.show()

print(t)
print(f"last iter evaluation: {pInter} \n")

#Plotting points
"""
xcoordinates = [int(Encoder().grayToBin(pInter[x][0]), 2)/100 for x in range(len(pInter))]
print(xcoordinates)
ycoordinates = [ga.evalFuncy(pInter[x][1]) for x in range(len(pInter))]
print(ycoordinates)

ga.addPointPlot(xcoordinates, ycoordinates)

plt.show()
"""