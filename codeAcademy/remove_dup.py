#!/usr/bin/env python
"""
Removes duplicates from the input list.
Ex:
$ ./remove_dup.py 
Original List: [2, 1, 2, 1, 3, 4, 5, 5, 4, 6, 6, 6, 5, 5, 7, 8, 9, 1, 2, 4]
After removing duplicates: [2, 1, 3, 4, 5, 6, 7, 8, 9]
"""
def remove_duplicates(my_list):
    to_return=[]
    for item in my_list:
        try:
            found=to_return.index(item)
        except:
            to_return.append(item)
    return to_return
    
seq=[2,1,2,1,3,4,5,5,4,6,6,6,5,5,7,8,9,1,2,4]
print "Original List:",seq
print "After removing duplicates:",str(remove_duplicates(seq))
