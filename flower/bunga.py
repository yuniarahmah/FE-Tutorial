import turtle

turtle.bgcolor("black")
turtle.speed(50)
turtle.hideturtle("black")

Colors = ["pink","yellow","blue","red",]

for i in range(120):
    for bunga in Colors:
        turtle.color(bunga)
        turtle.circle(200-i,100)
        turtle.it(90)
        turtle.circle(200-i, 100)
        turtle.end_fill()
turtle.mainloop()