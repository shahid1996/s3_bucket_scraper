#!/usr/bin/env python
#on my computer, "python" means python3
#you might need to change to python3 instead

import sys
import os
import xml.etree.ElementTree as et 

def fileIsNotEmpty(filename):
    return os.stat(filename).st_size != 0

def main():
    #check if results.xml and/or bucket.txt are blank
    bucket_not_empty = fileIsNotEmpty("bucket.txt")
    results_not_empty = fileIsNotEmpty("results.xml")
    if (bucket_not_empty and results_not_empty):
        print("results.xml and bucket.txt passed preliminary check")
    else:
        print("Error: did you forget to run bucket_scraper.py first?")
        sys.exit(1)
    #proceed with program
    #parse XML


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nQuitting. Goodbye.")
        sys.exit()