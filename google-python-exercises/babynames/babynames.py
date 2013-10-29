#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import operator

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

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  fh=open(filename,'r')
  main_str=fh.read()
  fh.close()
  name_list={}
  rank_list={}
  year=re.search('(>Popularity\sin\s)(\d+)<',main_str).group(2).lstrip() 
  all_names=re.findall('<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',main_str)
  if len(all_names) > 0:
    for item in all_names:
      rank=int(item[0])
      boy=item[1]
      girl=item[2]
      names={'Boy':boy,'Girl':girl}
      rank_list[rank]=names

    name_list[year]=rank_list
  # +++your code here+++
  return name_list

def write_summary(filename,name_list):
    fh=open(filename,'w')
    year_list=name_list.keys()
    for year in year_list:
        fh.write("Rank Wise names list of Year: "+year+"\n")
        sorted_rank=sorted(name_list[year].iteritems(),key=operator.itemgetter(0))
        #for rank_list in name_list[year].keys():
        for rank_list in sorted_rank:
            fh.write("Rank:%5s\n\tBoy :%20s\n\tGirl:%20s\n" %(rank_list[0], rank_list[1]['Boy'], rank_list[1]['Girl']))
    fh.close()

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
  name_list=extract_names(args[0])
  if summary:
     write_summary(args[0]+".summary",name_list) 
  #for ranks in name_list[1:]:
  #  print ranks
  
if __name__ == '__main__':
  main()
