#!/bin/bash

# Create data folder if it doesn't exist
mkdir -p data

# Download CSV files with --no-check-certificate option
wget --no-check-certificate -P data https://ochem.eu/documents/tox24_train.csv
wget --no-check-certificate -P data https://ochem.eu/documents/tox24_test.csv
wget --no-check-certificate -P data https://ochem.eu/documents/tox24_all.csv