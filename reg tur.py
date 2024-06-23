import turtle
tao=turtle.Pen()
tao.shape('turtle')

def reg():
	for i in range(4):
		tao.forward(100)
		tao.left(90)

def go(x,y):
	tao.penup()
	tao.goto(x,y)
	tao.pendown()

go(200,200)
reg()
