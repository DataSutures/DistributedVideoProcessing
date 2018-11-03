#!/bin/bash
cd /Users/kimberlysmith/Documents/SeniorProject/VideoFrameParser
pachctl create-repo videos
pachctl create-pipeline -f frames.json 
pachctl put-file videos master AfterheavyrainHelsinki1948.mp4 -f ./vids/AfterheavyrainHelsinki1948.mp4
pachctl list-file videos master
pachctl create-pipeline -f frames.json
cd /Users/kimberlysmith/Documents/SeniorProject/FrameColorizer