#!/bin/bash
pachctl stop-pipeline frames
pachctl delete-pipeline frames
pachctl create-repo frames
dir="./frames"
for file in $dir;
do 
	pachctl put-file frames master $file -f $file
done
pachctl list-file frames master
commitID=$(pachctl start-commit frames master)
pachctl delete-file frames $commitID frames
pachctl finish-commit frames $commitID