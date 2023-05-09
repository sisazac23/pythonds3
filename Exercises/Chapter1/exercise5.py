# Implement the simple methods get_num and get_den that will return the numerator and denominator of a fraction.

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den