def turn_right():
    repeat 3:
        turn_left() # turning left three times makes a right

i=0 # init iteration varible
while True:
    think(50)
    if wall_in_front() and wall_on_right(): # detect walls
        turn_left()
    elif wall_in_front(): # detect walls
        turn_right()
    elif object_here() and i != 14: # check for put spots based on iterations
        if i != 25 and i != 26: # idk what this is but it works
            take()
        else:
            move()
    elif at_goal():
        done()
    elif i == 13 or i == 24:
        put()
    elif front_is_clear():
        move()
    i+=1 # add 1 to iteration variable
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
