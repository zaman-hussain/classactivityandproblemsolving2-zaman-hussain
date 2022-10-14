import turtle

PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20

LEFT = -(COLUMNS/2) * PIXEL_SIZE
TOP = (ROWS/2) * PIXEL_SIZE

def initialize():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(LEFT,TOP)
    turtle.pencolor('black')
    turtle.fillcolor('white')

def draw_pixel(pixel_color):
    turtle.pendown()
    turtle.pencolor('black')    
    turtle.fillcolor(pixel_color)
    turtle.begin_fill()

    sides = 0
    while sides < 4:
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
        sides += 1

    turtle.forward(PIXEL_SIZE)

    turtle.end_fill()
    turtle.penup()

def get_x(column):
    return LEFT + (PIXEL_SIZE*column)

def get_y(row):
    return TOP - (PIXEL_SIZE*row)

def move(row,column):
    turtle.penup()
    turtle.goto(get_x(column),get_y(row))

def draw_grid():
    turtle.tracer(False)
    row = 0
    while row < ROWS:
        col = 0
        move(row,col)
        while col < COLUMNS:
            draw_pixel("white")
            col += 1
        row += 1
    move(0,0)
    turtle.tracer(True)

def main():
    turtle.Screen().setup(width=1.0,height=1.0) # fullscreen
    initialize()
    draw_grid()

    #input("Press enter to continue...")   # for some Mac users!
    turtle.done()

if __name__ == "__main__":
    main()
