import pixart as p
import turtle

def odd_row(): #forms rows which have odd number
    for i in range(10):
        turtle.speed(0)
        p.draw_pixel('red')
        p.draw_pixel('black')
    
def even_row(): #forms rows which have even number
        for i in range(10):
            turtle.speed(0)
            p.draw_pixel('black')
            p.draw_pixel('red')

def main():
    p.turtle.Screen().setup(width=1.0,height=1.0) 
    p.initialize()
    p.draw_grid()
    a=0
    for i in range(10):
        odd_row()
        a=a+1
        p.move(a,0)
        even_row()
        a=a+1
        p.move(a,0)
        

main()
