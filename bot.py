from PIL import ImageGrab
import time
import cv2
import pyautogui
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
TESSDATA_PREFIX = 'C:/Program Files/Tesseract-OCR'

def find_mana(smth_to_find,where_find):
    img = cv2.imread(where_find,0)
    template = cv2.imread(smth_to_find,0)

    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    # Get the best match position from the match result.
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print('Best match top left position: %s' % str(max_loc))
    print('Best match confidence: %s' % max_val)

    threshold = 0.8
    top_left = (0, 0)
    if max_val >= threshold:
        needle_w = template.shape[1]
        needle_h = template.shape[0]

        top_left = max_loc
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

        cv2.rectangle(img, top_left, bottom_right,
                     color=(0, 255, 0), thickness=2, lineType=cv2.LINE_4)
        cv2.imshow('Result', img)
        cv2.waitKey()

    return top_left

def main():

    im = ImageGrab.grab()
    im.save('screenshot' + '.png', 'PNG')
    print('Screen Analysis')
    time.sleep(2)

def analys():
    pyautogui.FAILSAFE = False
    take_pic = True

    while take_pic == True:
        try:
            main()

            if find_mana('offers.png', 'screenshot.png') != (0, 0) or find_mana('offers_pressed.png', 'screenshot.png'):
                print('point 1')
                while find_mana('price.png', 'screenshot.png') != (0, 0) and find_mana('credits.png', 'screenshot.png') != (0, 0):

                    pyautogui.moveTo(find_mana('price.png', 'screenshot.png')[0], find_mana('price.png', 'screenshot.png')[1])

                    string_num = ImageGrab.grab(bbox=(
                    find_mana('price.png', 'screenshot.png')[0] + 75, find_mana('price.png', 'screenshot.png')[1] - 23,
                    find_mana('price.png', 'screenshot.png')[0] + 75 + 100, find_mana('price.png', 'screenshot.png')[1] - 10))

                    string_num.save( 'price_str' + '.png', 'PNG')
                    img2 = string_num.crop((0, 0, find_mana('credits.png', 'price_str.png')[0], 13))
                    img2.save( 'price_number' + '.png', 'PNG')
                    img = cv2.imread('price_number.png')
                    print('price = ' + pytesseract.image_to_string(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                                                                   config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'))
                    time.sleep(10)
                    main()
                if find_mana('price.png', 'screenshot.png') == (0, 0):
                    print('point 2')
                    if find_mana('list.png', 'screenshot.png') != (0, 0):
                        print('point 3')

                        time.sleep(5)
                    elif find_mana('offers.png', 'screenshot.png') != (0, 0):
                        pyautogui.moveTo(find_mana('offers.png', 'screenshot.png')[0],
                                         find_mana('offers.png', 'screenshot.png')[1]+5)
                        pyautogui.click()
                    main()

            elif find_mana('market.png', 'screenshot.png') != (0, 0):

                pyautogui.moveTo(find_mana('market.png', 'screenshot.png')[0] + 10, find_mana('market.png', 'screenshot.png')[1])
                pyautogui.click()

            elif find_mana('Furni.png', 'screenshot.png') != (0, 0):

                pyautogui.moveTo(find_mana('Furni.png', 'screenshot.png')[0]+10, find_mana('Furni.png', 'screenshot.png')[1]+10)
                pyautogui.click()

            elif find_mana('shop.png', 'screenshot.png') != (0, 0):

                pyautogui.moveTo(find_mana('shop.png', 'screenshot.png')[0]+10, find_mana('shop.png', 'screenshot.png')[1]+10)
                pyautogui.click()

        except:
            print('something is wrong')
