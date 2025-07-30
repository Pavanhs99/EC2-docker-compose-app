#!/bin/bash

timestamp=$(date "+%Y-%m-%d %H:%M:%S")

echo "$timestamp | system_info.sh: wrote to message.txt" >> /data/system_info.log

echo "$timestamp | flask: read message.txt and displayed it in http://13.201.190.160:5000" >> /data/system_info.log

