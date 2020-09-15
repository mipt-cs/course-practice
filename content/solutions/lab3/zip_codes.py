from record import start, finish
width = 400
height = 100
start(width, height, -width/2, height/3, 50, __file__)


from time import sleep
import turtle


def universal_painter(motions):
    for angle, step, flag in motions:
        turtle.left(angle)
        if flag:
            turtle.pendown()
        else:
            turtle.penup()
        turtle.forward(step)


turtle.speed(10)
turtle.color('blue')
turtle.pensize(2)

h1 = 30
h2 = h1*2**0.5

zero = [(-90, 2*h1, True), (90, h1, True), (90, 2*h1, True), (90, h1, True),
        (180, 2*h1, False)]
one = [(-90, h1, False), (135, h2, True), (-135, 2*h1, True),
       (180, 2*h1, False), (-90, h1, False)]
two = [(0, h1, True), (-90, h1, True), (-45, h2, True), (135, h1, True),
       (90, 2*h1, False), (-90, h1, False)]
three = [(0, h1, True), (-135, h2, True), (135, h1, True), (-135, h2, True),
         (135, h1, False), (90, 2*h1, False), (-90, h1, False)]
four = [(-90, h1, True), (90, h1, True), (-90, h1, True), (180, 2*h1, True),
        (-90, h1, False)]
seven = [(0, h1, True), (-135, h2, True), (45, h1, True), (180, 2*h1, False),
         (-90, 2*h1, False)]


universal_painter(one)
universal_painter(four)
universal_painter(one)
universal_painter(seven)
universal_painter(zero)
universal_painter(zero)

finish()
