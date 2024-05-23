import mouse
import pyautogui
import pydirectinput
import ait
import autoit
import time
import keyboard
from bot2 import take_good_screen
time.sleep(5)
monitor = {"top": 200, "left": 610, "width": 700, "height": 700}           
output = "screen.png"
take_good_screen(monitor, output)






'''
time.sleep(5)
keyboard.press('w')
time.sleep(0.1)
keyboard.press('v')
time.sleep(0.1)
keyboard.release('v')

'''
# autoit.mouse_move(mouse.get_position()[0] -237, mouse.get_position()[1], 100)
# autoit.mouse_move(mouse.get_position()[0] + 197, mouse.get_position()[1], 100) # 197 pixels = 90 degree


'''
##GOVNO##########
time.sleep(2)
keyboard.press('tab')
time.sleep(0.5)
keyboard.release('tab')
take_screen(monitor, output)
keyboard.press('tab')
time.sleep(0.3)
keyboard.release('tab')
##GOVNO##########

'''