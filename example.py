import random
import numpy as np

example = [['1101010', 0.02, 4, 0.08889], ['0100000', 0.01, 2, 0.04444], 
['0010000', 0.86, 9, 0.2], ['0110001', 0.46, 7, 0.15556], ['0000111', 0.12, 5, 0.11111], 
['1001010', 0.02, 6, 0.13333], ['0110111', 0.01, 8, 0.17778], ['1101001', 0.0, 2, 0.04444], 
['0111111', 0.0, 0, 0.0], ['0011111', 0.0, 0, 0.0]]

#population fitness
popFit = [example[ind][1] for ind in example]
print(popFit)
#popFit = sum(popFit)
#each chromossome probability
#indProbability = [example[ind][1]/popFit for ind in example]

#pInter = [np.random.choice(example, p=indProbability) for ind in example]

#print(pInter)