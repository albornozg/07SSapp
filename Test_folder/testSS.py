from pyautogui import *
import pyautogui
import time
#import keyboard
import random
import win32api, win32con
import numpy as np
import cv2
# import PySimpleGUI as sg

cond = True

"""
This is a test app to check if the detection of the images is working.
"""
min_match_count = 2

# Creamos la funcion que tomara la captura de pantalla
def screen_capture():
    screenshot = pyautogui.screenshot()
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Inicializamos el ORB detector
orb = cv2.ORB_create()

# Cargamos la imagen base (la pasamos a gray) y tomamos sus keypoints y descriptores
base_img = cv2.imread('SS_inventory-v.2.pngpng',cv2.IMREAD_GRAYSCALE)
kp1, des1 = orb.detectAndCompute(base_img, None)

# Creamos el objeto de fuerza bruta (brute force) con Hamming distance y cross-checking
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Creamos while loop para hacer deteccion en la pantalla y comparar
while cond:

    # Capturamos pantalla
    current_img = screen_capture()
    cv2.imwrite('TESTALL.png', current_img)
    current_img_gray = cv2.cvtColor(current_img, cv2.COLOR_BGR2GRAY)

    # creamos los descriptores de la segunda imagen (la pantalla)
    kp2, des2 = orb.detectAndCompute(current_img_gray, None)

    # condicional
    if des1 is not None and des2 is not None:

        matches = bf.match(des1, des2)
        matches = sorted(matches, key = lambda x:x.distance)

        print("Number of matches:", len(matches))

        #img3 = cv2.drawMatches(base_img, base_kp, current_img, kp2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        #cv2.imshow('Matches', img3)

        if len(matches) >= min_match_count:
            src_pts = np.float32([ kp1[m.queryIdx].pt for m in matches[:min_match_count] ]).reshape(-1,1,2)
            dst_pts = np.float32([ kp2[m.trainIdx].pt for m in matches[:min_match_count] ]).reshape(-1,1,2)

            M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            matchesMask = mask.ravel().tolist()

            h, w = img_reference.shape
            pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
            dst = cv2.perspectiveTransform(pts, M)

            # Find the centroid of the matched area
            centroid = np.mean(dst.reshape(-1, 2), axis=0)
            x, y = int(centroid[0]), int(centroid[1])

            # Move the mouse to the centroid of the matched area and click
            pyautogui.moveTo(x, y)
            pyautogui.click()
            print(f"Clicked at {x}, {y}")

        else:
            print("Not enough matches found - %d/%d" % (len(matches), min_match_count))
            sleep(1)

    else:
        print("No matches detected at all")
        cond = False
        exit

    # Break loop with 'q' key
    key = cv2.waitKey(50) & 0xFF
    print("Key pressed:", key if key != 255 else "None")  # 255 means no key was pressed
    if key == ord('q'):
        break

    # le damos un tiempo de espera de 1 seg
    time.sleep(1)

#cv2.destroyAllWindows()


    """
--------------------------------------------------
    try:
        pyautogui.locateOnScreen('SS_sword-v.1.png', grayscale=True, confidence=0.8)
        print("Detected")
        time.sleep(0.5)

    except pyautogui.ImageNotFoundException:
        print("Not Detected")
        time.sleep(0.5)
    """
