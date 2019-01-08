#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

# add tuple[1-2] name to dic
def Add_name(name, rank, dic):
  if (name in dic):
    #print name, dic[name]
    if int(dic[name]) > int(rank):
      #print name, dic[name], "->", rank
      dic[name] = int(rank)
  else:
    dic[name] = int(rank)
  return dic

# gets tuples of names data and returns ready dictionary in a form (name, rank)
def Form_dictionary(names_tuples):
  dic = {}
  for tuple in names_tuples:
    dic = Add_name(tuple[1], tuple[0], dic)
    dic = Add_name(tuple[2], tuple[0], dic)
  return dic

def Extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  list =[]
  f = open(filename, 'rU')
  wholefile = f.read()
  f.close()

  # find year
  year_find = re.search(r'Popularity in (\d+)', wholefile)
  if not year_find:
    #sys.stderr.write('Couldn\'t find the year!\n')
    print 'Couldn\'t find the year!\n'
    sys.exit(1)
  year = year_find.group(1)
  list.append(year) 

  # for regex: <td>3</td><td>Matthew</td><td>Brittany</td>
  names_findall = re.findall(r'\<td\>(\d+)\<\/td\>\<td\>(\w+)\<\/td\>\<td\>(\w+)\<\/td\>', wholefile)
  if not names_findall:
    print 'Couldn\'t find the names!\n'
    sys.exit(1)

  # create dictionary and list of names
  dict = Form_dictionary(names_findall)
  for name, rank in sorted(dict.items()):
    list.append(name + ' ' + str(rank))

  return list


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:
    #print filename, ":\n"
    print '\n'.join(Extract_names(filename)) + '\n'
  
if __name__ == '__main__':
  main()
