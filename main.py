#2021 AP Creat Task
#Imports
import turtle as trtl
import random as rand
#Variables
wn = trtl.Screen()
startgame = trtl.Turtle()
start_text = trtl.Turtle()
number = 0
greenvalue = 0
redvalue = 0
ball1 = trtl.Turtle()
ball2 = trtl.Turtle()
ball3 = trtl.Turtle()
ball4 = trtl.Turtle()
ball5 = trtl.Turtle()
ball6 = trtl.Turtle()
fontsetup = ("Arial", 15, "normal")
color_list = ["green","red"]
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
    global greenvalue
    global redvalue
    ball1.fillcolor(rand.choice(color_list))
    #use fillcolor
    '''
    if(ball1.color == "green"):
        greenvalue += 1
    else:
        redvalue += 1
        '''
    ball2.fillcolor(rand.choice(color_list))
    ball3.fillcolor(rand.choice(color_list))
    ball4.fillcolor(rand.choice(color_list))
    ball5.fillcolor(rand.choice(color_list))
    ball6.fillcolor(rand.choice(color_list))

#def ball_click():
    #if(ball1.color =="red"):




#Run functions
ball_fillcolor()
#ball_click
#-----function calls-----
#startgame.onclick()
wn.listen()
wn.mainloop()
