import turtle
col=('red','yellow','green','blue','orange','white')
t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
t.speed(100)
for i in range (520):

 t.color(col[i%6])
 t.forward(i*1.5)
 t.left(59)
 t.width(5)

