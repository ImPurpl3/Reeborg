from library import *

think(50) # brain go brrrrr

def hurdle(): # go over hurdle
    turn("left")
    move()
    turn("right")
    move()
    turn("right")
    move()
    turn("left")

while not at_goal():
    if front_is_clear():
        move()
    else:
        hurdle()
    
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