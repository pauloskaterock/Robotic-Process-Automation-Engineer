# import pyautogui
# from time import sleep

# # Basic screen information
# screen_width, screen_height = pyautogui.size() # Get the screen size
# print(f"Screen width: {screen_width}, Screen height: {screen_height}")

# # Mouse movements
# pyautogui.moveTo(100, 100) # Move the mouse to (100, 100)
# pyautogui.moveTo(200, 200, duration=1.5) # Move the mouse to (200, 200) over 1.5 seconds
# pyautogui.moveRel(50, 50) # Move the mouse 50 pixels right and 50 pixels down
# pyautogui.moveRel(-50, -50, duration=1) # Move the mouse back to the original position over 1 second

# # Mouse clicks
# pyautogui.click() # Click the mouse
# pyautogui.click(100, 100) # Click the mouse at (100, 100)
# pyautogui.doubleClick() # Double click the mouse
# pyautogui.rightClick() # Right click the mouse
# pyautogui.middleClick() # Middle click the mouse

# # Mouse drag
# pyautogui.dragTo(300, 300, duration=1.5) # Drag the mouse to (300, 300) over 1.5 seconds
# pyautogui.dragRel(100, 100, duration=2) # Drag the mouse 100 pixels right and 100 pixels down over 2 seconds

# # Mouse scroll
# pyautogui.scroll(500) # Scroll up 500 units
# pyautogui.scroll(-500) # Scroll down 500 units

# # Mouse position
# current_mouse_x, current_mouse_y = pyautogui.position() # Get the current mouse position
# print(f"Current mouse position: ({current_mouse_x}, {current_mouse_y})")

# # Screen information
# screen = pyautogui.screenshot() # Take a screenshot
# screen.save("screenshot.png") # Save the screenshot

# # Pixel color
# pixel_color = pyautogui.pixel(100, 100) # Get the color of the pixel at (100, 100)
# print(f"Pixel color at (100, 100): {pixel_color}")
# is_color = pyautogui.pixelMatchesColor(100, 100, (255, 255, 255)) # Check if the pixel at (100, 100) is white
# print(f"Is the pixel at (100, 100) white? {is_color}")

# # Alert
# pyautogui.alert('This is an alert box.') # Show an alert box
# pyautogui.confirm('Shall we proceed?') # Show a confirmation box
# pyautogui.prompt('What is your name?') # Show a prompt box
# pyautogui.password('Enter password:') # Show a password box

# # Typing
# pyautogui.typewrite('Hello world!') # Type out 'Hello world!'
# pyautogui.typewrite('Hello world!', interval=0.25) # Type out 'Hello world!' with quarter-second pause in between each key
# pyautogui.press('enter') # Press the Enter key
# pyautogui.press(['left', 'left', 'left', 'left']) # Press the left arrow key four times
# pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination

# # Special keys
# pyautogui.press('f1') # Press the F1 key
# pyautogui.press('volumemute') # Press the volume mute key

# # Key down and up
# pyautogui.keyDown('shift') # Press the Shift key down
# pyautogui.press('left') # Press the left arrow key
# pyautogui.keyUp('shift') # Release the Shift key

# # Locate on screen
# button_location = pyautogui.locateOnScreen('button.png') # Locate a button on the screen
# print(f"Button location: {button_location}")
# button_center = pyautogui.locateCenterOnScreen('button.png') # Locate the center of the button on the screen
# print(f"Button center: {button_center}")
# all_buttons = pyautogui.locateAllOnScreen('button.png') # Locate all instances of the button on the screen
# print(f"All button locations: {list(all_buttons)}")

# # Locate on screen with confidence
# try:
#     button_location = pyautogui.locateOnScreen('button.png', confidence=0.9) # Locate a button on the screen with 90% confidence
#     print(f"Button location: {button_location}")
# except pyautogui.ImageNotFoundException:
#     print("Button not found")

# # Relative locating
# left, top, width, height = pyautogui.locateOnScreen('button.png')
# pyautogui.click(left + width/2, top + height/2) # Click the center of the located button

# # Window operations
# active_window = pyautogui.getActiveWindow() # Get the currently active window
# print(f"Active window: {active_window}")
# all_windows = pyautogui.getWindows() # Get a list of all windows
# print(f"All windows: {all_windows}")

# # Screenshot part of screen
# part_screen = pyautogui.screenshot(region=(0, 0, 300, 400)) # Take a screenshot of a specific region
# part_screen.save("part_screenshot.png") # Save the partial screenshot

# # Locate by color
# matches = list(pyautogui.locateAll('button.png', confidence=0.8)) # Locate all matches of 'button.png' with 80% confidence
# print(f"Matches found: {matches}")

# # Mouse button state
# is_pressed = pyautogui.mouseDown() # Check if a mouse button is currently pressed
# print(f"Is mouse button pressed? {is_pressed}")

# # Dragging with easing functions
# pyautogui.dragTo(500, 500, duration=1, tween=pyautogui.easeInOutQuad) # Drag to (500, 500) using ease-in-out quad

# # Mouse clicks with button argument
# pyautogui.click(button='right') # Right click
# pyautogui.click(button='middle') # Middle click

# # Dragging with relative movement
# pyautogui.dragRel(100, 0, duration=1, button='left') # Drag to the right with the left button held down

# # Typing shortcuts
# pyautogui.write('Hello world!') # Write 'Hello world!'
# pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y']) # Write 'a', 'b', move left twice, then 'X', 'Y'

# # Hotkey combinations
# pyautogui.hotkey('ctrl', 'shift', 'esc') # Press Ctrl-Shift-Esc

# # Pause and fail-safes
# pyautogui.PAUSE = 2.5 # Add a pause of 2.5 seconds between each call
# pyautogui.FAILSAFE = True # Enable fail-safe which raises an exception if the mouse is moved to a corner of the screen

# # Mouse information
# mouse_info = pyautogui.mouseInfo() # Get the mouse info (position and RGB values)
# print(f"Mouse info: {mouse_info}")

# # Screenshot and saving
# pyautogui.screenshot('my_screenshot.png') # Take a screenshot and save it as 'my_screenshot.png'

# # Get RGB value of pixel
# rgb_value = pyautogui.pixel(200, 300) # Get the RGB value of the pixel at (200, 300)
# print(f"RGB value at (200, 300): {rgb_value}")

# # Check if pixel matches
# pixel_match = pyautogui.pixelMatchesColor(200, 300, (255, 0, 0)) # Check if the pixel at (200, 300) matches the color (255, 0, 0)
# print(f"Pixel matches color? {pixel_match}")

# # Center location
# center_location = pyautogui.center((0, 0, 100, 200)) # Get the center of a region
# print(f"Center location: {center_location}")

# # Mouse up
# pyautogui.mouseUp() # Release the mouse button

# # Mouse down with button argument
# pyautogui.mouseDown(button='right') # Press down the right mouse button

# # Sleep
# sleep(2) # Pause for 2 seconds

# # Working with images
# icon_location = pyautogui.locateOnScreen('icon.png') # Locate an icon on the screen
# pyautogui.click(icon_location) # Click the icon

# # Region-based locating
# region_icon = pyautogui.locateOnScreen('icon.png', region=(0, 0, 300, 400)) # Locate an icon within a specific region
# print(f"Region icon location: {region_icon}")

# # Display information
# print(pyautogui.displayMousePosition()) # Display the mouse position

# # Fail-safe triggering
# try:
#     pyautogui.moveTo(0, 0) # Move to the top-left corner to trigger the fail-safe
# except pyautogui.FailSafeException:
#     print("Fail-safe triggered")

# # Fail-safe enabled/disabled
# pyautogui.FAILSAFE = False # Disable the fail-safe
# pyautogui.FAILSAFE = True # Enable the fail-safe again

# # Click and double click
# pyautogui.click(x=100, y=Here's a revised version of the code that includes 100 commonly used `pyautogui` commands, formatted for use in Visual Studio Code:

# ```python
# import pyautogui
# from time import sleep

# # Basic screen information
# screen_width, screen_height = pyautogui.size() # Get the screen size
# print(f"Screen width: {screen_width}, Screen height: {screen_height}")

# # Mouse movements
# pyautogui.moveTo(100, 100) # Move the mouse to (100, 100)
# pyautogui.moveTo(200, 200, duration=1.5) # Move the mouse to (200, 200) over 1.5 seconds
# pyautogui.moveRel(50, 50) # Move the mouse 50 pixels right and 50 pixels down
# pyautogui.moveRel(-50, -50, duration=1) # Move the mouse back to the original position over 1 second

# # Mouse clicks
# pyautogui.click() # Click the mouse
# pyautogui.click(100, 100) # Click the mouse at (100, 100)
# pyautogui.doubleClick() # Double click the mouse
# pyautogui.rightClick() # Right click the mouse
# pyautogui.middleClick() # Middle click the mouse

# # Mouse drag
# pyautogui.dragTo(300, 300, duration=1.5) # Drag the mouse to (300, 300) over 1.5 seconds
# pyautogui.dragRel(100, 100, duration=2) # Drag the mouse 100 pixels right and 100 pixels down over 2 seconds

# # Mouse scroll
# pyautogui.scroll(500) # Scroll up 500 units
# pyautogui.scroll(-500) # Scroll down 500 units

# # Mouse position
# current_mouse_x, current_mouse_y = pyautogui.position() # Get the current mouse position
# print(f"Current mouse position: ({current_mouse_x}, {current_mouse_y})")

# # Screen information
# screen = pyautogui.screenshot() # Take a screenshot
# screen.save("screenshot.png") # Save the screenshot

# # Pixel color
# pixel_color = pyautogui.pixel(100, 100) # Get the color of the pixel at (100, 100)
# print(f"Pixel color at (100, 100): {pixel_color}")
# is_color = pyautogui.pixelMatchesColor(100, 100, (255, 255, 255)) # Check if the pixel at (100, 100) is white
# print(f"Is the pixel at (100, 100) white? {is_color}")

# # Alert
# pyautogui.alert('This is an alert box.') # Show an alert box
# pyautogui.confirm('Shall we proceed?') # Show a confirmation box
# pyautogui.prompt('What is your name?') # Show a prompt box
# pyautogui.password('Enter password:') # Show a password box

# # Typing
# pyautogui.typewrite('Hello world!') # Type out 'Hello world!'
# pyautogui.typewrite('Hello world!', interval=0.25) # Type out 'Hello world!' with quarter-second pause in between each key
# pyautogui.press('enter') # Press the Enter key
# pyautogui.press(['left', 'left', 'left', 'left']) # Press the left arrow key four times
# pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination

# # Special keys
# pyautogui.press('f1') # Press the F1 key
# pyautogui.press('volumemute') # Press the volume mute key

# # Key down and up
# pyautogui.keyDown('shift') # Press the Shift key down
# pyautogui.press('left') # Press the left arrow key
# pyautogui.keyUp('shift') # Release the Shift key

# # Locate on screen
# button_location = pyautogui.locateOnScreen('button.png') # Locate a button on the screen
# print(f"Button location: {button_location}")
# button_center = pyautogui.locateCenterOnScreen('button.png') # Locate the center of the button on the screen
# print(f"Button center: {button_center}")
# all_buttons = pyautogui.locateAllOnScreen('button.png') # Locate all instances of the button on the screen
# print(f"All button locations: {list(all_buttons)}")

# # Locate on screen with confidence
# try:
#     button_location = pyautogui.locateOnScreen('button.png', confidence=0.9) # Locate a button on the screen with 90% confidence
#     print(f"Button location: {button_location}")
# except pyautogui.ImageNotFoundException:
#     print("Button not found")

# # Relative locating
# left, top, width, height = pyautogui.locateOnScreen('button.png')
# pyautogui.click(left + width/2, top + height/2) # Click the center of the located button

# # Window operations
# active_window = pyautogui.getActiveWindow() # Get the currently active window
# print(f"Active window: {active_window}")
# all_windows = pyautogui.getWindows() # Get a list of all windows
# print(f"All windows: {all_windows}")

# # Screenshot part of screen
# part_screen = pyautogui.screenshot(region=(0, 0, 300, 400)) # Take a screenshot of a specific region
# part_screen.save("part_screenshot.png") # Save the partial screenshot

# # Locate by color
# matches = list(pyautogui.locateAll('button.png', confidence=0.8)) # Locate all matches of 'button.png' with 80% confidence
# print(f"Matches found: {matches}")

# # Mouse button state
# is_pressed = pyautogui.mouseDown() # Check if a mouse button is currently pressed
# print(f"Is mouse button pressed? {is_pressed}")

# # Dragging with easing functions
# pyautogui.dragTo(500, 500, duration=1, tween=pyautogui.easeInOutQuad) # Drag to (500, 500) using ease-in-out quad

# # Mouse clicks with button argument
# pyautogui.click(button='right') # Right click
# pyautogui.click(button='middle') # Middle click

# # Dragging with relative movement
# pyautogui.dragRel(100, 0, duration=1, button='left') # Drag to the right with the left button held down

# # Typing shortcuts
# pyautogui.write('Hello world!') # Write 'Hello world!'
# pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y']) # Write 'a', 'b', move left twice, then 'X', 'Y'

# # Hotkey combinations
# pyautogui.hotkey('ctrl', 'shift', 'esc') # Press Ctrl-Shift-Esc

# # Pause and fail-safes
# pyautogui.PAUSE = 2.5 # Add a pause of 2.5 seconds between each call
# pyautogui.FAILSAFE = True # Enable fail-safe which raises an exception if the mouse is moved to a corner of the screen

# # Mouse information
# mouse_info = pyautogui.mouseInfo() # Get the mouse info (position and RGB values)
# print(f"Mouse info: {mouse_info}")

# # Screenshot and saving
# pyautogui.screenshot('my_screenshot.png') # Take a screenshot and save it as 'my_screenshot.png'

# # Get RGB value of pixel
# rgb_value = pyautogui.pixel(200, 300) # Get the RGB value of the pixel at (200, 300)
# print(f"RGB value at (200, 300): {rgb_value}")

# # Check if pixel matches
# pixel_match = pyautogui.pixelMatchesColor(200, 300, (255, 0, 0)) # Check if the pixel at (200, 300) matches the color (255, 0, 0)
# print(f"Pixel matches color? {pixel_match}")

# # Center location
# center_location = pyautogui.center((0, 0, 100, 200)) # Get the center of a region
# print(f"Center location: {center_location}")

# # Mouse up
# pyautogui.mouseUp() # Release the mouse button

# # Mouse down with button argument
# pyautogui.mouseDown(button='right') # Press down the right mouse button

# # Sleep
# sleep(2) # Pause for 2 seconds

# # Working with images
# icon_location = pyautogui.locateOnScreen('icon.png') # Locate an icon on the screen
# pyautogui.click(icon_location) # Click the icon

# # Region-based locating
# region_icon = pyautogui.locateOnScreen('icon.png', region=(0, 0, 300, 400)) # Locate an icon within a specific region
# print(f"Region icon location: {region_icon}")

# # Display information
# print(pyautogui.displayMousePosition()) # Display the mouse position

# # Fail-safe triggering
# try:
#     pyautogui.moveTo(0, 0) # Move to the top-left corner to trigger the fail-safe
# except pyautogui.FailSafeException:
#     print("Fail-safe triggered")

# # Fail-safe enabled/disabled
# pyautogui.FAILSAFE = False # Disable the fail-safe
# pyautogui.FAILSAFE = True # Enable the fail-safe again

# # Click and double click
# pyautogui.click(x=100Here's a list of 100 commonly used commands in `pyautogui`, formatted for use in Visual Studio Code:

# ```python
# import pyautogui
# from time import sleep

# # Basic screen information
# screen_width, screen_height = pyautogui.size() # Get the screen size
# print(f"Screen width: {screen_width}, Screen height: {screen_height}")

# # Mouse movements
# pyautogui.moveTo(100, 100) # Move the mouse to (100, 100)
# pyautogui.moveTo(200, 200, duration=1.5) # Move the mouse to (200, 200) over 1.5 seconds
# pyautogui.moveRel(50, 50) # Move the mouse 50 pixels right and 50 pixels down
# pyautogui.moveRel(-50, -50, duration=1) # Move the mouse back to the original position over 1 second

# # Mouse clicks
# pyautogui.click() # Click the mouse
# pyautogui.click(100, 100) # Click the mouse at (100, 100)
# pyautogui.doubleClick() # Double click the mouse
# pyautogui.rightClick() # Right click the mouse
# pyautogui.middleClick() # Middle click the mouse

# # Mouse drag
# pyautogui.dragTo(300, 300, duration=1.5) # Drag the mouse to (300, 300) over 1.5 seconds
# pyautogui.dragRel(100, 100, duration=2) # Drag the mouse 100 pixels right and 100 pixels down over 2 seconds

# # Mouse scroll
# pyautogui.scroll(500) # Scroll up 500 units
# pyautogui.scroll(-500) # Scroll down 500 units

# # Mouse position
# current_mouse_x, current_mouse_y = pyautogui.position() # Get the current mouse position
# print(f"Current mouse position: ({current_mouse_x}, {current_mouse_y})")

# # Screen information
# screen = pyautogui.screenshot() # Take a screenshot
# screen.save("screenshot.png") # Save the screenshot

# # Pixel color
# pixel_color = pyautogui.pixel(100, 100) # Get the color of the pixel at (100, 100)
# print(f"Pixel color at (100, 100): {pixel_color}")
# is_color = pyautogui.pixelMatchesColor(100, 100, (255, 255, 255)) # Check if the pixel at (100, 100) is white
# print(f"Is the pixel at (100, 100) white? {is_color}")

# # Alert
# pyautogui.alert('This is an alert box.') # Show an alert box
# pyautogui.confirm('Shall we proceed?') # Show a confirmation box
# pyautogui.prompt('What is your name?') # Show a prompt box
# pyautogui.password('Enter password:') # Show a password box

# # Typing
# pyautogui.typewrite('Hello world!') # Type out 'Hello world!'
# pyautogui.typewrite('Hello world!', interval=0.25) # Type out 'Hello world!' with quarter-second pause in between each key
# pyautogui.press('enter') # Press the Enter key
# pyautogui.press(['left', 'left', 'left', 'left']) # Press the left arrow key four times
# pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination

# # Special keys
# pyautogui.press('f1') # Press the F1 key
# pyautogui.press('volumemute') # Press the volume mute key

# # Key down and up
# pyautogui.keyDown('shift') # Press the Shift key down
# pyautogui.press('left') # Press the left arrow key
# pyautogui.keyUp('shift') # Release the Shift key

# # Locate on screen
# button_location = pyautogui.locateOnScreen('button.png') # Locate a button on the screen
# print(f"Button location: {button_location}")
# button_center = pyautogui.locateCenterOnScreen('button.png') # Locate the center of the button on the screen
# print(f"Button center: {button_center}")
# all_buttons = pyautogui.locateAllOnScreen('button.png') # Locate all instances of the button on the screen
# print(f"All button locations: {list(all_buttons)}")

# # Locate on screen with confidence
# try:
#     button_location = pyautogui.locateOnScreen('button.png', confidence=0.9) # Locate a button on the screen with 90% confidence
#     print(f"Button location: {button_location}")
# except pyautogui.ImageNotFoundException:
#     print("Button not found")

# # Relative locating
# left, top, width, height = pyautogui.locateOnScreen('button.png')
# pyautogui.click(left + width/2, top + height/2) # Click the center of the located button

# # Window operations
# active_window = pyautogui.getActiveWindow() # Get the currently active window
# print(f"Active window: {active_window}")
# all_windows = pyautogui.getWindows() # Get a list of all windows
# print(f"All windows: {all_windows}")

# # Screenshot part of screen
# part_screen = pyautogui.screenshot(region=(0, 0, 300, 400)) # Take a screenshot of a specific region
# part_screen.save("part_screenshot.png") # Save the partial screenshot

# # Locate by color
# matches = list(pyautogui.locateAll('button.png', confidence=0.8)) # Locate all matches of 'button.png' with 80% confidence
# print(f"Matches found: {matches}")

# # Mouse button state
# is_pressed = pyautogui.mouseDown() # Check if a mouse button is currently pressed
# print(f"Is mouse button pressed? {is_pressed}")

# # Dragging with easing functions
# pyautogui.dragTo(500, 500, duration=1, tween=pyautogui.easeInOutQuad) # Drag to (500, 500) using ease-in-out quad

# # Mouse clicks with button argument
# pyautogui.click(button='right') # Right click
# pyautogui.click(button='middle') # Middle click

# # Dragging with relative movement
# pyautogui.dragRel(100, 0, duration=1, button='left') # Drag to the right with the left button held down

# # Typing shortcuts
# pyautogui.write('Hello world!') # Write 'Hello world!'
# pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y']) # Write 'a', 'b', move left twice, then 'X', 'Y'

# # Hotkey combinations
# pyautogui.hotkey('ctrl', 'shift', 'esc') # Press Ctrl-Shift-Esc

# # Pause and fail-safes
# pyautogui.PAUSE = 2.5 # Add a pause of 2.5 seconds between each call
# pyautogui.FAILSAFE = True # Enable fail-safe which raises an exception if the mouse is moved to a corner of the screen

# # Mouse information
# mouse_info = pyautogui.mouseInfo() # Get the mouse info (position and RGB values)
# print(f"Mouse info: {mouse_info}")

# # Screenshot and saving
# pyautogui.screenshot('my_screenshot.png') # Take a screenshot and save it as 'my_screenshot.png'

# # Get RGB value of pixel
# rgb_value = pyautogui.pixel(200, 300) # Get the RGB value of the pixel at (200, 300)
# print(f"RGB value at (200, 300): {rgb_value}")

# # Check if pixel matches
# pixel_match = pyautogui.pixelMatchesColor(200, 300, (255, 0, 0)) # Check if the pixel at (200, 300) matches the color (255, 0, 0)
# print(f"Pixel matches color? {pixel_match}")

# # Center location
# center_location = pyautogui.center((0, 0, 100, 200)) # Get the center of a region
# print(f"Center location: {center_location}")

# # Mouse up
# pyautogui.mouseUp() # Release the mouse button

# # Mouse down with button argument
# pyautogui.mouseDown(button='right') # Press down the right mouse button

# # Sleep
# sleep(2) # Pause for 2 seconds

# # Working with images
# icon_location = pyautogui.locateOnScreen('icon.png') # Locate an icon on the screen
# pyautogui.click(icon_location) # Click the icon

# # Region-based locating
# region_icon = pyautogui.locateOnScreen('icon.png', region=(0, 0, 300, 400)) # Locate an icon within a specific region
# print(f"Region icon location: {region_icon}")

# # Display information
# print(pyautogui.displayMousePosition()) # Display the mouse position

# # Fail-safe triggering
# try:
#     pyautogui.moveTo(0, 0) # Move to the top-left corner to trigger the fail-safe
# except pyautogui.FailSafeException:
#     print("Fail-safe triggered")

# # Fail-safe enabled/disabled
# pyautogui.FAILSAFE = False # Disable the fail-safe
# pyautogui.FAILSAFE = True # Enable the fail-safe again

# # Click and double click
# pyautogui.click(x=100, y=200)Aqui está uma lista de 100 comandos do `pyautogui`, organizada e formatada para ser utilizada no Visual Studio Code:

# ```python
# import pyautogui
# from time import sleep

# # Informações básicas da tela
# screen_width, screen_height = pyautogui.size()  # Obter o tamanho da tela
# print(f"Largura da tela: {screen_width}, Altura da tela: {screen_height}")

# # Movimentos do mouse
# pyautogui.moveTo(100, 100)  # Mover o mouse para (100, 100)
# pyautogui.moveTo(200, 200, duration=1.5)  # Mover o mouse para (200, 200) em 1.5 segundos
# pyautogui.moveRel(50, 50)  # Mover o mouse 50 pixels para a direita e 50 pixels para baixo
# pyautogui.moveRel(-50, -50, duration=1)  # Mover o mouse de volta para a posição original em 1 segundo

# # Cliques do mouse
# pyautogui.click()  # Clicar com o mouse
# pyautogui.click(100, 100)  # Clicar com o mouse em (100, 100)
# pyautogui.doubleClick()  # Clicar duas vezes com o mouse
# pyautogui.rightClick()  # Clicar com o botão direito do mouse
# pyautogui.middleClick()  # Clicar com o botão do meio do mouse

# # Arrastar o mouse
# pyautogui.dragTo(300, 300, duration=1.5)  # Arrastar o mouse para (300, 300) em 1.5 segundos
# pyautogui.dragRel(100, 100, duration=2)  # Arrastar o mouse 100 pixels para a direita e 100 pixels para baixo em 2 segundos

# # Rolagem do mouse
# pyautogui.scroll(500)  # Rolar para cima 500 unidades
# pyautogui.scroll(-500)  # Rolar para baixo 500 unidades

# # Posição do mouse
# current_mouse_x, current_mouse_y = pyautogui.position()  # Obter a posição atual do mouse
# print(f"Posição atual do mouse: ({current_mouse_x}, {current_mouse_y})")

# # Captura de tela
# screen = pyautogui.screenshot()  # Tirar uma captura de tela
# screen.save("screenshot.png")  # Salvar a captura de tela

# # Cor do pixel
# pixel_color = pyautogui.pixel(100, 100)  # Obter a cor do pixel em (100, 100)
# print(f"Cor do pixel em (100, 100): {pixel_color}")
# is_color = pyautogui.pixelMatchesColor(100, 100, (255, 255, 255))  # Verificar se o pixel em (100, 100) é branco
# print(f"O pixel em (100, 100) é branco? {is_color}")

# # Caixas de diálogo
# pyautogui.alert('Esta é uma caixa de alerta.')  # Mostrar uma caixa de alerta
# pyautogui.confirm('Devemos continuar?')  # Mostrar uma caixa de confirmação
# pyautogui.prompt('Qual é o seu nome?')  # Mostrar uma caixa de prompt
# pyautogui.password('Digite a senha:')  # Mostrar uma caixa de senha

# # Digitação
# pyautogui.typewrite('Olá, mundo!')  # Digitar 'Olá, mundo!'
# pyautogui.typewrite('Olá, mundo!', interval=0.25)  # Digitar 'Olá, mundo!' com intervalo de 0.25 segundos entre cada tecla
# pyautogui.press('enter')  # Pressionar a tecla Enter
# pyautogui.press(['left', 'left', 'left', 'left'])  # Pressionar a tecla de seta para a esquerda quatro vezes
# pyautogui.hotkey('ctrl', 'c')  # Pressionar a combinação de teclas Ctrl-C

# # Teclas especiais
# pyautogui.press('f1')  # Pressionar a tecla F1
# pyautogui.press('volumemute')  # Pressionar a tecla de mute de volume

# # Manter tecla pressionada e soltar
# pyautogui.keyDown('shift')  # Manter a tecla Shift pressionada
# pyautogui.press('left')  # Pressionar a tecla de seta para a esquerda
# pyautogui.keyUp('shift')  # Soltar a tecla Shift

# # Localizar na tela
# button_location = pyautogui.locateOnScreen('button.png')  # Localizar um botão na tela
# print(f"Localização do botão: {button_location}")
# button_center = pyautogui.locateCenterOnScreen('button.png')  # Localizar o centro do botão na tela
# print(f"Centro do botão: {button_center}")
# all_buttons = pyautogui.locateAllOnScreen('button.png')  # Localizar todas as instâncias do botão na tela
# print(f"Todas as localizações do botão: {list(all_buttons)}")

# # Localizar na tela com confiança
# try:
#     button_location = pyautogui.locateOnScreen('button.png', confidence=0.9)  # Localizar um botão na tela com 90% de confiança
#     print(f"Localização do botão: {button_location}")
# except pyautogui.ImageNotFoundException:
#     print("Botão não encontrado")

# # Localização relativa
# left, top, width, height = pyautogui.locateOnScreen('button.png')
# pyautogui.click(left + width/2, top + height/2)  # Clicar no centro do botão localizado

# # Operações de janela
# active_window = pyautogui.getActiveWindow()  # Obter a janela ativa atualmente
# print(f"Janela ativa: {active_window}")
# all_windows = pyautogui.getWindows()  # Obter uma lista de todas as janelas
# print(f"Todas as janelas: {all_windows}")

# # Captura de tela de parte da tela
# part_screen = pyautogui.screenshot(region=(0, 0, 300, 400))  # Tirar uma captura de tela de uma região específica
# part_screen.save("part_screenshot.png")  # Salvar a captura de tela parcial

# # Localizar por cor
# matches = list(pyautogui.locateAll('button.png', confidence=0.8))  # Localizar todas as correspondências de 'button.png' com 80% de confiança
# print(f"Correspondências encontradas: {matches}")

# # Estado do botão do mouse
# is_pressed = pyautogui.mouseDown()  # Verificar se um botão do mouse está pressionado
# print(f"Botão do mouse pressionado? {is_pressed}")

# # Arrastar com funções de suavização
# pyautogui.dragTo(500, 500, duration=1, tween=pyautogui.easeInOutQuad)  # Arrastar para (500, 500) usando suavização de entrada e saída

# # Cliques do mouse com argumento de botão
# pyautogui.click(button='right')  # Clicar com o botão direito
# pyautogui.click(button='middle')  # Clicar com o botão do meio

# # Arrastar com movimento relativo
# pyautogui.dragRel(100, 0, duration=1, button='left')  # Arrastar para a direita com o botão esquerdo pressionado

# # Atalhos de digitação
# pyautogui.write('Olá, mundo!')  # Escrever 'Olá, mundo!'
# pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y'])  # Escrever 'a', 'b', mover para a esquerda duas vezes, depois 'X', 'Y'

# # Combinações de teclas
# pyautogui.hotkey('ctrl', 'shift', 'esc')  # Pressionar Ctrl-Shift-Esc

# # Pausa e fail-safes
# pyautogui.PAUSE = 2.5  # Adicionar uma pausa de 2.5 segundos entre cada chamada
# pyautogui.FAILSAFE = True  # Habilitar o fail-safe que levanta uma exceção se o mouse for movido para um canto da tela

# # Informação do mouse
# mouse_info = pyautogui.mouseInfo()  # Obter a informação do mouse (posição e valores RGB)
# print(f"Informação do mouse: {mouse_info}")

# # Captura de tela e salvamento
# pyautogui.screenshot('my_screenshot.png')  # Tirar uma captura de tela e salvar como 'my_screenshot.png'

# # Obter valor RGB do pixel
# rgb_value = pyautogui.pixel(200, 300)  # Obter o valor RGB do pixel em (200, 300)
# print(f"Valor RGB em (200, 300): {rgb_value}")

# # Verificar se o pixel corresponde
# pixel_match = pyautogui.pixelMatchesColor(200, 300, (255, 0, 0))  # Verificar se o pixel em (200, 300) corresponde à cor (255, 0, 0)
# print(f"O pixel corresponde à cor? {pixel_match}")

# # Localização central
# center_location = pyautogui.center((0, 0, 100, 200))  # Obter o centro de uma região
# print(f"Localização central: {center_location}")

# # Soltar oSegue a lista de 100 comandos do `pyautogui` organizada para uso no Visual Studio Code:

# ```python
# import pyautogui
# from time import sleep

# # Informações básicas da tela
# screen_width, screen_height = pyautogui.size()  # Obter o tamanho da tela
# print(f"Largura da tela: {screen_width}, Altura da tela: {screen_height}")

# # Movimentos do mouse
# pyautogui.moveTo(100, 100)  # Mover o mouse para (100, 100)
# pyautogui.moveTo(200, 200, duration=1.5)  # Mover o mouse para (200, 200) em 1.5 segundos
# pyautogui.moveRel(50, 50)  # Mover o mouse 50 pixels para a direita e 50 pixels para baixo
# pyautogui.moveRel(-50, -50, duration=1)  # Mover o mouse de volta para a posição original em 1 segundo

# # Cliques do mouse
# pyautogui.click()  # Clicar com o mouse
# pyautogui.click(100, 100)  # Clicar com o mouse em (100, 100)
# pyautogui.doubleClick()  # Clicar duas vezes com o mouse
# pyautogui.rightClick()  # Clicar com o botão direito do mouse
# pyautogui.middleClick()  # Clicar com o botão do meio do mouse

# # Arrastar o mouse
# pyautogui.dragTo(300, 300, duration=1.5)  # Arrastar o mouse para (300, 300) em 1.5 segundos
# pyautogui.dragRel(100, 100, duration=2)  # Arrastar o mouse 100 pixels para a direita e 100 pixels para baixo em 2 segundos

# # Rolagem do mouse
# pyautogui.scroll(500)  # Rolar para cima 500 unidades
# pyautogui.scroll(-500)  # Rolar para baixo 500 unidades

# # Posição do mouse
# current_mouse_x, current_mouse_y = pyautogui.position()  # Obter a posição atual do mouse
# print(f"Posição atual do mouse: ({current_mouse_x}, {current_mouse_y})")

# # Captura de tela
# screen = pyautogui.screenshot()  # Tirar uma captura de tela
# screen.save("screenshot.png")  # Salvar a captura de tela

# # Cor do pixel
# pixel_color = pyautogui.pixel(100, 100)  # Obter a cor do pixel em (100, 100)
# print(f"Cor do pixel em (100, 100): {pixel_color}")
# is_color = pyautogui.pixelMatchesColor(100, 100, (255, 255, 255))  # Verificar se o pixel em (100, 100) é branco
# print(f"O pixel em (100, 100) é branco? {is_color}")

# # Caixas de diálogo
# pyautogui.alert('Esta é uma caixa de alerta.')  # Mostrar uma caixa de alerta
# pyautogui.confirm('Devemos continuar?')  # Mostrar uma caixa de confirmação
# pyautogui.prompt('Qual é o seu nome?')  # Mostrar uma caixa de prompt
# pyautogui.password('Digite a senha:')  # Mostrar uma caixa de senha

# # Digitação
# pyautogui.typewrite('Olá, mundo!')  # Digitar 'Olá, mundo!'
# pyautogui.typewrite('Olá, mundo!', interval=0.25)  # Digitar 'Olá, mundo!' com intervalo de 0.25 segundos entre cada tecla
# pyautogui.press('enter')  # Pressionar a tecla Enter
# pyautogui.press(['left', 'left', 'left', 'left'])  # Pressionar a tecla de seta para a esquerda quatro vezes
# pyautogui.hotkey('ctrl', 'c')  # Pressionar a combinação de teclas Ctrl-C

# # Teclas especiais
# pyautogui.press('f1')  # Pressionar a tecla F1
# pyautogui.press('volumemute')  # Pressionar a tecla de mute de volume

# # Manter tecla pressionada e soltar
# pyautogui.keyDown('shift')  # Manter a tecla Shift pressionada
# pyautogui.press('left')  # Pressionar a tecla de seta para a esquerda
# pyautogui.keyUp('shift')  # Soltar a tecla Shift

# # Localizar na tela
# button_location = pyautogui.locateOnScreen('button.png')  # Localizar um botão na tela
# print(f"Localização do botão: {button_location}")
# button_center = pyautogui.locateCenterOnScreen('button.png')  # Localizar o centro do botão na tela
# print(f"Centro do botão: {button_center}")
# all_buttons = pyautogui.locateAllOnScreen('button.png')  # Localizar todas as instâncias do botão na tela
# print(f"Todas as localizações do botão: {list(all_buttons)}")

# # Localizar na tela com confiança
# try:
#     button_location = pyautogui.locateOnScreen('button.png', confidence=0.9)  # Localizar um botão na tela com 90% de confiança
#     print(f"Localização do botão: {button_location}")
# except pyautogui.ImageNotFoundException:
#     print("Botão não encontrado")

# # Localização relativa
# left, top, width, height = pyautogui.locateOnScreen('button.png')
# pyautogui.click(left + width/2, top + height/2)  # Clicar no centro do botão localizado

# # Operações de janela
# active_window = pyautogui.getActiveWindow()  # Obter a janela ativa atualmente
# print(f"Janela ativa: {active_window}")
# all_windows = pyautogui.getWindows()  # Obter uma lista de todas as janelas
# print(f"Todas as janelas: {all_windows}")

# # Captura de tela de parte da tela
# part_screen = pyautogui.screenshot(region=(0, 0, 300, 400))  # Tirar uma captura de tela de uma região específica
# part_screen.save("part_screenshot.png")  # Salvar a captura de tela parcial

# # Localizar por cor
# matches = list(pyautogui.locateAll('button.png', confidence=0.8))  # Localizar todas as correspondências de 'button.png' com 80% de confiança
# print(f"Correspondências encontradas: {matches}")

# # Estado do botão do mouse
# is_pressed = pyautogui.mouseDown()  # Verificar se um botão do mouse está pressionado
# print(f"Botão do mouse pressionado? {is_pressed}")

# # Arrastar com funções de suavização
# pyautogui.dragTo(500, 500, duration=1, tween=pyautogui.easeInOutQuad)  # Arrastar para (500, 500) usando suavização de entrada e saída

# # Cliques do mouse com argumento de botão
# pyautogui.click(button='right')  # Clicar com o botão direito
# pyautogui.click(button='middle')  # Clicar com o botão do meio

# # Arrastar com movimento relativo
# pyautogui.dragRel(100, 0, duration=1, button='left')  # Arrastar para a direita com o botão esquerdo pressionado

# # Atalhos de digitação
# pyautogui.write('Olá, mundo!')  # Escrever 'Olá, mundo!'
# pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y'])  # Escrever 'a', 'b', mover para a esquerda duas vezes, depois 'X', 'Y'

# # Combinações de teclas
# pyautogui.hotkey('ctrl', 'shift', 'esc')  # Pressionar Ctrl-Shift-Esc

# # Pausa e fail-safes
# pyautogui.PAUSE = 2.5  # Adicionar uma pausa de 2.5 segundos entre cada chamada
# pyautogui.FAILSAFE = True  # Habilitar o fail-safe que levanta uma exceção se o mouse for movido para um canto da tela

# # Informação do mouse
# mouse_info = pyautogui.mouseInfo()  # Obter a informação do mouse (posição e valores RGB)
# print(f"Informação do mouse: {mouse_info}")

# # Captura de tela e salvamento
# pyautogui.screenshot('my_screenshot.png')  # Tirar uma captura de tela e salvar como 'my_screenshot.png'

# # Obter valor RGB do pixel
# rgb_value = pyautogui.pixel(200, 300)  # Obter o valor RGB do pixel em (200, 300)
# print(f"Valor RGB em (200, 300): {rgb_value}")

# # Verificar se o pixel corresponde
# pixel_match = pyautogui.pixelMatchesColor(200, 300, (255, 0, 0))  # Verificar se o pixel em (200, 300) corresponde à cor (255, 0, 0)
# print(f"O pixel corresponde à cor? {pixel_match}")

# # Localização central
# center_location = pyautogui.center((0, 0, 100, 200))  # Obter o centro de uma região
# print(f"Localização central: {center_location}")

# # Soltar o botão do mouse
# pySegue a lista de 100 comandos do `pyautogui` organizada e formatada para uso no Visual Studio Code:

# ```python
# import pyautogui
# from time import sleep

# # Informações básicas da tela
# screen_width, screen_height = pyautogui.size()  # Obter o tamanho da tela
# print(f"Largura da tela: {screen_width}, Altura da tela: {screen_height}")

# # Movimentos do mouse
# pyautogui.moveTo(100, 100)  # Mover o mouse para (100, 100)
# pyautogui.moveTo(200, 200, duration=1.5)  # Mover o mouse para (200, 200) em 1.5 segundos
# pyautogui.moveRel(50, 50)  # Mover o mouse 50 pixels para a direita e 50 pixels para baixo
# pyautogui.moveRel(-50, -50, duration=1)  # Mover o mouse de volta para a posição original em 1 segundo

# # Cliques do mouse
# pyautogui.click()  # Clicar com o mouse
# pyautogui.click(100, 100)  # Clicar com o mouse em (100, 100)
# pyautogui.doubleClick()  # Clicar duas vezes com o mouse
# pyautogui.rightClick()  # Clicar com o botão direito do mouse
# pyautogui.middleClick()  # Clicar com o botão do meio do mouse

# # Arrastar o mouse
# pyautogui.dragTo(300, 300, duration=1.5)  # Arrastar o mouse para (300, 300) em 1.5 segundos
# pyautogui.dragRel(100, 100, duration=2)  # Arrastar o mouse 100 pixels para a direita e 100 pixels para baixo em 2 segundos

# # Rolagem do mouse
# pyautogui.scroll(500)  # Rolar para cima 500 unidades
# pyautogui.scroll(-500)  # Rolar para baixo 500 unidades

# # Posição do mouse
# current_mouse_x, current_mouse_y = pyautogui.position()  # Obter a posição atual do mouse
# print(f"Posição atual do mouse: ({current_mouse_x}, {current_mouse_y})")

# # Captura de tela
# screen = pyautogui.screenshot()  # Tirar uma captura de tela
# screen.save("screenshot.png")  # Salvar a captura de tela

# # Cor do pixel
# pixel_color = pyautogui.pixel(100, 100)  # Obter a cor do pixel em (100, 100)
# print(f"Cor do pixel em (100, 100): {pixel_color}")
# is_color = pyautogui.pixelMatchesColor(100, 100, (255, 255, 255))  # Verificar se o pixel em (100, 100) é branco
# print(f"O pixel em (100, 100) é branco? {is_color}")

# # Caixas de diálogo
# pyautogui.alert('Esta é uma caixa de alerta.')  # Mostrar uma caixa de alerta
# pyautogui.confirm('Devemos continuar?')  # Mostrar uma caixa de confirmação
# pyautogui.prompt('Qual é o seu nome?')  # Mostrar uma caixa de prompt
# pyautogui.password('Digite a senha:')  # Mostrar uma caixa de senha

# # Digitação
# pyautogui.typewrite('Olá, mundo!')  # Digitar 'Olá, mundo!'
# pyautogui.typewrite('Olá, mundo!', interval=0.25)  # Digitar 'Olá, mundo!' com intervalo de 0.25 segundos entre cada tecla
# pyautogui.press('enter')  # Pressionar a tecla Enter
# pyautogui.press(['left', 'left', 'left', 'left'])  # Pressionar a tecla de seta para a esquerda quatro vezes
# pyautogui.hotkey('ctrl', 'c')  # Pressionar a combinação de teclas Ctrl-C

# # Teclas especiais
# pyautogui.press('f1')  # Pressionar a tecla F1
# pyautogui.press('volumemute')  # Pressionar a tecla de mute de volume

# # Manter tecla pressionada e soltar
# pyautogui.keyDown('shift')  # Manter a tecla Shift pressionada
# pyautogui.press('left')  # Pressionar a tecla de seta para a esquerda
# pyautogui.keyUp('shift')  # Soltar a tecla Shift

# # Localizar na tela
# button_location = pyautogui.locateOnScreen('button.png')  # Localizar um botão na tela
# print(f"Localização do botão: {button_location}")
# button_center = pyautogui.locateCenterOnScreen('button.png')  # Localizar o centro do botão na tela
# print(f"Centro do botão: {button_center}")
# all_buttons = pyautogui.locateAllOnScreen('button.png')  # Localizar todas as instâncias do botão na tela
# print(f"Todas as localizações do botão: {list(all_buttons)}")

# # Localizar na tela com confiança
# try:
#     button_location = pyautogui.locateOnScreen('button.png', confidence=0.9)  # Localizar um botão na tela com 90% de confiança
#     print(f"Localização do botão: {button_location}")
# except pyautogui.ImageNotFoundException:
#     print("Botão não encontrado")

# # Localização relativa
# left, top, width, height = pyautogui.locateOnScreen('button.png')
# pyautogui.click(left + width/2, top + height/2)  # Clicar no centro do botão localizado

# # Operações de janela
# active_window = pyautogui.getActiveWindow()  # Obter a janela ativa atualmente
# print(f"Janela ativa: {active_window}")
# all_windows = pyautogui.getWindows()  # Obter uma lista de todas as janelas
# print(f"Todas as janelas: {all_windows}")

# # Captura de tela de parte da tela
# part_screen = pyautogui.screenshot(region=(0, 0, 300, 400))  # Tirar uma captura de tela de uma região específica
# part_screen.save("part_screenshot.png")  # Salvar a captura de tela parcial

# # Localizar por cor
# matches = list(pyautogui.locateAll('button.png', confidence=0.8))  # Localizar todas as correspondências de 'button.png' com 80% de confiança
# print(f"Correspondências encontradas: {matches}")

# # Estado do botão do mouse
# is_pressed = pyautogui.mouseDown()  # Verificar se um botão do mouse está pressionado
# print(f"Botão do mouse pressionado? {is_pressed}")

# # Arrastar com funções de suavização
# pyautogui.dragTo(500, 500, duration=1, tween=pyautogui.easeInOutQuad)  # Arrastar para (500, 500) usando suavização de entrada e saída

# # Cliques do mouse com argumento de botão
# pyautogui.click(button='right')  # Clicar com o botão direito
# pyautogui.click(button='middle')  # Clicar com o botão do meio

# # Arrastar com movimento relativo
# pyautogui.dragRel(100, 0, duration=1, button='left')  # Arrastar para a direita com o botão esquerdo pressionado

# # Atalhos de digitação
# pyautogui.write('Olá, mundo!')  # Escrever 'Olá, mundo!'
# pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y'])  # Escrever 'a', 'b', mover para a esquerda duas vezes, depois 'X', 'Y'

# # Combinações de teclas
# pyautogui.hotkey('ctrl', 'shift', 'esc')  # Pressionar Ctrl-Shift-Esc

# # Pausa e fail-safes
# pyautogui.PAUSE = 2.5  # Adicionar uma pausa de 2.5 segundos entre cada chamada
# pyautogui.FAILSAFE = True  # Habilitar o fail-safe que levanta uma exceção se o mouse for movido para um canto da tela

# # Informação do mouse
# mouse_info = pyautogui.mouseInfo()  # Obter a informação do mouse (posição e valores RGB)
# print(f"Informação do mouse: {mouse_info}")

# # Captura de tela e salvamento
# pyautogui.screenshot('my_screenshot.png')  # Tirar uma captura de tela e salvar como 'my_screenshot.png'

# # Obter valor RGB do pixel
# rgb_value = pyautogui.pixel(200, 300)  # Obter o valor RGB do pixel em (200, 300)
# print(f"Valor RGB em (200, 300): {rgb_value}")

# # Verificar se o pixel corresponde
# pixel_match = pyautogui.pixelMatchesColor(200, 300, (255, 0, 0))  # Verificar se o pixel em (200, 300) corresponde à cor (255, 0, 0)
# print(f"O pixel corresponde à cor? {pixel_match}")

# # Localização central
# center_location = pyautogui.center((0, 0, 100, 200))  # Obter o centro de uma região
# print(f"Localização central: {center_location}")

# # Soltar o botão do
