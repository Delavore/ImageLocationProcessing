import sys
import pyxel
from PIL import Image
import math

COLOR_ROAD = (255, 255, 255, 255)
# COLOR_ROAD = (134, 141, 134, 255)
COLOR_PLAYER = (1, 144, 219, 255)
RANGE_COLOR_PLAYER = ((0, 20), (100, 150), (150, 230))

BORDER_OFFSET = 5
STEP = 1
CENTER_DOT_BORDER = 8
CURSOR_BORDER = 37
HALF_SIDE = 4

# approximation some coordinates into one coordinate using arithmetical mean
def getAprox(coords: list) -> list:
    coord = [0, 0]

    for c in coords:    
        coord[0] += c[0]
        coord[1] += c[1]
    
    # checking division by zero
    if len(coords) == 0:
        sys.exit('getApprox: len(coords) = 0, division by zero')

    coord[0] /= len(coords)
    coord[1] /= len(coords)

    return coord

# количество точек, которые находятся в пределах квадрата со стороной halfSide*2 для каждой координаты 
# quantity of points that are within square with side halfSide*2 for each coordinate
# player - all coordinates of player
def getDotsInSquare(player: list, halfSide: int) -> list:
    quantity = []
     
    for i in range(len(player)):
        # upper-left coordinate of square
        upLeft = (player[i][0] - halfSide, player[i][1] + halfSide)
        # down-right coordinate of square
        downRight = (player[i][0] + halfSide, player[i][1] - halfSide) 

        # counting quantity of points in a square for current vertex
        cnt = 0
        for j in range(len(player)):
            if (upLeft[0] <= player[j][0] <= downRight[0] and 
                upLeft[1] >= player[j][1] >= downRight[1]): 
                cnt += 1

        quantity.append(cnt)
    return quantity

# return the coordinate of the player's center and the direction vector
def getPerson(screen: str) -> list:
    # precomputation
    img = Image.open(screen)
    pix = img.load()
    width, height = img.size

    # get all dots that relation the player
    player = []
    for y in range(BORDER_OFFSET, height-BORDER_OFFSET, STEP):
        for x in range(BORDER_OFFSET, width-BORDER_OFFSET, STEP):
            color = pix[x, y]

            if ((RANGE_COLOR_PLAYER[0][0] <= color[0] <= RANGE_COLOR_PLAYER[0][1]) and
                (RANGE_COLOR_PLAYER[1][0] <= color[1] <= RANGE_COLOR_PLAYER[1][1]) and 
                (RANGE_COLOR_PLAYER[2][0] <= color[2] <= RANGE_COLOR_PLAYER[2][1])):
                player.append((x, y))

    # abort
    if len(player) == 0:
        return [-1, -1]

    quantities = getDotsInSquare(player, HALF_SIDE)

    centerDotCoord = []
    cursorCoord = []
    
    # find coordinates of cursor and center of Player
    for i in range(len(player)):        
        if quantities[i] <= CENTER_DOT_BORDER:
            centerDotCoord.append(player[i])
        elif quantities[i] >= CURSOR_BORDER:
            cursorCoord.append(player[i])

    # abort
    if len(centerDotCoord) == 0 or len(cursorCoord) == 0:
        return [-1, -1]
        
    # approximate coordinates
    centerDotCoord = getAprox(centerDotCoord)
    cursorCoord = getAprox(cursorCoord)

    # dirVec - directionVector
    dirVec = [cursorCoord[0] - centerDotCoord[0], cursorCoord[1] - centerDotCoord[1]]
    vecLen = ((cursorCoord[0] - centerDotCoord[0])**2 + 
         (cursorCoord[1] - centerDotCoord[1])**2)**0.5
    
    # normalize vector
    dirVec[0] /= vecLen
    dirVec[1] /= vecLen

    return [centerDotCoord, dirVec]

# get angel between direction vector of player and target coordinate
def getAngle(playerCoord: list, dirVec: list, targetCoord: list) -> float:
    helpVec = (targetCoord[0] - playerCoord[0], targetCoord[1] - playerCoord[1])

    # calculate the cosine of the angle between dirVec and helpVec using scolar multiplication
    cosAlpha = ((dirVec[0] * helpVec[0] + dirVec[1] * helpVec[1]) / 
    ((((helpVec[0])**2 + (helpVec[1])**2)**0.5) * (((dirVec[0])**2 + (dirVec[1])**2)**0.5)))
    
    print("cosa", cosAlpha)
    
    alpha = math.acos(cosAlpha)
    alpha = alpha * 180 / math.pi
 
    # calculate the sign of the angle using the vector product
    tmp = dirVec[0] * helpVec[1] - helpVec[0] * dirVec[1]

    '''
    if tmp >= 0:
        sign = 1
    else:
        sign = -1

    return alpha * sign
    '''
    return alpha if tmp >= 0 else -alpha

#
def getRoad(imgPng) -> list:
    img = Image.open(imgPng)
    pix = img.load()
    width, height = img.size
    x = 0
    y = 0
    road = []

    for y in range(BORDER_OFFSET, height-BORDER_OFFSET, STEP):
        for x in range(BORDER_OFFSET, width-BORDER_OFFSET, STEP):
            color = pix[x, y]
            if (COLOR_ROAD[0]-7 <= color[0] <= COLOR_ROAD[0]+7 and 
            COLOR_ROAD[1]-7 <= color[1] <= COLOR_ROAD[1]+7 and
            COLOR_ROAD[2]-7 <= color[2] <= COLOR_ROAD[2]+7):
                road.append((x, y))
    return road

def aproxRoad(road: list, halfSide: int):
    tmp1 = []
    tmp2 = []

    i = 0
    while i < len(road):
        if i >= len(road):
            break
        upLeft = (road[i][0] - halfSide, road[i][1] + halfSide) 
        downRight = (road[i][0] + halfSide, road[i][1] - halfSide) 
        tmp1 = []

        j = 0
        while j < len(road):
            if j >= len(road):
                break
            if (upLeft[0] <= road[j][0] <= downRight[0] and 
                upLeft[1] >= road[j][1] >= downRight[1]): 
                tmp1.append(road[j])
                road.pop(j)
                j -= 1
            j += 1
        tmp2.append(tmp1)

    tmp3 = []
    for i in range(len(tmp2)):
        tmp3.append(getAprox(tmp2[i]))
        tmp3[i][0] = int(tmp3[i][0])
        tmp3[i][1] = int(tmp3[i][1])
    return tmp3

#         ,--. 
#        ((\\)
#        \-_/  
#      .--.v.-.
#     /( .)( .)\  sexAprox 
#     \ \    /  \/‾‾
#      \_) .(    
#       /    \
#      :   Y  :
#######`.   \ :#########  
#########`.  \:######### 
#          `) )  
#          / /:  
#         / / :
#        (_\/_\

def aproxSex(road1: list, halfSide: int):
    tmp = []
    road = []
    for i in range(len(road1)):
        road.append(road1[i])
    tmp.append(road[0])
    road.pop(0)
    target = tmp[0]

    i = 0
    while True:   
        flag = True

        upLeft = (target[0] - halfSide, target[1] + halfSide) 
        downRight = (target[0] + halfSide, target[1] - halfSide) 

        j = 0
        while j < len(road):
            if (upLeft[0] <= road[j][0] <= downRight[0] and 
                upLeft[1] >= road[j][1] >= downRight[1]): 
                tmp.append(road[j])
                target = road[j]
                road.pop(j)
                j -= 1
                flag = False
                break
            j += 1

        if flag:
            break  

    # second_peace #    

    target = tmp[0]  
    tmp2 = []      

    i = 0
    while True:
        flag = True

        upLeft = (target[0] - halfSide, target[1] + halfSide) 
        downRight = (target[0] + halfSide, target[1] - halfSide) 

        j = 0
        while j < len(road):
            if (upLeft[0] <= road[j][0] <= downRight[0] and 
                upLeft[1] >= road[j][1] >= downRight[1]): 
                tmp2.append(road[j])
                target = road[j]
                road.pop(j)
                j -= 1
                flag = False
                break
            j += 1
        if flag:
            break
        
    tmp2 = list(reversed(tmp2))
    tmp2.extend(tmp)
    return tmp2    

u = getRoad("map2.png") 
u1 = aproxSex(u, 1)
u2 = aproxRoad(u1, 5)
print(u2)

class Game:
    def __init__(self):
        width, height, self.player, self.road = [700, 700, (300, 300), u2]
        pyxel.init(width, height)
        print(width, height, self.player, len(self.road))
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)
        for c in self.road:
            pyxel.circ(c[0], c[1], 1, pyxel.COLOR_WHITE) #10
        pyxel.circ(self.player[0], self.player[1], 3, pyxel.COLOR_RED)

Game()

