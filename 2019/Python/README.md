# AOC2019

My solutions for Advent of Code 2019

# Code Template

Run the following command in the root directory to generate a folder for day `number` containing two copies of `template.py` (one for each part of the question).  

    python make.py [number]
    
# CURL Command to Get Input File

Replace `session-cookie` and `day` in the command below to automatically pull the input file for the given day's problem.

    curl -v --cookie "session=[session-cookie]" https://adventofcode.com/2019/day/[day]/input > input.txt
