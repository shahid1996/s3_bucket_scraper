#!/usr/bin/env python
#on my computer, "python" means python3
#you might need to change to python3 instead

import sys

def main():
    if (len(sys.argv) != 3):
        print("Error: invalid number of command line args")
        print("Use it like this: bucket_scraper.py example.com 1234")
        print("First arg you provide to it is the S3 bucket.\nAnd the second is the max-keys value.")
        exit(1)

    print(sys.argv[1])
    print(sys.argv[2])


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nQuitting. Goodbye.")
        sys.exit()