#!/usr/bin/env python
def anti_vowel(string):
    output=""
    for index in range(0,len(string)):
        char=string[index].lower()
        if not (char in "aeiou"):
            output+=string[index]
            
    return output
    
    
string=raw_input("Enter your string: ")
print "This is your string with all vowels removed: "+anti_vowel(string)
