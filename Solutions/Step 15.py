from library import *

think(50) # think faster

# get lined up
move()
turn("right")
move()

# loooooop
while not at_goal():
    
    # corner detection
    if wall_in_front() and wall_on_right():
        turn("left")
    
    # hole detection
    if not wall_on_right():
        turn("right")
        build_wall()
        turn("left")
        
    # go forward
    else:
        move()
        
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
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
