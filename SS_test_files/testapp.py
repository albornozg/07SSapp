from pyautogui import *
import pyautogui
import time
import random
import win32api, win32con
import cv2
import numpy as np
from tkinter import *
from tkinter import ttk
from function_files import *
# import PySimpleGUI as sg

"""
def select_screen():
    root = Tk()
    root.title("07 Screenshotter")

    content = ttk.Frame(root)
    content.grid(column=0, row=0)

    label_1 = ttk.Label(content, text='Select the skills you would like to have hidden:')
    label_1.grid(column=0, row=0)

    frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=2000, height=1000)
    frame.grid(column=0, row=1)



    rcvar = BooleanVar(value=False)
    constvar = BooleanVar(value=False)
    agivar = BooleanVar(value=False)
    hervar = BooleanVar(value=False)
    thievar = BooleanVar(value=False)
    crafvar = BooleanVar(value=False)
    fletvar = BooleanVar(value=False)
    slayvar = BooleanVar(value=False)
    huntvar = BooleanVar(value=False)
    minvar = BooleanVar(value=False)
    smivar = BooleanVar(value=False)
    fishvar = BooleanVar(value=False)
    cookvar = BooleanVar(value=False)
    firevar = BooleanVar(value=False)
    woodvar = BooleanVar(value=False)
    farvar = BooleanVar(value=False)
    ach_dia = BooleanVar(value=False)

    rc = ttk.Checkbutton(frame, text="Runecraft", variable=rcvar, onvalue=True)
    const = ttk.Checkbutton(frame, text="Construction", variable=constvar, onvalue=True)
    agi = ttk.Checkbutton(frame, text="Agility", variable=agivar, onvalue=True)
    herb = ttk.Checkbutton(frame, text="Herblore", variable=hervar, onvalue=True)
    thie = ttk.Checkbutton(frame, text="Thieving", variable=thievar, onvalue=True)
    craf = ttk.Checkbutton(frame, text="Crafting", variable=crafvar, onvalue=True)
    flet = ttk.Checkbutton(frame, text="Fletching", variable=fletvar, onvalue=True)
    slay = ttk.Checkbutton(frame, text="Slayer", variable=slayvar, onvalue=True)
    hunt = ttk.Checkbutton(frame, text="Hunter", variable=huntvar, onvalue=True)
    min = ttk.Checkbutton(frame, text="Mining", variable=minvar, onvalue=True)
    smi = ttk.Checkbutton(frame, text="Smithing", variable=smivar, onvalue=True)
    fish = ttk.Checkbutton(frame, text="Fishing", variable=fishvar, onvalue=True)
    cook = ttk.Checkbutton(frame, text="Cooking", variable=cookvar, onvalue=True)
    fire = ttk.Checkbutton(frame, text="Firemaking", variable=firevar, onvalue=True)
    wood = ttk.Checkbutton(frame, text="Woodcutting", variable=woodvar, onvalue=True)
    far = ttk.Checkbutton(frame, text="Farming", variable=farvar, onvalue=True)

    achiev = ttk.Checkbutton(content, text="Include Achievement Diaries?", variable=ach_dia, onvalue=True)

    rc.grid(column=0, row=0, sticky="w")
    const.grid(column=0, row=1, sticky="w")
    agi.grid(column=0, row=2, sticky="w")
    herb.grid(column=0, row=3, sticky="w")
    thie.grid(column=1, row=0, sticky="w")
    craf.grid(column=1, row=1, sticky="w")
    flet.grid(column=1, row=2, sticky="w")
    slay.grid(column=1, row=3, sticky="w")
    hunt.grid(column=2, row=0, sticky="w")
    min.grid(column=2, row=1, sticky="w")
    smi.grid(column=2, row=2, sticky="w")
    fish.grid(column=2, row=3, sticky="w")
    cook.grid(column=3, row=0, sticky="w")
    fire.grid(column=3, row=1, sticky="w")
    wood.grid(column=3, row=2, sticky="w")
    far.grid(column=3, row=3, sticky="w")

    achiev.grid(column=0, row=4, columnspan=3)

    root.mainloop()
"""

"""
root = Tk()
root.title("Welcome!")

welcome_label = ttk.Label(root, text='Welcome to the screenshotter version 1. This simple app was created by Gabriel Albornoz')
welcome_label.grid(column=0, row=0)

okay_button = ttk.Button(root, text='Okay', command=select_screen)
cancel_button = ttk.Button(root, text='Cancel', command=root.destroy)

okay_button.grid(column=0, row=1)
cancel_button.grid(column=1, row=1)



root.mainloop()
"""
# tkinter test

root = Tk()
root.title("07 Screenshotter")

content = ttk.Frame(root)
content.grid(column=0, row=0)

label_1 = ttk.Label(content, text='Select the skills you would like to have hidden:')
label_1.grid(column=0, row=0)

frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=2000, height=1000)
frame.grid(column=0, row=1)



rcvar = BooleanVar(value=False)
constvar = BooleanVar(value=False)
agivar = BooleanVar(value=False)
hervar = BooleanVar(value=False)
thievar = BooleanVar(value=False)
crafvar = BooleanVar(value=False)
fletvar = BooleanVar(value=False)
slayvar = BooleanVar(value=False)
huntvar = BooleanVar(value=False)
minvar = BooleanVar(value=False)
smivar = BooleanVar(value=False)
fishvar = BooleanVar(value=False)
cookvar = BooleanVar(value=False)
firevar = BooleanVar(value=False)
woodvar = BooleanVar(value=False)
farvar = BooleanVar(value=False)
ach_dia = BooleanVar(value=False)

rc = ttk.Checkbutton(frame, text="Runecraft", variable=rcvar, onvalue=True)
const = ttk.Checkbutton(frame, text="Construction", variable=constvar, onvalue=True)
agi = ttk.Checkbutton(frame, text="Agility", variable=agivar, onvalue=True)
herb = ttk.Checkbutton(frame, text="Herblore", variable=hervar, onvalue=True)
thie = ttk.Checkbutton(frame, text="Thieving", variable=thievar, onvalue=True)
craf = ttk.Checkbutton(frame, text="Crafting", variable=crafvar, onvalue=True)
flet = ttk.Checkbutton(frame, text="Fletching", variable=fletvar, onvalue=True)
slay = ttk.Checkbutton(frame, text="Slayer", variable=slayvar, onvalue=True)
hunt = ttk.Checkbutton(frame, text="Hunter", variable=huntvar, onvalue=True)
min = ttk.Checkbutton(frame, text="Mining", variable=minvar, onvalue=True)
smi = ttk.Checkbutton(frame, text="Smithing", variable=smivar, onvalue=True)
fish = ttk.Checkbutton(frame, text="Fishing", variable=fishvar, onvalue=True)
cook = ttk.Checkbutton(frame, text="Cooking", variable=cookvar, onvalue=True)
fire = ttk.Checkbutton(frame, text="Firemaking", variable=firevar, onvalue=True)
wood = ttk.Checkbutton(frame, text="Woodcutting", variable=woodvar, onvalue=True)
far = ttk.Checkbutton(frame, text="Farming", variable=farvar, onvalue=True)

achiev = ttk.Checkbutton(content, text="Include Achievement Diaries?", variable=ach_dia, onvalue=True)

rc.grid(column=0, row=0, sticky="w")
const.grid(column=0, row=1, sticky="w")
agi.grid(column=0, row=2, sticky="w")
herb.grid(column=0, row=3, sticky="w")
thie.grid(column=1, row=0, sticky="w")
craf.grid(column=1, row=1, sticky="w")
flet.grid(column=1, row=2, sticky="w")
slay.grid(column=1, row=3, sticky="w")
hunt.grid(column=2, row=0, sticky="w")
min.grid(column=2, row=1, sticky="w")
smi.grid(column=2, row=2, sticky="w")
fish.grid(column=2, row=3, sticky="w")
cook.grid(column=3, row=0, sticky="w")
fire.grid(column=3, row=1, sticky="w")
wood.grid(column=3, row=2, sticky="w")
far.grid(column=3, row=3, sticky="w")

achiev.grid(column=0, row=4, columnspan=3)

root.mainloop()


"""
okc = confirm(text='Welcome to the remastered version. This simple app was created by Gabriel Albornoz', title='Initio', buttons=['OK', 'Cancel'])
ach_dia = confirm(text='Do you want to include the Achievement Diaries into the image?', title='Achievement Diaries?', buttons=['Yes', 'No'])

if okc == 'OK':
    try:
        base_ss(ach_dia)
        
    except pyautogui.ImageNotFoundException:
        alert(text='Runelite not detected. Try again.', title='Warning', button='OK')
        exit      
else:
    exit
"""
