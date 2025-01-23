#!/bin/sh

# Check if python3 is installed, and install if not
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found, installing..."
    apt-get update && apt-get install -y python3
fi

# Run your Python script or whatever command you need
python3 add.py config.ini
