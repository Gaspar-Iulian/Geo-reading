import turtle
radius= 8
extend = 80
angle= 180
x=0
y=0
geo = turtle.Turtle()
background =turtle.Screen() 
#chenar
geo.pensize(9)
geo.pencolor("black")
geo.speed(10)
geo.forward(250)
geo.circle(radius,extend)
geo.forward(250)
geo.circle(radius,extend)
geo.setheading(angle)
geo.forward(450)
geo.circle(radius,extend)
angle=-83
geo.setheading(angle)
geo.forward(250)
geo.circle(radius,extend)
angle=180
geo.setheading(angle)
# cercuri stanga
geo.back(300)
geo.penup()
geo.goto(x-70 ,y + 220)
geo.pendown()
radius=25
geo.circle(radius)
geo.penup()
geo.goto(x-60 ,y + 150)
geo.pendown()
geo.circle(radius)
geo.circle(radius)
geo.penup()
geo.goto(x-50 ,y + 80)
geo.pendown()
geo.circle(radius)
#cercuri dreapta 
geo.penup()
geo.goto(x+200 ,y + 220)
geo.pendown()
radius=25
geo.circle(radius)
geo.penup()
geo.goto(x+190 ,y + 150)
geo.pendown()
geo.circle(radius)
geo.circle(radius)
geo.penup()
geo.goto(x+180 ,y + 80)
geo.pendown()
geo.circle(radius)
# linie punctata 
dashes=[10,5]
geo.penup()
geo.goto(x+50,y+250)
geo.pendown
background.bgcolor("white")

turtle.done()

