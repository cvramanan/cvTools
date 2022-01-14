import cv2
from cv2 import VideoCapture
import numpy as np


FILENAME = ''

cam = VideoCapture(FILENAME)

while cam.isOpen():
    ret_val, img = cam.read()
    if not ret_val:
        break
    cv2.imshow('img', img)
    if cv2.waitKey(1) == 27:
        break
