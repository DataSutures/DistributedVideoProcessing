#!/bin/bash
/Users/kimberlysmith/Documents/SeniorProject/FrameColorizer
rm -r frames
mkdir frames
pachctl list-file frames master > frames.txt
cat frames.txt | awk -F '\\.jpg' '{print $1".jpg"}' > frames2.txt
cat frames2.txt | sed '/^NAME/d' > frames3.txt
cat frames3.txt | awk '610<=NR && NR <=619' > frames4.txt
lines=$(cat frames4.txt)
for line in $lines;
do 
    pachctl get-file frames master $line --output ./frames/$line
done
ls ./frames
pachctl stop-pipeline frames
pachctl delete-pipeline frames
pachctl create-repo frames

lines=$(ls ./frames)
for line in $lines;
do 
    pachctl put-file frames master $line -f ./frames/$line
done
