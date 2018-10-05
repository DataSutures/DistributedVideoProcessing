import os
import sys
import cv2

def extractFrames(vid):
    tail = os.path.split(vid)[1]
    count = 0
    vidcap = cv2.VideoCapture(vid)
    success, frame = vidcap.read()
    success = True
    while success:
        success, frame = vidcap.read()
        sys.stdout.write('Read a new frame: %s' % success)
        cv2.imwrite(os.path.join("/pfs/out", os.path.splitext(tail)[0]+str(count)+'.jpg'), frame)
        count = count + 1


for dirpath, dirs, files in os.walk("/pfs/vids"):
    for file in files:
        extractFrames(os.path.join(dirpath, file))
