
import matplotlib.pyplot as plt
import math
import random
from encoder3 import Encoder3
import numpy as np
import cv2 as cv

class GeneticAlgorithm3:
    """Contains most of the methods that drive the main
    algorithm"""

    def __init__(self, n=10, i=0.0, f=1.0, p=0.001):
        """
        n: number of individuals
		i: range lower limit
		f: range upper limit
		p: range step
		"""
        self.i = i
        self.f = f
        self.p = p
        self.n = n

    def intToGray(self, ind):

        if ind < 0:
            ind = Encoder3().binToGray(format((abs(ind)), 'b'))
            grayInd = '1' + ind

        elif ind == 0:
            return '00000'

        else:
            ind = Encoder3().binToGray(format((ind), 'b'))
            grayInd = '0' + ind

        return grayInd

    def grayToInt(self, coordinate):

        if coordinate == '00000':
            return 0
        elif coordinate[0] == '1':
            return int(Encoder3().grayToBin(coordinate[1:]), 2)
        elif coordinate[0] == '0':
            return (int(Encoder3().grayToBin(coordinate[1:]), 2))*-1

    def randGrayPopulation(self):

        p = [[GeneticAlgorithm3().intToGray(random.randint(-10, 10)), 
            GeneticAlgorithm3().intToGray(random.randint(-10, 10))] for x in range(self.n)]

        return p

    def evalFunc(self, x, y):
        """Evaluates a given value"""

        #parse str to int when necessary
        if type(x) == str:
            x = GeneticAlgorithm3().grayToInt(x)
            y = GeneticAlgorithm3().grayToInt(y)

        return (1-x)**2 + 100*(y-(x**2))**2

    def fitness(self, p):
        """Evaluates each individual in population"""

        f = []

        for ind in range(len(p)):
            #the value is stored in the index 1
            indFit = GeneticAlgorithm3().evalFunc(p[ind][0], p[ind][1])
            f.append(indFit)

        return f

    def best(self, p, f):
        """Get the best chromosome of the population"""

        #best individual evaluation
        best = min(f)
        i = f.index(best)
        #getting chromosome
        bInd = p[i]

        return bInd

    def linRank(self, f):
        """generates each individual linear ranking"""

        #list of individuals evaluations
        i = f[:]
        f = sorted(f, reverse=True)
        #list of linear rankings based on the number of individuals
        r = []
        lr = []
        l = [round((2*x)/(len(f)*(len(f)-1)), 5) for x in range(len(f))]

        for x in range(len(f)):
            val = i[x]
            #adding the ranking value to index 2
            r.append(f.index(val))
            #adding the linear ranking value to index 3
            lr.append(l[f.index(val)])

        return r, lr

    def rouleteWheelSel(self, p, f):
        """roulete wheel selection method"""

        #getting the sum of all elemnts in fv
        ft = sum(f)
        #getting each chromossome probability
        indProbability = [f[ind]/ft for ind in range(len(p))]
        indProbability = 1 - np.array(indProbability)
        aux = [x for x in range(len(p))]
        #getting the index of individuals selected
        indSelected = [np.random.choice(aux, p=indProbability) for ind in range(len(p))]
        #individuals selected added to a new population list
        aux = [p[indSelected[x]] for x in range(len(p))]

        return aux

    def tournSelec(self, p, lr, rn=3):
        """tournament selection method"""

        aux = []

        for x in range(len(p)):
            #three random int samples are generated
            rInd = random.sample(range(len(p)), rn)
            #getting 3 random individuals based on the rInd index numbers
            best = [lr[rInd[x]] for x in range(len(rInd))]
            #getting the best index individual based on the max value
            i = best.index(max(best))

            aux.append(p[rInd[i]])

        return aux

    def crossover(self, p, pc=0.6):
        """crossover method, first algorithm to variate the population"""

        #generating a probability value for each pair of individuals in population
        rPairs = [round(random.random(), 1) for x in range(int(len(p)/2))]
        #determining the point cross
        crossPoint = [random.randint(1, 3) for x in range(int(len(p)/2))]

        for x in range(int(len(p)/2)):
            
            if rPairs[x] <= pc:
                
                #taking the index of pairs with crossover probabilities
                p1 = x*2
                p2 = (x*2)+1
                
                #storing their chromosomes
                chromosomex1 = p[p1][0]
                chromosomey1 = p[p1][1]
                chromosomex2 = p[p2][0]
                chromosomey2 = p[p2][1]
                 
                #slicing the chromosomes from their crosspoints
                cromoSlicex1 = chromosomex1[crossPoint[x]:]
                cromoSlicey1 = chromosomey1[crossPoint[x]:]
                cromoSlicex2 = chromosomex2[crossPoint[x]:]
                cromoSlicey2 = chromosomey2[crossPoint[x]:]
                 
                #replacing the chromosomes on their places
                p[p1][0] = chromosomex1.replace(chromosomex1[crossPoint[x]:], cromoSlicex2, 1)
                p[p1][1] = chromosomey1.replace(chromosomey1[crossPoint[x]:], cromoSlicey2, 1)
                p[p2][0] = chromosomex2.replace(chromosomex2[crossPoint[x]:], cromoSlicex1, 1)
                p[p2][1] = chromosomey2.replace(chromosomey2[crossPoint[x]:], cromoSlicey1, 1)

        return p

    def mutBit(self, chromosome, rVal, pm):
        """give a chromosome mutated to mutate method
        when the random value is less than pm 'mutation probability'"""
        
        for x in range(5):
            if rVal[x] <= pm:
                
                lChrom = list(chromosome)
                lChrom[x] = str((int(chromosome[x])-1)**2)
                chromosome = ''.join(lChrom)
                
                return chromosome

    def mutate(self, p, pm=0.02):
        """matation method, second algorithm to variate the population"""

        for x in range(len(p)):
            #generating a probability value for each bite
            rValx = [round(random.random(), 2) for x in range(5)]
            rValy = [round(random.random(), 2) for x in range(5)]
            #getting each individual chromosome of population
            chromosomex = p[x][0]
            chromosomey = p[x][1]
            #instantiating a mutByte object
            mutBitx = GeneticAlgorithm3().mutBit(chromosomex, rValx, pm)
            mutBity = GeneticAlgorithm3().mutBit(chromosomey, rValy, pm)
             
            if (mutBitx is not None):
                #replacing chromosome when mutByte return a chromosome
                p[x][0] = mutBitx

            if (mutBity is not None):
                #replacing chromosome when mutByte return a chromosome
                p[x][1] = mutBity

        return p

    def plotFunct(self):
        """Return 'ax', a the subplot function in the figure"""
        
        #getting the x and y values
        xVal = [val for val in np.arange(self.i, self.f, self.p)]
        yVal = [GeneticAlgorithm3().evalFunc(val) for val in np.arange(self.i, self.f, self.p)]

        fig, ax = plt.subplots()
        ax.plot(xVal, yVal)
        #defining the axis space
        ax.axis([0, 1.1, 0, 1.1])
        
        return ax

    def addPointPlot(self, px, py):
        """Return 'ax', a subplot with the function with given points"""
        
        ax = GeneticAlgorithm3().plotFunct()
        #giving x and y points
        ax.scatter(px, py, s=50)
        
        return ax