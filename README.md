# Anti-Duplicator

This script will help you to find duplicates in your file storage. 
It finds files with both same name and size and show it with ways.

# How to Install

Python 3 should be already installed.

# Quickstart

For start script you need to run the script in console/terminal.
Required parameter is the full way to the folder, where you want to find duplicate files.

Example:
```bash
$ python duplicates.py /Users/ExampleUser/
```

# Output example:
```
Collecting files from the folder...
Counting files sizes...
Duplicate finding...
There is some duplicated files: 
File "file1.txt" with size 5440 bytes.
Paths:
/Users/ExampleUser/file1.txt
/Users/ExampleUser/exampleDirectory/file1.txt
--------------
```

# Project Goals

The code is written for educational purposes. 
Training course for web-developers - [DEVMAN.org](https://devman.org)
