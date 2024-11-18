#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Download raw files
if ! command -v wget &> /dev/null; then
    echo "wget not found! Install it using 'brew install wget'"
    exit 1
fi

wget https://www.saifmohammad.com/WebDocs/stance-data-all-annotations.zip
unzip stance-data-all-annotations.zip
rm stance-data-all-annotations.zip

# Ensure required directories exist
if [ ! -d "data-all-annotations" ]; then
    echo "Downloaded data directory not found! Exiting."
    exit 1
fi

# Merge testA and testB
sed 1d data-all-annotations/testdata-taskB-all-annotations.txt > data-all-annotations/testdata-taskB-all-annotations-noheader.txt
cat data-all-annotations/testdata-taskA-all-annotations.txt data-all-annotations/testdata-taskB-all-annotations-noheader.txt > data-all-annotations/testdata-all-annotations.txt

# Merge training and trial
sed 1d data-all-annotations/trainingdata-all-annotations.txt > data-all-annotations/trainingdata-all-annotations-noheader.txt
cat data-all-annotations/trialdata-all-annotations.txt data-all-annotations/trainingdata-all-annotations-noheader.txt > data-all-annotations/traindata-all-annotations.txt

# Create directory with train/test/val files
mkdir data/semeval2016
mv data/data-all-annotations/testdata-all-annotations.txt data/semeval2016/test.tsv
mv data/data-all-annotations/traindata-all-annotations.txt data/semeval2016/train.tsv

# remove directory with raw files
rm -fr data/data-all-annotations
