import pyautogui
import time
from me import variables

def click_in_meet ():
  while variables.recording:
    print('click_in_meet')
    pyautogui.click(1800, 550, duration=0.5)
    time.sleep(60)