import turtle
window = turtle.Screen()
window.title("Moya Game")
window.bgcolor("black")
window.setup(width=800 , height=600)
window.tracer(0)


# paddle 1
pad1=turtle.Turtle()
pad1.speed(0)
pad1.shape("square")
pad1.color("white")
pad1.shapesize(stretch_wid=5,stretch_len=1)
pad1.penup()
pad1.goto(-300,0)

def mov1 () :
    a=pad1.ycor()
    a +=20
    pad1.sety(a)
def mov2 () :
    q=pad1.ycor()
    q -=20
    pad1.sety(q)





# paddle 2
pad2=turtle.Turtle()
pad2.speed(0)
pad2.shape("square")
pad2.color("white")
pad2.shapesize(stretch_wid=5,stretch_len=1)
pad2.penup()
pad2.goto(300,0)

def mov3():
    p = pad2.ycor()
    p += 20
    pad2.sety(p)

def mov4():
    m = pad2.ycor()
    m -= 20
    pad2.sety(m) 


window.listen()
window.onkeypress(mov3, "p")
window.onkeypress(mov4, "m")
window.onkeypress(mov1,"a")
window.onkeypress(mov2,"q")

#balle
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

ball.dx =0.5
ball.dy =-0.5



while True :
    window.update()
    #balle move
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #balle rebande
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1 

    #paddel rebonde
    
    if (ball.ycor()<pad2.ycor()+50 and ball.ycor()>pad2.ycor() -50) and ball.xcor()>280 and ball.xcor()<290  : 
        ball.setx(280)
        ball.dx *= -1  
        

    if (ball.ycor()<pad1.ycor()+50 and ball.ycor()>pad1.ycor() -50) and ball.xcor()<-280 and ball.xcor()>-290  : 
        ball.setx(-280)
        ball.dx *= -1   
