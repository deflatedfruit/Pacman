# The basic version to clone and modify

from turtle import *
from tkinter import *

root = Tk()
canv = Canvas(root,width=500,height=500)
screen = TurtleScreen(canv)
canv.grid(row=0,column=0)
t = RawPen(screen)
t.speed(0)
screen.setworldcoordinates(0,-500,500,0)

screen.bgcolor("#000000")
WALLCOLOR = "#000099"
PLAYERCOLOR = "#ffff00"
FILLED = True
SIZE = 10
score = 0
nodes = []

brd = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
    [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1],
    [4,4,4,4,4,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,4,4,4,4,4],
    [4,4,4,4,4,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,4,4,4,4,4],
    [4,4,4,4,4,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,4,4,4,4,4],
    [4,4,4,4,4,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,4,4,4,4,4],
    [4,4,4,4,4,1,0,1,1,0,1,4,4,4,4,4,4,1,0,1,1,0,1,4,4,4,4,4],
    [4,4,4,4,4,1,0,0,0,0,1,4,4,4,4,4,4,1,0,0,0,0,1,4,4,4,4,4],
    [4,4,4,4,4,1,0,1,1,0,1,4,4,4,4,4,4,1,0,1,1,0,1,4,4,4,4,4],
    [4,4,4,4,4,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,4,4,4,4,4],
    [4,4,4,4,4,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,4,4,4,4,4],
    [4,4,4,4,4,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,4,4,4,4,4],
    [1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
    [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
    [1,0,0,0,1,1,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
    [1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1],
    [1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1],
    [1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    # 0 is a food pellet
    # 1 is a wall
    # 2 is the player
    # 3 is an empty space
    # 4 is a different empty space

canv.configure(height=len(brd)*SIZE, width=len(brd[0])*SIZE)

# this bit does the nodes
for a in range(len(brd)):
    for b in range(len(brd[a])):
        try:
            if (brd[a][b] == 0 or brd[a][b] == 3) and ((brd[a+1][b] == 0 or brd[a-1][b] == 0) and (brd[a][b+1] == 0 or brd[a][b-1] == 0)):
                nodes.append((a,b))
        except IndexError:
            pass
def draw_square(color, location):
    t.goto(location[0], location[1])
    t.pd()
    t.color(color)
    if FILLED:
        t.begin_fill()
    for c in range(4):
        t.fd(SIZE-1)
        t.rt(90)
    t.end_fill()
    t.fd(SIZE-1)
    t.pu()


def draw_board():
    t.pu()
    t.ht()
    t.goto(0, 0)
    screen.tracer(0)
    for a in range(len(brd)):
        for b in range(len(brd[a])):
            if brd[a][b] == 0:
                t.pu()
                t.fd(SIZE/2)
                t.rt(90)
                t.fd(SIZE/2)
                if (a,b) not in nodes:
                    t.dot(SIZE/10,"#ffffff")
                else:
                    t.dot(SIZE/2,"#ffffff")
                t.bk(SIZE/2)
                t.lt(90)
                t.fd(SIZE/2)
            elif brd[a][b] == 1:
                draw_square(WALLCOLOR, convert((a,b)))
            elif brd[a][b] == 2:
                draw_square(PLAYERCOLOR, convert((a,b)))
        t.goto(convert((0,a)))
    screen.update()


def convert(coords):
    x = coords[1]
    y = coords[0]
    return (x*SIZE,-y*SIZE)


def move(direction):
    global player
    for a in enumerate(brd):
        for b in enumerate(a[1]):
            if b[1] == 2:
                player = (a[0], b[0])

    def __set__(a,b):
        global player, score
        draw_square(color=screen.bgcolor(), location=convert(player))
        brd[player[0]][player[1]] = 3
        player = (player[0]+a, player[1]+b)
        if brd[player[0]][player[1]] == 0:
            score += 1
        brd[player[0]][player[1]] = 2
        draw_square(color=PLAYERCOLOR, location=convert(player))

    if direction == "left"    and brd[player[0]][player[1]-1]%3 == 0:
        __set__(0,-1)
    elif direction == "right" and brd[player[0]][player[1]+1]%3 == 0:
        __set__(0,1)
    elif direction == "up"    and brd[player[0]-1][player[1]]%3 == 0:
        __set__(-1,0)
    elif direction == "down"  and brd[player[0]+1][player[1]]%3 == 0:
        __set__(1,0)


def next_frame():
    screen.onkeypress(lambda x="right": move(x),"Right")
    screen.onkeypress(lambda x="left": move(x), "Left")
    screen.onkeypress(lambda x="up": move(x),   "Up")
    screen.onkeypress(lambda x="down": move(x), "Down")
    screen.listen()
    root.after(10, next_frame)
    

draw_board()
next_frame()
