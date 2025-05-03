#!/bin/bash

# Check if a file path is provided
if [ "$#" -ne 1 ]; then
  echo "Usage: ./script.sh <path_to_input_file>"
  exit 1
fi

# Run the Python script with the provided file path
python3 ./scripts/main.py "$1"
