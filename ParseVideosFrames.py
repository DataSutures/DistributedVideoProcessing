# frames.py
import sys
import os
import cv2

def extractFrames(vid):
    count = 0
    vidcap = cv2.VideoCapture(vid)
    success,frame = vidcap.read()
    success = True
    while success:
      success,frame = vidcap.read()
      print ('Read a new frame: ', success)
      cv2.imwrite(os.path.normpath("/pfs/out" + "/frame%d.jpg" % count), frame)
      count = count + 1

for dirpath, dirs, files in os.walk("/pfs/videos"):
	for file in files:
    extractFrames(os.path.join(dirpath,file))