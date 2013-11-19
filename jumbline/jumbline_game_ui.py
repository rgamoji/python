#!/usr/bin/env python
from jumbline_util import JumblineUI
if __name__ == "__main__":
    fp=open("./TWL06.txt","r")
    choice=int(raw_input("Enter length of the word (min 5,max 15): "))
    app = JumblineUI(None,fp,choice)
    app.mainloop()
