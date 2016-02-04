#!/usr/bin/python3
#-*- coding: utf-8 -*-

__author__ = 'a2zh'

import os
import sys

def searchFiles(filename, root):
    return [f for x in os.walk(root) for f in x[2] if filename
            in f]

if(__name__ == '__main__'):
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        root = sys.argv[2]
        print('searching files contain: "', filename, '" in "', root, '"')
        print(searchFiles(filename, root))
    else:
        print('missing arguments')

