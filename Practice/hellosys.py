#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 12:03:53 2018

@author: elishatam
"""

import sys

def main():
    print 'Hello', sys.argv[1]
    # command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored
    
# Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
    main()