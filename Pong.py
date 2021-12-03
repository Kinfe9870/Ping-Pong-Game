import turtle

win = turtle.Screen()
win.title("Pong Game by @Kinfe Oyefuga")  # Title of the screen
win.bgcolor("Black")  # Background colour of the window
win.setup(width=800, height=600)  # Height and width of the window
win.tracer(0)  # speed up the game basically

# Score
score_a = 0
score_b = 0

# Paddle A
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.shapesize(stretch_len=1, stretch_wid=5)
paddle1.color("White")
paddle1.penup()
paddle1.goto(-350, 0)

# Paddle B
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.shapesize(stretch_len=1, stretch_wid=5)
paddle2.color("White")
paddle2.penup()
paddle2.goto(+350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("White")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Times new roman", 20, "normal"))

# Function to move pad
def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)


def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)


def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)


def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)


# Keyboard binding
win.listen()
win.onkeypress(paddle1_up, "w")
win.onkeypress(paddle1_down, "s")
win.onkeypress(paddle2_up, "Up")
win.onkeypress(paddle2_down, "Down")

# Main game loop
while True:
    win.update()  # Every time the loop runs, the screen is updated

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Boarder checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A: {} Player B: {} ".format(score_a, score_b), align="center", font=("Times new roman", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {} Player B: {} ".format(score_a, score_b), align="center", font=("Times new roman", 20, "normal"))


    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
