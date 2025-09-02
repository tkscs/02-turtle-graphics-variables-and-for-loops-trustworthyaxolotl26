from turtle import *
#/summon turtle

speed(10)

def cyrusDraw():
    pencolor("green")
    right(90)
    forward(200)
    right(45)
    forward(100)
    goto(0, -200)
    left(90)
    forward(100)
    up()
    goto(25,70)
    down()
    for i in range(100):
        forward(2.5)
        right(3.6)
    up()
    goto(-10,50)
    dot()
    goto(10,50)
    dot()
    goto(0,-75)
    down()
    forward(105)
    goto(0,-75)
    right(90)
    forward(105)
    up()
    goto(-20, 20)
    down()
    right(180)
    forward(25)
    right(90)
    forward(25)
    up()
    goto(-50, 20)
    left(180)
    down()
    forward(15)

cyrusDraw()

def colorShape():
    pencolor("red")
    for i in range(3):
        forward(100)
        right(120)

    pencolor("orange")
    for i in range(4):
        forward(100)
        right(90)
        
    pencolor("yellow")
    for i in range(5):
        forward(100)
        right(72)

    pencolor("green")
    for i in range(6):
        forward(100)
        right(60)

    pencolor("blue")
    for i in range(7):
        forward(100)
        right(51.5)

    for i in range(100):
        forward(10)
        right(3.6)

exitonclick()
