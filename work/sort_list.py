from random import randint
class Sort(object):

    def __init__(self):
        pass
    def swap(self,n1,n2):
        n1,n2=n2,n1
        return [n1,n2]
    
    def bubble_sort(self,original,reverse=False):
        if len(original) < 1:
           return
        for i in range(0,len(original)):
            swapped = False
            j=len(original) - 1
            while j > i:
                if reverse:
                   if original[j] < original[j-1]:
                      original[j],original[j-1]=self.swap(original[j],original[j-1])
                      swapped = True
                else:
                   if original[j] > original[j-1]:
                      original[j],original[j-1]=self.swap(original[j],original[j-1])
                      swapped = True
                j-=1
            if not swapped:
               break
    def convert_string_to_ascii(self,string):
        return [ord(string[i]) for i in range(0,len(string))]
    def convert_ascii_to_string(self,n_list):
        return "".join([chr(n_list[i]) for i in range(0,len(n_list))])
