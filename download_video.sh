#!/bin/bash
pachctl list-file videoWriter master > out.txt
cat out.txt | awk -F '\\.jpg' '{print $1".jpg"}' > out1.txt
cat out1.txt | sed '/^NAME/d' > out2.txt
lines=$(cat out2.txt)
for line in $lines;
do 
    pachctl get-file videoWriter master $line --output ./out/$line
done
ls ./out
rm out.txt
rm out1.txt
rm out2.txt