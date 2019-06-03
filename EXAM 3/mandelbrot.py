# Mingjun Pan, panxx422

# I understand this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing
# any aspect of the examination with anyone will result in failing the course.
# I further certify that this program represents my own work none it was
# obtained from any source other than material presented as part of the
# course.
class Mandelbort():
    def __init__(self, c, limit=50):
        self.__colormap = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black']
        self.__cardinality = 0
        self.__limit = limit

        z = c
        for i in range(limit):
            z = z * z + c
            # print(z.__repr__())
            if z.__abs__() <= 2.0:
                self.__cardinality += 1

    def get_color(self):
        # print(int(self.__cardinality / self.__limit * (len(self.__colormap)-1)))
        return self.__colormap[round(self.__cardinality / self.__limit * (len(self.__colormap) - 1))]
