import matplotlib.pyplot as plt
from encoder import Encoder
import random
import numpy as np
from GeneticAlgorithm import *

#Initialize a non repeated random population of ten individuals, index0:cromossome
n = 10

ga = GeneticAlgorithm(n)

p = ga.randPopulation()
#print(f"init population: {p} \n")

bChromosomep = [0, 0]
t = 1

while t < 5:

    #append fitness value to p, index1: fitness
    p = ga.fitness(p)
    #print(f"first evaluation: {p} \n")

    #getting the best individual of the generation
    
    bChromosome = ga.best(p)
    print(f"best chromosome: {bChromosome} \n")
    if bChromosome[1] > bChromosomep[1]:
        bChromosomep = bChromosome
    print(f"first best chromosome population: {bChromosomep} \n")

    #append ranking and linear ranking values to p, index2: rank, index3: linRank
    p = ga.linRank(p)
    #print(f"ranking addition: {p} \n")

    #Roulete wheel selection

    pInter = ga.rouleteWheelSel(p)

    #Tournament selection, rn: number of random individuals per tournament
    rn = 8

    #pInter = ga.tournSelec(p, rn)

    #print(f"tournament selection: {pInter} \n")

    #crossover

    #probability crossover, must be betwen 0.6 < pc < 1.0
    pc = 0.6

    pInter = ga.crossover(pInter, pc)
    #print(f"crossover: {pInter} \n")

    #mutation

    pm =0.02

    pInter = ga.mutate(pInter)

    #print(f"mutation: {pInter} \n")

    #evaluation

    pInter = ga.fitness(pInter)

    t += 1

    #adding the best of the generation
    print(f"best chromosome population: {bChromosomep} \n")
    pInter[0] = bChromosomep

    print(f"last loop iter evaluation: {pInter} \n")

    
    xcoordinates = [int(Encoder().grayToBin(pInter[x][0]), 2)/100 for x in range(len(pInter))]
    print(xcoordinates)
    ycoordinates = [ga.evalFuncy(xcoordinates[x]) for x in range(len(pInter))]
    #ycoordinates = [ga.evalFuncy(pInter[x][0]) for x in range(len(pInter))]
    print(ycoordinates)

    ga.addPointPlot(xcoordinates, ycoordinates)

    plt.show()
    

print(t)
print(f"last iter evaluation: {pInter} \n")

#Plotting points
"""
xcoordinates = [int(Encoder().grayToBin(pInter[x][0]), 2)/100 for x in range(len(pInter))]
print(xcoordinates)
ycoordinates = [ga.evalFuncy(xcoordinates[x]) for x in range(len(xcoordinates))]
print(ycoordinates)

ga.addPointPlot(xcoordinates, ycoordinates)

plt.show()
"""