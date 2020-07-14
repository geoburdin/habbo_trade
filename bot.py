from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import ImageGrab
import os
import time
import cv2
import numpy as np
import pyautogui


def find_mana(smth_to_find):
    img = cv2.imread("screenshot.png")  # картинка, на которой ищем объект
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # преобразуем её в серуюш
    template = cv2.imread(smth_to_find,
                          cv2.IMREAD_GRAYSCALE)  # объект, который преобразуем в серый, и ищем его на gray_img
    w, h = template.shape[::-1]  # инвертируем из (y,x) в (x,y)
    result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.5)
    pt=(0,0)
    # рисует прямоугольник вокруг объекта
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 3)

    return pt

def main():
    # делает скриншот игры, закоментируйте, если понадобится, так как скриншот я выложил снизу, как и сам объект

    im = ImageGrab.grab()
    output = im.save(os.getcwd() + '\\screenshot' + '.png', 'PNG')
    print('\nСкриншот сделан и сохранён\n')

pyautogui.FAILSAFE=False
take_pic=True
while take_pic==True:
    time.sleep(5)
    main()
    if find_mana('shop.png')!=(0,0):
        main()
        pyautogui.moveTo(find_mana('shop.png')[0]+10, find_mana('shop.png')[1]+10)
        pyautogui.click()
    elif find_mana('price.png') != (0, 0) and find_mana('credits.png') != (0, 0):
        main()
        pyautogui.moveTo(find_mana('price.png')[0], find_mana('price.png')[1])
        im = ImageGrab.grab(bbox =(find_mana('price.png')[0]+75, find_mana('price.png')[1]-30, find_mana('credits.png')[0]-45, find_mana('price.png')[1]-10))
        output = im.save(os.getcwd() + '\\price_number' + '.png', 'PNG')
    elif find_mana('offers.png') != (0, 0):
        main()
        pyautogui.moveTo(find_mana('offers.png')[0] + 10, find_mana('offers.png')[1] + 10)
        pyautogui.click()
    elif find_mana('market.png') != (0, 0):
        main()
        pyautogui.moveTo(find_mana('market.png')[0] + 10, find_mana('market.png')[1] + 10)
        pyautogui.click()
    elif find_mana('Furni.png')!=(0,0):
        main()
        pyautogui.moveTo(find_mana('Furni.png')[0]+10, find_mana('Furni.png')[1]+10)
        pyautogui.click()
