#2021 AP Creat Task
#Imports
import turtle as trtl
import random as rand
#Variables
wn = trtl.Screen()
startgame = trtl.Turtle()
start_text = trtl.Turtle()
number = 0
value = 0
ball1 = trtl.Turtle()
ball2 = trtl.Turtle()
ball3 = trtl.Turtle()
ball4 = trtl.Turtle()
ball5 = trtl.Turtle()
ball6 = trtl.Turtle()
fontsetup = ("Arial", 15, "normal")
color_list = ["green","red"]
number_list = ["1","2"]
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
#Setup ball1
ball1.shape("circle")
ball1.speed(0)
ball1.penup()
ball1.fillcolor("green")
ball1.turtlesize(5)
ball1.backward(250)


#Setup ball2
ball2.shape("circle")
ball2.speed(0)
ball2.penup()
ball2.fillcolor("green")
ball2.turtlesize(5)
ball2.backward(150)


#Setup ball3
ball3.shape("circle")
ball3.speed(0)
ball3.penup()
ball3.fillcolor("green")
ball3.turtlesize(5)
ball3.backward(50)


#Setup ball4
ball4.shape("circle")
ball4.speed(0)
ball4.penup()
ball4.fillcolor("green")
ball4.turtlesize(5)
ball4.forward(50)


#Setup ball5
ball5.shape("circle")
ball5.speed(0)
ball5.penup()
ball5.fillcolor("green")
ball5.turtlesize(5)
ball5.forward(150)


#Setup ball6
ball6.shape("circle")
ball6.speed(0)
ball6.penup()
ball6.fillcolor("green")
ball6.turtlesize(5)
ball6.forward(250)


#Functions

def ball_color():
    global value
    ball1.color(rand.choice(color_list))
    if(ball1.color == "red"):
        value += 1
    else:
        value += 2
    ball2.color(rand.choice(color_list))
    if (ball2.color == "red"):
        value += 1
    else:
        value += 2
    ball3.color(rand.choice(color_list))
    if (ball3.color == "red"):
        value += 1
    else:
        value += 2
    ball4.color(rand.choice(color_list))
    if (ball4.color == "red"):
        value += 1
    else:
        value += 2
    ball5.color(rand.choice(color_list))
    if (ball5.color == "red"):
        value += 1
    else:
        value += 2
    ball6.color(rand.choice(color_list))
    if (ball6.color == "red"):
        value += 1
    else:
        value += 2
    print(value)



#Run functions
ball_color()

#-----function calls-----
#startgame.onclick()
wn.listen()
wn.mainloop()
