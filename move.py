import pyautogui
import time

pyautogui.FAILSAFE=False
time.sleep(8)
for i in range(1,1000):
    for i in range(1,50):
        pyautogui.moveRel(0, 20, duration=1)
    for x in range(1,50):
        pyautogui.moveRel(20, 0, duration=1)


