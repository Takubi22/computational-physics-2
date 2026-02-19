#!/opt/anaconda3/envs/py311/bin/python3

import sys

inputfolder  = sys.argv[1]
outputfolder = sys.argv[2]

print('Input folder is: ' + inputfolder, 'Output folder is: ' + outputfolder)

print('Now provide number please:')

inputnumber = input()

print('Thanks, the number provided is: ' + inputnumber)
