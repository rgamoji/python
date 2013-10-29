#!/usr/bin/python
from random import randint
from word_jumble_class import JumbleWord
import sys 
from os import system

class ScrabbleMain(object):
    afile=None
    out_list={3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[],14:[],15:[]}
    max_word_len=0

    def __init__(self,file_name):
        self.afile=open(file_name,"r")
    
    def random_line(self,afile):
        line = next(afile)
        for num, aline in enumerate(afile):
          if random.randrange(num + 2): continue
          line = aline
        afile.seek(0)
        return line

    def build_word_list(self):
        word=self.afile.readline().strip()
        while len(word) > 0 :
            if len(word) > 2:
                item_len=len(word)
                self.out_list[item_len].append(word)
            word=self.afile.readline().strip()
        self.afile.close()
        return self.out_list

    def get_input_word(self,input):
        my_out_list=self.build_word_list()
        guess_word=""
        guess_word=my_out_list[input][randint(0,len(my_out_list[input]))]
        return guess_word

    def lengthOf(self,input):
        return len(input)

    def create_words(self,guess_word):
        min_length = 3
        master_list=[]
        for length in range(min_length,len(guess_word)+1):
            for word in self.out_list[length]:
                if self.is_word_in_list(guess_word,word):
		   master_list.append(word)
        master_list=sorted(master_list,key=self.lengthOf)
        return master_list

    def is_word_in_list(self,guess_word,word):
        found=False
        for char in word:
            if char in guess_word and (word.count(char) <= guess_word.count(char)):
               found=True
            else:
               found=False
               break
        return found
    """
        word=self.random_line(self.afile).strip()
        if len(word) == input:
           return word
        return self.build_word_list(input)
    """ 
def usage():
    print "Usage: [--game [word_length]] [--my_word [word]]"
    print "--game: To play the scrabble word game with a word having [word_length] characters. Default is 5"
    print "--my_word: Use this option to see all the words within the input [word]"
def print_summary(isSummary,user_list,my_list=None):
    score=0
    if isSummary:
       print "%15s %15s" %("Your Guesses","Correct List")
       for count in range(0,len(user_list)):
           print "%15s %15s" %(user_list[count],my_list[count])
       for item in user_list:
           score+=compute_score(item)
       print "Your Score is: %10d" %(score)
    else:
        for item in user_list:
            print "",item
       
def compute_score(word):
    score_dict = {
                 "a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, 
                 "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
                 "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, "z": 10
                }
    score=0
    if word.find('-') != -1:
       return 0
    for char in word.lower():
        score+=score_dict[char]
    print "Score for:",word,"is:",score
    return score
"""
def main():    
    args=sys.argv[1:]
    if not args:
       usage()
       sys.exit(1) 
    scr=ScrabbleMain("/Users/rgamoji/personal/python/twl/TWL06.txt")
    print args
    if args[0] == '--game':
       if len(args) == 1:
          choice=5
       else:
          choice=int(args[1])
       orig_word=scr.get_input_word(choice)
       jumbled=JumbleWord().jumble(orig_word)
       all_words=scr.create_words(orig_word)
       guess_list=[]
       for item in all_words:
           guess_list.append("".join("-"*len(item)))
       count=len(all_words)
       try:
          while count > 0:
              system("clear")
              print "Your Word:",jumbled," and you have",count,"attempts remaining."
              print_summary(False,guess_list)
              guess=raw_input("Enter your guess: ").upper()
              if guess in all_words:
                 if guess == orig_word:
                    print "Wow! You guessed the tough One!"
                    print "Awarding bonus attempts."
                    count += 5
                 guess_list[all_words.index(guess)]=guess
              count -= 1
       except KeyboardInterrupt:
             print "\nIt's ok to get bored!"
	     print_summary(True,guess_list,all_words)
             sys.exit(0)
       system("clear")
       if "".join(guess_list).find('-') != -1:
          print "Sorry! You lost!"
	  print_summary(True,guess_list,all_words)
       else:
            "Congratulations! You guess all the words correctly."
	    print_summary(True,guess_list,all_words)
    elif args[0] == '--my_word':
         print "You chose:",args[0],"and",args[1]
         word=args[1]
         if not word.isalpha():
             print word,"is not an alphabetical word. Enter correct word."
             sys.exit(1)
         scr.build_word_list()
         all_words=scr.create_words(word)
         print_summary(False,all_words)

def play_game(guess,guess_list,all_words):
    try:
        pass
    except KeyboardInterrupt:
          print "\nIt's ok to get bored!"
	  print_summary(True,guess_list,all_words)
          sys.exit(0)
       
if __name__ == '__main__':
   main() 
"""
