#!/usr/bin/env python

def compute(dec):
    binary=[]
    #outer_index=0
    inner_list=[]
    while dec > 0:
       bit=dec % 2
       dec=dec / 2
       inner_list.insert(0,bit)
       if len(inner_list) == 8:
          binary.insert(0,inner_list)
          inner_list=[]
    return binary

def main():
    num=int(input("Enter an integer: "))
    print "Binary:",compute(num)

if __name__ == "__main__":
   main()
