import turtle

def rectangle(x,y):
    turtle.penup()
    turtle.home()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color("maroon")
    turtle.begin_fill()
    
    for i in range(2):
        turtle.forward(250)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
        
    turtle.end_fill()    
    
def arm():
    turtle.penup()
    turtle.goto(50,-70)
    turtle.pendown()
    turtle.color("darkred")
    turtle.begin_fill()
    
    turtle.left(22)
    turtle.forward(255)
    #turtle.right(22)
    #turtle.forward(14)
    
    turtle.right(90)
    turtle.forward(30)
    
    turtle.right(90)
    turtle.forward(250)
    
    turtle.end_fill()
    
    
def main():
    
    turtle.shape("turtle")
    turtle.mode("logo")
    
    turtle.bgcolor("black")
    turtle.speed(3)
    
    #rectangle(-50, -70) 
    #rectangle(50, -70) 
    arm()
    rectangle(-50, -70) 
    rectangle(50, -70)    
    
    turtle.hideturtle()
    
    turtle.exitonclick()    
    
if __name__ == "__main__":
    main()

