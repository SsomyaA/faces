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

    if (w/h) > (1280/720): # Scale based on the width
        color_img = cv2.resize(color_img, (1280, int(h*1280/w)))
    else: # Scale based on the height
        color_img = cv2.resize(color_img, (int(w*720/h), 720))
    
    # Convert the colored image to black and white image to compatible with opencv
    
    gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY).copy()

    # Load haar cascade and detect faces
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
    faces = cascade.detectMultiScale(gray_img)
    print(f'Found {len(faces)} faces in {os.path.basename(img_path)} image')

    # To draw rectangle on facees
    if display:
        for (x, y, w, h) in faces:
            cv2.rectangle(color_img, (x, y), (x+w, y+h), (0, 255,0), 3)

        # Display the image with OpenCV
        cv2.startWindowThread()
        cv2.imshow('Facial Detecction', color_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        

    return json.dumps({'countFaces': len(faces), 'imageLocation': img_path})


def main():
    # Opening the file
    root = Tk()
    root.withdraw()
    img_path = filedialog.askopenfilename(initialdir = './photos', title = 'Choose an Image to Analyze', filetypes = (('JPEG','*.jpg;*.jpeg'), ('GIF','*.gif'), ('PNG','*.png'), ('all files','*.*')))
    output = detectFaces(img_path, display = True)
    json_path = '.'.join(img_path.split('.')[:-1]) + '.json'
    x = input("Do you want to save the output {} 'Yes/No'")
    if x.lower() in ('y', 'ye', 'yes'):
        f = open(json_path, 'w')
        f.write(output)
        f.close()
        print('Result has been saved')
        print(json_path)


if __name__ == "__main__":
    main()