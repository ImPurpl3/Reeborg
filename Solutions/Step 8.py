from library import *

think(50) # brain go brrrrr

dontPlace = True
x=0 # dandelion count

while dontPlace == True:
    move()
        
    if object_here("dandelion"): # pick up dandelion when on one
        take()
        x+=1 # add 1 to danedelion count
        
    if wall_in_front(): # turn around and stop loop
        turn("around")
        dontPlace = False

repeat 12:
    move() # go back
    
for i in range(x): # put down as many as we picked up
    put()
    
move()
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