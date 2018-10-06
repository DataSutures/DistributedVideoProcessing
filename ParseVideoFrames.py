import os
import sys
import cv2
from matplotlib import pyplot as plt
def extractFrames(vid):
    tail = os.path.split(vid)[1]
    count = 0
    vidcap = cv2.VideoCapture(vid)
    success, frame = vidcap.read()
    success = True
    while success:
        success, frame = vidcap.read()
        sys.stdout.write('Read a new frame: %s' % success)
        plt.imsave(os.path.join("/pfs/frames", os.path.splitext(tail)[0]+'_'+str(count)+'.png'),frame, cmap = 'gray')
        count = count + 1


for dirpath, dirs, files in os.walk("/pfs/videos"):
    for file in files:
        extractFrames(os.path.join(dirpath, file))
