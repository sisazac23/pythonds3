# In the definition of fractions we assumed that negative fractions have a negative numerator and a positive denominator. 
# Using a negative denominator would cause some of the relational operators to give incorrect results. In general, this is an unnecessary constraint.
# Modify the constructor to allow the user to pass a negative denominator so that all of the operators continue to work properly.


class Fraction:
    def __init__(self, top, bottom):
        if type(self.num) != int or type(self.den) != int:
            raise TypeError("Numerator and denominator must be integers")
        self.num = top
        self.den = bottom
        common = self.gcd(self.num, self.den)
        self.num = self.num // common
        self.den = self.den // common
        if self.den < 0:
            self.num = -self.num
            self.den = -self.den
 

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
    
    def __gt__(self, other_fraction):
        return self.num/self.den > other_fraction.num/other_fraction.den
    
    def __ge__(self, other_fraction):
        return self.num/self.den >= other_fraction.num/other_fraction.den
    
    def __lt__(self, other_fraction):
        return self.num/self.den < other_fraction.num/other_fraction.den
    
    def __le__(self, other_fraction):
        return self.num/self.den <= other_fraction.num/other_fraction.den
    
    def __ne__(self, other_fraction):
        return self.num/self.den != other_fraction.num/other_fraction.den
    
    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - \
            self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)
    
    def __mul__(self,other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)
    
    def __truediv__(self,other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        return Fraction(new_num, new_den)