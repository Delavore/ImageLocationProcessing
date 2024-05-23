import mss 
import pyxel
from PIL import Image
import math

vec = (0,1)
ncoord = (246, 624)
coord = (173, 570)

BORDER_OFFSET = 5
STEP = 1 # 5 
COLOR_ROAD = (255, 255, 255, 255)
# COLOR_PLAYER = (255, 0, 0, 255)
COLOR_PLAYER = (1, 144, 219, 255)
(14, 114, 167) 

def parse_image(imgPng):
    road = []
    img = Image.open(imgPng)
    pix = img.load()
    road2zdream = pix[238, 473]
    # print(road2zdream)
    width, height = img.size
    x = 0
    y = 0
    
    player = None
    player2 = list() 
    for y in range(BORDER_OFFSET, height-BORDER_OFFSET, STEP):
        for x in range(BORDER_OFFSET, width-BORDER_OFFSET, STEP):
            color = pix[x, y]
            if color == COLOR_ROAD:
                road.append((x, y))
           # elif color == COLOR_PLAYER:
            #    player = (x, y)
            elif (0 <= color[0] <= 20) and (100 <= color[1] <= 150) and (150 <= color[2] <= 230):
                player2.append((x, y))
                player = (x, y)
    print(player2)

    vert = list()

    for i in range(len (player2)):
        cnt = 0
        upLeft = (player2[i][0] - 4, player2[i][1] + 4) 
        downRight = (player2[i][0] + 4, player2[i][1] - 4) 
        for j in range (len (player2)):
            if upLeft[0] <= player2[j][0] <= downRight[0] and upLeft[1] >= player2[j][1] >= downRight[1]: 
                cnt += 1
        vert.append(cnt)

        print(cnt)

    for i in range(len (player2)):
        if vert [i] >= 37: 
            print('Here', player2[i])

    # print(road[0][0])
   # start foo
    return player

    print("We are here", player2)            
    road2zdream = []
    for i in range(0,len(road)-4,400):
        road2zdream.append(((road[i][0] + road[i+1][0] + road[i+2][0] + road[i+3][0]) / 4, 
        (road[i][1] + road[i+1][1] + road[i+2][1] + road[i+3][1]) / 4))
   # print(len(road2zdream))
    print(len(road))
    
    road3zdream = []
    for i in range(0, len(road)-4, 400):
        road3zdream.append((road[i][0], road[i][1]))
    print(len(road3zdream))     
    return x, y, player, road # road
# print(parse_image())



def one_dot(imgPng):
    img = Image.open(imgPng)
    pix = img.load()
    width, height = img.size

    x = 0
    y = 0
    road = (0, 0)

    flag = True
    for y in range(BORDER_OFFSET, height-BORDER_OFFSET, STEP):
        for x in range(BORDER_OFFSET, width-BORDER_OFFSET, STEP):
            color = pix[x, y]
            if color == COLOR_ROAD and flag:
                road = (x, y)
                flag = False

    nvec = (ncoord[0] - coord[0], ncoord[1] - coord[1])
    cosa = (vec[0] * nvec[0] + vec[1] * nvec[1]) / (((nvec[0] - vec[0])**2 + (nvec[1] - vec[1])**2)**0.5)
    alpha = math.acos(cosa)
    alpha = alpha * 180 / math.pi

    print("nvec:", nvec)
    print("cosa:", cosa)
    print("alpha:", alpha)
    print(coord)
    print(ncoord)
    print((vec[0] * nvec[0] + vec[1] * nvec[1]))

    # cosa = (coord[0] * ncoord[0] + coord[1] * ncoord[1]) / ((ncoord[0] - coord[0])**2 + (ncoord[1] - coord[1])**2)
    # alpha = math.acos(cosa)

    return road
# print(one_dot('mapVector2.png'))
print(parse_image('screen.png'))






'''
        new vector = (x - x0; y - y0)

        a * b = |a| * |b| * cosa => cosa = (a * b) / (|a| * |b|) => (x * x0 + y * y0) / ((x - x0)**2 + (y - y0)**2)

        
        


'''











'''
class Game:
    def __init__(self):
        width, height, self.player, self.road = parse_image()
        pyxel.init(width, height)
        print(width, height, self.player, len(self.road))
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

        
    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)
        for c in self.road:
            pyxel.circ(c[0], c[1], 10, pyxel.COLOR_WHITE) #10
        pyxel.circ(self.player[0], self.player[1], 30, pyxel.COLOR_RED)


Game()
'''
