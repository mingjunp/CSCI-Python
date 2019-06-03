# Mingjun Pan, panxx422

# I understand this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing
# any aspect of the examination with anyone will result in failing the course.
# I further certify that this program represents my own work none it was
# obtained from any source other than material presented as part of the
# course.
import turtle
import mandelbrot
import complex


class Display():
    def __init__(self, size=300):
        turtle.hideturtle()
        turtle.speed(0)
        turtle.pensize(1)
        turtle.tracer(5000, 0)
        scr = turtle.getscreen()
        scr.onclick(self.click)
        scr.listen()
        self.__size = size
        self.__default = self.__size / 4
        self.__sx = 0
        self.__sy = 0
        self.draw()

    def click(self, x, y):
        # turtle is not drawing
        if not turtle.isdown():
            if abs(x) <= self.__size / 2 and abs(y) <= self.__size / 2:
                self.zoom(x, y)
                # else does nothing

    def zoom(self, x, y):
        turtle.clear()
        self.__sx += x / self.__default * (self.__size / 4)
        self.__sy += y / self.__default * (self.__size / 4)
        self.__default *= 2
        self.draw()

    def draw(self):

        x = -self.__size / 2
        y = -self.__size / 2
        sign = 1
        turtle.pendown()
        for i in range(self.__size):
            for j in range(self.__size):
                # convert x to real, y to imag
                c = complex.Complex(float(x / self.__default + self.__sx / (self.__size / 4)),
                                    float(y / self.__default + self.__sy / (self.__size / 4)))
                m = mandelbrot.Mandelbort(c, 50)
                turtle.goto(x, y + 1)
                turtle.color(m.get_color())
                if y == self.__size / 2:
                    sign = 1
                if y == -self.__size / 2:
                    sign = 2
                if sign == 1:
                    y -= 1
                if sign == 2:
                    y += 1
            x += 1
        turtle.penup()


def main():
    d = Display(600)
    turtle.mainloop()


if __name__ == '__main__':
    main()
