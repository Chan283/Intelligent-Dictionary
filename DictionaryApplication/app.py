import json
import difflib
from tkinter import *
from msvcrt import getch

data = json.load(open("data.json"))

def translate():
	word=e1.get()
	t1.delete(1.0,END)	#Delete everythn from start to END
	if word.title() in data.keys():		#word.title() will chk for specific nouns
		for item in data[word.title()]:
			t1.insert(END,"\n- " + item)
	elif word.lower() in data.keys():	#chk if entered word irrespective of case should match with dict's keys
		for item in data[word.lower()]:
			t1.insert(END,"\n- " + item)
	else:
		if difflib.get_close_matches(word.lower(),data.keys()):
			t1.insert(END,"Did you mean: ")
			for item in difflib.get_close_matches(word.lower(),data.keys()):
				t1.insert(END,"\n- " + item)
		else:
			t1.insert(END,"Invalid word")

window=Tk()

l1=Label(window,text='Intelligent Dictionary',font=('molot',23),height=4)
l1.pack()

f1=Frame(window)

l2=Label(f1,text='Word to Search')
l2.pack(side=LEFT,fill=X)

e1=Entry(f1)
e1.pack(side=LEFT,fill=X)

b1=Button(f1,text='Search',command=translate)
b1.pack(side=RIGHT,fill=X)

f1.pack()

f2=Frame(window)

l3=Label(f2,text='Result')
l3.pack(side=LEFT,fill=X)

t1=Text(f2)
t1.pack(side=RIGHT,fill=X)

f2.pack()

window.mainloop()