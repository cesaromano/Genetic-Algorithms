#hamming distance
from GeneticAlgorithm import *

n = 8
ga = GeneticAlgorithm(n)

s = ['111101101111']
p = ['101001010101', '101011001001', '111010100100', '010100101011', '011101000110', '011001101100', '110010110100', '110000111010']

h = ga.hammingDist(p, s)
print(h)

hf = ga.hammingFit(p, s)

print(hf)