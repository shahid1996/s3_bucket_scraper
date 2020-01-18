#!/usr/bin/env python
#on my computer, "python" means python3
#you might need to change to python3 instead

import sys

def main():
    #variables for the request
    number_of_args = 0
    max_keys = 1000
    bucket = ""
    final_url = ""

    #getting command line arguments    
    if (len(sys.argv) == 2):
        number_of_args = 2
        print("2 args means you only specified the bucket and not the max-keys")
        bucket = sys.argv[1]
        print("bucket: " + bucket)
    elif (len(sys.argv) == 3):
        number_of_args = 3
        print("specified both the domain and max-keys")
        bucket = sys.argv[1]
        max_keys = sys.argv[2]
        print("bucket: " + bucket)
        print("max_keys: " + max_keys)
    else:
        print("Error: invalid number of command line arguments.")
        print("There are 2 ways to use this program:")
        print("1. bucket_scraper.py example.s3.amazonaws.com 1234")
        print("2. bucket_scraper.py example.s3.amazonaws.com")
        print("Args are the S3 bucket and optional max-keys value.")
        exit(1)
    

    


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nQuitting. Goodbye.")
        sys.exit()