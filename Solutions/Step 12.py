from library import *

think(50) # brain go brrrrr
x=0

move()
turn("left")
moveLoop(2)

while object_here("apple"):
    take()
    x+=1

turn("around")
moveLoop(3)
turn("left")
moveLoop(4)
turn("left")
moveLoop(4)

for i in range(x):
    put()
    
turn("around")
moveLoop(4)
turn("right")
moveLoop(5)
turn("left")
moveLoop(2)
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