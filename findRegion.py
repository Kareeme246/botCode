import pyautogui
import time

# pyautogui.displayMousePosition()
im1 = pyautogui.screenshot(region=(55, 945, 120, 40))
im1.save(r"./savedimage.png")

rArray = []
gArray = []
bArray = []

rArray2 = []
gArray2 = []
bArray2 = []

healthX = 0
healthY = 0
manaX = 110
manaY = 30
statusPic = pyautogui.screenshot(region=(55, 945, 120, 40))
r, g, b = statusPic.getpixel((healthX, healthY))
r2, g2, b2 = statusPic.getpixel((manaX, manaY))

for i in range(1, 60):
    print(i)
    r, g, b = statusPic.getpixel((healthX, healthY))
    rArray.append(r)
    gArray.append(g)
    bArray.append(b)
    r2, g2, b2 = statusPic.getpixel((manaX, manaY))
    rArray2.append(r2)
    gArray2.append(g2)
    bArray2.append(b2)
    time.sleep(1)

print(min(rArray), max(rArray))   #
print(min(gArray), max(gArray))   #
print(min(bArray), max(bArray))   #
print(min(rArray2), max(rArray2))
print(min(gArray2), max(gArray2))
print(min(bArray2), max(bArray2))

# 55 945 Health
# 165 975 Mana

# Health Relative coordinates: (110,30)
# Mana Relative coordinates: (,)
