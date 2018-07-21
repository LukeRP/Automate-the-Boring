#! /usr/bin/env python3
'''
regex_search.py

This program will 1) take a string, 2) open every .txt file in a directory, 
3) perform a regex search to find all (if any) instances of that string 
in the files, and 4) print matches to the screen (terminal).
'''

import os, sys
import regex as re 

path_base = '/your_path_base_here' # e.g. /Users/LukeRP
target = '/your_path_target' # e.g. /Downloads
dirt = path_base + target
os.chdir(dirt)

# Compile the regex to search for:

check = re.compile(' \w*\'s ')   # Any characters with an 's at the end, e.g. " spider's "

# Open() every .txt file in a given folder, check, print, and close():

files = os.listdir(dirt)

for path in files:
    
    if os.path.splitext(path)[1] == '.txt':
        base = os.path.basename(path)
        txt_file = open(base)
        
        check_list = []
        the_lines = []
        
        for line in txt_file:
            the_lines.append(line)
        
        for item in the_lines:
            stuff = check.findall(item)
            for thing in stuff:
                check_list.append(thing)
                
        if len(check_list) > 0:
            print('\nMatches found in {}: \n'.format(base))
            
            for item in check_list:
                print('    ' + item + '\n')
        else:
            print('\nNo matches found in {}.\n\n'.format(base))
        
        txt_file.close()
