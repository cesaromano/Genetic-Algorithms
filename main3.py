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
t = 0
ni = 50
metric = []

while t < ni:
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
    rn = 6
    p = ga.tournSelec(p, lr, rn)
    #print(f"tournament selection: {p} \n")

    #Roulete wheel selection
    #p = ga.rouleteWheelSel(p, f)
    #print(f"roulete wheel selection: {p} \n")

    #crossover, probability crossover must be betwen 0.6 < pc < 1.0
    pc = 0.2
    p = ga.crossover(p, pc)
    #print(f"crossover: {p} \n")

    #mutation
    pm =0.01
    p = ga.mutate(p, pm)
    #print(f"mutation: {p} \n")

    #adding the best of the generation to the next population
    p[0] = bIndP
    #evalBInd = ga.evalFunc(bInd[0], bInd[1])
    #print(evalBInd)

    #append last fitness value to p index 1
    f = ga.fitness(p)

    metric.append(sum(f)/len(f))

    print(f"last iter population: {f} \n")
    print(p)

    t+=1

xVal = [val for val in range(ni)]
yVal = metric

fig, ax = plt.subplots()
ax.plot(xVal, yVal, label="Mean fitness")
#defining the axis space
ax.axis([0, ni, 0, 1200000])

ax.legend(shadow=True, fancybox=True)
plt.title(f"Best Included pc={pc}, pm={pm}, p={n}, ri={rn}")
plt.xlabel("Generation")
plt.ylabel("f(x, y)")

plt.show()