import pyautogui
import time

jalan = False

print("Aim Trainer Berjalan")

while 1 :
    time.sleep(0.001)
    target = pyautogui.locateOnScreen('Target.png', confidence = 0.4)
    if target != None:
        print("Terlihat")
        print("x={0} , y ={1}".format(pyautogui.center(target).x, pyautogui.center(target).y))
        pyautogui.click(pyautogui.center(target).x, pyautogui.center(target).y)
        # pyautogui.click('Target.png')
    else :
        print("Tidak Terlihat")
