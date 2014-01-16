#!/usr/bin/env python
"""
Calculates the median in an input list.
If the list is even-length, median is average of the middle 2 elements.
Ex:
$ ./median.py
Input List: [23.5, 22, 19.8, 17.6, 12.0, 10, 8, 2, 4, 6.7]
List length: Even
Median: 11.0
"""
def get_list_len_type(my_list):
    if (len(my_list) %2 == 0):
        return "Even"
    else:
        return "Odd"
def sort_list(my_list):
    return sorted(my_list)
def median(my_list):
    list_len_type=get_list_len_type(my_list)
    sorted_list=sort_list(my_list)
    if list_len_type == "Even":
        index_first=((len(sorted_list)/2) - 1)
        index_second=len(sorted_list)/2
        return float(sorted_list[index_first]+sorted_list[index_second])/2
    else:
        return float(sorted_list[len(sorted_list)/2])
        
        
sq=[23.5,22,19.8,17.6,12.0,10,8,2,4,6.7]
print "Input List:",sq
print "List length:",get_list_len_type(sq)
Median=str(median(sq))
print "Median:",Median
