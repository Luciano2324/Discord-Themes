import pyautogui as pg
import time
import webbrowser
import darkMode
import ligthMode

def start(customBackground, bg):
    webbrowser.open("https://discord.com/channels/@me")
    time.sleep(6)
    pg.press("f12")
    time.sleep(5)
    pg.hotkey("ctrl","shift","p")
    pg.write("show elements")
    pg.press("enter")
    time.sleep(3)
    pg.hotkey("ctrl","shift","p")
    pg.write("dock to right")
    pg.press("enter")
    time.sleep(1)
    pg.press("down")
    pg.press("enter")
    pg.press("tab")
    pg.press("right")
    pg.press("space")
    pg.write("custom-theme-background")
    pg.press("enter")
    time.sleep(1)
    pg.press("home")
    pg.press("down")
    pg.press("enter")
    pg.press(["tab", "tab"])
    pg.press("delete")
    pg.press("enter")
    pg.press("end")
    pg.press(["tab"]*2)
    time.sleep(1)
    pg.hotkey("ctrl","z")
    pg.press(["tab"]*2)
    pg.write(":root")
    time.sleep(2)
    pg.press(["tab"]*6)
    pg.press("left")
    pg.press("enter")
    pg.press(["tab"]*13)
    time.sleep(0.5)
    pg.write(customBackground)
    time.sleep(2)
    for var in bg:
        pg.write(var)
        time.sleep(0.5)
    pg.press("f12")

print('')
print('Do you have dark mode or ligth mode on your Discord Web? Select a number:')
print('1) Dark Mode')
print('2) Ligth Mode')
print('')
x = int(input())
if(x>2 and x<1):
    print("Must enter a valid number")
if(x==1):
    print('')
    print("What custom theme do you want for your Discord webpage? Select an option with a number:")
    print("1) Sunset.")
    print("2) Chroma Glow.")
    print("3) Under the Sea.")
    print('')
    y = int(input())
    if(y<1 or y>3):
        print("Must enter a valid number")
    if(y==1):
        start(darkMode.sunsetColor, darkMode.bgsDarkMode)
    if(y==2):
        start(darkMode.chromaGlow, darkMode.bgsDarkMode)
    if(y==3):
        start(darkMode.underTheSea, darkMode.bgsDarkMode)
if(x==2):
    print('')
    print("What custom theme do you want for your Discord webpage? Select an option with a number:")
    print("1) Citrus Sherbert.")
    print("2) Sunrise.")
    print('')
    y = int(input())
    if(y<1 or y>3):
        print("Must enter a valid number")
    if(y==1):
        start(ligthMode.citrusSherbert, ligthMode.bgsLightMode)
    if(y==2):
        start(ligthMode.sunrise, ligthMode.bgsLightMode)