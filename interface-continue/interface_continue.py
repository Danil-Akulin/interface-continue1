from random import shuffle
from tkinter import *
from tkinter import ttk
import random
from tkinter.filedialog import *
from tkinter import scrolledtext
import sys
from tkinter.messagebox import *
import sys, fileinput


mas4=[0]


fail = open(r"C:\Users\danil\Рабочий стол\voprosi.txt", "r", encoding='UTF-8')
mas1 = []
mas2 = []
for line in fail:
    n = line.find(",")
    mas1.append(line[0:n].strip())
    mas2.append(str(line[n+1:len(line)].strip()))
fail.close()

del mas1[1::2]
del mas2[1::2]


shuffle(mas1)
del mas1[6:16]

root=Tk()
root.geometry("700x500")
root.title('Опросник')
tabs=ttk.Notebook(root)
tabs_list=[]

M=Menu(root)
root.config(menu=M)
m1=Menu(M,tearoff=0)
M.add_cascade(label='Вопросы',menu=m1)

l1 = Label(text=mas1, font="Arial 11")
l1.config(bd=30)
l1.pack()


def first_question():
    l1 = Label(text=mas1[0])
    l1.config(bd=30)
    l1.pack()


def two_question():
    l1 = Label(text=mas1[1], font="Arial 11")
    l1.config(bd=30)
    l1.pack()


def three_question():
    l1 = Label(text=mas1[2], font="Arial 11")
    l1.config(bd=30)
    l1.pack()


def four_question():
    l1 = Label(text=mas1[3], font="Arial 11")
    l1.config(bd=30)
    l1.pack()


def five_question():
    l1 = Label(text=mas1[4], font="Arial 11")
    l1.config(bd=30)
    l1.pack()


def activated():
    mas4[0]+=1
    print(mas4)


tab1 = Frame(tabs)
tab2 = Frame(tabs)
tab3 = Frame(tabs)
tab4 = Frame(tabs)
tab5 = Frame(tabs)


tabs.add(tab1, text='первый')
tabs.add(tab2, text='второй')
tabs.add(tab3, text='третий')
tabs.add(tab4, text='четвёртый')
tabs.add(tab5, text='пятый')


lbl1 = Label(tab1)
lbl1.grid(column=0, row=0)
btn = Button(tab1, text="да")
btn.grid(column=1, row=0)
btn1 = Button(tab1, text="нет",command=activated)
btn1.grid(column=2, row=0)

lbl1 = Label(tab2)
lbl1.grid(column=0, row=0)
btn = Button(tab2, text="да")
btn.grid(column=1, row=0)
btn1 = Button(tab2, text="нет",command=activated)
btn1.grid(column=2, row=0)

lbl1 = Label(tab3)
lbl1.grid(column=0, row=0)
btn = Button(tab3, text="да",command=activated)
btn.grid(column=1, row=0)
btn1 = Button(tab3, text="нет")
btn1.grid(column=2, row=0)

lbl1 = Label(tab4)
lbl1.grid(column=0, row=0)
btn = Button(tab4, text="да")
btn.grid(column=1, row=0)
btn1 = Button(tab4, text="нет",command=activated)
btn1.grid(column=2, row=0)


lbl1 = Label(tab5)
lbl1.grid(column=0, row=0)
btn = Button(tab5, text="да",command=activated)
btn.grid(column=1, row=0)
btn1 = Button(tab5, text="нет")
btn1.grid(column=2, row=0)
tabs.pack(fill='both')


if mas4[0] >= int('3'):
    fail = open(r"C:\Users\danil\Рабочий стол\oiged.txt", "a", encoding='UTF-8')
    fail.write('Прошёл\n')
    fail.close()

if mas4[0] <= int('2'):
    fail = open(r"C:\Users\danil\Рабочий стол\valed.txt", "a", encoding='UTF-8')
    fail.write('не Прошёл\n')
    fail.close()
root.mainloop()