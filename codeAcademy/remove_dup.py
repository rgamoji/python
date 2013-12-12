#!/usr/bin/env python
def remove_duplicates(my_list):
    to_return=[]
    for item in my_list:
        try:
            found=to_return.index(item)
        except:
            to_return.append(item)
    return to_return
    
seq=[2,1,2,1,3,4,5,5,4,6,6,6,5,5,7,8,9,1,2,4]
print seq
print str(remove_duplicates(seq))
