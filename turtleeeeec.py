from turtle import *
bgcolor('black')
color('cyan')
speed(11)
right(45)
for i in range(150):
    circle(30)
    if 7 < i < 62:
        left(5)
    if 60 <i < 133:
        right(20)
    if  i < 80:
        forward(25)
    else:
        forward