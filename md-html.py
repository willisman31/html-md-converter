# mdhtml.py
# Converts Markdown language into HTML

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", type=string, help="enter input file name with relative path", nargs='?', default=0, const=0)
parser.add_argument("--output", type=string, help="enter the desired output file name without an extension", nargs='?', default='output')
args = parser.parse_args()




