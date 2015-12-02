from sort_list import Sort
from random import randint

def main():
   string=raw_input("Enter a String: ")
   sort_me=Sort()
   n_list=sort_me.convert_string_to_ascii(string)
   sort_me.bubble_sort(n_list,True)
   print sort_me.convert_ascii_to_string(n_list)
   original=[]
   for n in range(0,10):
       original.append(randint(0,100))
   print original
   sort_me.bubble_sort(original,True)
   print original
   sort_me.bubble_sort(original)
   print original
if __name__ == "__main__":
   main()
