import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.color("green")
turtle.left(90)

turtle.backward(100)
turtle.speed(200)
turtle.shape("turtle")

def tree(i):
    if i < 10:
        return
    
    else:
        turtle.forward(i)
        turtle.color("white")  #flower
        turtle.circle(2)
        turtle.color("lightgreen")    #stem
        turtle.left(30)
        tree(3*i/4)
        turtle.right(60)
        tree(3*i/4)        
        turtle.left(30)
        turtle.backward(i)
        
tree(100)        
turtle.exitonclick()