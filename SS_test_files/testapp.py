from pyautogui import *
import pyautogui
import time
import random
import win32api, win32con
import cv2
import numpy as np
# import PySimpleGUI as sg

# First square would be on 106,11 ; 149,53 ; w=53 , h=36
width = 233
height = 320

# definimos la funcion para la toma de captura de pantalla
def base_ss():
    im1_location = pyautogui.locateOnScreen('SS_sword-v.1.png', grayscale=True, confidence=0.8)
    im2_location = pyautogui.locateOnScreen('SS_quest-v.2.png', grayscale=True, confidence=0.7)
    im3_location = pyautogui.locateOnScreen('SS_inventory-v.3.png', grayscale=True, confidence=0.7)

    x_base = int(im1_location.left)
    y_base = int(im1_location.top)


    im2_loc_point = pyautogui.center(im2_location)
    im3_loc_point = pyautogui.center(im3_location)

    s1 = pyautogui.screenshot(region=(x_base, y_base, width, height))
    s1 = np.array(s1)


    pyautogui.click(im2_loc_point.x, im2_loc_point.y)
    time.sleep(0.25)
    s2 = pyautogui.screenshot(region=(x_base, y_base, width, height))
    
    if ach_dia == 'Yes':
        pyautogui.click(im2_loc_point.x + 120, im2_loc_point.y + 45)
        time.sleep(0.5)
        s4 = pyautogui.screenshot(region=(x_base, y_base, width, height))
        time.sleep(0.5)
        pyautogui.click(im2_loc_point.x + 146, im2_loc_point.y + 314)
        s5 = pyautogui.screenshot(region=(x_base, y_base, width, height))
    else:
        pass
    
    s2 = np.array(s2)

    time.sleep(0.25)

    pyautogui.click(im3_loc_point.x, im3_loc_point.y)
    s3 = pyautogui.screenshot(region=(x_base, y_base, width, height))
    s3 = np.array(s3)

    ss_BGR = np.concatenate((s3, s1, s2), axis=1)
    ss_RGB = cv2.cvtColor(ss_BGR, cv2.COLOR_BGR2RGB)
    ss_BGR_ad = np.concatenate((s3, s1, s2, s4, s5), axis=1)
    ss_RGB_ad = cv2.cvtColor(ss_BGR_ad, cv2.COLOR_BGR2RGB)

        
    alert(text='Pictures have  been taken!', title='Complete', button='OK')   
    if ach_dia == 'Yes':
        return cv2.imwrite('Screenshot.png', ss_RGB_ad)
    else:
        return cv2.imwrite('Screenshot.png', ss_RGB)

okc = confirm(text='Welcome to the remastered version. This simple app was created by Gabriel Albornoz', title='Initio', buttons=['OK', 'Cancel'])
ach_dia = confirm(text='Do you want to include the Achievement Diaries into the image?', title='Achievement Diaries?', buttons=['Yes', 'No'])

if okc == 'OK':
    try:
        base_ss()
        
    except pyautogui.ImageNotFoundException:
        alert(text='Runelite not detected. Try again.', title='Warning', button='OK')
        exit      
else:
    exit
