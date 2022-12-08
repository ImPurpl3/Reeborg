move()
while True:
    if wall_in_front():
        turn_left()
    elif at_goal():
        done()
    else:
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
