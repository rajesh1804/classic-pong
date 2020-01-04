import turtle
import winsound

win = turtle.Screen()
win.title('Pong Game by Rajesh')
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)

#author
author = turtle.Turtle()
author.speed(0)
author.color('yellow')
author.penup()
author.hideturtle()
author.goto(-370,280)
author.write('Rajesh',align='center',font=('Courier',10,'normal'))

#score
score_a=0
score_b=0

#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.25 #used to move the ball by 0.1 pixels
ball.dy = 0.25 #used to move the ball by 0.1 pixels

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,265)
pen.write('Player A: '+str(score_a)+'  Player B : '+str(score_b),align='center',font=('Courier',20,'normal'))

#function
def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
     y = paddle_b.ycor()
     y+=20
     paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#keyboard binding
win.listen()
win.onkeypress(paddle_a_up,'w')
win.onkeypress(paddle_a_down,'s')
win.onkeypress(paddle_b_up,'Up')
win.onkeypress(paddle_b_down,'Down')

#main
while True:
    win.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checks
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        winsound.PlaySound('bounce2.wav', winsound.SND_ASYNC)
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
        winsound.PlaySound('bounce2.wav', winsound.SND_ASYNC)
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write('Player A: {}  Player B: {}'.format(score_a,score_b),align='center',font=('Courier',20,'normal'))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write('Player A: {} Player B: {}'.format(score_a,score_b),align='center',font=('Courier',20,'normal'))

    #paddle_b & ball collision
    if ball.xcor()>340 and ball.xcor()<350 and (ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50):
        ball.setx(340)
        ball.dx*=-1
        winsound.PlaySound('bounce1.wav', winsound.SND_ASYNC)

    #paddle_a & ball collision
    if ball.xcor()<-340 and ball.xcor()>-350 and (ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50):
        ball.setx(-340)
        ball.dx*=-1
        winsound.PlaySound('bounce1.wav', winsound.SND_ASYNC)