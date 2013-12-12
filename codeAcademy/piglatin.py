#!/usr/bin/env python
def check_y(word):
    chk_str="aeiouy"
    for c in word.lower():
        if c in "aeiou":
           chk_str="aeiou"
    return chk_str
def single_char(word):
    my_string=""
    if word.lower() in ("aeiou"):
       my_string=word+"yay"
    else:
       my_string=word+"ay"
    return my_string
def get_prefix(word):
    my_string=""
    index=0
    chk_str=check_y(word)
    for c in word.lower():
        if c in chk_str:
            return my_string
        else:
            my_string+=c
def get_stem(word):
    my_string=""
    index=0
    chk_str=check_y(word)
    for c in word.lower():
        if c in chk_str:
           index=word.index(c)
           my_string=word[index::]
           return my_string
def translate(word):
    if not word[0:-1:].isalpha():
       return word
    final_str=""
    char=''
    preserve_case=False
    punct=False
    if len(word) == 1:
       return single_char(word)
    if word[0].isupper():
       preserve_case=True
    if not word[-1].isalpha():
       char=word[-1]
       punct=True
    if not word[0].lower() in "aeiou":
        prefix=get_prefix(word)
        stem=get_stem(word)
        if preserve_case:
           stem=stem[0].upper()+stem[1::]
        if punct:
           final_str=stem[0:len(stem)-1:]+prefix.lower()+"ay"+char
        else:
           final_str=stem+prefix.lower()+"ay"
    else:
      if punct:
         final_str=word[0:len(word)-1:]+"way"+char
      else:
         final_str=word+"way"
    return final_str

sentence=raw_input("Enter a word or sentence: ")
output=""
if sentence.find(" ") != -1:
   for word in sentence.split(" "):
       output+=translate(word)+" "
else:
   output=translate(sentence)

print output

