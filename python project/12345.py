import justin
import greg

tiles=[]

def play_on():
    global e1
    string=e1.get()
    a=string.upper()
    tiles.append(a)
    string='The tiles you can play on are '+a
    text.insert(END,string)
    
def your_tiles():
    global e2
    string=e2.get()
    b=string.upper()
    tiles.append(b)
    string='\nThe tiles that you have are '+b
    text.insert(END,string)
    set_tiles,your_tiles=justin.input_list(tiles)
    word_list=greg.list_of_words()
    possibilities=justin.possible_combos(set_tiles,your_tiles)
    plays=justin.possible_plays(word_list,possibilities)
    string=justin.best_word(plays)
    string='\n'+string
    text.insert(END,string)
    str1='\nAll of your possible plays are:'
    text.insert(END,str1)
    text.insert(END,plays)

def convert():
    global score_entry
    string=score_entry.get()
    string=string.upper()
    points = str(justin.scrabble_score(string))
    points = '\n'+str(string)+' is worth '+str(points)+' points'
    text.insert(END,points)

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
text.grid(row=4,column=4)


prompt_label=Label(root,text = 'Enter one of your word options:')
prompt_label.grid(row=2,column=0)
score_entry=Entry(root)
score_entry.grid(row=3,column=0)
calc_button=Button(root,text='Word score',command=convert)
calc_button.grid(row=3,column=1)


root.mainloop()
