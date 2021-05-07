"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

"""

# Código modificado
# Autor: Daniela Avila Luna A01378664
# Autor: Liam Garay Monroy  A01750632

from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
target_speed = 1
ball_speed = vector(300, 300)

def tap(x, y):
    """ Función que calcula la velocidad de la pelota
    con los valores del click del mouse en la pantalla.

    Args:
        x ([float]): [posición en x del tap]
        y ([float]): [posición en y del tap]
    """
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + ball_speed.x) / 30
        speed.y = (y + ball_speed.y) / 25


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:  #velocidad de los targets
        target.x -= target_speed 

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()