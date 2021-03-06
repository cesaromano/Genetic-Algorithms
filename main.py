import matplotlib.pyplot as plt
from encoder import Encoder
from GeneticAlgorithm import *

#Initialize a non repeated random population of ten individuals, index 0:cromossome
n = 10
ga = GeneticAlgorithm(n)
p = ga.randGrayPopulation()

#append fitness value to p index 1
p = ga.fitness(p)
#best chromosome population value
bChromosomeP = '0000000'
#counter
t = 0
ni = 50

metric = []

while t < ni:

    #getting the best individual of the generation
    bChromosome = ga.best(p)
    evalBChromosome = ga.evalFunc(int(Encoder().grayToBin(bChromosome), 2)/100)
    evalBChromosomeP = ga.evalFunc(int(Encoder().grayToBin(bChromosomeP), 2)/100)
    if evalBChromosome > evalBChromosomeP:
        bChromosomeP = bChromosome

    #append ranking and linear ranking values to p, index 2: rank, index 3: linRank
    p = ga.linRank(p)

    #Roulete wheel selection
    #p = ga.rouleteWheelSel(p)

    #Tournament selection, rn: number of random individuals per tournament
    rn = 9
    p = ga.tournSelec(p, rn)
    #print(f"tournament selection: {p} \n")

    #crossover, probability crossover must be betwen 0.6 < pc < 1.0
    pc = 0.9
    p = ga.crossover(p, pc)
    #print(f"crossover: {p} \n")

    #mutation
    pm =0.02
    p = ga.mutate(p, pm)

    #adding the best of the generation to the next population
    p[0][0] = bChromosomeP

    #append last fitness value to p index 1
    p = ga.fitness(p)
    #print(f"last iter population: {p} \n")

    #ploting the results
    xcoordinates = [int(Encoder().grayToBin(p[x][0]), 2)/100 for x in range(len(p))]
    print(f"x coordinates: {xcoordinates}")
    ycoordinates = [ga.evalFunc(xcoordinates[x]) for x in range(len(p))]
    print(f"y coordinates: {ycoordinates} \n")

    metric.append(sum(ycoordinates)/len(ycoordinates))



    #ga.addPointPlot(xcoordinates, ycoordinates)

    #plt.show()

    t += 1

xVal = [val for val in range(ni)]
yVal = metric

fig, ax = plt.subplots()
ax.plot(xVal, yVal, label="Mean fitness")
#defining the axis space
ax.axis([0, ni, 0, 1.0])

ax.legend(shadow=True, fancybox=True)
plt.title(f"Not Best Included pc={pc}, pm={pm}, p={n}, ri={rn}")
plt.xlabel("Generation")
plt.ylabel("f(x)")

plt.show()