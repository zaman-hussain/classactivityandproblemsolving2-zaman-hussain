import turtle 

PIXEL_SIZE=20

def draw():
    turtle.speed(0)
    turtle.begin_fill()
    turtle.down()
    for i in range(4):
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
    turtle.up()
    turtle.end_fill()
    turtle.forward(PIXEL_SIZE)

def draw_black_pixel():
   draw_row()
   color_row() 
def draw_white_pixel():
   draw_row()
   color_row() 
def draw_red_pixel():
   draw_row()
   color_row() 
def draw_yellow_pixel():
   draw_row()
   color_row() 
def draw_orange_pixel():
   draw_row()
   color_row() 
def draw_green_pixel():
   draw_row()
   color_row() 
def draw_yellowgreen_pixel():
   draw_row()
   color_row() 
def draw_sienna_pixel():
   draw_row()
   color_row() 
def draw_tan_pixel():
   draw_row()
   color_row() 
def draw_gray_pixel():
   draw_row()
   color_row() 
def draw_darkgray_pixel():
    draw_row()
    color_row()

def draw_row(xcoordinate,ycoordinate,row,column,color):
    for i in range(1):
        xcoordinate+=PIXEL_SIZE*column
        ycoordinate+=PIXEL_SIZE*row
        xcoordinate+=PIXEL_SIZE
        turtle.up()
        turtle.fillcolor(color)
        turtle.goto(xcoordinate,ycoordinate)
        draw()

def color_row(colors,xcoordinate,ycoordinate):
    for i in colors:
        xcoordinate+=PIXEL_SIZE
        if i=='0':
            draw_row(xcoordinate,ycoordinate,5,4,'black')
        elif i=='1':
            draw_row(xcoordinate,ycoordinate,5,4,'white')
        elif i=='2':
            draw_row(xcoordinate,ycoordinate,5,4,'red')
        elif i=='3':
            draw_row(xcoordinate,ycoordinate,5,4,'yellow')
        elif i=='4':
            draw_row(xcoordinate,ycoordinate,5,4,'orange')
        elif i=='5':
            draw_row(xcoordinate,ycoordinate,5,4,'green')
        elif i=='6':
            draw_row(xcoordinate,ycoordinate,5,4,'yellowgreen')
        elif i=='7':
            draw_row(xcoordinate,ycoordinate,5,4,'sienna')
        elif i=='8':
            draw_row(xcoordinate,ycoordinate,5,4,'tan')
        elif i=='9':
            draw_row(xcoordinate,ycoordinate,5,4,'gray')
        elif i=='A':
            draw_row(xcoordinate,ycoordinate,5,4,'darkgray')
        else:
            return False

def main():
    xcoordinate=-450
    ycoordinate=150
    while True:
        colors=input("Please Enter a String :- ")
        for i in colors:
            if (i!='0') or (i!='1') or (i!='2') or (i!='3') or (i!='4') (i!='5') or (i!='6') or (i!='7') or (i!='8') or (i!='9') or (i!='A'):
                ycoordinate-=PIXEL_SIZE
                color_row(colors,xcoordinate,ycoordinate)
                colors=input("Please Enter a String :- ")
            else:
                break

if __name__=="__main__":
    main()