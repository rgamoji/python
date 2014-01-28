#!/usr/bin/python
from jumbline_util import JumblineBuilder,JumblineGame
import sys 
import time
from os import system,path
from json import loads
def main():    
    word_file=open("./TWL06.txt")
    #word_file=open("/usr/share/dict/words")
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
        print sys.argv,"are the args"
        if args[0] == '--game':
           if len(args) == 1:
              choice=5
              print "Defaulting to",choice
           else:
              choice=int(args[1])
           game.play_game(sys.argv[1],choice)
        elif args[0] == '--print_stats':
           game.print_stats(sys.argv[1])

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
