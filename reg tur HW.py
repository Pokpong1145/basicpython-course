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

def flower():
    for i in range(4):
        tao.circle(360)
        tao.left(360/4)

def stem():
        tao.right(90)
        tao.forward(300)
    
        
flower()
stem()
go(200,200)
flower()
stem()
go(-200,-200)
flower()
stem()

