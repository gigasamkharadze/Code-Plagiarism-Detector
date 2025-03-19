#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <repository-url> <destination-directory>"
    exit 1
fi

REPO_URL=$1
DEST_DIR=$2

if [ -d "$DEST_DIR/.git" ] && git -C "$DEST_DIR" rev-parse --is-inside-work-tree > /dev/null 2>&1; then
    echo "Repository is already cloned in $DEST_DIR"
    exit 0
fi

if git clone "$REPO_URL" "$DEST_DIR" > /dev/null 2>&1; then
    echo "Repository cloned successfully in $DEST_DIR"
else
    exit 1
fi
