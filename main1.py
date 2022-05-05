from numpy import hamming
from GeneticAlgorithm1 import *

#solution vector
s = ['111101101111']

#ideal fitness
iFit = 12

#Initialize a non repeated random population of n individuals
n = 8
ga = GeneticAlgorithm1(n)
p = ga.randBitPopulation()
print(f"first population: {p} \n")
#ga.representate(p)
#getting hamming distance
#h = ga.hammingDist(p, s)
#print(f"hamming distance: {h} \n")
#getting hamming fit directly
hf = ga.hammingFit(p, s, iFit)
print(f"hamming fitness: {hf} \n")
#stop criterion
sc = 0
#loop control
t = 0
#number of iterations
ni = 170

#while t < ni and sc < iFit:
while t < ni and sc < iFit:

    #getting the max hamming fit value as a stop criterion
    if max(hf) > sc:
        sc = max(hf)
    print(f"stop criterion: {sc} \n")

    #roulete wheel slection
    p = ga.rouleteWheelSel(p, hf)
    #print(f"selected population: {p} \n")

    #crossover
    pc = 0.6
    p = ga.crossover(p, pc)
    #print(f"crossover population: {p} \n")
    
    #mutate
    pm=0.02
    p = ga.mutate(p, pm)
    #print(f"population mutated: {p} \n")

    #last iter hamming fit
    hf = ga.hammingFit(p, s, iFit)
    #print(f"hamming fitness: {hf} \n")

    #total fit
    tf = sum(hf)
    print(f"total fitness: {tf} \n")

    #mean fit
    mf = tf/len(p)
    print(f"mean fitness: {mf} \n")

    t+=1

print(t)
ga.representate(p)