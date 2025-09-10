import pyautogui
import time

x,y = pyautogui.position()

time.sleep(10)

print(f'x: {x}, y: {y}')