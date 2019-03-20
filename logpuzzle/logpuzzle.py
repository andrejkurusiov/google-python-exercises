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


def path_exists(dir):
  """ Returns 1 is given path doesn't exist; otherwise 0. """
  if os.path.exists(dir): return 1
  else: return 0

""" def sortedFn(s):
  # sorts strings like 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-babf.jpg' by file name
  return re.search(r'\w*-\w*.jpg$', os.path.basename(s)).group(0) """

""" def wget(url):
  # Tries reading given URL, if it works and of 'text/html' type, returns base url
  try:
    ufile = urllib.urlopen(url)
    if ufile.info().gettype() == 'text/html':
      return ufile.geturl()
    else:
      return 'url ' + url + ' is not text/html type.'
  except IOError:
    return 'problem reading url: ' + url """

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  result = []
  if not path_exists(filename):
    print 'Path ' + filename + ' doesn\'t exist!'
    sys.exit(1)
  
  # get base url from the filename
  match = re.search(r'\S*_(\S*)', filename)
  host = 'http://' + match.group(1)
  """   try:
    ufile = urllib.urlopen('http://' + match.group(1))
    print ufile.geturl()
  except IOError:
    print 'error retrieving ' + match.group(1) """
  
  # read file for urls
  file = open(filename, 'rU')
  for line in file:
    match = re.search(r'\S*puzzle\S*', line)
    if match:
      result.append(host + match.group())
  file.close()
  # sort the list and remove duplicates (-> set)
  #return sorted(set(result), key=sortedFn)
  return sorted(set(result))


def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  #print wget(args[0])
  #sys.exit(0)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
