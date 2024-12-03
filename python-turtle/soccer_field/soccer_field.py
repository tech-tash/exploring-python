import turtle

def rectangle(x, y, length):
    turtle.color("white")
    turtle.pensize(1)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length/2)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length/2)
    
def circle():
    turtle.penup()      #circle in the middle
    turtle.backward(420)
    turtle.backward(20)
    turtle.right(90)
    #turtle.pensize(1)
    turtle.pendown()
    turtle.circle(120, 360) 
    
    
def goal_post():
    turtle.forward(140)  #outer rectangle
    turtle.left(90)
    turtle.pendown()
    turtle.forward(160)
    turtle.right(90)
    turtle.forward(320)
    turtle.right(90)
    turtle.forward(160)
    
    turtle.penup()   #inner rectangle
    turtle.right(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(50)
    
def inner_coloured():        #inner goalposts triangles
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.begin_fill()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(10)
    turtle.end_fill()    
    
    
def main():    
    turtle.bgcolor("darkgreen")    
    #turtle.speed(0.2)    
    rectangle(-630, 315, 1255)  #big rectangle
    turtle.penup()
    
    turtle.right(90)     #line in the middle
    turtle.pendown()
    turtle.forward(1255/2)
    turtle.right(90)
    turtle.forward(1255/2)
    
    circle()
    turtle.penup()       #inner shaded circle
    turtle.left(90)
    turtle.forward(110)
    turtle.right(90)
    turtle.begin_fill()
    turtle.circle(10, 360)
    turtle.end_fill()
    
    turtle.penup()        #rectangle left goal post
    turtle.goto(-630, 315)
    turtle.left(90)
        
    goal_post()
    inner_coloured()
    turtle.penup()
    turtle.goto(625, -312)
    turtle.right(90)
    goal_post()   
    inner_coloured()    
    
    turtle.exitonclick() 
    
main()    