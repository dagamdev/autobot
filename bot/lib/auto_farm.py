import pyautogui
import time
from typing import Tuple

auto_chainersfarm = False
auto_chainersfarm_thread = None

def harvest_and_sow (firstPosition: Tuple[int, int], secondPosition: Tuple[int, int]):
  steps = [
    (firstPosition, 1, True),
    (secondPosition, 1.25),
    (firstPosition, 3),
    (secondPosition, 1.25),
    (secondPosition, 1.25),
  ]

  for step in steps:
    if not auto_chainersfarm:
      break 
    time.sleep(step[1])
    pyautogui.click(step[0], duration=0.4, clicks=2 if True in step else 1, interval=0.2)

  

def auto_chainersfarm_loop (): 
  while auto_chainersfarm:
    harvest_and_sow((928, 705), (934, 631))
    # harvest_and_sow((1020, 782), (1020, 686))
    time.sleep(122)