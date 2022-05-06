from numpy import hamming
from GeneticAlgorithm1 import *
import matplotlib.pyplot as plt

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
#getting hamming fit
hf = ga.hammingFit(p, s, iFit)
#print(f"hamming fitness: {hf} \n")
#stop criterion
sc = 0
#loop control
t = 0
#number of iterations
ni = 170

minHD = []
meanHD = []
bestGen = []

while t < ni and sc < iFit:

    #getting the max hamming fit value as a stop criterion
    if max(hf) > sc:
        sc = max(hf)
        bestGen = p
    #print(f"stop criterion: {sc} \n")

    #roulete wheel slection
    p = ga.rouleteWheelSel(p, hf)
    #print(f"selected population: {p} \n")

    #crossover
    pc = 0.5
    p = ga.crossover(p, pc)
    #print(f"crossover population: {p} \n")
    
    #mutate
    pm=0.01
    p = ga.mutate(p, pm)
    #print(f"population mutated: {p} \n")

    #last iter hamming fit
    hf = ga.hammingFit(p, s, iFit)
    #print(f"hamming fitness: {hf} \n")

    #total fit
    tf = sum(hf)
    #print(f"total fitness: {tf} \n")

    #mean fit
    mf = tf/len(p)
    #print(f"mean fitness: {mf} \n")

    #hamming distance min
    minHD.append(min(ga.hammingDist(p, s)))
    meanHD.append(sum(ga.hammingDist(p, s))/len(p))

    t+=1

#print(t)


#print(minHD)
#print(meanHD)

ga.representate(bestGen)
print(f"Best Hamming Distance Fitness: {sc} \n")
#print(f"total fitness: {tf} \n")
#print(f"mean fitness: {mf} \n")

xVal1 = [val for val in range(len(meanHD))]
yVal1 = meanHD
yVal2 = minHD

fig, ax = plt.subplots()
ax.plot(xVal1, yVal1, label="Mean Hamming Distance")
ax.plot(xVal1, yVal2, label="Min Hamming Distance")
#defining the axis space
ax.axis([0, 180, 0, 12])

ax.legend(shadow=True, fancybox=True)
plt.title("Not Best included pc=0.5, pm=0.01")
plt.xlabel("Generation")
plt.ylabel("Hamming Distance")

plt.show()