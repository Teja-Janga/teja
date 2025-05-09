import turtle
t=turtle.Turtle()
t.speed(0)
s=turtle.Screen()
s.bgcolor("black")

#Body of the Lens
t.color('cadetblue4')
t.begin_fill()
t.fd(140)
t.circle(5,90)
t.fd(185)
t.circle(5,90)
t.fd(140)
t.circle(5,90)
t.fd(185)
t.circle(5,90)
t.end_fill()

#LensScreen
t.penup()
t.goto(-1,186)
t.pendown()
t.pensize(2)
t.pencolor('gray60')
t.fillcolor("black")
t.begin_fill()
t.rt(90)
t.fd(95)
t.circle(5,90)
t.fd(132)
t.circle(5,90)
t.fd(95)
t.circle(5,90)
t.fd(132)
t.circle(5,90)
t.end_fill()

#Circle in the LensScreen
t.penup()
t.goto(5,140)
t.pendown()
t.pensize(2)
t.pencolor("gray40")
t.pensize(1)
t.circle(45)

#Internal Circle1
t.penup()
t.goto(32,160)
t.pendown()
t.circle(16)

#Internal Circl2
t.penup()
t.goto(32,120)
t.pendown()
t.circle(16)

#Lens on Circle1
t.penup()
t.goto(37,160)
t.pendown()
t.circle(11)
t.penup()
t.goto(42,160)
t.pendown()
t.fillcolor('gray50')
t.begin_fill()
t.circle(6)
t.end_fill()

#Lens on Circle1
t.penup()
t.goto(37,120)
t.pendown()
t.circle(11)
t.penup()
t.goto(42,120)
t.pendown()
t.fillcolor('gray50')
t.begin_fill()
t.circle(6)
t.end_fill()

#Text on Lens
t.penup()
t.goto(120,110)
t.pendown()
t.pencolor('black')

text=(" "*65)+"1.79-2.4/24-25mm"
text_color="white"

canvas=s.getcanvas()
for char in text:
    canvas.create_text(t.xcor(), t.ycor(), text=char, angle=90,font=("Arial", 6, "normal"), fill=text_color)
    t.sety(t.ycor()-3.5)

t.penup()
t.goto(120,110)
t.pendown()
t.pencolor("black")
t.fd(23)
t.penup()
t.fd(87)
t.pendown()
t.pencolor('cadetblue4')
t.back(88)

#Lens under the LensScreen
t.penup()
t.goto(17,75)
t.pendown()
t.color('black')
t.begin_fill()
t.fd(20)
t.circle(3,90)
t.fd(20)
t.circle(3,90)
t.fd(20)
t.circle(3,90)
t.fd(20)
t.circle(3,90)
t.end_fill()

#Circle inside the Lens under the LensScreen
t.penup()
t.goto(22,65)
t.pendown()
t.pencolor('gray40')
t.circle(8)
t.penup()
t.goto(26,65)
t.pendown()
t.fillcolor('gray50')
t.begin_fill()
t.circle(4)
t.end_fill()

#Flashlight
t.penup()
t.goto(40,44)
t.pendown()
t.fillcolor('cornsilk3')
t.begin_fill()
t.rt(90)
t.fd(20)
t.circle(3,90)
t.fd(7)
t.circle(3,90)
t.fd(20)
t.circle(3,90)
t.fd(7)
t.circle(3,90)
t.end_fill()

#Lens in Flashlight
t.penup()
t.goto(30,42)
t.pendown()
#t.pencolor("white")
t.fillcolor('khaki4')
t.begin_fill()
t.circle(5)
t.end_fill()

#Text down the Lens
t.penup()
t.goto(50,28)
t.pendown()
t.lt(180)
t.pencolor('white')
t.write("NEO",font=("pixel",10))
t.penup()
t.goto(80,34)
t.pendown()
t.write("OIS",font=("pixel",5))
t.penup()
t.goto(80,30)
t.pendown()
t.write("AI Camera",font=("pixel",4))

#Description
t.penup()
t.goto(-200,225)
t.pendown()
t.pencolor("red")
t.write("Phone CameraLens Using Python Turtle Module",font=("times",19,'bold'))

t.hideturtle()
turtle.exitonclick()