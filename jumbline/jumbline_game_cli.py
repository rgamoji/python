#!/usr/bin/python
#from word_jumble_class import JumbleWord
from jumbline_util import JumblineBuilder,JumblineGame
import sys 
import time
from os import system,path
from json import loads
def main():    
    word_file=open("./TWL06.txt")
    #scr=JumblineBuilder(word_file)
    game=JumblineGame(word_file)
    if len(sys.argv) <= 1:
        usage()
        sys.exit(1) 
    elif sys.argv[1].startswith('--') and sys.argv[1] == '--my_word':
        args=sys.argv[1:]
        word=args[1]
        game.fill_words(word.upper())
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
           stat_fp=open(stat_file,"w")
        else:
           stat_fp=open(stat_file,"a+")
    
        if args[0] == '--game':
           if len(args) == 1:
              choice=5
           else:
              choice=int(args[1])
           loop=raw_input("Play in loop(y/n): ")
           if loop.lower() == 'y':
              print "You chose Loop mode. Press Ctrl-C to stop playing."
              try:
                 while 1: 
                     #orig_word=scr.get_input_word(choice)
                     #jumbled=scr.jumble(orig_word)
                     #all_words=scr.create_words(orig_word)
                     game.play_game(stat_fp,choice)
              except KeyboardInterrupt:
                 print "Exiting the game now."
           else:
              game.play_game(stat_fp,choice)
                 
        elif args[0] == '--print_stats':
           game.print_stats(stat_file)
        
        if not stat_fp.closed:
           stat_fp.flush()
           stat_fp.close()
        if not word_file.closed:
           word_file.close()
    
def usage():
    print "Usage: [<player_name> [--game [word_length] [--print_stats]] [--my_word [word]]"
    print "<player_name> to save the statistics."
    print "--game: To play the scrabble word game with a word having [word_length] characters. Default is 5"
    print "--print_stats: To display the game statistics of <player_name>"
    print "--my_word: Use this option to see all the words within the input [word]"

if __name__ == '__main__':
   main() 
