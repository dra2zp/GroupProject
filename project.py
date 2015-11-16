import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint

#########
#Description goes here
#########

#Initialize World
name = "Name Goes Here"
width = 500
height = 500
rw.newDisplay(width, height, name)

################################################################

# Display the state by drawing a cat at that x coordinate
myimage = dw.loadImage("Image Name Goes Here")

# state -> image (IO)
# draw the cat halfway up the screen (height/2) and at the x
# coordinate given by the first component of the state tuple
#
def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(myimage, (state[0], state[1]))


################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# Note that pos is accessed as state[0], and delta-pos
# as state[1]. Later on we'll see how to access state
# components by name (as we saw with records in Idris).
#
# state -> state
def updateState(state):
    return((state[0]+state[2],state[1]+state[3],state[2],state[3]))

################################################################

# Terminate the simulation when the x coord reaches the screen edge,
# that is, when pos is less then zero or greater than the screen width
# state -> bool
def endState(state):
    if (state[0] > width or state[0] < 0 or state[1]>height or state[1]<0):
        return True
    else:
        return False


################################################################

# We handle each event by printing (a serialized version of) it on the console
# and by then responding to the event. If the event is not a "mouse button down
# event" we ignore it by just returning the current state unchanged. Otherwise
# we return a new state, with pos the same as in the original state, but
# delta-pos reversed: if the cat was moving right, we update delta-pos so that
# it moves left, and vice versa. Each mouse down event changes the cat
# direction. The game is to keep the cat alive by not letting it run off the
# edge of the screen.
#
# state -> event -> state
#
def handleEvent(state, event):
#    print("Handling event: " + str(event))
    if (event.type == pg.MOUSEBUTTONDOWN):
        return((state[0],state[1],randint(-5,5),randint(-5,5)))
    else:
        return(state)

################################################################

# World state will be single x coordinate at left edge of world

# The cat starts at the upper left corner, moving right and down
initState = (randint(150,350), randint(150,350), randint(1,5), randint(1,5))

# Run the simulation no faster than 60 frames per second
frameRate = 60

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
