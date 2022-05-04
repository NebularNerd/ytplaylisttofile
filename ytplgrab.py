# Download YT Playlist to plain text file
# Author: NebularNerd Version 1.0 (2022)
# https://github.com/NebularNerd/ytplaylisttofile
# Install required packages
import sys
import os
import re
import argparse
# ---- Make some nice args
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,description='Strip YT video links from html to new file\nVisit https://github.com/NebularNerd/ytplaylisttofile for more information')                                               
parser.add_argument("--infile", "-i", type=str, required=True, help='Path to input raw html from YT Playlist page')
parser.add_argument("--outfile", "-o", type=str, required=True, help='Path to output processed file')                                             
args = parser.parse_args()
# ---- Now we can do stuff
print('\nYT Playlist to text file') 
print('Using file: ' + args.infile)
# ---- Lets find those vids
textfile = open(args.infile, 'r', encoding="utf8")
filetext = textfile.read()
textfile.close()
matches = re.findall("\/watch\?v=(.*?\&)", filetext)
howmany_a = len(re.findall("\/watch\?v=(.*?\&)", filetext))
# ---- Remove duplicates
matches = list( dict.fromkeys(matches) )
howmany_b = len(matches)
print("We found " + str(howmany_a) + " matches")
print("We have " + str(howmany_b) + " matches after removing duplicates\n")
# ---- List and write images from matches
print('Links found\n')
groupnum = 0
for x in range(howmany_b):
    matchstring=str(matches[groupnum])
    matchstringa="https://www.youtube.com/watch?v="+matchstring[:-1]
    print(matchstringa)
    with open(args.outfile, 'a', encoding='utf-8') as f:
        writeme = matchstringa + '\n'
        f. writelines(writeme)
    groupnum = groupnum+1
f.close()









