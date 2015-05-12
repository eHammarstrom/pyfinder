#!/usr/bin/env python

import argparse
import os
import glob
from collections import defaultdict

def main():
    p = argparse.ArgumentParser(description='Directory search')
    p.add_argument('--search', '-s', help='Enter x amount of file names', nargs='+')
    p.add_argument('--directory', '-d', '-dir', help='Enter a directory name', nargs=1)
    args = p.parse_args()
    finePrint(search(args.search, args.directory))

def search(s_args, s_dir):
    hits = defaultdict(list)
    os.chdir(s_dir[0])
    for file in glob.glob("*.py"):
        with open(file) as f:
            contents = f.read()
        for s_arg in s_args:
            if s_arg in contents:
                hits[s_arg].append(file)
    return hits

def finePrint(toPrint):
    count = 0
    for k,v in toPrint.items():
        print(k + "  -->  " + "<{0}>".format(">, <".join(v)))


if __name__ == '__main__':
    main()
