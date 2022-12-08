from library import *

set_max_nb_steps(2000) # set new max because it took too many steps one time on a 8x8 board
think(50) # fast!

# goes to top left corner for orientation/calibration
def calibrate():
    while not is_facing_north():
        turn("left")
    
    while front_is_clear():
        move()
        
    turn("left")
    
    while front_is_clear():
        move()
        
# moves until wall
def goUntilWall():
    while front_is_clear():
        move()

calibrate() # goes to top left corner

turn("around") # turns to face east

# variable setup
i=0
loopBreak = False

# to move down each row
def moveDown():
    turn("left")
    
    # get orientation to figure out which way to go down
    if is_facing_north():
        turn("right")
        move()
        turn("right")
    else:
        turn("left")
        move()
        turn("left")
        
    turn("right")

# main loop
while loopBreak == False:
    think(5) # think faster
    if object_here("carrot"):
        take()
        i+=1 # counting how many we pick up
    
    if front_is_clear() and not object_here("carrot"):
        move()
        
    elif not front_is_clear() and not object_here("carrot"):
        # checks for if we're at the end of a column
        if not wall_on_right():
            if not at_goal():
                # move down if we're at end of column
                moveDown()
            else:
                loopBreak = True
        # stop loop because we're at bottom corner
        else:
            loopBreak = True

# go back to home corner
calibrate()

# get oriented
while not is_facing_north():
    turn("left")

turn("right")    

# gets us to dropoff spot
goUntilWall()

# drop off count
for x in range(i):
    put()

# orient and move to goal
turn("around")
goUntilWall()
turn("left")
goUntilWall()

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