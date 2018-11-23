#!/bin/bash
cd /Users/kimberlysmith/Documents/SeniorProject/VideoFrameParser
pachctl create-repo videos
pachctl create-pipeline -f frames.json 
pachctl put-file videos master 044605935-american-protesters-relaxing-e.mp4 -f ./vids/044605935-american-protesters-relaxing-e.mp4
pachctl list-file videos master
cd /Users/kimberlysmith/Documents/SeniorProject/FrameColorizer