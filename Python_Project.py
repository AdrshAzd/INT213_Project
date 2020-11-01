from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import Toplevel,messagebox,filedialog
from PIL import Image, ImageTk
from tkinter import Tk, Label
import random
top=Tk()
colors = ['red','green','blue','yellow','pink','red2','gold2']

from tkinter import *
# keep the question in a separate json file
q = [
    "Capital of India",
    "South most city in India",
]

options = [
    ["Delhi", "Mumbai", "Kolkata", "Chennai"],
    ["Delhi", "Mumbai", "Chennai", "Kanyakumari"],
]

a = [1, 4]

class Quiz:
    def _init_(self, master):
        self.opt_selected = IntVar()
        self.qn = 0
        self.correct = 0
        self.ques = self.create_q(master, self.qn)
        self.opts = self.create_options(master, 4)
        self.display_q(self.qn)
        self.button = Button(master, text="Back", command=self.back_btn)
        self.button.pack(side=BOTTOM)
        self.button = Button(master, text="Next", command=self.next_btn)
        self.button.pack(side=BOTTOM)

    def create_q(self, master, qn):
        w = Label(master, text=q[qn])
        w.pack(side=TOP)
        return w

    def create_options(self, master, n):
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(master, text="foo", variable=self.opt_selected, value=b_val+1)
            b.append(btn)
            btn.pack(side=TOP, anchor="w")
            b_val = b_val + 1
        return b

    def display_q(self, qn):
        b_val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def check_q(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True
        return False

    def print_results(self):
        print("Score: ", self.correct, "/", len(q))

    def back_btn(self):
        print("go back")

    def next_btn(self):
        if self.check_q(self.qn):
            print("Correct")
            self.correct += 1
        else:
            print("Wrong")
        self.qn = self.qn + 1
        if self.qn >= len(q):
            self.print_results()
        else:
            self.display_q(self.qn)


def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2,IntroLabelColorTick)
def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(200,IntroLabelTick)
top.title('Online Quiz')
top.config(bg='white')
top.geometry('800x400')
top.resizable(False,False)
canvas = Canvas(bg='white')
canvas.pack(expand=YES, fill=BOTH)
image = ImageTk.PhotoImage(file="a.jpg")
canvas.create_image(0, 0, image=image, anchor=NW)    
ss = 'A.S.A MULTIMEDIA QUIZ 2020'
count = 0
text = ''
##################################
SliderLabel = Label(top,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=4,width=25,bg='cyan')
SliderLabel.place(x=80,y=0)
IntroLabelTick()
IntroLabelColorTick()   
label1 = Label(top,text='Name',fg='blue',font=('Arial',10,'bold'))
label1.place(x=300,y=100)
entry1 = Entry(top,fg="Black",bd=5)
entry1.place(x=450,y=100)

label2 = Label(top,text='Section',fg='blue',font=('Arial',10,'bold'))
label2.place(x=300,y=150)
entry2 = Entry(top,fg="Black",bd=5)
entry2.place(x=450,y=150)
label3 = Label(top,text='Registration Number',fg='blue',font=('Arial',10,'bold'))
label3.place(x=300,y=200)
entry3 = Entry(top,fg="Black",bd=5)
entry3.place(x=450,y=200)

label4 = Label(top,text='Email Id',fg='blue',font=('Arial',10,'bold'))
label4.place(x=300,y=250)
entry4 = Entry(top,fg="Black",bd=5)
entry4.place(x=450,y=250)

button0 = Button(top,text='Submit',relief=RAISED,bg="green",fg="black",command=Quiz)
button0.place(x=500,y=300)
button1 = Button(top,text='Reset',relief=RAISED,bg="red",fg="black")
button1.place(x=600,y=300)
top.mainloop()

root = Tk()
root.geometry("500x300")
app = Quiz()
root.mainloop()
