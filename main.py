from turtle import *
from time import sleep

t = Turtle()
t.speed(7)

# PLANO CARTESIANO

def plano_cartesiano():
    t.color("red")
    t.pu()
    
    # eixo X
    t.goto(-300, 0)
    t.pd()
    t.goto(300, 0)
    t.stamp()
    
    t.pu()
    
    # eixo Y
    t.goto(0, -300)
    t.pd()
    t.setheading(90)
    t.goto(0, 300)
    t.stamp()
    t.setheading(0)
    t.hideturtle()

# DEF FUNCOES (MAT)

def f_raiz(x):
    return x ** 0.5

def f_inversa(x):
    return 1 / x

def f_exp(x):
    return 2 ** x

def f_p1(x):
    return 5 - (x ** 2)

def f_p2(x):
    return (x ** 2) - (5 * x) + 6

def f_cubica(x):
    return (x ** 3) - (x ** 2) - x + 1

# DEF FUNCOES

def funcao_raiz():
    plano_cartesiano()
    t.color("blue")
    t.pu()
    for x in range(0, 150):
        x = x / 10
        y = f_raiz(x)
        t.goto(x * 20, y * 20)
        t.pd()

def funcao_inversa():
    plano_cartesiano()
    t.color("black")
    t.pu()
    for i in range(-100, -1):
        x = i / 10
        y = f_inversa(x)
        t.goto(x * 20, y * 50)
        t.pd()
    t.pu()
    for i in range(1, 101):
        x = i / 10
        y = f_inversa(x)
        t.goto(x * 20, y * 50)
        t.pd()

def funcao_exponencial():
    plano_cartesiano()
    t.color("green")
    t.pu()
    for x in range(-50, 50):
        x = x / 10
        y = f_exp(x)
        t.goto(x * 20, y * 20)
        t.pd()

def funcao_parabola1():
    plano_cartesiano()
    t.color("purple")
    t.pu()
    for x in range(-100, 101):
        x = x / 10
        y = f_p1(x)
        t.goto(x * 20, y * 20)
        t.pd()

def funcao_parabola2():
    plano_cartesiano()
    t.color("orange")
    t.pu()
    for x in range(-100, 101):
        x = x / 10
        y = f_p2(x)
        t.goto(x * 20, y * 20)
        t.pd()

def funcao_cubica():
    plano_cartesiano()
    t.color("brown")
    t.pu()
    for x in range(-50, 51):
        x = x / 10
        y = f_cubica(x)
        t.goto(x * 20, y * 20)
        t.pd()

# EXECUCAO

funcao_raiz()
sleep(2)
t.clear()

funcao_inversa()
sleep(2)
t.clear()

funcao_exponencial()
sleep(2)
t.clear()

funcao_parabola1()
sleep(2)
t.clear()

funcao_parabola2()
sleep(2)
t.clear()

funcao_cubica()

# EXTRA

from random import randint

def corrida(n):
    tartarugas = []
    for i in range(n):
        t2 = Turtle()
        t2.penup()
        t2.speed(0)
        t2.goto(-250, 150 - i * 40)
        tartarugas.append(t2)
    for _ in range(50):
        for t2 in tartarugas:
            t2.forward(randint(1, 5))

corrida(3)

mainloop()