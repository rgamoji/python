#!/usr/bin/env python
import sys
import operator

def append(char,stat_dict):
    if char.isalpha():
        if char.lower() in stat_dict.keys():
           stat_dict[char.lower()]+=1
        else:
           stat_dict[char.lower()]=1

def compute(stat_dict,char_count):
    for item in stat_dict.keys():
        percent=round((float(stat_dict[item]) / char_count) * 100,3)
        stat_dict[item]=percent

def usage():
    print "Usage:",sys.argv[0]," <file_name>"
    sys.exit(1)

def main():
    if len(sys.argv) < 2:
       usage()
    stat_dict={}
    file_name=sys.argv[1]
    fp=open(file_name,"r")
    line=fp.readline()
    char_count=0
    while len(line) != 0:
        for char in "".join(line.strip().split()):
            append(char,stat_dict)
            char_count+=1
        line=fp.readline()
    compute(stat_dict,char_count)
    '''
    for item in stat_dict.keys():
        print item,":",stat_dict[item]
    print "Total Characters in the file: ",char_count
    '''
    print "Frequency Analaysis of",file_name,"in %, sorted highest to lowest:"
    for item in sorted(stat_dict.iteritems(),key=operator.itemgetter(1),reverse=True):
        print "%c: %2.2f" %(item[0],item[1])
    if not fp.closed:
       fp.close()


if __name__ == '__main__':
   main()

      
    
