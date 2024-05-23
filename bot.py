import pyxel
from PIL import Image
import math

COLOR_ROAD = (255, 255, 255, 255)
# COLOR_ROAD = (134, 141, 134, 255)
COLOR_PLAYER = (1, 144, 219, 255)
BORDER_OFFSET = 5
STEP = 1
CENTER_DOT_BORDER = 8
CURSOR_BORDER = 37
HALF_SIDE = 4
#
def getAprox(coords: list) -> list:
    coord = [0, 0]

    for c in coords:    
        coord[0] += c[0]
        coord[1] += c[1]
    coord[0] /= len(coords)
    coord[1] /= len(coords)
    return coord
#
def getPlayerVert(player: list, hSide: int) -> list:
    vertecies = []

    for i in range(len(player)):
        upLeft = (player[i][0] - hSide, player[i][1] + hSide) 
        downRight = (player[i][0] + hSide, player[i][1] - hSide) 

        cnt = 0
        for j in range(len(player)):
            if upLeft[0] <= player[j][0] <= downRight[0] and upLeft[1] >= player[j][1] >= downRight[1]: 
                cnt += 1

        vertecies.append(cnt)
    return vertecies
#
def getPerson(myImg) -> list:
    img = Image.open(myImg)
    pix = img.load()
    width, height = img.size

    x = 0
    y = 0
    player = []
    for y in range(BORDER_OFFSET, height-BORDER_OFFSET, STEP):
        for x in range(BORDER_OFFSET, width-BORDER_OFFSET, STEP):
            color = pix[x, y]
            if (0 <= color[0] <= 20) and (100 <= color[1] <= 150) and (150 <= color[2] <= 230): 
                player.append((x, y))
    if len(player) == 0:
        return [-1, -1]

    vertecies = getPlayerVert(player, HALF_SIDE)
    tmp1 = []
    tmp2 = []
    
    for i in range(len(player)):        
        if vertecies[i] <= CENTER_DOT_BORDER:
            tmp1.append(player[i])
        elif vertecies[i] >= CURSOR_BORDER:
            tmp2.append(player[i])
    if len(tmp1) == 0 or len(tmp2) == 0:
        return [-1, -1]
        
    centerDotCoord = getAprox(tmp1)
    cursorCoord = getAprox(tmp2)
    vec = [cursorCoord[0] - centerDotCoord[0], cursorCoord[1] - centerDotCoord[1]]
    h = ((cursorCoord[0] - centerDotCoord[0])**2 + (cursorCoord[1] - centerDotCoord[1])**2)**0.5
    vec[0] /= h
    vec[1] /= h
    return [centerDotCoord, vec]

def getAngle(playerCoord: list, playerVec: list, targetCoord: list) -> float:
    newVec = (targetCoord[0] - playerCoord[0], targetCoord[1] - playerCoord[1])
    cosa = (playerVec[0] * newVec[0] + playerVec[1] * newVec[1]) / ((((newVec[0])**2 + (newVec[1])**2)**0.5) * (((playerVec[0])**2 + (playerVec[1])**2)**0.5))
    print("cosa", cosa)
    
    alpha = math.acos(cosa)
    alpha = alpha * 180 / math.pi
    tmp = playerVec[0] * newVec[1] - newVec[0] * playerVec[1]
    
    if tmp >= 0:
        sign = 1
    else:
        sign = -1
    return alpha * sign
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

def aproxRoad(road: list, hSide: int):
    tmp1 = []
    tmp2 = []

    i = 0
    while i < len(road):
        if i >= len(road):
            break
        upLeft = (road[i][0] - hSide, road[i][1] + hSide) 
        downRight = (road[i][0] + hSide, road[i][1] - hSide) 
        tmp1 = []

        j = 0
        while j < len(road):
            if j >= len(road):
                break
            if upLeft[0] <= road[j][0] <= downRight[0] and upLeft[1] >= road[j][1] >= downRight[1]: 
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

############      
#   .--.   #
#   _˘˘ _  #sexAprox   
#  /(.)(.)\/‾‾  
#  \_) .(  #
#   (  Y ) #
############

def aproxSex(road1: list, hSide: int):
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

        upLeft = (target[0] - hSide, target[1] + hSide) 
        downRight = (target[0] + hSide, target[1] - hSide) 

        j = 0
        while j < len(road):
            if upLeft[0] <= road[j][0] <= downRight[0] and upLeft[1] >= road[j][1] >= downRight[1]: 
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

        upLeft = (target[0] - hSide, target[1] + hSide) 
        downRight = (target[0] + hSide, target[1] - hSide) 

        j = 0
        while j < len(road):
            if upLeft[0] <= road[j][0] <= downRight[0] and upLeft[1] >= road[j][1] >= downRight[1]: 
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

