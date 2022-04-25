class Encoder:
    """Encode an int number to gray code 
    ands visceversa"""

    def __init__(self):

        pass

    def binAdd(self, x, y):
        """add one by one binary digits"""

        #parse str value to int
        x = int(x)
        y = int(y)

        if x and y == 1:
            return str(0)

        return str(x+y)

    def grayToBin(self, gray):
        """convert a binary sequence to gray code sequence"""

        if len(gray) == 1:
            return gray
        
        #first bin of the new sequence is the same bin
        binl = []
        binl.append(gray[0])
        #second bin of the new sequence is the addition betwen two first bins
        result = Encoder.binAdd(self, gray[0], gray[1])
        binl.append(result)

        #addition betwen each bin result and next bin in the binary sequence
        for i in range(1, len(gray)-1):

            j = i+1
            result2 = Encoder.binAdd(self, result, gray[j])
            binl.append(result2)
            result = result2

        #parse list to string
        listToBinStr = ''.join(binl)

        return listToBinStr

    def binToGray(self, bin):
        """convert a gray code sequence to binary sequence"""

        if len(bin) == 1:
            return bin

        #first bin of the new sequence is the same bin
        binl = []
        binl.append(bin[0])

        #addition betwen each gray bin sequence
        for i in range(0, len(bin)-1):

            j = i+1
            result = Encoder.binAdd(self, bin[i], bin[j])
            binl.append(result)

        #parse list to string
        listToGrayStr = ''.join(binl)

        return listToGrayStr