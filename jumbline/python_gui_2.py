#!/usr/bin/env python      
import Tkinter as tk       
from scrabble_game Import ScrabbleMain
from word_jumble_class import Jumbled
import word_jumble_class
class Application(tk.Frame):              
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   
        self.grid()                       
        self.createWidgets()

    def createWidgets(self,correct_list):
        self.quitButton = tk.Button(self, text='Quit',command=self.quit)            
        self.quitButton.grid()            
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
app = Application()                       
app.master.title('Sample application')    
app.mainloop()                            
