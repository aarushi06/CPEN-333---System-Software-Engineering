# student name: Aarushi Mehra
# student number: 82519695
from turtle import *

first_row_colours = ["#0081C8", "#000000", "#EE334E"]  #blue, black, red color hex codes
second_row_colours = ["#FCB131", "#00A651"]    #yellow, green color hex codes
pensize(7)

for i in range(0,3):   #for loop for the upper row
    penup()
    setpos(-100+100*i, 0)
    pendown()
    color(first_row_colours[i], 'white')
    circle(45)

for i in range(0,2):   #for loop for the second row
    penup()
    setpos(-50+100*i, -50)
    pendown()
    color(second_row_colours[i], 'white')
    circle(45)
    penup()             #penup in the end


