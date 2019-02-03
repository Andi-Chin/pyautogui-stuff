import pyautogui
import time


screenWidth, screenHeight = pyautogui.size()

for i in range(100):
	time.sleep(0.2)
	print(pyautogui.position())