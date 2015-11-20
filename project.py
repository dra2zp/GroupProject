import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint

#########
#Description goes here
#########

#Initialize World
name = "Chase Game"
width = 500
height = 500
rw.newDisplay(width, height, name)

################################################################

dogimage = dw.loadImage("dog.bmp")
catimage = dw.loadImage("cat.bmp")

def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(dogimage, (state[0][0], state[0][1]))
    dw.draw(catimage, (200, 200))


################################################################

def updateState(state):
    if (state[2][0] == 1):
        if (state[2][1] == 0):
            state[0][3] = -dogspeed
    if (state[2][1] == 1):
        if (state[2][0] == 0):
            state[0][3] = dogspeed
    if (state[2][2] == 1):
        if (state[2][3] == 0):
            state[0][2] = -dogspeed
    if (state[2][3] == 1):
        if (state[2][2] == 0):
            state[0][2] = dogspeed
    return(((state[0][0]+state[0][2], state[0][1]+state[0][3], state[0][2], state[0][3]),(state[1][0]+state[1][2], state[1][1]+state[1][3], state[1][2], state[1][3]),state[2]))

################################################################

def endState(state):
    ##if (state[0] > width or state[0] < 0 or state[1]>height or state[1]<0):
        ##return True
    ##else:
        return False


################################################################

def handleEvent(state, event):
    if (event.type == pg.KEYDOWN and event.key == K_UP):
        return((state[0],state[1],(1, state[2][1], state[2][2], state[2][3])))
    elif (event.type == pg.KEYUP and event.key == K_UP):
        return((state[0],state[1],(0, state[2][1], state[2][2], state[2][3])))
    elif (event.type == pg.KEYDOWN and event.key == K_DOWN):
        return((state[0],state[1],(state[2][0], 1, state[2][2], state[2][3])))
    elif (event.type == pg.KEYUP and event.key == K_DOWN):
        return((state[0],state[1],(state[2][0], 0, state[2][2], state[2][3])))
    elif (event.type == pg.KEYDOWN and event.key == K_LEFT):
        return((state[0],state[1],(state[2][0], state[2][1], 1, state[2][3])))
    elif (event.type == pg.KEYUP and event.key == K_LEFT):
        return((state[0],state[1],(state[2][0], state[2][1], 0, state[2][3])))
    elif (event.type == pg.KEYDOWN and event.key == K_RIGHT):
        return((state[0],state[1],(state[2][0], state[2][1], state[2][2], 1)))
    elif (event.type == pg.KEYUP and event.key == K_RIGHT):
        return((state[0],state[1],(state[2][0], state[2][1], state[2][2], 0)))
    else:
        return(state)

################################################################

# World state will be single x coordinate at left edge of world
#dog position and velocity, cat position and velocity, up down left right states (in that order)
initState = ((0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0 ,0))
dogspeed = 3
# Run the simulation no faster than 60 frames per second
frameRate = 60

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent, endState, frameRate)
