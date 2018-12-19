from string import hexdigits

class NumberConverter(object):

    def __init__(self, number):
        self.number = number

    def dectobin(self):
        """ 
        Determine the size base 2 required
        Subtract subsequent base 2 until gone
        Return bin as string

        i.e. 1220
        2**10 = 1024 -> 1220 - 1024 = 196
        2**7 = 128 ->  196 - 128 = 68
        2^6 = 64 -> 68 - 64 = 4
        2^2 = 4 - 4 = 0
        return 10011000100
        """
        output_string = ""
        # determine base size
        basesize = 0
        while 2**basesize <= self.number:
            basesize += 1

        while basesize > -1:
            if 2**basesize <= self.number:
                output_string += '1'
                self.number -= 2**basesize
            else:
                output_string += '0'
            basesize -= 1
        return output_string


    def dectohex(self):

        touse = hexdigits[:16]
        output_string = ""
        basesize = 0

        while 16**basesize <= self.number:
            basesize += 1

        while basesize > -1:
            if 16**basesize <= self.number:
                divis, remain = self.helperfunction(16**basesize, self.number) 
                # if divis is greater than 16 need to carry over
                try:
                    output_string += hexdigits[divis]
                    self.number = remain
                except IndexError:
                    output_string += '0'
            basesize -= 1
        return output_string
   

    def helperfunction(self, denom, numer):

        divisor = numer / denom
        remainder = numer % denom
        return divisor, remainder

    def hextodec(self):
        pass

    def hextobin(self):
        pass

    def bintohex(self):
        pass

    def bintodec(self):
        pass


        
test = NumberConverter(1220)
print(test.dectohex())
