import os
import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

def extractFrames(vid):
    count = 0
    vidcap = cv2.VideoCapture(vid)
    success, frame = vidcap.read()
    while success:
        success, frame = vidcap.read()
        sys.stdout.write('Read a new frame: %s' % success)
        cv2.imwrite("pfs/out" + "/%#05d.jpg" % (count+1), frame)
        count = count + 1


for dirpath, dirs, files in os.walk('/pfs/videos'):
    for file in files:
        if os.stat(os.path.join(dirpath, file)).st_size > 0:
            extractFrames(os.path.join(dirpath, file))
