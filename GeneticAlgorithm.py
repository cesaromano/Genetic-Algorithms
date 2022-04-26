
import math
from encoder import Encoder

class GeneticAlgorithm:
    """Contains most of the methods that drive the main
    algorithm"""

    def __init__(self):
        pass

    def evalFunc(self, x):
        """Evaluates the function"""

        x = int(Encoder().grayToBin(x), 2)/100

        g = (2**(-2*((x-0.1)/0.9)**2))*(math.sin(5*math.pi*x))**6

        return x