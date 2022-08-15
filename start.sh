#!/bin/bash

is_running=$(ps -ef | grep '/usr/bin/flask' | grep -v 'grep' | wc -l | cut -d" " -f1)
if [[ "$is_running" != "0" ]]
then
    exit 0 
fi
echo "Restart flask"
cd /home/yokesan/dev/operation_management
flask run --host=0.0.0.0


