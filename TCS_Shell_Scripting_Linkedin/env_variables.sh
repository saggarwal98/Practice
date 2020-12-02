#!/bin/bash
echo path is $PATH
echo terminal is $TERM
if [ "$EDITOR" = "code" ]
then
  echo editor is $EDITOR
else
  echo editor not set
fi