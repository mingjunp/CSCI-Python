# Mingjun Pan, panxx422

# I understand this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing
# any aspect of the examination with anyone will result in failing the course.
# I further certify that this program represents my own work none it was
# obtained from any source other than material presented as part of the
# course.
import math

class Complex():
    def __init__(self, real=0, imag=0):
        self.__real = real
        self.__imag = imag

    def __repr__(self):
        if self.__real == 0:
            return str(self.__imag) + 'i'
        if self.__imag == 0:
            return str(self.__real)
        elif self.__imag > 0:
            return str(self.__real) + ' + ' + str(self.__imag) + 'i'
        elif self.__imag < 0:
            return str(self.__real) + '' + str(self.__imag) + 'i'

    def get_real(self):
        return self.__real

    def get_imag(self):
        return self.__imag

    def set_real(self, real):
        self.__real = real

    def set_imag(self, imag):
        self.__imag = imag

    def __add__(self, other):
        return Complex(self.get_real() + other.get_real(), self.get_imag() + other.get_imag())

    def __mul__(self, other):
        return Complex(self.get_real() * other.get_real() + self.get_imag() * other.get_imag() * (-1),
                       self.get_real() * other.get_imag() + self.get_imag() * other.get_real())

    def __abs__(self):
        return math.sqrt(self.get_real() * self.get_real() + self.get_imag() * self.get_imag())
