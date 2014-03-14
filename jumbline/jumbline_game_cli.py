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
    print sys.argv
    if len(sys.argv) <= 1:
        usage()
        sys.exit(1) 
    elif sys.argv[1] == '--my_word':
        args=sys.argv[1:]
        word=args[1]
        game.fill_words(word.upper())
    elif sys.argv[1] == '--game': 
        if len(sys.argv) == 2:
           choice=5
           print "Default Choice",choice
        else:
           choice=int(sys.argv[2])
           print "Choice:",choice
        game.play_game(choice)
    elif sys.argv[1] == '--print_stats':
         game.print_stats()
    if not word_file.closed:
       word_file.close()
    
def usage():
    print "Usage: [--game [word_length]] [--print_stats] [--my_word [word]]"
    print "--game: To play the scrabble word game with a word having [word_length] characters. Default is 5"
    print "--print_stats: To display the game statistics."
    print "--my_word: Use this option to see all the words within the input [word]"

if __name__ == '__main__':
   main() 
