def turn_right():
    think(1)
    repeat 3:
        turn_left()

def turn_back():
    think(25)
    turn_left()
    turn_left()
    
def grab_berri():
    think(100)
    repeat 2:
        move()
        take()
    turn_back()
    move()
    move()
    put()
    put()
    
repeat 2:
    think(50)
    move()
    turn_left()
    grab_berri()
    turn_left()
    move()
    turn_right()
    grab_berri()
    turn_right()

move()
move()
done()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
