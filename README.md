# S3 Bucket Scraper
A tool for scraping S3 buckets on AWS. 

Proof of concept security tool. 

Don't use it for buckets you're not allowed to access!

## Dependencies

- Python 3
- requests module for Python (pip install requests)

## How to use it

There are two programs: one is the one that scrapes S3 bucket XML, and the other will download files in keys, such as if there's a bucket for uploads.

This tool will not help you find S3 buckets. You need to do that yourself.

## Quick start guide

**To use this program, run bucket_scraper.py, then run key_downloader.py.**

Example usage:

Clone or download the repo, then cd to the repo directory, then use the following commands:

Step 1:
```
./bucket_scraper.py example.com/s3 123
```
Step 2:
```
./key_downloader.py
```
And that's it! Then check key_downloads for the results.

If you want to delete files that were downloaded, use this:
```
./reset.sh
```

## More in-depth stuff

There are 2 program files in this project:

```
bucket_scraper.py
key_downloader.py
```

There is also an optional shell script:

```
reset.sh
```

However, reset.sh was more important for me when I was writing this program, and it might be less useful to people who are using it. It gets rid of any data stuff you've downloaded after using this program. This was useful for me when I was committing to the repo. 

Data-related files and folders:

```
bucket.txt
results.xml
key_downloads/
```

There will be a file called results.xml, which is the result of running bucket_scraper.py. If you want to run it multiple times, you will have to rename results.xml to something else, as the results will be overwritten each time.

bucket.txt is a file that contains the bucket you used to download the XML. You don't have to edit it. bucket_scraper.py will fill it out automatically.

There is also a directory called key_downloads, which is the result of downloading files specified in \<key> tags in the S3 XML.

**key_downloader.py assumes that there are files with relative paths in the \<key>s in the XML, i.e. a \<key> of image.jpg means it will be available at example.s3.amazonaws.com/image.jpg, which is the S3 bucket you specified.**

bucket_scraper.py will scrape XML of an S3 bucket.

Here's how you use it:

```
bucket_scraper.py example.s3.amazonaws.com 123
```

In the above example, example.s3.amazonaws.com is the location of the AWS S3 bucket, and 123 is the number of keys to scrape, called max-keys. If you want to get everything, you could do this:

```
bucket_scraper.py example.s3.amazonaws.com 2147483647
```

However, I've never tried that many (if you specify the signed 32-bit int max, there might be millions of S3 objects, though it will only download the XML if it exists, i.e. an S3 bucket with 1,000 items will still only have 1,000 items if you specify 100 million for max-keys), and there might be performance issues that way. The default is 1000, but you can use other amounts (usually).

I haven't tried it with massive amounts of S3 objects in a single bucket, so who knows.

You can also just use it by specifying the bucket and nothing else, like so:

```
bucket_scraper.py example.s3.amazonaws.com
```

In the above example, the max-keys value will be the default of 1000.

key_downloader.py will download the files that are mentioned in the \<key>s in the results.xml file.

So basically, bucket_scraper.py is for downloading a list of files, and key_downloader.py downloads the files that are in the list.



