import turtle
wn = turtle.Screen()
wn.bgcolor("yellow")
a = turtle.Turtle()
a.shape("turtle")

def draw(x, y):

	a.clear()
	a.reset()	
	
	a.backward(50)
	a.right(90)
	a.forward(50)
	a.left(90)
	a.forward(50)
	a.right(90)
	a.forward(50)
	a.right(90)
	a.forward(50)

	a.penup()
	a.backward(70)
	a.pendown()

	a.right(110)
	a.forward(105)
	a.right(140)
	a.forward(105)
	a.left(180)
	a.forward(55)
	a.left(70)
	a.forward(35)
	
	a.penup()
	a.left(180)
	a.forward(90)	
	a.pendown()
	
	a.right(90)
	a.forward(50)
	a.left(180)
	a.forward(100)
	
	a.left(90)
	a.forward(45)
	a.left(180)
	a.forward(90)	

	a.penup()
	a.forward(18)
	a.pendown()
	
	a.right(90)
	a.forward(100)
	a.left(180)
	a.forward(50)
	a.right(90)
	a.forward(55)
	a.left(90)
	a.forward(50)
	a.left(180)
	a.forward(100)

	a.penup()
	a.left(90)
	a.forward(25)
	a.pendown()

	a.left(60)
	a.forward(110)	
	a.right(180)
	a.forward(55)
	a.right(123)
	a.forward(55)
	a.left(180)

	a.penup()
	a.forward(110)
	a.pendown()
	
	a.right(117)
	a.right(110)
	a.forward(105)
	a.right(140)
	a.forward(105)
	a.left(180)
	a.forward(55)
	a.left(70)
	a.forward(35)

draw(0, 0)
wn.onclick(draw)
wn.listen()
wn.mainloop()
