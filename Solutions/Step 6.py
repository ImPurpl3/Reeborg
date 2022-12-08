import library as l

think(100)

l.turn_right()
think(100)
l.moveLoop(2)
turn_left()

l.moveLoop(3)
    
turn_left()
l.moveLoop(2)
take()
l.turn_around()

think(100)
l.moveLoop(2)
l.turn_right()
think(100)

l.moveLoop(3)
l.turn_right()

think(100)
l.moveLoop(2)
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
    for i in range(t):
        move()