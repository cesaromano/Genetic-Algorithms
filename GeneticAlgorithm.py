
import math
from random import randint
from encoder import Encoder

class GeneticAlgorithm:
    """Contains most of the methods that drive the main
    algorithm"""

    def __init__(self, n=10):
        self.n = n

    def randPopulation(self):

        p = []
        aux = []
        t = 0
        #c = 0
        while t < self.n:
            randVal = randint(0, 100)
            if randVal in aux:
                #c+=1
                pass
            else:
                p.append([Encoder().binToGray(format((randVal), 'b'))])
                aux.append(randVal)
                t+=1

        return p

    def fitness(self, p):

        for x in range(0, len(p)):
            p[x].append(GeneticAlgorithm().evalFunc(p[x][0]))

        return p

    def linRank(self, p):

        fv = [p[x][1] for x in range(0, len(p))]
        i = fv[:]
        fv = sorted(fv)
        lr = [round((2*x)/(len(p)*(len(p)-1)), 5) for x in range(0, len(p))]

        for x in range(0, len(p)):
            val = i[x]
            p[x].append(fv.index(val))
            p[x].append(lr[fv.index(val)])

        return p

    def evalFunc(self, x):
        """Evaluates the function"""

        x = int(Encoder().grayToBin(x), 2)/100

        g = (2**(-2*((x-0.1)/0.9)**2))*(math.sin(5*math.pi*x))**6

        return x