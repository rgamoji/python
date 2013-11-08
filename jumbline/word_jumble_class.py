from random import randint
from sys import exit
class JumbleWord(object):
    def __init__(self):
      pass
    def jumble(self,word):
        scrambled=""
        scr_string=""
        guess_list=[]
        next=0
        while True:
           next=randint(0,len(word)-1)
           if not next in guess_list:
              scr_string+=word[next]
              guess_list.append(next)
           if len(scr_string) == len(word):
              break
        return scr_string
    def open_file(self):
        word_file = open("/usr/share/dict/words","r")
        return word_file    
    
    def close_file(self,file):
        if not file.closed:
           file.close()
    
    def build_word_list(self,file,char):
        word_list=[]
        if file.closed:
           return word_list
        line=file.readline()
        while not len(line) == 0:
             if line.startswith(char.lower()) or line.startswith(char):
                word_list.append(line.rstrip())
             line=file.readline()
        return word_list 
    def build_dictionary(self,my_dict,file,char):
        if file.closed:
           return my_dict
        file.seek(0)
        value_list = self.build_word_list(file,char)
        my_dict[char]=value_list
        return my_dict
    
    def build_num_key(self,dict):
        num_key_dict={}
        key_num=1
        for key in dict:
            num_key_dict[key_num] = key
            key_num+=1
        return num_key_dict
    
    def get_random_word(self,my_dict,key):
        count=1
        random_word=""
        my_words = []
        for keys in my_dict.keys():
            if count == key:
               my_words=my_dict[keys]
            count+=1
        random_key=randint(0,len(my_words))
        return my_words[random_key]
    
    def fill_guess_word(self,my_word,guess_str,char):
        if char == "":
           print "Sorry! That was an empty guess!"
           return guess_str
        c_count = my_word.count(char)
        if c_count == 0:
           print "Your guess[",char,"] is no where in the word."
           return guess_str
        s_list = list(guess_str)
        for item in range(0,len(my_word)):
            if char == my_word[item]:
               if c_count == 1: 
                  s_list[item]=char
                  return "".join(s_list)
               else:
                  if char in guess_str:
                      indexOfChar=guess_str.index(char)
                      if item > indexOfChar:
                         s_list[item]=char
                         return "".join(s_list)
                  else:
                      s_list[item]=char
                      return "".join(s_list)
