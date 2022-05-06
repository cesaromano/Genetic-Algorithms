
import random
import numpy as np
import cv2 as cv

class GeneticAlgorithm1:
    """Contains most of the methods that drive the main1
    algorithm"""

    def __init__(self, n=10):
        
        #n: number of individuals
        self.n = n

    def randBitPopulation(self):
        """Generates a new population of n individuals"""

        bit = ('010101010101')
        p = [''.join(random.sample(bit, 12)) for ind in range(self.n)]

        return p

    def compBits(self, sInd, pInd):
        """Help hammingDist comparing each vector with the solution vector"""

        counter = 0

        for bit in range(len(sInd)):
            if pInd[bit] != sInd[bit]:
                counter += 1

        return counter

    def hammingDist(self, p, s):
        """Calculates the hamming distance for each chromosome
        """

        h = []

        for ind in range(len(p)):
            #uses the compBits function to compare each vector with the solution vector
            h.append(GeneticAlgorithm1().compBits(s[0], p[ind]))

        return h

    def hammingFit(self, p, s, iFit):
        """Fitness the population based on the hamming
        distance measure and the desired measure"""

        #getting each chromosome hamming distance
        h = GeneticAlgorithm1().hammingDist(p, s)
        #diference betwen hamming hamming distance and ideal fitness measure
        hf = [iFit-h[hd] for hd in range(len(h))]

        return hf

    def fitness(self, p):
        """Evaluates each individual in population"""

        for x in range(len(p)):
            #the value is stored in the index 1
            p[x][1] = GeneticAlgorithm1().evalFunc(p[x][0])

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

    def rouleteWheelSel(self, p, hf):
        """roulete wheel selection method"""

        #getting the sum of all elemnts in fv
        fv = sum(hf)
        #getting each chromossome probability
        indProbability = [hf[ind]/fv for ind in range(len(hf))]
        aux = [x for x in range(len(hf))]
        #getting the index of individuals selected
        indSelected = [np.random.choice(aux, p=indProbability) for ind in range(len(hf))]
        #individuals selected added to a new population list
        aux = [p[indSelected[x]] for x in range(len(hf))]

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
                chromosome1 = p[p1]
                chromosome2 = p[p2]
                 
                #slicing the chromosomes from their crosspoints
                cromoSlice1 = chromosome1[crossPoint[x]:]
                cromoSlice2 = chromosome2[crossPoint[x]:]
                 
                #replacing the chromosomes on their places
                p[p1] = chromosome1.replace(chromosome1[crossPoint[x]:], cromoSlice2, 1)
                p[p2] = chromosome2.replace(chromosome2[crossPoint[x]:], cromoSlice1, 1)

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
            rVal = [round(random.random(), 2) for x in range(12)]
            #getting each individual chromosome of population
            chromosome = p[x]
            #instantiating a mutByte object
            mutBit1 = GeneticAlgorithm1().mutBit(chromosome, rVal, pm)
             
            if (mutBit1 is not None):
                #replacing chromosome when mutByte return a chromosome
                p[x] = mutBit1

        return p

    def representate(self, p):
        """Representate as jpg image each chromosome"""

        for ind in range(len(p)):
            #parse each chromosome string to list and then to np.array
            img = np.array(list(p[ind]), dtype='uint8')
            #reshape each 1d vector to a 2d 4x3 size
            img = np.reshape(img, (4, 3))
            #replacing 1 to 200 in order to get a constrasted image
            img = np.where(img==1, 200, img)
            height, width = img.shape[:2]
            #amplifying the image using INTER_NEAREST mask
            img = cv.resize(img,(50*width, 50*height), interpolation = cv.INTER_NEAREST)
            #showing the image
            cv.imwrite(f'example{ind}.jpg', img)
            cv.imshow(f'Image {1}', img)
            cv.waitKey(0)
            cv.destroyAllWindows