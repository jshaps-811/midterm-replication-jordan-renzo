#!/bin/bash

# Define the directory to process
directory="../midterm-replication-jordan-renzo/configs/english" 

# Check if the directory exists
if [ ! -d "$directory" ]; then
  echo "Error: Directory '$directory' not found."
  exit 1
fi

# Loop through each file in the specified directory
for file in "$directory"/*; do
  # Check if it's a regular file (not a directory)
  if [ -f "$file" ]; then
    echo "Processing file: $file"
    # Replace the following line with the command or script you want to run on each file
    # Example: run a custom script on the file
    
    
    # Example: print the content of the file
    python ../NLPScholar/main.py $file
  fi
done

echo "Finished processing files in '$directory'."