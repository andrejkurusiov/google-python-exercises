#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

# returns a list of the absolute paths of the special files in the given directory
def get_special_paths(dir):
  abspathlist = []  # all files' absolute paths' list
  filenames = os.listdir(dir)
  for filex in filenames:
    # check if special --> to list
    filename_special = re.search(r'\w*__\w+__.*', filex)
    if filename_special:
      abspathlist.append(os.path.abspath(os.path.join(dir, filex)))

  return abspathlist


# given a list of paths, copies those files into the given directory
def copy_to(todir, fromdir):
  #print 'copy_to function'
  #print 'todir: ', todir
  #print 'os.path.exists(todir): ', os.path.exists(todir)
  if not os.path.exists(todir):
    print "error: target directory does not exist, creating.."
    os.mkdir(todir)
    print todir, " directory is created."
    #sys.exit(1)
  filelist = get_special_paths(fromdir)
  for filex in filelist:
    os.path.join(todir, os.path.basename(filex))
    print 'copying', os.path.basename(filex), 'to', todir, 'folder..',
    shutil.copy(filex, todir)
    print 'done.'
  return


# given a list of paths, zip those files up into the given zipfile
def zip_to(paths, zippath):
  print 'zip_to function'
  return


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]"
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  dir = args[0]
  if todir: copy_to(todir, dir); return
  if tozip: zip_to(tozip, dir); return
  if(todir == '' and tozip == ''): print '\n'.join(get_special_paths(dir)); return

if __name__ == "__main__":
  main()
