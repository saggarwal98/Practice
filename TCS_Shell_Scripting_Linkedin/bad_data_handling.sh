#!/bin/bash
VALID=0
while [ $VALID -ne 1 ]
do
  read -p "enter name and age: " NAME AGE
  if [[ (-z $NAME)  || (-z $AGE ) ]]
  then
    echo "Not enough parameters passed"
    continue
  elif [[ ! $NAME =~ ^[A-Za-z]+$ ]]
  then
    echo "Non alpha numberic characters enetered in name:[$NAME]"
    continue
  elif [[ ! $AGE =~ ^[0-9]+$ ]]
  then
    echo "Non digits entered in age:[$AGE]"
    continue
  fi
  VALID=1
done
echo "Name:$NAME Age:$AGE"