import os
import sys
import cv2
from matplotlib import pyplot as plt

def extractFrames(vid):
    vidcap = cv2.VideoCapture(vid)
    success, frame = vidcap.read()
    if success:
        success, frame = vidcap.read()
        tail = os.path.split(vid)[1]
        sys.stdout.write('\nRead a new frame: %s' % success)
        plt.imsave(os.path.join("/pfs/out", os.path.splitext(tail)[0]+'_'+str(count)+'.png'),frame, cmap = 'gray')


for dirpath, dirs, files in os.walk("/pfs/videos"):
    for file in files:
        extractFrames(os.path.join(dirpath, file))
