import os
import sys
import cv2

def extractFrames(vid):
    count = 0
    vidcap = cv2.VideoCapture(vid)
    success, frame = vidcap.read()
    success = True
    while success:
        success, frame = vidcap.read()
        sys.stdout.write('Read a new frame: %s' % success)
        cv2.imwrite(os.path.normpath("/pfs/frames" + "/frame%d.jpg " % count), frame)
        count = count + 1


for dirpath, dirs, files in os.walk("/pfs/vids"):
    for file in files:
        extractFrames(os.path.join(dirpath, file))
