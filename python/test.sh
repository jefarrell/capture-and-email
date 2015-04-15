#!/bin/sh
SERVICE='Breach'
 
if ps ax | grep -v grep | grep $SERVICE > /dev/null
then
    echo "$SERVICE service running, everything is fine"
    #import -window root $HOME/Users/johnfarrell/Desktop/filename.png
    echo $(python captureUpload.py) 
else
    echo "$SERVICE is not running!" 
fi





# set CHECK = ps ax | grep -v grep | grep $SERVICE > /dev/null
# while [ "$CHECK" == true ];
# do
# echo "$SERVICE service running, everything is fine"
# done