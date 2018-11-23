#!/bin/bash
cd /Users/kimberlysmith/Documents/SeniorProject/VideoFrameParser
pachctl create-repo videos
pachctl create-pipeline -f frames.json 
cd /Users/kimberlysmith/Documents/SeniorProject/FrameColorizer
pachctl create-pipeline -f colorize.json 
cd /Users/kimberlysmith/Documents/SeniorProject/VideoFrameParser
pachctl create-pipeline -f framesToVideo.json 
cd /Users/kimberlysmith/Documents/SeniorProject/VideoFrameParser