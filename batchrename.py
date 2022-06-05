from distutils import extension
import os
import shutil

inputDir = "/home/venkataramananc/Downloads/-1/empty/"
outputDir = "/home/venkataramananc/Downloads/-1/empty/"
cnt = 21100

for i in os.listdir(inputDir):
    extension = i.split(".")[-1]
    filenameNew = str(cnt)+"."+extension
    shutil.move(inputDir + i, outputDir + filenameNew)
    cnt += 1