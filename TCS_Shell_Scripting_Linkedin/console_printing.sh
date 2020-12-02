#!/bin/bash
read COUNT
start=1
while [ $COUNT -ge $start ]
do
  echo COUNT=$start
  one=1
  start=$(($start+$one))
done
echo "Loop Finished"