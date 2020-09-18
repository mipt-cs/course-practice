from record import start, finish
width = 400
height = 200
zero = -100


import os
import turtle

t = turtle.Turtle('circle')
t.shapesize(0.5)
t.speed(0)
t.up()
t.goto(0, zero)
t.down()

start(width, height, -width/2, height, 50, __file__)
t.fd(200)
t.bk(400)

v = [30, 60]
dt = 0.05
g = -9.8
k_air = 0.07
k_elast = 0.9
k_friction = 0.5


def abs_v(v):
    return (v[0] * v[0] + v[1] * v[1]) ** 0.5


def update_velocity():
    global v, dt, t
    if t.ycor() <= zero:
        v[1] *= -k_elast
        v[0] -= k_friction * v[0] * dt
    else:
        v[1] += (g - k_air * v[1]) * dt
        v[0] -= k_air * v[0] * dt


while abs_v(v) > 0.1:
    t.goto(t.xcor() + v[0] * dt, t.ycor() + v[1] * dt)
    update_velocity()

finish()
name = os.path.splitext(os.path.basename(__file__))[0]
os.system(f'bash create_gif.sh {name} 0.05')
