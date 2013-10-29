#!/usr/bin/python
from random import randint
from word_jumble_class import JumbleWord
import sys 
import time
from os import system,path
from json import loads

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
def main():    
    scr=ScrabbleMain("./TWL06.txt")
    if len(sys.argv) <= 1:
        usage()
        sys.exit(1) 
    elif sys.argv[1].startswith('--') and sys.argv[1] == '--my_word':
        args=sys.argv[1:]
        print "You chose:",args[0],"and",args[1]
        word=args[1]
        fill_words(word.upper(),scr)
    else: 
        if sys.argv[1].startswith('--'):
           usage()
           exit(1)
        args=sys.argv[2:]
        player_name=sys.argv[1]
        stat_file_path="./"
        stat_file_name=player_name+"_result.txt"
        stat_file=stat_file_path+stat_file_name
        if not path.exists(stat_file):
           print "Looks like this is your first time."
           stat_fp=open(stat_file,"w")
        else:
           print "Player already exists."
           stat_fp=open(stat_file,"a+")
    
        if args[0] == '--game':
           if len(args) == 1:
              choice=5
           else:
              choice=int(args[1])
           orig_word=scr.get_input_word(choice)
           jumbled=JumbleWord().jumble(orig_word)
           all_words=scr.create_words(orig_word)
           play_game(stat_fp,choice,jumbled,all_words,orig_word)
    
        elif args[0] == '--print_stats':
           print_stats(stat_file)
        
        if not stat_fp.closed:
           print stat_file,"is still open. Closing it."
           stat_fp.close()
    
def usage():
    print "Usage: [<player_name> [--game [word_length] [--print_stats]] [--my_word [word]]"
    print "<player_name> to save the statistics."
    print "--game: To play the scrabble word game with a word having [word_length] characters. Default is 5"
    print "--print_stats: To display the game statistics of <player_name>"
    print "--my_word: Use this option to see all the words within the input [word]"
   

def print_summary(isSummary,user_list,my_list=None):
    score=0
    if isSummary:
       print "%15s %15s" %("Your Guesses","Correct List")
       for count in range(0,len(user_list)):
           print "%15s %15s" %(user_list[count],my_list[count])
       for item in user_list:
           score+=compute_score(item)
       print "Your total Score is: ",score
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
    return score
      
def fill_words(word,scr):
    if not word.isalpha():
       print word,"is not an alphabetical word. Enter correct word."
       sys.exit(1)
    scr.build_word_list()
    all_words=scr.create_words(word)
    print_summary(False,all_words)

def play_game(stat_file,choice,jumbled,all_words,orig_word):
    guess_list=[]
    for item in all_words:
        guess_list.append("".join("-"*len(item)))
    count=len(all_words)
    try:
       while count > 0 and "".join(guess_list).find('-') != -1:
           system("clear")
           print "Your Word:",jumbled," and you have",count,"attempts remaining."
           print_summary(False,guess_list)
           guess=raw_input("Enter your guess: ").upper()
           if guess in all_words:
               if len(guess) == len(orig_word) and guess not in guess_list:
                  print "Wow! You guessed the tough One!"
                  print "Awarding bonus attempts."
                  count += 5
               guess_list[all_words.index(guess)]=guess
           count -= 1
    except KeyboardInterrupt:
          print "\nIt's ok to get bored!"
	  print_summary(True,guess_list,all_words)
          choice=raw_input("Do you want to save this results to file? (y/n): ")
          if choice.lower() in "Yy":
             save_game(stat_file,'Interrupt',jumbled,guess_list,all_words)
          sys.exit(0)
    system("clear")
    if "".join(guess_list).find('-') != -1:
        result='Lost'
        print "Sorry! You lost!"
	print_summary(True,guess_list,all_words)
    else:
        result='Win'
        print "Congratulations! You guess all the words correctly."
        print_summary(True,guess_list,all_words)
    choice=raw_input("Do you want to save this results to file? (y/n): ")
    if choice.lower() in "Yy":
         save_game(stat_file,result,jumbled,guess_list,all_words)
       
    
def save_game(results,result,guess_word,guess_list,all_words):
    score=0
    for item in guess_list:
        score += compute_score(item)
    result_dict={time.asctime().replace(" ","_"):{'Result':result,'Word':guess_word,'Guessed':guess_list,'Correct':all_words,'Score':score}}
    results.write(str(result_dict)+"\n")
    results.close()

def print_stats(fileName):
    result_list=[]
    fp=open(fileName,"r")
    line = fp.readline()
    while len(line) > 0:
        line=line.strip().replace('\'','\"')
        result_dict=loads(line)
        result_list.append(result_dict)
        line=fp.readline()
    print "No of Games Played: ",len(result_list)
    win_count=0
    lost_count=0
    incomplete=0
    for item in result_list:
        for key in item.keys():
            if item[key]['Result'] == "Win":
               win_count += 1
            elif item[key]['Result'] == "Lost":
               lost_count += 1
            else:
               incomplete += 1
            #print "Played On:",key.replace("_"," "),"\nWord you Played:",item[key]['Word']
    print "No Of Games Won:",win_count,"No Of Games Lost:",lost_count,"Incomplete Games:",incomplete
    fp.close()
        
if __name__ == '__main__':
   main() 
