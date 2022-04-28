
import math
import random
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
            randVal = random.randint(0, 100)
            if randVal in aux:
                #c+=1
                pass
            else:
                p.append([Encoder().binToGray(format((randVal), 'b')), 0, 0, 0])
                aux.append(randVal)
                t+=1

        return p

    def fitness(self, p):

        for x in range(0, len(p)):
            p[x][1] = GeneticAlgorithm().evalFunc(p[x][0])

        return p

    def linRank(self, p):

        fv = [p[x][1] for x in range(0, len(p))]
        i = fv[:]
        fv = sorted(fv)
        lr = [round((2*x)/(len(p)*(len(p)-1)), 5) for x in range(0, len(p))]

        for x in range(0, len(p)):
            val = i[x]
            p[x][2] = fv.index(val)
            p[x][3] = lr[fv.index(val)]

        return p

    def tournSelec(self, p, rn=3):

        pInter = []

        for x in range(len(p)):
            rInd = random.sample(range(0, 10), rn)
            best = [p[rInd[x]][3] for x in range(len(rInd))]
            i = best.index(max(best))
            pInter.append(p[rInd[i]])

        return pInter

    def crossover(self, pInter, pc=0.6):

        rPairs = [round(random.random(), 1) for x in range(int(len(pInter)/2))]
        crossPoint = random.sample(range(1, 6), 5)

        #print(f"pInter bef: {pInter}")

        #print(rPairs)
        #print(crossPoint)

        for x in range(int(len(pInter)/2)):
            
            if rPairs[x] <= pc:
                
                p1 = x*2
                p2 = (x*2)+1
                
                cromossome1 = pInter[p1][0]
                cromossome2 = pInter[p2][0]
                #print(cromossome1, cromossome2)
                 
                cromoSlice1 = cromossome1[crossPoint[x]:]
                cromoSlice2 = cromossome2[crossPoint[x]:]
                #print(cromoSlice1, cromoSlice2)
                 
                pInter[p1][0] = cromossome1.replace(cromossome1[crossPoint[x]:], cromoSlice2, 1)
                pInter[p2][0] = cromossome2.replace(cromossome2[crossPoint[x]:], cromoSlice1, 1)

        #print(f"pInter aft: {pInter}")

        return pInter

    def mutByte(self, chromosome, rVal, pm):
        
        lVal = []
        
        for x in range(7):
                                             
            if rVal[x] <= pm:
                
                lChrom = list(chromosome)
                lChrom[x] = str((int(chromosome[x])-1)**2)
                chromosome = ''.join(lChrom)
                #lVal.append(rVal[x])
                
                return chromosome

    def mutate(self, pInter, pm=0.02):

        for x in range(len(pInter)):
            rVal = [round(random.random(), 2) for x in range(7)]
            chromosome = pInter[x][0]
            #print(chromosome)
            # #print(rVal)
            
            mutByte1 = GeneticAlgorithm().mutByte(chromosome, rVal, pm)
            
            #print(mutByte1)
             
            if (mutByte1 is not None):
                pInter[x][0] = mutByte1
                #print(pInter[x][0])

        return pInter

    def evalFunc(self, x):
        """Evaluates the function"""

        x = int(Encoder().grayToBin(x), 2)/100

        g = (2**(-2*((x-0.1)/0.9)**2))*(math.sin(5*math.pi*x))**6

        return x