import mss
import time
import keyboard 
import mouse
import pyautogui
import pydirectinput
import ait
import autoit
import math
from bot import *                                  

time.sleep(5)
cnt = 0
cnt2 = 0 

# path = [(239,508), (219,505), (197,546),(209,584), (288,578),(285,551), (274,493),(267,474), (261,474),(262,477),(254,477)]
# path = [(170, 32), (240, 34), (336, 45), (412, 29), (477, 52), (570, 46), (600, 55), (622, 42), (671, 75), (670, 152), (640, 210), (570, 220), (550, 276), (500, 251), (400, 244), (355, 293), (380, 340), (367, 414), (440, 420), (486, 381), (512, 336), (547, 300), (630, 300), (636, 350), (630, 408), (631, 463), (600, 500), (613, 546), (600, 581), (571, 614), (540, 636), (482, 656), (435, 662), (400, 680), (367, 657), (320, 612), (280, 610), (224, 621), (160, 625), (120, 560), (120, 500), (100, 460), (110, 420), (105, 371), (107, 300), (103, 216), (113, 182), (151, 162), (183, 151), (190, 121), (188, 80), (162, 71), (153, 46)]
path = [(58, 112), (102, 136), (115, 190)]  
lastCoord = []

for i in range(len(path)):
   lastCoord.append(path[i])  
   
monitor = {"top": 242, "left": 1227, "width": 640, "height": 640}  # ДЛЯ РЕЖИМА ИСПЫТАНИЯ        
output = "screen.png"

def take_screen(mon: dict, out: str) -> None:
   with mss.mss() as sct:
      sct_img = sct.grab(mon)
      mss.tools.to_png(sct_img.rgb, sct_img.size, output=out)

def takeGoodScreen(mon: dict, out: str) -> None:
   keyboard.press('tab')
   time.sleep(0.2)
   keyboard.release('tab')
   take_screen(monitor, output)
   keyboard.press('tab')   
   time.sleep(0.2)
   keyboard.release('tab')

x = 90
j = 0
i = 0

takeGoodScreen(monitor, output)

targetCoord = path[i]     
playerCoord, playerVec = getPerson('screen.png')
if playerCoord == - 1 and playerVec == - 1:
   print('word')
 #  continue
   
# ОПРЕДЕЛЕНИЕ БЛИЖАЙШЕЙ ТОЧКИ        
mn = 1000000
indMn = -1
for i in range (len(path)):
  h = ((path [i][0] - playerCoord[0])**2 + (path[i][1] - playerCoord[1])**2)**0.5
  if h < mn:
     mn = h
     indMn = i
     
i = indMn
alpha = getAngle(playerCoord, playerVec, path[i])

autoit.mouse_move(mouse.get_position()[0] + int(alpha * 2.19), mouse.get_position()[1], 100)
time.sleep(1)
keyboard.press('w')
keyboard.press(']')        

while True:                
   print('targetCoord ->', path[i], i)
   print('playerCoord ->', playerCoord, i)
   takeGoodScreen(monitor, output)                       
   targetCoord = path[i]                  
   playerCoord, playerVec = getPerson('screen.png')
   if playerCoord == - 1 and playerVec == - 1:
      continue

   lastCoord[j] = playerCoord
   j += 1
   j %= len(lastCoord)
    
   cnt = 0
   for k in range(len(lastCoord)-1):
      if lastCoord[k] == lastCoord[k + 1]:
         cnt += 1                
         
 # ОБРАБОТКА СТОЛКНОВЕНИЯ      
   if lastCoord[(j-1) % len(lastCoord)] == lastCoord[(j-2) % len(lastCoord)] and lastCoord[(j-1) % len(lastCoord)] == lastCoord[(j-3) % len(lastCoord)]:
      print('stuck')

      keyboard.press('w')
      time.sleep(0.1)
      keyboard.press('v')
      time.sleep(0.5)
      keyboard.release('v')
      keyboard.release('w')
      keyboard.release(']')
      autoit.mouse_move(mouse.get_position()[0] + int(x * 2.19), mouse.get_position()[1], 20)

      x += 90
      x %= 360

      time.sleep(0.5)
      keyboard.press('w')
      keyboard.press(']')        
      time.sleep(3)
      keyboard.release('w')
      keyboard.release(']')

      print('targetCoord2 ->', path[i], i)
      takeGoodScreen(monitor, output)
      playerCoord, playerVec = getPerson('screen.png')

      if playerCoord == - 1 and playerVec == - 1:
         continue

      alpha = getAngle(playerCoord, playerVec, path[i])
      autoit.mouse_move(mouse.get_position()[0] + int(alpha * 2.19), mouse.get_position()[1], 20)
      time.sleep(0.5)
      keyboard.press('w')
      keyboard.press(']')
   
   takeGoodScreen(monitor, output)
   playerCoord, playerVec = getPerson('screen.png')
   if playerCoord == - 1 and playerVec == - 1:
      continue

   upLeft = (targetCoord[0] - HALF_SIDE, targetCoord[1] + HALF_SIDE) 
   downRight = (targetCoord[0] + HALF_SIDE, targetCoord[1] - HALF_SIDE) 

   alpha = getAngle(playerCoord, playerVec, path[i])
   autoit.mouse_move(mouse.get_position()[0] + int(alpha * 2.19), mouse.get_position()[1], 20)
   time.sleep(0.3)
      
   if upLeft[0] <= playerCoord[0] <= downRight[0] and upLeft[1] >= playerCoord[1] >= downRight[1]:   
      i += 1
      i %= len(path)
      print('targetCoord inside ->', path[i], i)
   print(alpha)
   print(output)
