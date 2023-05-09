# In many ways it would be better if all fractions were maintained in lowest terms right from the start. Modify the constructor for the Fraction class so that GCD is used to reduce fractions immediately. 
# Notice that this means the __add__ function no longer needs to reduce. Make the necessary modifications.

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
        common = self.gcd(self.num, self.den)
        self.num = self.num // common
        self.den = self.den // common

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def gcd(self, m, n):
        while m % n != 0:
            old_m = m
            old_n = n

            m = old_n
            n = old_m % old_n
        return n
    
    def add(self, other_fraction):
        new_num = self.num * other_fraction.den + \
            self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)