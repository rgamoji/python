#!/usr/bin/python
from jumbline_util import JumblineBuilder,JumblineGame
import sys 
import time
from os import system,path
from json import loads
def main():    
    if len(sys.argv) <= 1:
        usage()
        sys.exit(1) 
    #word_file=open("/usr/share/dict/words")
    word_file=open("./TWL06.txt")
    game=JumblineGame(word_file)
    if sys.argv[1] == '--my_word':
        word=sys.argv[2]
        game.fill_words(word.upper())
    elif sys.argv[1] == '--game': 
        if len(sys.argv) == 2:
           choice=5
           print "Default Choice",choice
        else:
           choice=int(sys.argv[2])
           print "Choice:",choice
        game.play_game(choice)
    elif sys.argv[1] == '--hangman': 
        if len(sys.argv) == 2:
           choice=8
           print "Default Choice",choice
        else:
           choice=int(sys.argv[2])
           print "Choice:",choice
        game.hangman(choice)
    elif sys.argv[1] == '--print_stats':
         game.print_stats()
    if not word_file.closed:
       word_file.close()
    
def usage():
    print "Usage: <word_file>[--game [word_length]] [--print_stats] [--my_word [word]] [--hangman [word_length]]"
    print "<word_file> is the file containing words. Default is /usr/share/dict/words"
    print "--game: To play the scrabble word game with a word having [word_length] characters. Default is 5"
    print "--print_stats: To display the game statistics."
    print "--my_word: Use this option to see all the words within the input [word]"
    print "--hangman: To play the hangman type word game with a word having [word_length] characters. Default is 8"

if __name__ == '__main__':
   main() 
