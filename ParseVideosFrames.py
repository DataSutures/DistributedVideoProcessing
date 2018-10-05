# frames.py
import sys
import os
import cv2

def extractFrames(vid):
#    tail = os.path.split(vid)[1]
     count = 0
#    vidcap = cv2.VideoCapture(vid)
#    success,frame = vidcap.read()
#    success = True
 #   while success:
#      success,frame = vidcap.read()
 #     print ('Read a new frame: ', success)
  #    cv2.imwrite(os.path.normpath("/pfs/out" + os.path.splitext(tail)[0]+"frame%d.jpg" % #count), frame)
    count = count + 1
    h = open(“/pfs/out/hello.txt”, “w”) 
	fh.write(“Put the text you want to add here”) 
for dirpath, dirs, files in os.walk("/pfs/videos"):
	for file in files:
    extractFrames(os.path.join(dirpath,file))