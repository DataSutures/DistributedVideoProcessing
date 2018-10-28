#!/bin/bash
pachctl stop-pipeline frames
pachctl delete-pipeline frames
pachctl create-repo frames
dir="./frames"
for file in $dir;
do 
	echo $file
	pachctl put-file frames master $file -f $file
done
pachctl list-file frames master
