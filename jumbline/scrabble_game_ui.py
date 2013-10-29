#!/usr/bin/env python
import Tkinter
from scrabble_game import ScrabbleMain
from word_jumble_class import JumbleWord
class Scrabble_Frame(Tkinter.Frame):
    def __init__(self,parent,word,guess_list,correct_list):
        Tkinter.Frame.__init__(self,parent)
        self.parent = parent
        self.word=word
        self.correct_list=correct_list
        self.guess_list=guess_list 
        self.initialize(self.word,self.guess_list)
        self.count=0

    def initialize(self,word,guess_list):
        self.grid()
        #self.drawLayout(word,guess_list)
        self.createCanvas()
        #self.setScroll()
        #self.yscrollcommand=self.scrollBar.set()
        self.grid_columnconfigure(0,weight=1)
        #self.resizable(True,True)
        self.update()
        self.pack()
        #self.geometry(self.geometry())       

    def setScroll(self):
        self.scrollBar = Tkinter.Scrollbar(self,orient=Tkinter.VERTICAL)
        self.scrollBar.grid()

    def createCanvas(self):
        self.c = Tkinter.Canvas(self)
        self.c.grid(column=0,row=1,sticky='W')
        self.createWidgets(self.word,self.guess_list)
        self.drawLayout(self.word,self.ui_textField_row)
        #self.setScroll()

    def createWidgets(self,word,guess_list):
        self.ui_textField_row=[]
        for my_word in guess_list:
            self.textField = Tkinter.Entry(self.c,width=len(my_word)+1)
            self.textField.insert(0,my_word)
            self.ui_textField_row.append(self.textField)
        self.play_label = Tkinter.StringVar()
        self.play_label.set(word)
        self.play_word = Tkinter.Entry(self,textvariable=self.play_label,width=len(word)+1)
        self.status_label=Tkinter.StringVar()
        self.status_textField=Tkinter.Entry(self,textvariable=self.status_label)
        self.play_area_label = Tkinter.StringVar()
        self.play_area = Tkinter.Entry(self,textvariable=self.play_area_label,width=len(word)+1)

    def drawLayout(self,word,ui_txt_list):
        rw=0
        col=0
        element=1
        for textField in ui_txt_list:
            if element % 5 == 0:
               col += 1
               rw=0
            textField.grid(column=col,row=rw,sticky='W')
            textField.grid_propagate(False)
            textField.config(fg="black",bg="orange")
            element+=1
            rw+=1
        self.play_word.grid(column=0,row=0,sticky='W')
        self.play_word.grid_propagate(False)
        self.play_area.grid(column=0,row=2,sticky='W')
        self.play_area.bind("<Return>",self.OnPressEnter)
        self.status_textField.grid(column=0,row=3,sticky='W')
        

    def validate(self,guess):
        if guess in self.correct_list and not guess in self.guess_list:
           self.guess_list[self.correct_list.index(guess)]=guess
           return True

    def OnPressEnter(self,event):
        self.count+=1
        left=len(self.guess_list) - self.count
        userInput=self.play_area_label.get().upper()
        if self.count < len(self.correct_list):
           if self.validate(userInput):
              self.ui_textField_row[self.guess_list.index(userInput)].delete(0,len(self.ui_textField_row[self.guess_list.index(userInput)].get()))
              self.ui_textField_row[self.guess_list.index(userInput)].insert(0,userInput)
              self.ui_textField_row[self.guess_list.index(userInput)].config(fg="black",bg="green")
              self.ui_textField_row[self.guess_list.index(userInput)].config(relief=Tkinter.GROOVE)
              self.status_label.set("Attempts Left: "+str(left))
              self.status_textField.config(fg="black",bg="green")
           else:
              self.status_label.set("Attempts Left: "+str(left))
              self.status_textField.config(fg="black",bg="red")
        else:
           if "".join(self.guess_list).find('-') == -1:
               self.status_label.set("Congratulations! You Won!")
               self.status_textField.config(fg="black",bg="green")
           self.status_label.set("You Lost!")
           self.status_textField.config(fg="black",bg="red")
           self.play_area.config(state=Tkinter.DISABLED)
           index=0
           for field in self.ui_textField_row:
               field.delete(0,len(field.get()))
               field.config(fg="black",bg="green")
               field.config(relief=Tkinter.GROOVE)
               field.insert(0,self.correct_list[index])
               index+=1
        if "".join(self.guess_list).find('-') == -1:
           self.status_label.set("Congratulations! You Won!")
           self.status_textField.config(fg="black",bg="green")
        self.play_area_label.set("")

if __name__ == "__main__":
    scr=ScrabbleMain("/Users/rgamoji/personal/python/twl/TWL06.txt")
    orig_word=scr.get_input_word(5)
    jumbled=JumbleWord().jumble(orig_word)
    all_words=scr.create_words(orig_word)
    guess_list=[]
    for item in all_words:
        guess_list.append("".join("-"*len(item)))
    app = Scrabble_Frame(None,jumbled,guess_list,all_words)
    #app.title('Scrabble Game - By Gamoji')
    app.mainloop()
