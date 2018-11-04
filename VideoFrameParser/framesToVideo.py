import os
import sys
import cv2
import argparse

# Define input args
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-out","--output",required=False, default='/pfs/out/', help="default output path is pachyderm file system ./pfs/out.")
    parser.add_argument("-in","--input",required=False, default='/pfs/colorize', help="default input path is pachyderm file system ./pfs/colorize.")
    parser.add_argument("-fps", required=False, default='20', help="Default is 20 frames per second.")
    args = vars(parser.parse_args())
    return args
    

# Parse input args
args = parse_args()
inPath = args['input']
outPath = args['output']
fps = args['fps']

# Determine width and Height of first image
image = os.listdir(inPath)[0]
image_path = os.path.join(inPath, image)
if os.stat(image_path).st_size > 0:
    frame = cv2.imread(image_path)
    height, width, channels = frame.shape
    
# Set up Video Writer
filename = os.path.splitext(image)[0]
fourcc = cv2.VideoWriter_fourcc(*'FMP4')
writer = cv2.VideoWriter(outPath+filename+'.mp4', fourcc, 20.0, (width, height))


# Read and write images to video
for image in sorted(os.listdir(inPath)):
    image_path = os.path.join(inPath, image)
    if os.stat(image_path).st_size > 0:
        frame = cv2.imread(image_path)
        writer.write(frame)
        
# Release everything if job is finished
writer.release()
cv2.destroyAllWindows()