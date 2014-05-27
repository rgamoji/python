#!/usr/bin/env python
import random
from sort_list import Sort

def get_min_max(my_list):
    count=1
    min=my_list[0]
    max=my_list[0]
    next_max=my_list[0]
    while count < len(my_list):
        if my_list[count] < min:
              min=my_list[count]
        elif my_list[count] > max:
              max=my_list[count]
        elif my_list[count] < max and my_list[count] > next_max:
              next_max=my_list[count]
        count+=1
    return (min,max,next_max)

def main():
    my_list=[]
    count=0
    while count < 20:
        my_list.append(random.randint(-10,300))
        count+=1
    items=get_min_max(my_list)
    print "Input:",my_list
    print "Smallest:",items[0]
    print "Largest:",items[1]
    print "Second Largest:",items[2]
    
    Sort().bubble_sort(my_list)
    print "Sorted List: ", my_list

if __name__ == '__main__':
   main()
