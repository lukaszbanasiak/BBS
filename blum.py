import sys
import random
import primes


class BlumBlumShub(object):

    def getPrime(self, bits):
        while True:
            p = primes.bigppr(bits)
            if p & 3 == 3:
                return p

    def generateN(self, bits):
        p = self.getPrime(bits/2)
        while 1:
            q = self.getPrime(bits/2)
            if p != q:
                return p * q

    def __init__(self, bits):
        self.n = self.generateN(bits)
        print "n = " + repr(self.n)
        length = self.bitLen(self.n)
        seed = random.getrandbits(length)
        self.setSeed(seed)

    def setSeed(self, seed):
        self.state = seed % self.n

    def bitLen(self, x):
        assert x > 0
        q = 0
        while x:
            q += 1
            x >>= 1
        return q

    def next(self, numBits):
        result = 0
        for i in xrange(numBits):
            self.state = (self.state**2) % self.n
            result = (result << 1) | (self.state&1)

        return result

if __name__ == "__main__":

    number_blum = int(raw_input('Blum number: '))
    number_bit = int(raw_input('Numbers of bits: '))
    number_amount = int(raw_input('Numbers to generate: '))

    bbs = BlumBlumShub(number_blum)

    for i in xrange (number_amount):
        print(bin(bbs.next(number_bit)))
