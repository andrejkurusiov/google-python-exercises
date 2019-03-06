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

def path_exists(dir):
  """ Returns 1 is given path doesn't exist; otherwise 0. """
  if not os.path.exists(dir): return 1
  else: return 0


def check_path(dir, todir, funct):
  """
    Checks two paths for existence and depending on funct value creates missing path.
  """
  errcode = 0
  errmsg = ''
  if funct == 'get_special_paths':
    errcode = path_exists(dir)
    if errcode: errmsg = 'Path ' + dir + ' does not exist!'
  elif funct == 'copy_to':
    errcode = path_exists(dir)
    if errcode:
      errmsg = 'Path ' + dir + ' does not exist!'
      return (errcode, errmsg)
    errcode = path_exists(todir)
    if errcode: # path doesn't exist, try creating directories
      try:
        os.makedirs(todir)
        errcode = 0
      except IOError:
        errmsg = 'Can\'t create ' + todir + ' folder!'
        return (errcode, errmsg)
  elif funct == 'zip_to':
    errcode = path_exists(dir)
    if errcode:
      errmsg = 'Path ' + dir + ' does not exist!'
      return (errcode, errmsg)
    errcode = path_exists(os.path.dirname(todir)) # decode path only as filename can be in the input string
    if errcode: # path doesn't exist, try creating directories
      try:
        os.makedirs(os.path.dirname(todir))
        errcode = 0
        errmsg = 'New path ' + os.path.dirname(todir) + ' created.'
      except IOError:
        errmsg = 'Can\'t create ' + todir + ' folder!'
        return (errcode, errmsg)
  else:
    errcode = 1
    errmsg = 'check_path: funct not recognized!'
  return (errcode, errmsg)


# returns a list of the absolute paths of the special files in the given directory
def get_special_paths(dir):
  abspathlist = []  # all files' absolute paths' list
  (errcode, errtext) = check_path(dir, '', 'get_special_paths')
  if errcode:
    print errtext
    return abspathlist
  filenames = os.listdir(dir)
  for filex in filenames:
    # check if special --> to list
    filename_special = re.search(r'\w*__\w+__.*', filex)
    if filename_special:
      abspathlist.append(os.path.abspath(os.path.join(dir, filex)))
  return abspathlist


def copy_to(todir, fromdir):
  # given a list of paths, copies those files into the given directory
  (errcode, errtext) = check_path(fromdir, todir, 'copy_to')
  if errcode:
    print errtext
    return
  filelist = get_special_paths(fromdir)
  for filex in filelist:
    os.path.join(todir, os.path.basename(filex))
    print 'Copying', os.path.basename(filex), 'to', todir, 'folder..',
    shutil.copy(filex, todir)
    print 'done.'
  return


def zip_to(zipfile, zippath):
  # given a list of paths, zip those files up into the given zipfile
  print 'zip_to function: make "'+ zipfile + '" file from special files found in "' + zippath + '" folder.'
  (errcode, errtext) = check_path(zippath, zipfile, 'zip_to') # check zip file path and create it if necessary
  if errcode:
    sys.stderr.write(errtext + '\n')
    sys.stderr.write('Errorcode: ' + str(errcode) + '\n')
    sys.exit(errcode)
  if errtext: print errtext # info about dir created
  cmd = 'zip -j ' + zipfile
  filenames = get_special_paths(zippath)
  if len(filenames) == 0:
    print 'No files to archive, exiting.'
    sys.exit(0)
  for fname in filenames:
     cmd = cmd + ' ' + fname
  print 'Command to be run:', cmd
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write('Problem creating zip file: ' + zipfile + '\n')
    sys.stderr.write(output + '\n')
    sys.exit('status: ' + str(status) + '\n')
  else: print 'Done!'
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
