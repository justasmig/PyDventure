'''
Documentations used: 
1. https://docs.python.org/3/tutorial/classes.html
2. https://github.com/boppreh/keyboard
3. https://www.pythonforbeginners.com/basics/string-manipulation-in-python
4.
5.
6.

'''

import os
import time
import keyboard

stage = 1
def levels():
    currStage = ''
    if stage == 1:  # 0123456789012345678
        currStage = ["  |                ", 
                     "  |             >  ",   #1
                     "  |             >  ",   #2
                     "  |             >  ",   #3
                     "  |             |  ",   #4
                     "  |             |  ",   #5
                     "  |_____________|  ",   #6
                     "                   "]   #7
    if stage == 2:
        currStage = ["                |  ",   #0
                     "  <             |  ",
                     "  <             |  ",   #2
                     "  <             |  ",
                     "  |             |  ",   #4
                     "  |             |  ",
                     "  |____|________>  ",   #6
                     "                   "]
    if stage == 3:
        currStage = ["  |             1  ",   #0
                     "  |             1  ",
                     "  |             1  ",   #2
                     "  |             1  ",
                     "  |             1  ",   #4
                     "  |       |     1  ",
                     "  <_______|_____1  ",   #6
                     "                   "]
        
    if stage == 420:
        currStage = ["  !!!!!!!!!!!!!!!!!!CONGRATULATIONS!!!!!!!!!!!!!!!!!!  ",   #0
                     "  |                 You Have Unlocked               |  ",
                     "  |                 The BIGGER levels.              |  ",   #2
                     "  |                                                 |  ",
                     "  |                                                 >  ",   #4
                     "  |                                                 |  ",
                     "  |                                                 |  ",   #6
                     "  |_________________________________________________|  ",   
                     "                                                       "]   #8
    if stage == 421:
        currStage = ["  !!!!!!!!!!!!!!!!!!CONGRATULATIONS!!!!!!!!!!!!!!!!!!  ",   #0
                     "  |                                                 |  ",
                     "  |                                                 |  ",   #2
                     "  |                                                 |  ",
                     "  <                                                 >  ",   #4
                     "  |                                                 |  ",
                     "  |                THEY ARE COOLER (and bigger)     |  ",   #6
                     "  |_________________________________________________|  ",   
                     "                                                       "]   #8
    if stage == 422:
        currStage = ["  !!!!!!!!!!!!!!!!!!CONGRATULATIONS!!!!!!!!!!!!!!!!!!  ",   #0
                     "  |                                                 |  ",
                     "  |                                                 |  ",   #2
                     "  |                                                 |  ",
                     "  <                   ^ = death                     >  ",   #4
                     "  |                                                 >  ",
                     "  |           ...cooler AND imposible... GL HF      >  ",   #6
                     "  |____________________                             >  ",   
                     "                       ^^^^^+++^^^^^^^^^^^^^^^^^^^^^   ",
                     "                                                       "]   #8
    if stage == 423:
        currStage = ["  !!!!!!!!!!!!!!!!!!CONGRATULATIONS!!!!!!!!!!!!!!!!!!  ",   #0
                     "  |                                                 |  ",
                     "  |                                                 |  ",   #2
                     "  |                                                 |  ",
                     "  |                   THAT'S NOT POSSIBLE           |  ",   #4
                     "  |                               WTF               |  ",
                     "  |           But congrats winning the game.        |  ",   #6
                     "  |____________________             Please crash    |  ",   
                     "                                        yourself out   ",
                     "                                                       "]   #8
    return currStage

### PLAYER PARAMS AND FUNCTIONS ###
class Player:
    position = [3, 6] #x, y
    canJump = True
    sprite = '8'
    jumpHeight = 2
    isJumping = False
    onGround = False
    bigStage = True
    alive = True
plr = Player()
origCurrentStage = levels()
currentStage = levels()
currentInput = ""


# old jump function
def Jump():
    i = 0
    plr.isJumping = True
    plr.canJump = False
    while i < plr.jumpHeight:
        Move('up', plr)
        i += 1
    plr.isJumping = False
    plr.canJump = True

def CanMove(dir):
    plrX = plr.position[0]
    plrY = plr.position[1]
    plrLine = currentStage[plrY]
    if dir == 'right':
        if plrLine[plrX+1:plrX+2] != "|": #or plrLine[plrX+1:plrX+1] == "_":
            return True
        else:
             False
    if dir == 'left':
        if plrLine[plrX-1:plrX] != "|": #or plrLine[plrX-1:plrX-1] == "_":
            return True
        else:
             False

def PlrDetectGround():
    plrX = plr.position[0]
    plrY = plr.position[1]
    if origCurrentStage[plrY][plrX] == "_" or  origCurrentStage[plrY][plrX] == "|":
        plr.onGround = True
    else:
        plr.onGround = False
### OBJECT FUNCTIONS ###
def Move(dir, obj):
    if dir == 'right':
        obj.position[0] += 1
    if dir == 'left':
        obj.position[0] -= 1
    if dir == 'up':
        obj.position[1] -= 1

def Gravity(obj):
    obj.position[1] += 1
    

### RENDERING ###
def CoNgRAtS_YoU_wOn_THe_GamE_By_CrAShInG_ThE_ReNDeR_L00P_GG_FU111223123212312331231231231231231231231232123121331231221323132123213231123321123231213():     
    plrX = plr.position[0]
    plrY = plr.position[1]
    #plrLine = currentStage[plrY]
    origLine = origCurrentStage[plrY]
    modifiedLine = origLine[:plrX] + plr.sprite + origLine[plrX+1:]
    currentStage[plrY] = modifiedLine
    currentStage[plrY-1] = origCurrentStage[plrY-1]
    currentStage[plrY+1] = origCurrentStage[plrY+1] # CONGRATULAAAAAAAAAAAAAAAAAATITOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOONS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! PLOT TWIST U DIED AND NOW UR IN HEAVEN
    
    
def RenderStage(stage):

    # For small stages
    if plr.bigStage == False:
        print('{}\n{}\n{}\n{}'.format(
            stage[plr.position[1]-2], 
            stage[plr.position[1]-1], 
            stage[plr.position[1]], 
            stage[plr.position[1]+1]
                )
            )
    elif plr.bigStage == True:
        print('{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(
            stage[plr.position[1]-5], 
            stage[plr.position[1]-4], 
            stage[plr.position[1]-3], 
            stage[plr.position[1]-2], 
            stage[plr.position[1]-1], 
            stage[plr.position[1]], 
            stage[plr.position[1]+1]
                )
            )
ticks = 0
jumpingTicks = 0
### GAME LOOP ###
while True:
    plrX = plr.position[0]
    plrY = plr.position[1]
    ticks += 1
    PlrDetectGround()
    ### CHECKING STAGE SWITCHING ###
    if origCurrentStage[plrY][plrX] == "1":
        stage = 420
        origCurrentStage = levels()
        currentStage = levels()
        plr.position[0] = 22
        plr.position[1] = 0
        plr.bigStage = True
        plr.onGround = False
    elif origCurrentStage[plrY][plrX] == ">" or origCurrentStage[plrY][plrX] == "+":
        plr.position[0] = 3
        stage += 1
        origCurrentStage = levels()
        currentStage = levels()
        plr.onGround = True
    
    elif origCurrentStage[plrY][plrX] == "<":
        plr.position[0] = 15
        stage -= 1
        origCurrentStage = levels()
        currentStage = levels()
        plr.onGround = True
    elif origCurrentStage[plrY][plrX] == "^":
        plr.alive = False
        
    if plr.onGround == False and plr.isJumping == False:
        Gravity(plr)
        
    ### INPUT ###
    currentInput = ""
    if keyboard.is_pressed("d"):
        currentInput = "D"
        if CanMove("right"):
            Move('right', plr)
    if keyboard.is_pressed("a"):
        currentInput = "A"
        if CanMove("left"):
            Move('left', plr)
    if keyboard.is_pressed("w"):
        currentInput = "W"
        if plr.isJumping == False and plr.onGround == True:
            plr.isJumping = True
            jumpingTicks = ticks + 3
            
    ### JUMPING ###
    if jumpingTicks > ticks:
        Move("up", plr)
        plr.isJumping = True
    else: 
        plr.isJumping = False
        
    ### RENDERING ###
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n\n\n\n\n')
    if plr.alive:
        CoNgRAtS_YoU_wOn_THe_GamE_By_CrAShInG_ThE_ReNDeR_L00P_GG_FU111223123212312331231231231231231231231232123121331231221323132123213231123321123231213()    
        RenderStage(currentStage)
    else:
        print ("   U    D I E D    . . .")
        break
    print('\n plrX = {},  plr Y = {} \n current input: {} \n what is on right: "{}" \n what is on left: "{}" '.format(plr.position[0], plr.position[1], currentInput, currentStage[plr.position[1]][plr.position[0]+1:plr.position[0]+2], currentStage[plr.position[1]][plr.position[0]-1:plr.position[0]]))
    time.sleep(0.1)