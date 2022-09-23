import turtle

# screen

wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("pong game")
wn.setup(width=1000, height=600)
wn.tracer(0)


# center line
line = turtle.Turtle()
line.speed(0)
line.shape("square")
line.color("white")
line.shapesize(stretch_wid=100, stretch_len=0.5)
line.penup()
line.goto(0, 0)

# up line
line = turtle.Turtle()
line.speed(0)
line.shape("square")
line.color("white")
line.shapesize(stretch_wid=1, stretch_len=100)
line.penup()
line.goto(0, -290)

# down line
line = turtle.Turtle()
line.speed(0)
line.shape("square")
line.color("white")
line.shapesize(stretch_wid=1, stretch_len=100)
line.penup()
line.goto(0, 305)

# left line
line = turtle.Turtle()
line.speed(0)
line.shape("square")
line.color("white")
line.shapesize(stretch_wid=100, stretch_len=1)
line.penup()
line.goto(-490, 0)

# right line
line = turtle.Turtle()
line.speed(0)
line.shape("square")
line.color("white")
line.shapesize(stretch_wid=100, stretch_len=1)
line.penup()
line.goto(490, 0)


# rocket R

rocket_R = turtle.Turtle()
rocket_R.speed(0)
rocket_R.shape("square")
rocket_R.color("aqua")
rocket_R.shapesize(stretch_wid=5, stretch_len=1)
rocket_R.penup()
rocket_R.goto(450, 0)


def rocket_R_up():
    Y = rocket_R.ycor()
    Y += 25
    rocket_R.sety(Y)


def rocket_R_down():
    Y = rocket_R.ycor()
    Y -= 25
    rocket_R.sety(Y)



# rocket L

rocket_L = turtle.Turtle()
rocket_L.speed(0)
rocket_L.shape("square")
rocket_L.color("red")
rocket_L.shapesize(stretch_wid=5, stretch_len=1)
rocket_L.penup()
rocket_L.goto(-450, 0)


def rocket_L_up():
    Y = rocket_L.ycor()
    Y += 25
    rocket_L.sety(Y)


def rocket_L_down():
    Y = rocket_L.ycor()
    Y -= 25
    rocket_L.sety(Y)


# ball


ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("orange")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = -0.5


# control rockets
wn.listen()
N = None

wn.onkeypress(rocket_R_up, "Up")
wn.onkeypress(rocket_R_down, "Down")

wn.onkeypress(rocket_L_up, "w")

wn.onkeypress(rocket_L_down, "s")

# marks player
mark_player_R = 0
mark_player_L = 0

# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("white")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0    Right_player: 0",align="center", font=("Courier", 24, "normal"))


while True:
    wn.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(mark_player_L, mark_player_R), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -450:
        ball.goto(0, 0)
        ball.dx *= -1
        mark_player_R += 1

        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
            mark_player_L, mark_player_R), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() > 450:
        ball.goto(0, 0)
        ball.dx *= -1
        mark_player_L += 1
       # Paddle ball collision
    if (ball.xcor() > 430) and (ball.ycor() < rocket_R.ycor()+40 and ball.ycor() > rocket_R.ycor()-40):
        ball.setx(430)
        ball.dx*=-1  

    if (ball.xcor() < -430) and (ball.ycor()<rocket_L.ycor()+40 and ball.ycor()>rocket_L.ycor()-40):
        ball.setx(-430)
        ball.dx*=-1
