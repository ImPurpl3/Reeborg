from library import *

i=0 # one move at a time count
ii=0 # turn around count (used for up or down, resets to 0)
iii=0 # turn around count (doesnt clear)
stopLoop = False # for the while loop

# line up
moveLoop(2)
turn("left")
moveLoop(2)

while stopLoop == False:
    think(50) # brain go brrrrr
    
    if object_here("carrot"):
        take()
    else:
        move()
        i+=1 # add to count for each move
    
    # extra grab incase we miss one
    if object_here("carrot"):
        take()
    
    if i==5:
        iii+=1 # add to count for breaking the loop
    
    # turn around going down
    if i==5 and ii == 0 and ii != 5:
        turn("right")
        move()
        turn("right")
        i=0
        ii+=1
        
    # turn around going up
    elif i==5 and ii == 1 and ii != 5:
        turn("left")
        move()
        turn("left")
        i=0
        ii=0
    elif iii == 6:
        stopLoop = True # break the loop
        
turn("around")
moveLoop(3)

# put carrots down
while carries_object("carrot"):
    put()
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