from library import *

think(25) # yeah

# get moved in place
moveLoop(3)
turn("right")
move()

# main loop
while not at_goal():
    
    # turn if at a corner
    if wall_in_front():
        if wall_on_right():
            turn("left")
        else:
            turn("right")
            
    # if we can move, move
    elif front_is_clear():
        move()
            
    if right_is_clear():
        move()
        
        # check if theres a window or just a open turn
        if right_is_clear():
            # if open turn, do the turn
            turn("around")
            move()
            turn("left")
        else:
            # if windows detected, close it
            turn("around")
            move()
            turn("left")
            build_wall()
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