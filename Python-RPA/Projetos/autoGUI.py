# import pyautogui
# pyautogui.size()

import pyautogui


# # Get the screen size
# screen_width, screen_height = pyautogui.size()

# # Print the screen size
# print(f"Screen width: {screen_width}")
# print(f"Screen height: {screen_height}")

pyautogui.position()
pyautogui.moveTo(156,100)
pyautogui.click()

#mport sleep
from time import sleep

sleep(5)

pyautogui.dragTo(7,100)
pyautogui.hotkey('crtl', 'c')

arquivo_novo = pyautogui.position()
pyautogui.moveTo(arquivo_novo)
pyautogui.click()

sleep(5)

pyautogui.hotkey('crtl', 'v')

