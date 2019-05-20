# Importing modules
import cv2
import os
import json
import imageio
from tkinter import *
import tkinter as tk
from tkinter import filedialog

def detectFaces(img_path, display = False):
    try:
        if img_path.lower().endswith(('.jpeg', '.jpg')):
            color_img = cv2.imread(img_path)
        elif img_path.lower().endswith('.png'):
            color_img = cv2.imread(img_path)
        elif img_path.lower().endswith('.gif'):
            color_img = imageio.mimread(img_path)[0] # Take 1st frame of GIF images
            color_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB)
    except Exception as e:
        raise e

    # To Scale image fit within(1280x720)
    h = color_img.shape[0] # measure the height
    w = color_img.shape[1] # measure the width
    print(h)
    print(w)
    

    



def main():
    # Opening the file
    root = Tk()
    root.withdraw()
    img_path = filedialog.askopenfilename(initialdir = './photos', title = 'Choose an Image to Analyze', filetypes = (('JPEG','*.jpg;*.jpeg'), ('GIF','*.gif'), ('PNG','*.png'), ('all files','*.*')))
    detectFaces(img_path, display = True)


if __name__ == "__main__":
    main()