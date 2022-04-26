#2021 AP Creat Task
#Imports
import turtle as trtl
import random as rand
#Variables
wn = trtl.Screen()
number = 0
timer = 30
score = 0
scorevalue = 0
counternumber = 1000
fontsetup = ("Arial", 20, "normal",)
timerup = False
scorechanger = trtl.Turtle()
startgame = trtl.Turtle()
start_text = trtl.Turtle()
counter = trtl.Turtle()
ball1 = trtl.Turtle()
ball2 = trtl.Turtle()
ball3 = trtl.Turtle()
ball4 = trtl.Turtle()
ball5 = trtl.Turtle()
ball6 = trtl.Turtle()
#Variable setup
#Setup wn
wn.bgcolor("black")
#Setup startgame
startgame.penup()
startgame.shape("square")
startgame.fillcolor("green")
startgame.turtlesize(5)
startgame.hideturtle()
startgame.left(90)
startgame.forward(100)
startgame.showturtle()
#Setup start_text
start_text.penup()
start_text.hideturtle()
start_text.backward(20)
start_text.right(90)
start_text.forward(10)
start_text.backward(100)
start_text.write("Start", font=fontsetup)
#Setup counter
counter.hideturtle()
counter.color("white")
counter.penup()
counter.forward(250)
counter.right(90)
counter.forward(150)
#Setup scorechanger
scorechanger.hideturtle()
scorechanger.color("white")
scorechanger.penup()
scorechanger.backward(250)
scorechanger.right(90)
scorechanger.forward(150)
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
    global ball1color, ball2color, ball3color, ball4color, ball5color, ball6color, return_value
    color_list = ["green", "red", "red", "red", "red", "red"]
    return_value = color_list.pop(rand.randint(0, 5))
    ball1.fillcolor(return_value)
    ball1color = return_value
    return_value = color_list.pop(rand.randint(0, 4))
    ball2.fillcolor(return_value)
    ball2color = return_value
    return_value = color_list.pop(rand.randint(0, 3))
    ball3.fillcolor(return_value)
    ball3color = return_value
    return_value = color_list.pop(rand.randint(0, 2))
    ball4.fillcolor(return_value)
    ball4color = return_value
    return_value = color_list.pop(rand.randint(0, 1))
    ball5.fillcolor(return_value)
    ball5color = return_value
    return_value = color_list.pop(rand.randint(0, 0))
    ball6.fillcolor(return_value)
    ball6color = return_value

def countdown():
    global timer, timerUp
    counter.clear()
    if timer <= 0:
        timer -= 1
        counter.write("Finished", font=fontsetup,)
        gamedone(scorevalue)
        timerUp = True
    else:
        counter.write("time: " + str(timer), font=fontsetup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counternumber)

def gamedone(scorevalue):
    ball1.hideturtle()
    ball2.hideturtle()
    ball3.hideturtle()
    ball4.hideturtle()
    ball5.hideturtle()
    ball6.hideturtle()
    scorechanger.right(90)
    scorechanger.forward(110)
    scorechanger.clear()
    scorechanger.write("Final score: " + str(scorevalue), font=fontsetup)

def scoreadd(score):
    global scorevalue
    global addedscore
    score += 100
    addedscore = score + scorevalue
    scorechanger.clear()
    scorechanger.write(scorevalue + score, font=fontsetup)
    scorevalue = addedscore
    ball_fillcolor()

def scoresubtract(score):
    global scorevalue
    global addedscore
    score -= 100
    addedscore = score + scorevalue
    scorechanger.clear()
    scorechanger.write(scorevalue + score, font=fontsetup)
    scorevalue = addedscore

def ball_click(ballcolor, ball1):
    color = "red"
    global ball1color, ball2color, ball3color, ball4color, ball5color, ball6color
    list = [ball1color, ball2color, ball3color, ball4color, ball5color, ball6color]
    for i in list:
        if i == color:
            scoresubtract(score)
        else:
            scoreadd(score)
'''
def ball2_click(ball1color, ball1):
    color = "red"
    if ball2color == color:
        scoresubtract(score)
    else:
        scoreadd(score)

def ball3_click(ball1color, ball1):
    color = "red"
    if ball3color == color:
        scoresubtract(score)
    else:
        scoreadd(score)

def ball4_click(ball2color, ball1):
    color = "red"
    if ball4color == color:
        scoresubtract(score)
    else:
        scoreadd(score)

def ball5_click(ball1color, ball1):
    color = "red"
    if ball5color == color:
        scoresubtract(score)
    else:
        scoreadd(score)

def ball6_click(ball1color, ball1):
    color = "red"
    if ball6color == color:
        scoresubtract(score)
    else:
        scoreadd(score)
        '''

def gamestart(ball1, ball2):
    startgame.hideturtle()
    start_text.clear()
    ball_fillcolor()
    countdown()


#Run functions
#-----function calls----- problem with onclick?
wn.listen()
startgame.onclick(gamestart)
ball1.onclick(ball_click)
'''
ball2.onclick(ball2_click)
ball3.onclick(ball3_click)
ball4.onclick(ball4_click)
ball5.onclick(ball5_click)
ball6.onclick(ball6_click)
'''
wn.mainloop()
