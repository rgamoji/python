#!/usr/bin/env python
import random

def get_min_max(my_list):
    count=1
    min=my_list[0]
    max=my_list[0]
    while count < len(my_list):
        if my_list[count] < min:
              min=my_list[count]
        elif my_list[count] > max:
              max=my_list[count]
        count+=1
    return (min,max)

def main():
    my_list=[]
    count=0
    while count < 20:
        my_list.append(random.randint(-10,300))
        count+=1
    items=get_min_max(my_list)
    print "Input:",my_list
    print "Item with Minimum Value:",items[0]
    print "Item with Maximum Value:",items[1]

if __name__ == '__main__':
   main()
