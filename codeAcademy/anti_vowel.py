#!/usr/bin/env python
"""
Removes Vowels from the input String. 
Ex:
$ ./anti_vowel.py 
Enter your string: Hello World
This is your string with all vowels removed: Hll Wrld
"""
def anti_vowel(string):
    output=""
    for index in range(0,len(string)):
        char=string[index].lower()
        if not (char in "aeiou"):
            output+=string[index]
            
    return output
    
    
string=raw_input("Enter your string: ")
print "This is your string with all vowels removed: "+anti_vowel(string)
