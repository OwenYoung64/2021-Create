#2021 AP Creat Task
#Imports
import turtle as trtl

#Variables
wn = trtl.Screen()
startgame = trtl.Turtle()
start_text = trtl.Turtle()
greenball = trtl.Turtle()
redball = trtl.Turtle()
fontsetup = ("Arial", 15, "normal")
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
#Setup greenball
greenball.shape("circle")
greenball.fillcolor("green")
greenball.turtlesize(5)

#Setup redball
redball.shape("circle")
redball.fillcolor("red")
redball.turtlesize(5)
redball.forward(100)

#Functions

def draw_the_balls():






#-----function calls-----
#startgame.onclick()
wn.listen()
wn.mainloop()
