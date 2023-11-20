import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Hi, Esty & Alexander")

alexander = turtle.Turtle()
alexander.pensize(3)
alexander.shape("turtle")
alexander.speed(5)

ester = turtle.Turtle()
ester.color("hotpink")
ester.pensize(5)
ester.shape("turtle")

colors = ["yellow", "red", "purple", "blue"]

for i in range(len(colors)):
    alexander.color(colors[i])
    alexander.forward(50)
    alexander.left(90)

for i in range(3):
    ester.forward(80)
    ester.left(120)
    if i == 2:
        ester.right(180)
        ester.forward(80)

alexander.color("blue")
alexander.penup()
alexander.forward(80)
alexander.pendown()
for i in range(4):
    alexander.forward(50)
    alexander.left(90)

window.mainloop()