
import matplotlib.pyplot as plt
import math
import random
from encoder import Encoder
import numpy as np

class GeneticAlgorithm:
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

    def randPopulation(self):
        """Creates a population, a list of ten
        lists of individuals, each individual chromosome is
        stored in the index 0"""

        p = []
        aux = []
        t = 0

        while t < self.n:
            randVal = random.randint(0, 100)
            if randVal in aux:
                pass
            else:
                #Append a gray binary value if it isn't repeated
                p.append([Encoder().binToGray(format((randVal), 'b')), 0, 0, 0])
                aux.append(randVal)
                t+=1

        return p

    def fitness(self, p):
        """Evaluates each individual in population"""

        for x in range(len(p)):
            #the value is stored in the index 1
            p[x][1] = GeneticAlgorithm().evalFunc(p[x][0])

        return p

    def best(self, p):
        """Get the best chromosome of the population"""

        #list of individuals evaluations
        fv = [p[eval][1] for eval in range(len(p))]
        #best individual evaluation
        best = max(fv)
        i = fv.index(best)
        #getting chromosome
        bChromosome = p[i][0]

        return bChromosome

    def linRank(self, p):
        """generates each individual linear ranking"""

        #list of individuals evaluations
        fv = [p[eval][1] for eval in range(len(p))]
        i = fv[:]
        fv = sorted(fv)
        #list of linear rankings based on the number of individuals
        lr = [round((2*x)/(len(p)*(len(p)-1)), 5) for x in range(len(p))]

        for x in range(0, len(p)):
            val = i[x]
            #adding the ranking value to index 2
            p[x][2] = fv.index(val)
            #adding the linear ranking value to index 3
            p[x][3] = lr[fv.index(val)]

        return p

    def rouleteWheelSel(self, p):
        """roulete wheel selection method"""

        #list of individuals evaluations
        fv = [p[eval][1] for eval in range(len(p))]
        #getting the sum of all elemnts in fv
        fv = sum(fv)
        #getting each chromossome probability
        indProbability = [p[ind][1]/fv for ind in range(len(p))]
        aux = [x for x in range(len(p))]
        #getting the index of individuals selected
        indSelected = [np.random.choice(aux, p=indProbability) for ind in range(len(p))]
        #individuals selected added to a new population list
        aux = [p[indSelected[x]] for x in range(len(p))]

        return aux

    def tournSelec(self, p, rn=3):
        """tournament selection method"""

        aux = []

        for x in range(len(p)):
            #three random int samples are generated
            rInd = random.sample(range(0, 10), rn)
            #getting 3 random individuals based on the rInd index numbers
            best = [p[rInd[x]][3] for x in range(len(rInd))]
            #getting the best index individual based on the mas value
            i = best.index(max(best))

            aux.append(p[rInd[i]])

        return aux

    def crossover(self, p, pc=0.6):
        """crossover method, first algorithm to variate the population"""

        #generating a probability value for each pair of individuals in population
        rPairs = [round(random.random(), 1) for x in range(int(len(p)/2))]
        #determining the point cross
        crossPoint = [random.randint(1, 6) for x in range(int(len(p)/2))]

        for x in range(int(len(p)/2)):
            
            if rPairs[x] <= pc:
                
                #taking the index of pairs with crossover probabilities
                p1 = x*2
                p2 = (x*2)+1
                
                #storing their chromosomes
                chromosome1 = p[p1][0]
                chromosome2 = p[p2][0]
                 
                #slicing the chromosomes from their crosspoints
                cromoSlice1 = chromosome1[crossPoint[x]:]
                cromoSlice2 = chromosome2[crossPoint[x]:]
                 
                #replacing the chromosomes on their places
                p[p1][0] = chromosome1.replace(chromosome1[crossPoint[x]:], cromoSlice2, 1)
                p[p2][0] = chromosome2.replace(chromosome2[crossPoint[x]:], cromoSlice1, 1)

        return p

    def mutBit(self, chromosome, rVal, pm):
        """give a chromosome mutated to mutate method
        when the random value is less than pm 'mutation probability'"""
        
        for x in range(7):
            if rVal[x] <= pm:
                
                lChrom = list(chromosome)
                lChrom[x] = str((int(chromosome[x])-1)**2)
                chromosome = ''.join(lChrom)
                
                return chromosome

    def mutate(self, p, pm=0.02):
        """matation method, second algorithm to variate the population"""

        for x in range(len(p)):
            #generating a probability value for each bite
            rVal = [round(random.random(), 2) for x in range(7)]
            #getting each individual chromosome of population
            chromosome = p[x][0]
            #instantiating a mutByte object
            mutBit1 = GeneticAlgorithm().mutBit(chromosome, rVal, pm)
             
            if (mutBit1 is not None):
                #replacing chromosome when mutByte return a chromosome
                p[x][0] = mutBit1

        return p

    def evalFunc(self, x):
        """Evaluates a given value"""

        #parse str to int when necessary
        if type(x) == str:
            x = int(Encoder().grayToBin(x), 2)/100

        y = round((2**(-2*((x-0.1)/0.9)**2))*(math.sin(5*math.pi*x))**6, 2)

        return y

    def plotFunct(self):
        """Return 'ax', a the subplot function in the figure"""
        
        #getting the x and y values
        xVal = [val for val in np.arange(self.i, self.f, self.p)]
        yVal = [GeneticAlgorithm().evalFunc(val) for val in np.arange(self.i, self.f, self.p)]

        fig, ax = plt.subplots()
        ax.plot(xVal, yVal)
        #defining the axis space
        ax.axis([0, 1.1, 0, 1.1])
        
        return ax

    def addPointPlot(self, px, py):
        """Return 'ax', a subplot with the function with given points"""
        
        ax = GeneticAlgorithm().plotFunct()
        #giving x and y points
        ax.scatter(px, py, s=50)
        
        return ax