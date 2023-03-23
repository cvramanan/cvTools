import cv2
from cv2 import VideoCapture
import numpy as np
import time

INPUT_FILENAME = './datainput/boxes2.mp4'
OUTPUT_DIR = './dataoutput/'
cam = VideoCapture(INPUT_FILENAME)
i = 0
while cam.isOpened():
    ret_val, img = cam.read()
    if not ret_val:
        break
    # cv2.imshow('img', img)
    if(i % 10 == 0):
        cv2.imwrite(OUTPUT_DIR + 'frame%d.jpg' % i, img)
    i += 1
    if cv2.waitKey(1) == 27:
        break
