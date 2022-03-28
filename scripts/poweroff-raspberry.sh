#!/bin/bash

IP="192.168.1.8"

ping -c 1 -w 1 $IP > /dev/null

if [ $? -eq 0 ]; then
    ssh -i $HOME/.ssh/id_rsa wittano@$IP "sudo poweroff"
fi