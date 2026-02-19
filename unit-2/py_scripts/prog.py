#!/opt/anaconda3/envs/py311/bin/python3
# Import parsing library
import argparse

# Creating the parsing object
parser = argparse.ArgumentParser(description='Process some integers.')

# Multiple arguments
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')

# Creating the arguments object
args = parser.parse_args()

print(args.accumulate(args.integers))
