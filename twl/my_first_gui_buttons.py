import Tkinter
from scrabble_game import ScrabbleMain
from word_jumble_class import JumbleWord
class Scrabble_Frame(Tkinter.Tk):
    def __init__(self,parent,word,correct_list):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize(word,correct_list)

    def initialize(self,word,correct_list):
        self.grid()
        rw=1
        ui_buttons_row=[]
        ui_buttons_col=[]
        for my_word in correct_list:
            col=0
            for item in my_word:
                button = Tkinter.Button(self,text=item,command=self.OnButtonClick)
                button.grid(column=col,row=rw,columnspan=1)
                ui_buttons_col.append(button)
                col+=1
            rw+=1
            ui_buttons_row.append(ui_buttons_col)
            ui_buttons_col=[]
        
        """
        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=rw,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        #self.entryVariable.set(u"Enter text here.")
        self.entryVariable.set(word)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.labelVariable.set(u"Hello!")
        """
        self.grid_columnconfigure(0,weight=1)
        self.resizable(False,False)
        self.update()
        self.geometry(self.geometry())       
        #self.entry.focus_set()
        #self.entry.selection_range(0, Tkinter.END)

    def OnButtonClick(self):
        self.labelVariable.set( self.entryVariable.get()+" (You clicked the button)" )
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self,event):
        self.labelVariable.set( self.entryVariable.get()+" (You pressed ENTER)" )
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

if __name__ == "__main__":
    scr=ScrabbleMain("/Users/rgamoji/personal/python/twl/TWL06.txt")
    orig_word=scr.get_input_word(5)
    jumbled=JumbleWord().jumble(orig_word)
    all_words=scr.create_words(orig_word)
    guess_list=[]
    for item in all_words:
        guess_list.append("".join("-"*len(item)))
    app = Scrabble_Frame(None,jumbled,guess_list)
    app.title('Scrabble Game - By Gamoji')
    app.mainloop()
