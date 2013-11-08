#!/usr/bin/env python
from jumbline_util import JumblineBuilder,JumblineUI
if __name__ == "__main__":
    scr=JumblineBuilder("./TWL06.txt")
    orig_word=scr.get_input_word(5)
    jumbled=scr.jumble(orig_word)
    all_words=scr.create_words(orig_word)
    guess_list=[]
    for item in all_words:
        guess_list.append("".join("-"*len(item)))
    app = JumblineUI(None,jumbled,guess_list,all_words)
    #app.title('Scrabble Game - By Gamoji')
    app.mainloop()
