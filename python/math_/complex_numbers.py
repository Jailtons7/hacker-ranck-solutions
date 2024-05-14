"""
For this challenge, you are given two complex numbers, and you have to print the result of their
addition, subtraction, multiplication, division and modulus operations.

The real and imaginary precision part should be correct up to two decimal places.

Sample Input:
2 1
5 6

Sample Output:
7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i
"""
from __future__ import annotations


class Complex(object):
    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no: Complex):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real, imaginary)

    def __sub__(self, no: Complex):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return Complex(real, imaginary)

    def __mul__(self, no: Complex):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imaginary)

    def __truediv__(self, no: Complex):
        conjugate = Complex(no.real, -no.imaginary)
        numerator = self.__mul__(conjugate)
        denominator = no.__mul__(conjugate)
        return Complex(numerator.real / denominator.real, numerator.imaginary / denominator.real)

    def mod(self):
        real = (self.real ** 2 + self.imaginary ** 2) ** 0.5
        return Complex(real, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % self.real
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % self.imaginary
            else:
                result = "0.00-%.2fi" % abs(self.imaginary)
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
