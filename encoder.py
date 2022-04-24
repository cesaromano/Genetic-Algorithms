class Encoder:
    """Encode an int number to gray code 
    ands visceversa"""

    def __init__(self):

        pass

    def binAdd(self, x, y):

        x = int(x)
        y = int(y)

        if x and y == 1:
            return str(0)

        return str(x+y)

    def grayToBin(self, gray):

        if len(gray) == 1:
            return gray
        
        binl = []
        binl.append(gray[0])
        result = Encoder.binAdd(self, gray[0], gray[1])
        binl.append(result)

        for i in range(1, len(gray)-1):

            j = i+1
            result2 = Encoder.binAdd(self, result, gray[j])
            binl.append(result2)
            result = result2

        return int(''.join(binl), 2)