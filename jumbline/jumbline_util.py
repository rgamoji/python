from random import randint
import sys 
import time
from os import system,path
from json import loads
import Tkinter

class JumblineGame(object):
    def __init__(self,word_file):
        #self.word_file=word_file
        self.j_obj=JumblineBuilder(word_file)
    def print_summary(self,isSummary,user_list,my_list=None):
        score=0
        if isSummary:
           print "%15s %15s" %("Your Guesses","Correct List")
           for count in range(0,len(user_list)):
               print "%15s %15s" %(user_list[count],my_list[count])
           for item in user_list:
               score+=self.compute_score(item)
           print "Your total Score is: ",score
        else:
            for item in user_list:
                print "",item
           
    def compute_score(self,word):
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
          
    def fill_words(self,word):
        if not word.isalpha():
           print word,"is not an alphabetical word. Enter correct word."
           sys.exit(1)
        self.j_obj.build_word_list()
        all_words=self.j_obj.create_words(word)
        self.print_summary(False,all_words)
    
    def play_game(self,player,choice):
        repeat='y'
        print "Player is: ",player,"Choice is",choice
        stat_file=player+"_result.txt"
        if not path.exists(stat_file):
           stat_fp=open(stat_file,"w")
        else:
           stat_fp=open(stat_file,"a+")
        while repeat.lower() == 'y':
            orig_word=self.j_obj.get_input_word(choice)
            jumbled=self.j_obj.jumble(orig_word)
            all_words=self.j_obj.create_words(orig_word)
            guess_list=[]
            for item in all_words:
                guess_list.append("".join("-"*len(item)))
            count=len(all_words)
            try:
               while count > 0 and "".join(guess_list).find('-') != -1:
                   system("clear")
                   print "Your Word:",jumbled," and you have",count,"attempts remaining."
                   self.print_summary(False,guess_list)
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
        	  self.print_summary(True,guess_list,all_words)
                  save=raw_input("Do you want to save this results to file? (y/n): ")
                  if save.lower() == "y":
                     self.save_game(stat_fp,'Interrupt',jumbled,guess_list,all_words)
                  stat_fp.flush()
                  stat_fp.close()
                  sys.exit(0)
            system("clear")
            if "".join(guess_list).find('-') != -1:
                result='Lost'
                print "Sorry! You lost!"
        	self.print_summary(True,guess_list,all_words)
            else:
                result='Win'
                print "Congratulations! You guess all the words correctly."
                self.print_summary(True,guess_list,all_words)
            save=raw_input("Do you want to save this results to file? (y/n): ")
            if save.lower() == "y":
                 self.save_game(stat_fp,result,jumbled,guess_list,all_words)
            repeat=raw_input("Play Again? (y/n): ")
        stat_fp.flush()
        stat_fp.close()
        
    def save_game(self,results,result,guess_word,guess_list,all_words):
        score=0
        for item in guess_list:
            score += self.compute_score(item)
        result_dict={time.asctime().replace(" ","_"):{'Result':result,'Word':guess_word,'Guessed':guess_list,'Correct':all_words,'Score':score}}
        results.write(str(result_dict)+"\n")
        results.flush()
        #results.close()
    
    def print_stats(self,player):
        result_list=[]
        fp=open(player+"_result.txt","r")
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

class JumblineBuilder(object):
    afile=None
    out_list={3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[],14:[],15:[]}
    def __init__(self,file_name):
        self.afile=file_name
        #self.afile=open(file_name,"r")

    def __del__(self):
        if not self.afile.closed:
           self.afile.close()

    def jumble(self,word):
        scr_string=""
        guess_list=[]
        next=0
        while True:
           next=randint(0,len(word)-1)
           if not next in guess_list:
              scr_string+=word[next]
              guess_list.append(next)
           if len(scr_string) == len(word):
              break
        return scr_string
    """    
    Not used right now.
    def random_line(self,afile):
        line = next(afile)
        for num, aline in enumerate(afile):
          if random.randrange(num + 2): continue
          line = aline
        afile.seek(0)
        return line
    """
    def build_word_list(self):
        word=self.afile.readline().strip()
        #word=word_file.readline().strip()
        while len(word) > 0 :
            if len(word) > 2:
                item_len=len(word)
                self.out_list[item_len].append(word)
            word=self.afile.readline().strip()
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
Still a lot of work is pending for the UI Class.
Need to add a lot of features and ui gadgets. I am still working on it.
"""
class JumblineUI(Tkinter.Frame):
    def __init__(self,parent,word_file,choice=5):
        self.j_obj=JumblineBuilder(word_file)
        self.orig_word=self.j_obj.get_input_word(choice)
        self.jumbled=self.j_obj.jumble(self.orig_word)
        self.correct_list=self.j_obj.create_words(self.orig_word)
        #orig_word=scr.get_input_word(5)
        #jumbled=scr.jumble(orig_word)
        #all_words=scr.create_words(orig_word)
        self.guess_list=[]
        for item in self.correct_list:
            self.guess_list.append("".join("-"*len(item)))
        Tkinter.Frame.__init__(self,parent)
        self.parent=parent
        #self.word=word
        #self.correct_list=correct_list
        #self.guess_list=guess_list 
        self.initialize(self.orig_word,self.guess_list)
        self.count=0

    def initialize(self,word,guess_list):
        self.grid()
        self.createCanvas()
        self.grid_columnconfigure(0,weight=1)
        self.update()
        self.pack()

    def setScroll(self):
        self.scrollBar = Tkinter.Scrollbar(self,orient=Tkinter.VERTICAL)
        self.scrollBar.grid()

    def createCanvas(self):
        self.c = Tkinter.Canvas(self)
        self.c.grid(column=0,row=1,sticky='W')
        self.createWidgets(self.orig_word,self.guess_list)
        self.drawLayout(self.orig_word,self.ui_textField_row)
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
