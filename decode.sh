#!/bin/bash

fullfile=${1}
filename=$(basename -- "$fullfile")
extension="${filename##*.}"
filename="${filename%.*}"

# If the file exists
if [[ -e $1 ]]
then
    # unzip pcap file
    unzip $fullfile

    # Decode pcap into text file
    tshark -V -r data/$filename > ./pcaps/$filename.txt

    # # Run python decoder over file
    # ./decoder.py $filename.txt

    # # Remove txt file
    # rm $filename.txt

else
    echo "File does not exist"

fi
