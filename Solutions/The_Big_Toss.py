# The Big Toss Solution
# ImPurpl3 (Cole H.)

from library import *

# allow for more steps and think faster
set_max_nb_steps(1200)
think(0)

# set variable to the default robot
deRob = default_robot()

# face certain direction
def faceDirection(direction, reeb=deRob):
    while not reeb.is_facing_north():
        turn("right", reeb)
        
    if direction == "east":
        turn("right", reeb)
    elif direction == "south":
        turn("around", reeb)
    elif direction == "west":
        turn("left", reeb)
        
# custom function for moving that really helps
# goto x, y point
def gotoPoint(x, y, robot=deRob):
    # destination x, y variables
    destX = x
    destY = y
    
    # get robots current position
    startX = robot.position_here()[0]
    
    # figure out how many x we need to move to get to the destination
    xDiff = destX-startX
    
    # figure out which direction we need to face to go to the destination
    if xDiff < 0:
        faceDirection("west", robot)
    elif xDiff > 0:
        faceDirection("east", robot)
    
    # move x based on absolute value 
    for x in range(abs(xDiff)):
        # if we can move, move
        if robot.front_is_clear() == True:
            robot.move()
            continue
        else:
            # else, turn left
            turn("left", robot)

            # and see if we can move this way
            if robot.front_is_clear() == True:
                # move
                robot.move()
                # then relocate and break the loop
                gotoPoint(destX, destY, robot)
                break
            else:
                # else, turn around and move that way
                turn("around", robot)
                robot.move()

                # relocate and break loop
                gotoPoint(destX, destY, robot)
                break
            break
        
    # get robots current position
    startY = robot.position_here()[1]

    # figure out how many y we need to move to get to the destination
    yDiff = destY-startY
        
    # figure out which direction we need to face to go to the destination
    if yDiff < 0:
        faceDirection("south", robot)
    elif yDiff > 0:
        faceDirection("north", robot)
        
    # move y based on absolute value 
    # uses same rules as x mover
    for y in range(abs(yDiff)):
        if robot.front_is_clear() == True:
            robot.move()
            continue
        else:
            turn("right", robot)
            if robot.front_is_clear() == True:
                robot.move()
                gotoPoint(destX, destY, robot)
                break
            else:
                turn("around", robot)
                robot.move()
                gotoPoint(destX, destY, robot)
                break
            break

# array of the objects reeb has to pick up and place/toss down
objectArray = ["star", "apple", "leaf"]
        
# take all specified objects, args: object to take, robot that needs to take them (default if none passed through)
def takeAllObj(objt, robo=deRob):
    while robo.object_here(objt):
        robo.take(objt)
        
# toss all objects from array, args: robot that needs to toss (default if none passed through)
def tossAll(reeeb=deRob):
    for x in objectArray:
        while reeeb.carries_object(x):
            reeeb.toss(x)

# put down all specified objects, args: object to put, robot that needs to put (default if none passed through)
def putAll(objPut, robert=deRob):
    while robert.carries_object(objPut):
        robert.put(objPut)
            
# detect which quadrant of the map the spawned robot it in
def detectCorner():
    # get and set the default robot's current position
    pos = deRob.position_here()

    # if x coord is 10
    if pos[0] == 10:

        # if y coord is less that 2
        if pos[1] > 2:

            # quadrant is top right
            quad = "top_right"
        else:

            # else, quadrant is bottom right
            quad = "bottom_right"
    else:
        # else, quadrant is top left
        quad = "top_left"

    # return detected quadrant
    return quad

# mmm corn
corn = detectCorner()

# spawns more robots in depending on which quadrant the default robot is from
if corn == "top_right":

    # spawns top left, bottom right
    topLeftRobot = UsedRobot(1, 10)
    bottomRightRobot = UsedRobot(10, 1)
    topRightRobot = default_robot()

elif corn == "top_left":

    # spawns top right, bottom right
    topRightRobot = UsedRobot(10, 10)
    bottomRightRobot = UsedRobot(10, 1)
    topLeftRobot = default_robot()

elif corn == "bottom_right":

    # spawns top left, top right
    topLeftRobot = UsedRobot(1, 10)
    topRightRobot = UsedRobot(10, 10)
    bottomRightRobot = default_robot()

# spawns bottom left robot
bottomLeftRobot = UsedRobot(1, 1)
 
# sets trace colours for all the new robots because it looks nicer
bottomRightRobot.set_trace_color("#efff14")
topLeftRobot.set_trace_color("#ff1414")
topRightRobot.set_trace_color("#1cff14")
bottomLeftRobot.set_trace_color("#143fff")

# each robot goes to the point where the objects are
gotoPoint(1, 8, topLeftRobot)
gotoPoint(7, 7, topRightRobot)
gotoPoint(8, 3, bottomRightRobot)

# each robot takes all specified objects
takeAllObj("apple", topLeftRobot)
takeAllObj("leaf", topRightRobot)
takeAllObj("star", bottomRightRobot)

# each robot goes to the toss point
gotoPoint(3, 6, topLeftRobot)
gotoPoint(8, 7, topRightRobot)
gotoPoint(8, 6, topRightRobot)
gotoPoint(6, 3, bottomRightRobot)

# each robot tosses their objects over the wall
tossAll(topLeftRobot)
tossAll(topRightRobot)
tossAll(bottomRightRobot)

# bottom right robot goes to grab leafs from top right and then take them to the other wall to toss
gotoPoint(8, 5, bottomRightRobot)
takeAllObj("leaf", bottomRightRobot)
gotoPoint(6, 3, bottomRightRobot)
tossAll(bottomRightRobot)

# now all objects are in the bottom left quadrant

# bottom left robot goes and collects all objects
gotoPoint(5, 3, bottomLeftRobot)
takeAllObj("leaf", bottomLeftRobot)
takeAllObj("star", bottomLeftRobot)
gotoPoint(3, 5, bottomLeftRobot)
takeAllObj("apple", bottomLeftRobot)

# bottom left robot (with all objects) goes to the middle wall and tosses all objects
gotoPoint(4, 5, bottomLeftRobot)
tossAll(bottomLeftRobot)

# new robot inside the core spawns
insideRobot = UsedRobot(5, 5)
insideRobot.set_trace_color("#b114ff")

# inside robot takes all objects
for x in objectArray:
    takeAllObj(x, insideRobot)
    
# inside robot distributes all objects to their homes
gotoPoint(5, 6, insideRobot)
putAll("apple", insideRobot)
gotoPoint(6, 6, insideRobot)
putAll("leaf", insideRobot)
gotoPoint(6, 5, insideRobot)
putAll("star", insideRobot)

# top right robot builds walls
gotoPoint(7, 7, topRightRobot)
faceDirection("north", topRightRobot)
topRightRobot.build_wall()
faceDirection("east", topRightRobot)
topRightRobot.build_wall()

# bottom left robot builds walls
faceDirection("west", bottomLeftRobot)
bottomLeftRobot.build_wall()
gotoPoint(4, 4, bottomLeftRobot)
faceDirection("west", bottomLeftRobot)
bottomLeftRobot.build_wall()
faceDirection("south", bottomLeftRobot)
bottomLeftRobot.build_wall()
gotoPoint(5, 4, bottomLeftRobot)
faceDirection("south", bottomLeftRobot)
bottomLeftRobot.build_wall()

# done
done()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def moveLoop(t=None, rob=default_robot()):
    if t==None:
        while front_is_clear():
            rob.move()
    else:
        for i in range(t):
            rob.move()

def turn(direction, reob=default_robot()):
    if direction == "right":
        repeat 3:
            reob.turn_left()
    elif direction == "left":
        reob.turn_left()
    elif direction == "around" or direction == "back":
        reob.turn_left()
        reob.turn_left()