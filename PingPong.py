# imported turtle module
import turtle

wind = turtle.Screen()# intialize screen
wind.title("Ping Pong")# set the title
wind.bgcolor("black")# set the background color
wind.setup(width=800,height=600)# set the width and the heigth
wind.tracer(0)# stop the window from updating auto

# madrab 1
madrab1 = turtle.Turtle()# intialize turtle object
madrab1.speed(0)# set the speed animation
madrab1.shape("square")# set the shape
madrab1.color("blue")# set the color
madrab1.shapesize(stretch_wid=5,stretch_len=1) # set the shape to meet the size
madrab1.penup() # stops the objects from drawing lines
madrab1.goto(-350,0) # set the position of the objects

# madrab 2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5,stretch_len=1)
madrab2.penup()
madrab2.goto(350,0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .5
ball.dy = .5
#score
score1 = 0
score2 = 0
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1: 0  Player 2:0",align="center",font=("Courier",24,"normal"))
# function
def madrab1_Up():
    y= madrab1.ycor() # get the y of madrab1
    y +=20 # set the y to increase
    madrab1.sety(y) # set the y of the madrab1
def madrab1_down():
    y= madrab1.ycor()
    y -=20
    madrab1.sety(y)

def madrab2_Up():
    y= madrab2.ycor()
    y +=20
    madrab2.sety(y)
def madrab2_down():
    y= madrab2.ycor()
    y -=20
    madrab2.sety(y)
# keyboard bindings
wind.listen() # tell the window to expect keyword input
wind.onkeypress(madrab1_Up,"w") # when press w to call madrab1_Up function
wind.onkeypress(madrab1_down,"s")
wind.onkeypress(madrab2_Up,"Up")
wind.onkeypress(madrab2_down,"Down")
# game loop
while True:
    # update the screen everytime the loop run
    wind.update()
    # move the ball
    ball.setx(ball.xcor()+ball.dx) # ball starts at 0 and every time loop run  -->+dx value
    ball.sety(ball.ycor()+ball.dy) # ball starts at 0 and every time loop run  -->+dy value

    # border check
    # top border , bottom border 300px , ball 20px
    if ball.ycor() > 290: # if ball is at top
        ball.sety(290)
        ball.dy *=-1
    if ball.ycor() < -290: # if ball is at bottom
        ball.sety(-290)
        ball.dy *=-1

    if ball.xcor() > 390: # if ball is at right borer
        ball.goto(0,0) # put the ball in center
        ball.dx *=-1
        score1+=1
        score.clear()
        score.write("Player 1: {}  Player 2:{}".format(score1,score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *=-1
        score2+=1
        score.clear()
        score.write("Player 1: {}  Player 2:{}".format(score1,score2), align="center", font=("Courier", 24, "normal"))

    # tasadom madrab and ball
    if (ball.xcor() > 340 and ball.xcor()<350 and ball.ycor()< madrab2.ycor()+40 and ball.ycor() > madrab2.ycor()-40) :
            ball.setx(340)
            ball.dx *=-1

    if (ball.xcor() < -340 and ball.xcor()> -350 and ball.ycor()< madrab1.ycor()+40 and ball.ycor() > madrab1.ycor()-40) :
            ball.setx(-340)
            ball.dx *=-1






