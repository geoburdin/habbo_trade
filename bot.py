from PIL import ImageGrab
import time
import cv2
import pyautogui
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR/tesseract'
TESSDATA_PREFIX = 'Tesseract-OCR'


def find_mana(smth_to_find, where_find):
    img = cv2.imread(where_find, 0)
    template = cv2.imread(smth_to_find, 0)

    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    # Get the best match position from the match result.
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    threshold = 0.8
    top_left = (0, 0)
    if max_val >= threshold:
        top_left = max_loc

    return top_left


def get_price():
    pyautogui.moveTo(find_mana('price.png', 'screenshot.png')[0], find_mana('price.png', 'screenshot.png')[1])

    string_num = ImageGrab.grab(bbox=(
        find_mana('price.png', 'screenshot.png')[0], find_mana('price.png', 'screenshot.png')[1],
        find_mana('price.png', 'screenshot.png')[0] + 150, find_mana('price.png', 'screenshot.png')[1] + 14))

    string_num.save('price_str' + '.png', 'PNG')
    img2 = string_num.crop((28, 0, find_mana('credits.png', 'price_str.png')[0], 14))
    img2.save('price_number' + '.png', 'PNG')
    img = cv2.imread('price_number.png')
    price = pytesseract.image_to_string(
        cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
        config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'
    )
    return price


def get_text():
    pyautogui.moveTo(find_mana('price.png', 'screenshot.png')[0], find_mana('price.png', 'screenshot.png')[1] - 40)

    string_num = ImageGrab.grab(bbox=(
        find_mana('price.png', 'screenshot.png')[0], find_mana('price.png', 'screenshot.png')[1]-30,
        find_mana('price.png', 'screenshot.png')[0] + 150, find_mana('price.png', 'screenshot.png')[1] - 5))

    string_num.save('name_str' + '.png', 'PNG')

    img = cv2.imread('name_str.png')
    price = pytesseract.image_to_string(
        cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
        config='--psm 7 --oem 3 '
    )
    return price


def main():

    im = ImageGrab.grab()
    im.save('screenshot' + '.png', 'PNG')

    time.sleep(5)


def analys():
    pyautogui.FAILSAFE = False
    take_pic = True
    price = 0
    while take_pic == True:
        try:
            main()

            if find_mana('offers.png', 'screenshot.png') != (0, 0) or find_mana('offers_pressed.png', 'screenshot.png') != (0, 0):

                if find_mana('price.png', 'screenshot.png') != (0, 0) and find_mana('credits.png', 'screenshot.png') != (0, 0):

                    if price != 0:

                        pyautogui.moveTo(find_mana('search.png', 'screenshot.png')[0] + 5,
                                         find_mana('search.png', 'screenshot.png')[1] + 5)
                        pyautogui.click()
                        time.sleep(4)
                        price_now = get_price()
                        print('now price = ' + price_now)

                        if int(price_now) <= int(price):

                            pyautogui.moveTo(find_mana('buy.png', 'screenshot.png')[0] + 10,
                                             find_mana('buy.png', 'screenshot.png')[1] + 10)
                            pyautogui.click()
                            main()
                            time.sleep(3)
                            if find_mana('buy_final.png', 'screenshot.png')!=(0,0):
                                pyautogui.moveTo(find_mana('buy.png', 'screenshot.png')[0] + 10,
                                                 find_mana('buy.png', 'screenshot.png')[1] + 10)
                                pyautogui.click()
                                print('                  --- The item was bought ---')
                            print('I`m trying to buy the item')

                        time.sleep(10)
                        main()

                    elif price == 0:
                        item = get_text()
                        print(item)
                        price = get_price()
                        print('price = ' + price)
                        print('The price and item right? Press y or n')
                        response = input()
                        if response == 'n':
                            price = 0
                            item = None
                            print('Well, let\'s try again')
                        elif response == 'y':
                            print('Ok, got it')
                            print('Write the buy-price: ')
                            price = int(input())

                        else:
                            price = 0
                            item = None
                            print('Sorry, wrong letter')
                        time.sleep(3)
                        main()

                if find_mana('price.png', 'screenshot.png') == (0, 0):

                    if find_mana('offers.png', 'screenshot.png') != (0, 0):
                        pyautogui.moveTo(find_mana('offers.png', 'screenshot.png')[0],
                                         find_mana('offers.png', 'screenshot.png')[1]+5)
                        pyautogui.click()
                        print('I\'m in the offers \n Select an item please')
                        time.sleep(5)
                    main()

            elif find_mana('market.png', 'screenshot.png') != (0, 0):

                pyautogui.moveTo(find_mana('market.png', 'screenshot.png')[0] + 10, find_mana('market.png', 'screenshot.png')[1]+5)
                pyautogui.click()
                print('I\'m in the marketplace')
                time.sleep(5)

            elif find_mana('Furni.png', 'screenshot.png') != (0, 0):

                pyautogui.moveTo(find_mana('Furni.png', 'screenshot.png')[0]+10, find_mana('Furni.png', 'screenshot.png')[1]+10)
                pyautogui.click()
                print('I\'m in the Furni')
                time.sleep(5)

            elif find_mana('shop.png', 'screenshot.png') != (0, 0):

                pyautogui.moveTo(find_mana('shop.png', 'screenshot.png')[0]+10, find_mana('shop.png', 'screenshot.png')[1]+10)
                pyautogui.click()
                print('I\'m in the shop')
                price = 0
                time.sleep(5)

        except Exception as e:
            time.sleep(1)

