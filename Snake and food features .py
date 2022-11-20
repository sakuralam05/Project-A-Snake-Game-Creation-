
# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor(green")
 
# the width and height can be put as user's choice
wn.setup(width=700, height=600)
wn.tracer(0)
 
 
# head of the snake
head = turtle.Turtle()
head.shape("circle")
head.color("pink")
head.penup()
head.goto(0, 0)
head.direction = "Stop"
 
 
# food in the game
food = turtle.Turtle()
colors = random.choice(['red', 'green'，'black','pink'])
shapes = random.choice(['square', 'triangle', 'circle','rectangle'])
food.speed(2.00)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)
 
 
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center",
          font=("candara", 24, "bold"))