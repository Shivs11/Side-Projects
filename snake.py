import turtle
import time
import math
import random

delay = 0.1
score = 0
highscore = 0
length = [] #Length of the snake

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align = "center", font = ("Courier", 24, "normal"))


window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("green")
window.setup(width = 600, height = 600)
window.tracer(0) #Turns of the Screen updates

# Creating food for the snake:
food = turtle.Turtle()
food.speed(0) #animation speed of the module
food.color("red")
food.shape("circle")
food.penup()
food.goto(0 , 100)


# Creating a snake.
myhead = turtle.Turtle()
myhead.speed(0) #animation speed of the module
myhead.color("black")
myhead.shape("square")
myhead.penup()
myhead.goto(0 , 0)
myhead.direction = "stop"

def move():
    if myhead.direction == "up":
        y  = myhead.ycor()
        myhead.sety(y + 20)

    if myhead.direction == "down":
        y  = myhead.ycor()
        myhead.sety(y - 20)

    if myhead.direction == "left":
        x  = myhead.xcor()
        myhead.setx(x - 20)

    if myhead.direction == "right":
        x = myhead.xcor()
        myhead.setx(x + 20)

def uptime():
    if myhead.direction != "down":
        myhead.direction = "up"

def downtime():
    if myhead.direction!= "up":
        myhead.direction = "down"

def leftime():
    if myhead.direction!= "right":
        myhead.direction = "left"

def righttime():
    if myhead.direction != "left":
        myhead.direction = "right"

# Keyboard bindings:
window.listen()
window.onkeypress(uptime, "Up")
window.onkeypress(leftime, "Left")
window.onkeypress(righttime, "Right")
window.onkeypress(downtime, "Down")


# Main game loop
while True:
    window.update()

    # Check for collision with the border:
    if myhead.xcor() > 290 or myhead.xcor() < -290 or myhead.ycor() > 290 or myhead.ycor() < -290:
        myhead.goto(0, 0)
        myhead.direction = "stop"
        # Hiding the segments
        for segment in length:
            segment.hideturtle()
        # Clearing the length list
        length.clear()

        # Resetting the score as well:
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score: {} High Score {}".format(score, highscore), align = "center", font = ("Courier", 24, "normal"))




    # Built in function to measure the distance between the two turtles
    if myhead.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.setposition(x , y)

        # Time to extend the snake:
        newone = turtle.Turtle()
        newone.speed(0)
        newone.shape("square")
        newone.color("grey")
        newone.penup()
        length.append(newone)

        # Shortening the delay
        delay -= 0.001

        # Increasing the score:
        score += 10
        if score > highscore:
            highscore = score

        pen.clear()
        pen.write("Score: {} High Score {}".format(score, highscore), align = "center", font = ("Courier", 24, "normal"))

    # Moving the end segments to the top
    for index in range(len(length)-1, 0, -1):
        x = length[index-1].xcor()
        y = length[index-1].ycor()
        length[index].goto(x , y)

    # Moving the segment 0 to where the head is:
    if len(length) > 0:
        x = myhead.xcor()
        y = myhead.ycor()
        length[0].goto(x, y)


    move()
    # checking for collision within body segments
    for segment in length:
        if segment.distance(myhead) < 20:
            time.sleep(1)
            myhead.goto(0, 0)
            myhead.direction = 'stop'

            for segment in length:
                segment.goto(1000, 1000)

            length.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: {} High Score {}".format(score, highscore), align = "center", font = ("Courier", 24, "normal"))

    time.sleep(delay)




window.mainloop()
