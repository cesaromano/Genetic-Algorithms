import matplotlib.pyplot as plt
from encoder3 import Encoder3
from GeneticAlgorithm3 import *

#Initialize a non repeated random population of ten individuals, index 0:cromossome
n = 8
ga = GeneticAlgorithm3(n)
p = ga.randGrayPopulation()
#print(f"first population: {p} \n")

#append fitness value to p index 1
f = ga.fitness(p)
print(f"first fitness population vector: {f} \n")

#best chromosome population value
bIndP = ['01111', '01111']

#counter
t = 1

while t < 50:
    #getting the best individual of the generation
    bInd = ga.best(p, f)
    evalBInd = ga.evalFunc(bInd[0], bInd[1])
    evalBIndP = ga.evalFunc(bIndP[0], bIndP[1])
    if evalBInd < evalBIndP:
        bIndP = bInd

    #append ranking and linear ranking values to p, index 2: rank, index 3: linRank
    r, lr = ga.linRank(f)
    #print(f"ranking: {r} \n")
    #print(f"linear ranking: {lr} \n")

    #Tournament selection, rn: number of random individuals per tournament
    rn = 2
    p = ga.tournSelec(p, lr, rn)
    #print(f"tournament selection: {p} \n")

    #Roulete wheel selection
    #p = ga.rouleteWheelSel(p, f)
    #print(f"roulete wheel selection: {p} \n")

    #crossover, probability crossover must be betwen 0.6 < pc < 1.0
    pc = 0.6
    p = ga.crossover(p, pc)
    #print(f"crossover: {p} \n")

    #mutation
    pm =0.02
    p = ga.mutate(p, pm)
    #print(f"mutation: {p} \n")

    #adding the best of the generation to the next population
    #p[0] = bIndP
    #evalBInd = ga.evalFunc(bInd[0], bInd[1])
    #print(evalBInd)

    #append last fitness value to p index 1
    f = ga.fitness(p)
    print(f"last iter population: {f} \n")

    t+=1

print(t)