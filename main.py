from encoder import Encoder

test1 = Encoder()

#print(int(test1.grayToBin(str(1000)), 2))

#print(test1.grayToBin(bin))

#print(test1.binToGray(bin))

bins = [format(x, "b") for x in range(0, 16)]
grays = []
decimal = []

for each in range(0, len(bins)):
    bintogray = test1.binToGray(bins[each])
    print(bintogray)
    grays.append(bintogray)

for each in range(0, len(grays)):
    graytobin = test1.grayToBin(grays[each])
    print(graytobin)
    bintodecimal = int(graytobin, 2)/100
    print(bintodecimal)