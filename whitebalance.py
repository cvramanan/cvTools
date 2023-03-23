import cv2 as cv 
import numpy as np
import time

def white_balance(img):
    result = cv.cvtColor(img, cv.COLOR_BGR2LAB)
    avg_a = np.average(result[:, :, 1])
    avg_b = np.average(result[:, :, 2])
    result[:, :, 1] = result[:, :, 1] - ((avg_a - 128) * (result[:, :, 0] / 255.0) * 1.1)
    result[:, :, 2] = result[:, :, 2] - ((avg_b - 128) * (result[:, :, 0] / 255.0) * 1.1)
    result = cv.cvtColor(result, cv.COLOR_LAB2BGR)
    return result

referenceImage = cv.imread("./datainput/reference.jpg")
inputImage = cv.imread("./datainput/input.jpg")
t = time.time()
outputImageA = white_balance(inputImage)
outputImageB = white_balance(referenceImage)
print("Time taken: ", time.time() - t)
cv.imshow("Reference", referenceImage)
cv.imshow("Input", inputImage)
cv.imshow("OutputA", outputImageA)
cv.imshow("OutputB", outputImageB)
cv.waitKey(0)