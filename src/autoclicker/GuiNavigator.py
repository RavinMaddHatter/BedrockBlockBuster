import pyautogui
import pygetwindow as gw
import time
from contextlib import suppress
import os
from PIL import ImageGrab
print(os.getcwd())
replace={"replace":"refference Images/replace.png"}
menus={
    "pause":"refference Images/pause.png",
    "main":"refference Images/hotbar.png",
    "chat":"refference Images/chat.png",
    "save_structure":"refference Images/save-structure-menu.png",
    "3d_export_menu":"refference Images/3d export_menu.png",
    "structure_export_menu":"refference Images/structure-export-menu.png",
    "save_3d":"refference Images/3d export.png"
    }
def screenshotMC():
    minecraft_win = gw.getWindowsWithTitle('Minecraft')[0]
    screenshot = ImageGrab.grab(all_screens=True)
    return screenshot
        
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
def reconnect():
    connect()
    time.sleep(0.5)
    send_command("/repeatlastblock")
def connect():
    returnMain()
    send_command("/connect localhost:3000")
def setup_pack():
    send_command("/getblocks")
def next_block():
    send_command("/nextblock")
def process_block(name):
    returnMain()
    pyautogui.mouseDown(button='right')
    time.sleep(0.2)
    pyautogui.mouseUp(button='right')
    time.sleep(0.2)
    screen = get_screen(menus, confidence_level=0.8)[0]
    if screen =="3d_export_menu":
        pyautogui.press("down")
        time.sleep(0.1)
        pyautogui.press("enter")
        time.sleep(0.1)
        pyautogui.press("enter")
        time.sleep(0.1)
        pyautogui.press("down")
        time.sleep(0.1)
    else:
        pyautogui.press("down")
        time.sleep(0.1)
        pyautogui.press("down")
        time.sleep(0.1)
    pyautogui.press("1")
    
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(0.1)
    pyautogui.press("right")
    time.sleep(0.1)
    pyautogui.press("down")
    time.sleep(0.1)
    pyautogui.press("enter")
    screen = get_screen(menus, confidence_level=0.8)[0]
    while not(screen=="save_structure"):
        screen = get_screen(menus, confidence_level=0.8)[0]
        time.sleep(0.1)
    pyautogui.write(name+".mcstructure")
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("y")
    returnMain()
    time.sleep(0.1)
    pyautogui.mouseDown(button='right')
    time.sleep(0.2)
    pyautogui.mouseUp(button='right')
    time.sleep(0.2)
    pyautogui.press("down")
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(0.1)
    pyautogui.press("down")
    time.sleep(0.1)
    pyautogui.press("down")
    time.sleep(0.1)
    pyautogui.press("down")
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(0.1)
    pyautogui.press("right")
    time.sleep(0.1)
    pyautogui.press("down")
    time.sleep(0.1)
    pyautogui.press("left")
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(0.1)
    screen = get_screen(menus, confidence_level=0.8)[0]
    while not(screen=="save_structure"):
        screen = get_screen(menus, confidence_level=0.8)[0]
        time.sleep(0.1)
    pyautogui.write(name+".glb")
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("y")
    
    
    
    
    
if __name__=="__main__":
    setup_pack()
    time.sleep(0.3)
    next_block()
    process_block("test")

