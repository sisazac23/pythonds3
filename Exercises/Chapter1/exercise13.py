# Research the __repr__ method. How does it differ from __str__? 
# When is it used? Implement __repr__.

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
    
    def __repr__(self):
        return str(self.num) + "/" + str(self.den)

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
    
    def __radd__(self, other_fraction):
        new_num = other_fraction.den * self.num + \
            other_fraction.num * self.den
        new_den = other_fraction.den * self.den
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