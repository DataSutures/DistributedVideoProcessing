import os
import sys
import cv2

def extractFrames(vid):
    count = 0
    vidcap = cv2.VideoCapture(vid)
    success, frame = vidcap.read()
    while success:
        success, frame = vidcap.read()
        sys.stdout.write('Read a new frame: %s' % success)
        cv2.imwrite(os.path.join('/pfs/out', '/'+str(count)+'.png'), frame)
        count = count + 1


for dirpath, dirs, files in os.walk('/pfs/videos'):
    for file in files:
        extractFrames(os.path.join(dirpath, file))
