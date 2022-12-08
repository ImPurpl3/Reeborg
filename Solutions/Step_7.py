from library import *

def plantAndMove(loop): # plants then moves
    for i in range(loop):
        move()
        put()

think(100)

def do_zero(): # plants the "0" circle
    put()
    plantAndMove(4)
    turn("left")
    plantAndMove(2)
    turn("left")
    plantAndMove(4)
    turn("left")
    plantAndMove(1)

def do_one(): # plants the "1" line
    put()
    plantAndMove(4)
    
move()
turn("left")
move()

do_one()

turn("right")
moveLoop(2)
turn("right")

do_zero()

turn("around")
moveLoop(3)
turn("right")

do_zero()

turn("around")
moveLoop(3)
turn("right")

do_one()

turn("around")
moveLoop(4)
turn("right")
moveLoop(2)
turn("right")

do_zero()

turn("around")
moveLoop(3)
turn("right")
moveLoop(5)
done()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_around():
    think(50)
    turn_left()
    turn_left()
    think(100)
    
def turn_right():
    think(50)
    repeat 3:
        turn_left()
        
def moveLoop(t):
    think(100)
    for i in range(t):
        move()
        
def turn(direction):
    think(50)
    if direction == "right":
        repeat 3:
            turn_left()
    elif direction == "left":
        turn_left()
    elif direction == "around" or direction == "back":
        turn_left()
        turn_left()