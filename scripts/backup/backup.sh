#!/bin/bash

if [ -z "$(command -v rsync)" ]; then
    echo "rsync not found";
    exit -1
fi

BACKUP_DIR=/mnt/backup

if [ ! -d $BACKUP_DIR ]; then
    sudo mkdir -p $BACKUP_DIR
    sudo chown $(whoami) $BACKUP_DIR
fi

CURRENT_DIR=$(dirname $0)

rsync -aAXv --delete --exclude-from="${CURRENT_DIR}/exclude.txt" $HOME /mnt/backup