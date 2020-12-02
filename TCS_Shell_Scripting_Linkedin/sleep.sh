#!/bin/bash
delay=0
if [ -z $1 ]
then
  read delay
else
  delay=$1
fi
echo Going to sleep for $delay seconds
sleep $delay
echo "Awake now!"
exit 0