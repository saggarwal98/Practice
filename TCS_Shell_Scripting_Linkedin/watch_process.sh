#!/bin/bash
STATUS=0
if [ -z $1 ]
then
  echo "Enter a process id"
  exit 1
fi
echo Watching process with pid $1
while [ $STATUS -eq 0 ]
do
  ps $1>/dev/null
  STATUS=$?
done
echo "Process with process id $1 has terminated"
exit 0