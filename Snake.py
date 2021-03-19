import random
from turtle import update, clear, ontimer, setup, \
    hideturtle, tracer, listen, onkey, done
from random import randrange
from freegames import square, vector
from tkinter import Button, Label, Tk, Frame


food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
# Declaramos variables que escojan de forma aleatoria un color
q = random.choice(['Green', 'Black', 'Blue', 'Brown', 'Purple'])
d = random.choice(['Green', 'Black', 'Blue', 'Brown', 'Purple'])
food.x = randrange(-15, 15) * 10
food.y = randrange(-15, 15) * 10
n = 0


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def inside(food):
    "Return True if food inside boundaries."
    return -200 < food.x < 190 and -200 < food.y < 190
    

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    food.move(n+1)
    

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    if not inside(food):
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        update()
    

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, d)

    square(food.x, food.y, 9, q)
    update()
    ontimer(move, 100)


''' Insertamos nuestras variables
para que el color sea aleatorio cada
vez que inicia'''

# Iniciamos Una funcion para iniciar nuestro juego


def S():
    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: change(10, 0), 'Right')
    onkey(lambda: change(-10, 0), 'Left')
    onkey(lambda: change(0, 10), 'Up')
    onkey(lambda: change(0, -10), 'Down')
    move()
    done()


def Menu():  # Declaramos una funcion para un menu de inicio
    root = Tk()
    root.geometry("450x100+200+50")
    mi_Frame = Frame().pack()
    labe1 = Label(mi_Frame, text='''|||||Bienvenido|||||
Le gustaria Jugar? \nPresione Para jugar\n  ''', fg="blue4").pack()
    boton = Button(mi_Frame, text='Ingresar', command = S).pack()
    root.mainloop()

    '''Declaramos un boton ligado a la funcion
    de arriba para activar el juego'''


Menu()
