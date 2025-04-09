# ejercicio 3
import turtle
import math 

v = turtle.Screen()
t = turtle.Turtle()

x,y = map(int,input("Ingrese las coordenadas del centro del circulo (x,y): ").split())
r = int(input("Ingrese el radio del circulo: "))

area = math.pi * (r **2)

turtle.shape("turtle")
turtle.color("red")
turtle.pensize(3)
turtle.penup()
turtle.goto(x,y-r)
turtle.pendown()
turtle.circle(r)

turtle.exitonclick()