#!/bin/bash
pachctl list-file frames master > frames.txt
cat frames.txt | awk -F '\\.jpg' '{print $1".jpg"}' > frames1.txt
cat frames1.txt | sed '/^NAME/d' > frames2.txt
lines=$(cat frames2.txt)
for line in $lines;
do 
    pachctl get-file frames master $line --output ./frames/american-protesters-cheering/BW/$line
done
ls ./frames
rm frames.txt
rm frames1.txt
rm frames2.txt