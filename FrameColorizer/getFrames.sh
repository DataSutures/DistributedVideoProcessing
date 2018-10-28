#!/bin/bash
mkdir frames
pachctl list-file frames master > frames.txt
cat frames.txt | awk -F '\\.jpg' '{print $1".jpg"}' > frames2.txt
cat frames2.txt | sed '/^NAME/d' > frames3.txt
cat frames3.txt | awk '200<=NR && NR <=306' > frames4.txt
lines=$(cat frames4.txt)
for line in $lines;
do 
    pachctl get-file frames master $line --output ./frames/$line
done
rm frames.txt frames2.txt frames3.txt
ls ./frames