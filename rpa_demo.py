import pyautogui
import time
"""
pyautogui.click(100, 100)
time.sleep(2)
pyautogui.rightClick(100,100)

time.sleep(5)
pyautogui.click(1814,808)

pyautogui.doubleClick(100,100)

pyautogui.moveTo(100, 100)
pyautogui.dragTo(200, 200, duration=0.5)

pyautogui.scroll(500)
"""
#keyboard operation
"""
time.sleep(3)

pyautogui.click(1165,883)

#time.sleep(3)
#pyautogui.write("python rpa_demo.py")
time.sleep(5)
#pyautogui.press('enter')

pyautogui.hotkey('ctrl','a')
"""

#image operation
location = pyautogui.locateOnScreen('copliot.png', confidence = 0.8)

print(location)