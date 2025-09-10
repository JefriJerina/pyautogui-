import pyautogui
import time

# Step 1: Open Start Menu (Windows key)
pyautogui.press('win')
time.sleep(1)

# Step 2: Type 'chrome' and open it
pyautogui.write('chrome', interval=0.1)
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)  # Wait for Chrome to open

# Step 3: Type the search query
pyautogui.write('Kayak Education Services', interval=0.1)
pyautogui.press('enter')
time.sleep(4)  # Wait for search results to load

# Step 4: Click the first link (approximate position)
# You might need to adjust this position depending on your screen resolution
# Use pyautogui.position() or pyautogui.displayMousePosition() to get accurate values
pyautogui.click(x=972, y=958)  # <-- adjust this based on your screen


