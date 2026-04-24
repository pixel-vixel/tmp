from turtle import*
x_start,y_start = -150,50
size = 100

positions = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
current_move = "cross"

screen = Screen()
screen.bgcolor("purple")

def draw_field(c):
    width(5)
    y = y_start
    x = x_start
    speed(0)
    pu()
    goto(x,y)
    pd()
    color(c)
    for col in range(3):
        for row in range(3):
            for i in range(4):
                fd(size)
                lt(90)
            fd(100)
        y -= 100
        pu()
        goto(x, y)
        pd()
    
def draw_cross(x, y):
    color("red")
    width(5)
    pu()
    goto(x, y)
    pd()
    setheading(45)
    fd(1.4*size)
    pu()
    goto(x+size, y)
    pd()
    setheading(135)
    fd(1.4*size)

def draw_zero(x, y):
    #твій код
    width(5)
    color("blue")
    pu()
    goto(x+size//2, y)
    pd()
    setheading(0)
    circle(size//2)
    
def check_click(x, y):
    global current_move, positions
    row, col = 0, 0
    if ((x < x_start or x > x_start + 3 * size) or
        (y > y_start + 100 or y < y_start - 2 * size)):
        print("Nothin' go out the box idiot, GET OUT!!")
    else:
        if x >= 50:
            x = 50
            col = 2
        elif x >= -50:
            x = -50
            col = 1
        elif x >= -150:
            x = -150
            col = 0

        if y >= 50:
            y = 50
            row = 0
        elif y >= -50:
            y = -50
            row = 1
        elif y >= -150:
            y = -150
            row = 2
        if positions[col + row * 3] != -1:
            print("There is a symbol here dumie")
        else:
            if current_move == "cross":
                draw_cross(x, y)
                current_move = "zero"
                positions[col + row * 3] = 1
            elif current_move == "zero":
                draw_zero(x, y)
                current_move = "cross"
                positions[col + row * 3] = 0
    

draw_field("#089db8")


screen.onclick(check_click)
done()