from random import randrange
from turtle import setup, ontimer, hideturtle, up, \
    tracer, onscreenclick, done, update, clear, goto, dot
from freegames import vector
from tkinter import Button, Label, Tk, Frame

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 270) / 25  # Modificamos la velocidad de la pelota
        speed.y = (y + 270) / 25


def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

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
            target.x -= 0.5
            #  Hacemos el juego infinito

    ontimer(move, 50)


def T():  # Declaramos nuestro juego como una funcion
    setup(420, 420, 370, 0)
    hideturtle()
    up()
    tracer(False)
    onscreenclick(tap)
    move()
    done()


def Menu():  # Declaramos una funcion para un menu de inicio
    root = Tk()
    root.geometry("450x100+200+50")
    root.configure(bg='Brown')
    Label(root, text='''|||||Bienvenido|||||
Le gustaria Jugar? \nPresione Para jugar\n  ''', fg="blue4").pack()
    Button(root, text='Ingresar', command = T).pack()
    root.mainloop()

    '''Declaramos un boton ligado a la funcion
    de arriba para activar el juego'''


Menu()
