#!/usr/bin/env python
#on my computer, "python" means python3
#you might need to change to python3 instead

import sys
import requests

#file-writing function
#can be used for writing a string or response
#example response usage:
#safe_write("results.xml", response.text)
def safe_write(filename, data):
    try:
        write_file = open(filename, "w")
        write_file.write(data)
        write_file.close()
    except IOError as e:
        print("IO exception when writing to " + filename + ":")
        print(e.args)
        sys.exit(1)

#main function
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
        print("1. bucket_scraper.py example.com/s3 1234")
        print("2. bucket_scraper.py example.com/s3")
        print("Do not put a slash at the end, as it could cause problems.")
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
    response = ""
    #checking if there were problems with downloading the file
    try:
        response = requests.get(final_url, headers=headers)
    except requests.RequestException as e:
        print("Request exception:")
        print(e.args)
        sys.exit(1)
    status = response.status_code
    #HTTP 200 means OK
    if (status != 200):
        print("Error code: " + status)
        sys.exit(1)
    elif (response == ""):
        print("Response error")
        sys.exit(1)
    else:
        #proceeding with the program
        print("Response to HTTP request was good")

        #writing the file to results.xml
        safe_write("results.xml", response.text)
        print("successfully wrote results.xml")

        #make a note of the bucket in bucket.txt
        safe_write("bucket.txt", bucket)
        
        print("Wrote to bucket file (keeps track for key_downloader)")



    


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nQuitting. Goodbye.")
        sys.exit()