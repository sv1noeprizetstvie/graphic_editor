from turtle import *


t = Turtle()
t.color('blue')
t.width(5)
t.shape('circle')
t.pendown()
t.speed(3)

def draw(x, y):
    t.goto(x, y)

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def setgreen():
    t.color('green')

def setblue():
    t.color('blue')

def setblack():
    t.color('black')

def setred():
    t.color('red')

def setyellow():
    t.color('yellow')

def stepright():
    t.goto(t.xcor( ) + 5, t.ycor())

def stepleft():
    t.goto(t.xcor( ) - 5, t.ycor())

def stepup():
    t.goto(t.xcor( ) , t.ycor()+5)

def stepdown():
    t.goto(t.xcor( ) , t.ycor()-5)
scr = t.getscreen()
scr.onscreenclick(move)
scr.listen()
scr.onkey(setgreen, 'g')
scr.onkey(setblue, 'h')
scr.onkey(setblack, 'j')
scr.onkey(setred, 'f')
scr.onkey(setyellow, 'k')

scr.onkey(stepright, 'd')
scr.onkey(stepleft, 'a')
scr.onkey(stepup, 'w')
scr.onkey(stepdown, 's')

t.ondrag(draw)
