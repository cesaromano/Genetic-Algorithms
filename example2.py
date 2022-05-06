import random
from encoder3 import Encoder3
import math

n = 6

def indToGray(ind):

    if ind < 0:
        ind = Encoder3().binToGray(format((abs(ind)), 'b'))
        grayInd = '1' + ind

    elif ind == 0:
        return '00000'

    else:
        ind = Encoder3().binToGray(format((ind), 'b'))
        grayInd = '0' + ind

    return grayInd

def grayToInd(coordinate):

    if coordinate == '00000':
        return 0
    elif coordinate[0] == '1':
        return int(Encoder3().grayToBin(coordinate[1:]), 2)
    elif coordinate[0] == '0':
        return (int(Encoder3().grayToBin(coordinate[1:]), 2))*-1

def randGrayPopulation(n):

    p = [[indToGray(random.randint(-10, 10)), indToGray(random.randint(-10, 10))] for x in range(n)]

    return p

p = randGrayPopulation(n)

def evalFunc(x, y):
    """Evaluates a given value"""

    #parse str to int when necessary
    if type(x) == str:
        x = grayToInd(x)
        print(x)
        y = grayToInd(y)
        print(y)

    return (1-x)**2 + 100*(y-(x**2))**2

print(evalFunc('00000', '00000'))