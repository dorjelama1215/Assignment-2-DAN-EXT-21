import turtle 

#Recursive function to draw one edge
def draw_edge(d,length,depth):
    if depth==0:                       #base case(if depth=0 draw a straight line)
        d.forward(length)         
    else:
     #Divide the line into 3 segments and apply case for depth>0
        draw_edge(d,length/3,depth-1)   #first segment
        d.right(60)                     #turn right to start inward indentation 
        draw_edge(d,length/3,depth-1)    #second segment 
        d.left(120)                   #turn left to draw the second side
        draw_edge(d,length/3,depth-1)   #third segment
        d.right(60)                     #turn right to return to original direction
        draw_edge(d,length/3,depth-1)        #fourth segment 

#User input
sides=int(input("Enter the number of sides:"))
length=int(input("Enter the side length:"))
depth=int(input("Enter the recursion depth:"))

#Turtle setup
d = turtle.Turtle()
d.speed(0)
d.penup()
d.goto(-length/2,length/2)   #center drawing
d.pendown()
d.hideturtle()

#Draw the polygon
angle=360/sides
for i in range(sides):
   draw_edge(d,length,depth)   #draw one edge 
   d.right(angle)         

turtle.done()