import justin
import greg

tiles=[]

def play_on():
    global e1
    string=e1.get()
    a=string.upper()
    tiles.append(a)
    string='The tiles you can play on are '+a+'\n'
    text.insert(END,string)
    
def your_tiles():
    global e2
    string=e2.get()
    b=string.upper()
    tiles.append(b)
    string=b+'\n'
    text.insert(END,string)
    set_tiles,your_tiles=justin.input_list(tiles)
    word_list=greg.list_of_words()
    possibilities=justin.possible_combos(set_tiles,your_tiles)
    plays=justin.possible_plays(word_list,possibilities)
    string=justin.best_word(plays)
    text.insert(END,string)
    
from tkinter import *
root=Tk()
root.title('Scrabble Cheater')
text=Text(root)
e1=Entry(root)
e1.grid(row=1,column=0)
b1=Button(root,text='Enter',command=play_on)
b1.grid(row=1,column=1)
l1=Label(root,text='Enter What Tiles You Can\nPlay On Below')
l1.grid(row=0,column=0)
e2=Entry(root)
e2.grid(row=1,column=2)
b2=Button(root,text='Enter',command=your_tiles)
b2.grid(row=1,column=3)
l2=Label(root,text='Enter Your Tiles Below')
l2.grid(row=0,column=2)
text.grid(row=2,column=4)
root.mainloop()



