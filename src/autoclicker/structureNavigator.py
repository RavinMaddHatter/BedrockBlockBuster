import pyautogui
import pygetwindow as gw
import time
from contextlib import suppress
import os
from PIL import ImageGrab
import pyperclip
print(os.getcwd())

pyautogui.PAUSE = 0 
replace={"replace":"refference Images/replace.png"}
menus={
    "pause":"refference Images/pause.png",
    "main":"refference Images/hotbar.png",
    "chat":"refference Images/chat.png",
    "save_menu":"refference Images/saveMenu.png",
    "structure_export_menu":"refference Images/structure-export-menu.png",
    "save_3d":"refference Images/3d export.png"
    }
reset_state = {
    "nope":"refference Images/not_reset.png",
    "home":"refference Images/reset.png"
    }
exportSelected_state = {
    #"nope":"refference Images/export_not_selected.png",
    "highlighted":"refference Images/export_highlighted.png",
    "highlighted2":"refference Images/export_highlighted2.png"
    }
def screenshotMC():
    minecraft_win = gw.getWindowsWithTitle('Minecraft')[0]
    screenshot = ImageGrab.grab(all_screens=True)
    return screenshot
def exportSelected():
    state = get_screen(exportSelected_state,confidence_level=0.80)
    print(state)
    return state[0]!="Unknown / No Menu Detected"
def restoreMC():
    minecraft_win = gw.getWindowsWithTitle('Minecraft')[0]
    if minecraft_win.isMinimized:
        minecraft_win.restore()
    minecraft_win.activate()
def get_screen(templates, confidence_level=0.8):
    screen = screenshotMC()
    for menu_name, image_path in templates.items():
        if not os.path.exists(image_path):
            print(f"Warning: Template missing at {image_path}")
        with suppress(pyautogui.ImageNotFoundException):
            location = pyautogui.locate(image_path, screen, confidence=confidence_level)
            if location is not None:
                return menu_name, location
    return "Unknown / No Menu Detected", None
def homeUI():
    state = get_screen(reset_state,confidence_level=0.98)
    while state[0]!="home":
        pyautogui.press("up")
        tick()
        state = get_screen(reset_state)
        
def tick():
    time.sleep(1/20)
def exportmcstructure(name):
    homeUI()
    screen = get_screen(menus)
    while screen[0] !="structure_export_menu":
        if screen[0]=="save_3d":
            pyautogui.press("down")
            tick()
            pyautogui.press("enter")
            tick()
            pyautogui.press("up")
            tick()
            pyautogui.press("up")
            tick()
            pyautogui.press("up")
            tick()
            pyautogui.press("enter")
            tick()
        else:
            throw
        screen = get_screen(menus)
    while not exportSelected():
        homeUI()
        pyautogui.press("right")
        tick()
        pyautogui.press("right")
        tick()
        pyautogui.press("down")
        tick()
    pyautogui.press("enter")
    while not (get_screen(menus)[0]=="save_menu"):
        tick()
    pyperclip.copy(name+".mcstructure")
    pyautogui.hotkey('ctrl', 'v')
    tick()
    pyautogui.press("enter")
    tick()
    while not (get_screen(menus)[0]=="structure_export_menu"):
        pyautogui.press("y")
        tick()

def export3d(name):
    homeUI()
    screen = get_screen(menus)
    while screen[0] !="save_3d" :
        if screen[0]=="structure_export_menu":
            pyautogui.press("down")
            tick()
            pyautogui.press("enter")
            tick()
            pyautogui.press("down")
            tick()
            pyautogui.press("down")
            tick()
            pyautogui.press("down")
            tick()
            pyautogui.press("enter")
            tick()
        else:
            throw
        screen = get_screen(menus)
    while not exportSelected():
        homeUI()
        pyautogui.press("right")
        tick()
        pyautogui.press("right")
        tick()
        pyautogui.press("down")
        tick()
        pyautogui.press("left")
        tick()
    pyautogui.press("enter")
    while not (get_screen(menus)[0]=="save_menu"):
        tick()
    pyperclip.copy(name+".glb")
    pyautogui.hotkey('ctrl', 'v')
    tick()
    pyautogui.press("enter")
    tick()
    while not (get_screen(menus)[0]=="save_3d"):
        pyautogui.press("y")
        tick()

def returnMain():
    restoreMC()
    time.sleep(0.05)
    screen = get_screen(menus, confidence_level=0.5)
    while not(screen[0]=="main"):
        pyautogui.press("esc")
        time.sleep(0.2)
        screen = get_screen(menus, confidence_level=0.5)
def send_command(command):
    returnMain()
    pyautogui.press("t")
    time.sleep(0.3)
    pyautogui.write(command)
    time.sleep(0.1)
    pyautogui.press("enter")
def connect():
    returnMain()
    send_command("/connect localhost:3000")
def enterStructure():
    returnMain()
    pyautogui.mouseDown(button='right')
    time.sleep(0.2)
    pyautogui.mouseUp(button='right')
    time.sleep(0.2)
    screen = get_screen(menus, confidence_level=0.8)
    if not(screen[0]=="structure_export_menu" or screen[0]=="save_3d"):
        throw    
if __name__=="__main__":
    restoreMC()
    enterStructure()
    exportmcstructure("test")
    export3d("test")

