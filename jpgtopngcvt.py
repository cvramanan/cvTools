import os
import cv2
import random


folder = "./datainput/jpg2png/"
distDir = "./dataoutput/jpg2png/"
for i in os.listdir(folder):
    img = cv2.imread(folder+i)
    extension = i.split(".")[-1]
    i = i[:-len(extension)]
    print(distDir+i+"png")
    cv2.imwrite(distDir+i+"png",img)
    print(img.shape)
    