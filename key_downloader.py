#!/usr/bin/env python
#on my computer, "python" means python3
#you might need to change to python3 instead

import sys
import os
import xml.etree.ElementTree as et
import requests

def safe_write_binary(filename, data):
    try:
        write_file = open(filename, "wb")
        write_file.write(data)
        write_file.close()
    except IOError as e:
        print("IO exception when writing to " + filename + ":")
        print(e.args)
        sys.exit(1)

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
    tree = et.parse("results.xml")
    root = tree.getroot()
    for node in root:
        contents = "{http://s3.amazonaws.com/doc/2006-03-01/}Contents"
        if (node.tag == contents):
            #getting the filenames from the <key> elements in results.xml
            file_url = node[0].text
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            #aaaaaaaaaaaaaaaa
            response = ""
            #turning the file name into the full url
            #opening the bucket file
            bucket_file = open("bucket.txt", "r")
            bucket = bucket_file.read()
            full_url = "https://" + bucket + "/" + file_url
            print(full_url)
            #checking if there were problems with downloading the file
            try:
                response = requests.get(full_url, headers=headers)
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
                print("File was downloaded successfully")
                file_path = "key_downloads/" + file_url
                safe_write_binary(file_path, response.content)
            #aaaaaaaaaaaaaaaaaaaaaaaaa
            

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nQuitting. Goodbye.")
        sys.exit()