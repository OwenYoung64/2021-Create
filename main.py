'''
Difficulty between 1 and 5 to determine the size of the balls
'''
#2021 AP Creat Task
#Imports
import turtle as trtl
import random as rand
#Variables
wn = trtl.Screen()
startgame = trtl.Turtle()
start_text = trtl.Turtle()
counter = trtl.Turtle()
number = 0
timer = 30
timerup = False
counternumber = 1000
ball1 = trtl.Turtle()
ball2 = trtl.Turtle()
ball3 = trtl.Turtle()
ball4 = trtl.Turtle()
ball5 = trtl.Turtle()
ball6 = trtl.Turtle()
fontsetup = ("Arial", 15, "normal",)
#Variable setup
#Setup wn
wn.bgcolor("black")
#Setup startgame
startgame.hideturtle()
startgame.penup()
startgame.shape("square")
startgame.fillcolor("green")
startgame.turtlesize(5)
#Setup start_text
start_text.hideturtle()
start_text.penup()
start_text.backward(20)
start_text.right(90)
start_text.forward(10)
#start_text.write("Start", font=fontsetup)
#Setup counter
counter.hideturtle()
counter.color("white")
counter.penup()
counter.forward(250)
counter.right(90)
counter.forward(150)
#Setup ball1
ball1.shape("circle")
ball1.speed(0)
ball1.penup()
ball1.turtlesize(5)
ball1.backward(250)


#Setup ball2
ball2.shape("circle")
ball2.speed(0)
ball2.penup()
ball2.turtlesize(5)
ball2.backward(150)


#Setup ball3
ball3.shape("circle")
ball3.speed(0)
ball3.penup()
ball3.turtlesize(5)
ball3.backward(50)


#Setup ball4
ball4.shape("circle")
ball4.speed(0)
ball4.penup()
ball4.turtlesize(5)
ball4.forward(50)


#Setup ball5
ball5.shape("circle")
ball5.speed(0)
ball5.penup()
ball5.turtlesize(5)
ball5.forward(150)


#Setup ball6
ball6.shape("circle")
ball6.speed(0)
ball6.penup()
ball6.turtlesize(5)
ball6.forward(250)


#Functions

def ball_fillcolor():
    color_list = ["green", "red", "red", "red", "red", "red"]
    return_value = color_list.pop(rand.randint(0, 5))
    ball1.fillcolor(return_value)
    ball1color = return_value
    print(ball1color)
    return_value = color_list.pop(rand.randint(0, 4))
    ball2.fillcolor(return_value)
    ball2color = return_value
    print(ball2color)
    return_value = color_list.pop(rand.randint(0, 3))
    ball3.fillcolor(return_value)
    ball3color = return_value
    print(ball3color)
    return_value = color_list.pop(rand.randint(0, 2))
    ball4.fillcolor(return_value)
    ball4color = return_value
    print(ball4color)
    return_value = color_list.pop(rand.randint(0, 1))
    ball5.fillcolor(return_value)
    ball5color = return_value
    print(ball5color)
    return_value = color_list.pop(rand.randint(0, 0))
    ball6.fillcolor(return_value)
    ball6color = return_value
    print(ball6color)

def countdown():
    global timer, timerUp
    counter.clear()
    if timer <= 0:
        timer -= 1
        counter.write("time's up", font=fontsetup,)
        timerUp = True
    else:
        counter.write("time: " + str(timer), font=fontsetup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counternumber)


def ball_click(ball1color, ball1):
    if ball1color != "green":
        print("Its red")
    else:
        print("its green")

#Run functions
ball_fillcolor()
countdown()
#-----function calls----- problem with onclick?
ball1.onclick(ball_click)
wn.listen()
wn.mainloop()