import turtle

def main():
    daniel = turtle.Turtle()    #Set up a turtle named "daniel"
    myWin = turtle.Screen()     #The graphics window

    #Draw a square
    for i in range(9):
        daniel.forward(100)     #Move forward 10 steps
        daniel.right(160)        #Turn 90 degrees to the right

    myWin.exitonclick()         #Close the window when clicked
    
main()		
	
