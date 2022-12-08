from library import *

think(25) # yeah

# set up banana and move
put("banana")
move()

while not object_here("banana"):
    # if we can turn right, turn right and move
    if right_is_clear():
        turn("right")
        move()
        
    # if we're at a corner, turn left
    elif not front_is_clear() and not right_is_clear():
        turn("left")
        
    # if we can move, move
    elif front_is_clear():
        move()

done()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
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