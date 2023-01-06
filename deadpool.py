import turtle as t

t.hideturtle()
t.bgcolor('black')
t.penup()
t.pensize(1)


#circle - circle 1
t.goto(0,-350)
t.pendown()
t.color('#A52A2A')
t.begin_fill()
t.circle(350)
t.penup()
t.end_fill()



#inner black circle-circle 2
t.pensize(1)
t.color("black")
t.begin_fill()
t.goto(0,-300)
t.pendown()
t.circle(300)
t.end_fill()
t.penup()


#black circle to be divided in two parts
t.color('#A52A2A')
t.begin_fill()
t.pendown()
t.forward(50)
t.left(90)
t.fd(600)
t.left(90)
t.forward(100)
t.left(90)
t.fd(600)
t.left(90)
t.forward(50)
t.end_fill()
t.penup()


#left eye
t.color('white')
t.goto(140,0)
t.pendown()
t.begin_fill()
t.left(40)
t.fd(139)
t.left(230)
for i in range(22):
    t.right(2)
    t.fd(7)
t.right(90)
t.fd(66)
t.end_fill()
t.penup()



#right eye
t.color('white')
t.begin_fill()
t.goto(-125,0)

t.pendown()

t.fd(139)
t.right(230)
for i in range(22):
    t.left(2)
    t.fd(7)
t.left(91)
t.fd(69)
t.end_fill()

t.done()
