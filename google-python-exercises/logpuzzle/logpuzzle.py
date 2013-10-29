#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  fh=open(filename,'r')
  s=fh.read()
  urls=re.findall('GET\s(\S+.jpg)\sHTTP',s)
  return urls
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  if not (os.path.exists(dest_dir)):
    print dest_dir,"does not exist. The downloads will be in the current directory."
    dest_dir="."
  index_file=open(dest_dir+"/index.html","w")
  index_file.write("<verbatim>"+"\n")
  index_file.write("<html>"+"\n")
  index_file.write("<body>"+"\n")
  for url in img_urls:
      dest_file=url.split("/")[-1]
      index_file.write("<img src=\""+dest_file+"\">")
      print "input file:",url,"saving to",dest_dir+'/'+dest_file
      urllib.urlretrieve(url,dest_dir+'/'+dest_file)
  index_file.write("\n")
  index_file.write("</body>"+"\n")
  index_file.write("</html>"+"\n")
  index_file.close()

  # +++your code here+++
  
def get_last(s):
    if s.split("/")[-1].count("-") > 1:
       return s.split("/")[-1].split("-")[2]
    return s.split("/")[-1]

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])
  filename=args[0]
  purge_list=[]
  for item in img_urls:
     if not item in purge_list:
        purge_list.append(item)
  purge_list=sorted(purge_list,key=get_last)
  servername=filename.split("_")[-1]
  for item in range(0,len(purge_list)):
      purge_list[item]="http://"+servername+purge_list[item]
  img_urls=purge_list
  del purge_list
  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
