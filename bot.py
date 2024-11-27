import pyautogui
import time
import keyboard
import random
import win32api
import win32con


screenshotStartingX = 550
screenshotStartingY = 400
screenshotWidth = 800
screenshotHeight = 250
# pyautogui.displayMousePosition()
# x1: 840 y1: 480
# x2:  y2:
# x3:  y3:
# Enchant RGB:
# RGB of empty mana ball: 99 81 71


def click(x, y):
    win32api.SetCursorPos((x, y))
    time.sleep(0.4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.15)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def wiggle():  # random but W > S on average
    win32api.keybd_event(0x57, 0, 0, 0)  # Press W
    time.sleep(round(random.uniform(0.2, 0.3), 2))
    win32api.keybd_event(0x57, 0, win32con.KEYEVENTF_KEYUP, 0)  # Release W

    win32api.keybd_event(0x53, 0, 0, 0)  # Press S
    time.sleep(round(random.uniform(0.15, 0.2), 2))
    win32api.keybd_event(0x53, 0, win32con.KEYEVENTF_KEYUP, 0)  # Release S


# Give time to switch to other tab
flag = True
print("Loading: ")
time.sleep(3)
startTime = time.time()
noC = 0

# Have mana R: 60 - 70, G: 11-16, B: 70-86
# x,y Mana (178,967) Relative coordinates: (138,47)
# Have Health R: 125-135, G: 36-40, B: 0-8
# x,y Health (40,920) Relative coordinates: (0,0)
healthX = 0
healthY = 0
manaX = 110
manaY = 30
# every 30 seconds check health to pop potion
while keyboard.is_pressed('space') == False:

    endTime = time.time()
    print("\nTaking Health and Mana Status screenshot...")
    statusPic = pyautogui.screenshot(region=(55, 945, 120, 40))
    r, g, b = statusPic.getpixel((healthX, healthY))
    r2, g2, b2 = statusPic.getpixel((manaX, manaY))
    print(r, g, b)
    print(r2, g2, b2)
    # The color is no longer red
    if r in range(106, 107, 1) and g in range(52, 53, 1) and b in range(32, 33, 1):
        print("Low Health!")
        click(225, 973)  # uses a potion
    # The color is no longer purple/blue
    elif r2 in range(87, 88, 1) and g2 in range(67, 68, 1) and b2 in range(48, 49, 1):
        print("Low Mana!")
        click(225, 973)  # uses a potion
    else:
        print("Health and Mana are good!")

    print("\nTaking deck screenshot...")
    pic = pyautogui.screenshot(region=(
        screenshotStartingX, screenshotStartingY, screenshotWidth, screenshotHeight))
    if pyautogui.locate("./EnchantedTempestInBattle(1920).png", pic, confidence=0.9) is not None:
        x, y = pyautogui.center(pyautogui.locate(
            "./EnchantedTempestInBattle(1920).png", pic, confidence=0.9))
        click(x+screenshotStartingX, y+screenshotStartingY)
        noC = 0
    elif pyautogui.locate("./EpicInBattle(1920).png", pic, confidence=0.9) is not None:
        print("It sees epic")
        x, y = pyautogui.center(pyautogui.locate(
            "./EpicInBattle(1920).png", pic, confidence=0.9))
        click(x+screenshotStartingX, y+screenshotStartingY)
        time.sleep(1)
        if pyautogui.locate("./TempestInBattle(1920).png", pic, confidence=0.9) is not None:
            print("It sees epic and tempest")

            x, y = pyautogui.center(pyautogui.locate(
                "./TempestInBattle(1920).png", pic, confidence=0.9))
            click(x+screenshotStartingX, y+screenshotStartingY)
            time.sleep(0.5)
            click(x+screenshotStartingX, y+screenshotStartingY)
            time.sleep(1)
            click(screenshotStartingX, screenshotStartingY)
            noC = 0
    elif noC >= 30:
        endTime = time.time() - 100
        break
    else:
        print("Didn't see anything")
        noC += 1
        win32api.SetCursorPos((screenshotStartingX, screenshotStartingY))
        wiggle()
        # if(flag):
        #     wiggle()
        #     flag = not flag
        # else:
        #     flag = not flag
    time.sleep(5)

print("Program was running for: " +
      str(round((endTime - startTime) / 60, 2)) + "min")
