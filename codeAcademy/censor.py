#!/usr/bin/env python

"""
Takes a sentence as input and masks the word of your choice.
Not a fool-proof program though! Developed it during my initial days of practice and left it. It doesn't work if your word as spl chars.
Ex:
$ ./censor.py 
Enter your string: what the heck
Enter what I should censor: heck
what the ****
$ ./censor.py 
Enter your string: What the heck!
Enter what I should censor: heck
What the heck!
$ ./censor.py 
Enter your string: What the heck!
Enter what I should censor: heck!
What the *****
"""
def censor(line,word):
    string=line.split(' ')
    output=""
    for item in string:
        if item == word:
            item="".join("*"*len(word))
        output=output+" "+item
    return output.lstrip()

string= raw_input("Enter your string: ")
cen= raw_input("Enter what I should censor: ")

print censor(string,cen)
