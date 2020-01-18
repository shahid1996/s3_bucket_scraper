#!/usr/bin/env python
#on my computer, "python" means python3
#you might need to change to python3 instead

import sys
import requests

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
    elif (len(sys.argv) == 3):
        number_of_args = 3
        print("specified both the domain and max-keys")
        bucket = sys.argv[1]
        max_keys = sys.argv[2]
    else:
        print("Error: invalid number of command line arguments.")
        print("There are 2 ways to use this program:")
        print("1. bucket_scraper.py example.com/s3/ 1234")
        print("2. bucket_scraper.py example.com/s3/")
        print("Args are the S3 bucket and optional max-keys value.")
        exit(1)
    #proceed with building URL
    print("bucket: " + bucket)
    print("max_keys: " + max_keys)
    #assumes HTTPS, but you might want to change this to HTTP instead
    final_url = "https://" + bucket + "?max-keys=" + str(max_keys)
    print(final_url)
    #download XML to results.xml
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    response = requests.get(final_url, headers=headers)
    print(response.content)

    


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nQuitting. Goodbye.")
        sys.exit()