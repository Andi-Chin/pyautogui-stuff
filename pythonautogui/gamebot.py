import pyautogui
import random
import time
from random import randint as rd
import sys

screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)
currentMouseX, currentMouseY = pyautogui.position()

time.sleep(2)

def move():
	iteration = 0
	while True:
		randNum = rd(0, 140)
		if randNum <= 20:
			randKey = 'w'
		elif randNum <= 40:
			randKey = 's'
		elif randNum <= 60:
			randKey = 'd'
		else:
			randKey = 'a'

		pyautogui.keyDown(randKey)

		time.sleep(rd(0, 20) / 10)

		pyautogui.keyUp(randKey)

		iteration += 1

		if iteration % 30 == 0:
			pyautogui.keyDown('a')

			time.sleep(10)

			pyautogui.keyUp('a')

		# pyautogui.moveTo(rd(100, 2500), rd(100, 1600))
		# time.sleep(1)

		# currentMouseX, currentMouseY = pyautogui.position()

		# if currentMouseX > 2500 or currentMouseY > 1600:
		# 	sys.exit()
		



move()