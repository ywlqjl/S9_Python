#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
fenetre = Tk()
fenetre.title('Calcutrice')

def get_input(entry, argu):
    entry.insert(END, argu)

def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)

def clear(entry):
    entry.delete(0, END)

def calc(entry):
    input = entry.get()
    output = str(eval(input.strip())) #strip:remove espaces, eval:calculer
    clear(entry)
    entry.insert(END, output)

def cal():
    root = Tk()
    root.title("Calc")
    root.resizable(0,0)


entry = Entry(justify='right')
entry.grid(row=0, column=0, columnspan=4,sticky=W+E+S+N) #returen est null donc...il faut 返回值为0

button0 = Button(fenetre, text='0', width=10, command=lambda : get_input(entry, '0')).grid(row=4, column=0, columnspan=2, sticky=W+E+S+N)
buttonPoint = Button(fenetre, text='.', width=5, command=lambda : get_input(entry, '.')).grid(row=4, column=2, columnspan=1, sticky=W+E+S+N)
buttonDev = Button(fenetre, text='/', width=5, command=lambda : get_input(entry, '/')).grid(row=4, column=3, columnspan=1,sticky=E+W+S+N)

button1 = Button(fenetre, text='1', width=5, command=lambda : get_input(entry, '1')).grid(row=3, column=2)
button2 = Button(fenetre, text='2', width=5, command=lambda : get_input(entry, '2')).grid(row=3, column=1)
button3 = Button(fenetre, text='3', width=5, command=lambda : get_input(entry, '3')).grid(row=3, column=0)
buttonMul = Button(fenetre, text='*', width=5, command=lambda : get_input(entry, '*')).grid(row=3, column=3)


button4 = Button(fenetre, text='4', width=5, command=lambda : get_input(entry, '4')).grid(row=2, column=2)
button5 = Button(fenetre, text='5', width=5, command=lambda : get_input(entry, '5')).grid(row=2, column=1)
button6 = Button(fenetre, text='6', width=5, command=lambda : get_input(entry, '6')).grid(row=2, column=0)
buttonMin = Button(fenetre, text='-', width=5, command=lambda : get_input(entry, '-')).grid(row=2, column=3)

button7 = Button(fenetre, text='7', width=5, command=lambda : get_input(entry, '7')).grid(row=1, column=2)
button8 = Button(fenetre, text='8', width=5, command=lambda : get_input(entry, '8')).grid(row=1, column=1)
button9 = Button(fenetre, text='9', width=5, command=lambda : get_input(entry, '9')).grid(row=1, column=0)
buttonAdd = Button(fenetre, text='+', width=5, command=lambda : get_input(entry, '+')).grid(row=1, column=3)

buttonAC = Button(fenetre, text='AC', width=5, command=lambda : clear(entry)).grid(row=5, column=0)
buttonC = Button(fenetre, text='C', width=5, command=lambda : backspace(entry)).grid(row=5, column=1)
buttonResult = Button(fenetre, text='=', width=5, command=lambda : calc(entry)).grid(row=5, column=3, columnspan=2)

fenetre.mainloop()
