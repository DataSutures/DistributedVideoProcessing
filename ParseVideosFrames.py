import sys
import argparse
import os
import cv2
print(cv2.__version__)

def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
      success,image = vidcap.read()
      print ('Read a new frame: ', success)
      cv2.imwrite(os.path.normpath(pathOut + "/frame%d.jpg" % count), image)
      count = count + 1

if __name__=="__main__":
    print("aba")
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--pathOut", help="path to images")
    args = a.parse_args()
    print(args)
    extractImages(args.pathIn, args.pathOut)