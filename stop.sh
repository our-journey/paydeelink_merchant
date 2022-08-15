#!/bin/bash

line=$(ps -ef | grep '/usr/bin/flask' | grep -v 'grep')
if [[ "$line" != "" ]]
then
    pid=${line:9:7}
    echo "Stop:[$pid]"
    kill -9 "$pid"
fi



