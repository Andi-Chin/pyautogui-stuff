import pyautogui
import time
time.sleep(3)
number = 0
while True:
	pyautogui.typewrite(str(number))

	pyautogui.press('enter')

	number += 1

	if number % 30 == 0:
		time.sleep(10)
	if number % 200 == 0:
		time.sleep(30)
	time.sleep(0.3)