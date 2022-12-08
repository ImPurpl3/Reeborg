from library import *

think(50) # fast!

while not at_goal():

    # if we can go right, go right and move
    if right_is_clear():
        turn("right")
        move()
    
    # if we can move forward, move forward
    elif front_is_clear():
        move()

    # turn move along wall
    elif front_is_clear and not right_is_clear():
        turn("left")

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