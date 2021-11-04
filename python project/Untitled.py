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
    text.insert(END,string,command=self.main_window.destroy)
    
    
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

class WordScoreGUI:
        
    def __init__(self):

        root=Tk()
        root.title('Scrabble Cheater')
        text=Text(root)
        e1=Entry(root)
        e1.pack()
        b1=Button(root,text='Enter',command=play_on)
        b1.pack()
        l1=Label(root,text='Enter What Tiles You Can\nPlay On Below')
        l1.gpack()
        e2=Entry(root)
        e2.pack()
        b2=Button(root,text='Enter',command=your_tiles)
        b2.pack()
        l2=Label(root,text='Enter Your Tiles Below')
        l2.pack()
        text.pack()

        self.main_window=tkinter.Tk()

        self.top_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)

        self.prompt_label=tkinter.Label(self.top_frame, \
                                        text = 'Enter one of your word options:')
        self.score_entry=tkinter.Entry(self.top_frame, \
                                       width = 10)

        self.prompt_label.pack(side = 'left')
        self.score_entry.pack(side = 'left')

        self.calc_button=tkinter.Button(self.bottom_frame, \
                                        text = 'Word score', \
                                        command = self.convert)
        self.quit_button=tkinter.Button(self.bottom_frame, \
                                        text = 'Quit', \
                                        command = self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()
        
        tkinter.mainloop()

    def convert(self):
        word=(self.score_entry.get())
        points = justin.scrabble_score(word)
        
        tkinter.messagebox.showinfo('Word Score', \
                                str(word)+' is '+ \
                                str(points) + ' points.')



word_conv = WordScoreGUI()




