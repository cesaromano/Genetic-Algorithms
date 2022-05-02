import random

example = [['1101010', 0.02, 4, 0.08889], ['0100000', 0.01, 2, 0.04444], 
['0010000', 0.86, 9, 0.2], ['0110001', 0.46, 7, 0.15556], ['0000111', 0.12, 5, 0.11111], 
['1001010', 0.02, 6, 0.13333], ['0110111', 0.01, 8, 0.17778], ['1101001', 0.0, 2, 0.04444], 
['0111111', 0.0, 0, 0.0], ['0011111', 0.0, 0, 0.0]]

fv = [example[x][1] for x in range(0, len(example))]
i = fv[:]
fv = sorted(fv)

print(fv)

lr = [round((2*x)/(len(example)*(len(example)-1)), 5) for x in range(len(example))]

print(lr)

pInter = []

for x in range(len(example)):
    #three random individuals are taken
    rInd = random.sample(range(0, 10), 3)
    best = [example[rInd[x]][3] for x in range(len(rInd))]
    i = best.index(max(best))
    pInter.append(example[rInd[i]])
    
print(pInter)
l = list(range(0, 6))
print(l)
#print(random.sample(l, 8))
crossPoint = [random.randint(1, 6) for x in range(int(len(pInter)/2))]
print(crossPoint)