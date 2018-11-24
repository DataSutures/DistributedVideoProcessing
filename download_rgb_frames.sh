#!/bin/bash
pachctl list-file colorize master > frames.txt
cat frames.txt | awk -F '\\.jpg' '{print $1".jpg"}' > frames1.txt
cat frames1.txt | sed '/^NAME/d' > frames2.txt
lines=$(cat frames2.txt)
for line in $lines;
do 
    pachctl get-file colorize master $line --output ./frames/douglas-macarthur-giving-speech/RGB/$line
done
ls ./frames
rm frames.txt
rm frames1.txt
rm frames2.txt