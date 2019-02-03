import pyautogui
import time
import random
from random import randint as rd
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

def send():
	time.sleep(3)
	pyautogui.moveTo(300, 400)
	pyautogui.click()

	time.sleep(1)

	pyautogui.typewrite('nogeorge2003@gmail.com')
	time.sleep(0.5)
	# pyautogui.press('tab')

	time.sleep(1)

	pyautogui.moveTo(2000, 1500)
	pyautogui.click()
	pyautogui.typewrite(random.choice(['hi', 'hello', 'you suck', 'lol', 'ur mama gey', 'you traush']))
	time.sleep(0.5)
	pyautogui.moveTo(1460, 1730)

	pyautogui.click()

	time.sleep(2)

while True:
	send()





    



'''
pyautogui.moveRel(None, 10)  # move mouse 10 pixels down

pyautogui.typewrite(random.choice(['a', 's', 'w']))
pyautogui.doubleClick()
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.tweens.easeInOutQuad)  # use tweening/easing function to move mouse over 2 seconds.
  # type with quarter-second pause in between each key
pyautogui.press('esc')
pyautogui.keyDown('shift')
pyautogui.typewrite(['left', 'left', 'left', 'left', 'left', 'left'])
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'c')
'''
