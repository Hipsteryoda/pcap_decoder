#!/bin/bash

fullfile=${1}
filename=$(basename -- "$fullfile")
extension="${filename##*.}"
file="${filename%.*}"

# If the file exists
if [[ -e $1 ]]
    then
        # unzip pcap file
        unzip $fullfile

        # Decode pcap into text file
        echo "Decoding pcap into text file"
        tshark -V -r data/$file > ./pcaps/$file.txt

        # Run python decoder over file
        echo "Analyzing and graphing stuff"
        ./decoder.py $file.txt

        # Remove txt file
        echo "Cleanup time"
        # rm -rf ./data/* ./pcaps/$filename.txt
        
        echo "All set"

    else
        echo "File does not exist"

fi
