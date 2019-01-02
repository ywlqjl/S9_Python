from tkinter import *
import tkinter.messagebox
import math

def get_input(entry, arg):
    entry.insert(END, arg)

def all_clear(entry):
    entry.delete(0, END)

def clear(entry):
    entry.delete((len(entry.get())-1), END)

def calTan(entry):
    input = entry.get().strip()
    result2 = math.tan((int(input)/180)* math.pi)
    all_clear(entry)
    entry.insert(END, result2)

def calSin(entry):
    input = entry.get().strip()
    resultSin = math.sin((int(input)/180)* math.pi)
    all_clear(entry)
    entry.insert(END, resultSin)

def calCos(entry):
    input = entry.get().strip()
    result2 = math.cos((int(input)/180)* math.pi)
    all_clear(entry)
    entry.insert(END, result2)

def calFac(entry):
    input = entry.get().strip()
    result2 = math.factorial(int(input))
    all_clear(entry)
    entry.insert(END, result2)

def calSquare(entry):
    input = entry.get().strip()
    result2 = int(input) * int(input)
    all_clear(entry)
    entry.insert(END, result2)

def calCube(entry):
    input = entry.get().strip()
    result2 = int(input) * int(input) * int(input)
    all_clear(entry)
    entry.insert(END, result2)

def calFabs(entry):
    input = entry.get().strip()
    result2 = math.fabs(int(input))
    all_clear(entry)
    entry.insert(END, result2)

def calSqrt(entry):
    input = entry.get().strip()
    result2 = math.sqrt(int(input))
    all_clear(entry)
    entry.insert(END, result2)

def cal(entry):
    input = entry.get()
    try:
        result = str(eval(input.strip()))
        all_clear(entry)
        entry.insert(END, result)
    except ZeroDivisionError:
        print("La variable denominateur est égale à 0.")
        all_clear(entry)


def quitProgram():
    bg.destroy()

def modeScientifique():
    calScientifique()

def modeBasique():
    calBasique()

def calBasique():
    global bg
    bg.title('Calculatrice')
    for btn in list_button_sci:
        btn.destroy()
    # bg.update_idletasks()
    # bg.geometry(400*200)
    global entry
    entry = Entry(justify='right')
    entry.grid(row=0, column=0, columnspan=5, sticky=N+W+S+E)

    button_c = Button(text='C', relief=RIDGE,width=5, command =lambda : clear(entry)).grid(row=4,column=1)
    button0 = Button(text='0', relief=RIDGE,width=5, command =lambda : get_input(entry,'0')).grid(row=4,column=2)
    button_ac = Button(text='AC', relief=RIDGE,width=5, command =lambda : all_clear(entry)).grid(row=4,column=3)

    button1 = Button(text='1', relief=RIDGE,width=5, command =lambda : get_input(entry,'1')).grid(row=3,column=1)
    button2 = Button(text='2', relief=RIDGE,width=5, command =lambda : get_input(entry,'2')).grid(row=3,column=2)
    button3 = Button(text='3', relief=RIDGE,width=5, command =lambda : get_input(entry,'3')).grid(row=3,column=3)

    button4 = Button(text='4', relief=RIDGE,width=5, command =lambda : get_input(entry,'4')).grid(row=2,column=1)
    button5 = Button(text='5', relief=RIDGE,width=5, command =lambda : get_input(entry,'5')).grid(row=2,column=2)
    button6 = Button(text='6', relief=RIDGE,width=5, command =lambda : get_input(entry,'6')).grid(row=2,column=3)

    button7 = Button(text='7', relief=RIDGE,width=5, command =lambda : get_input(entry,'7')).grid(row=1,column=1)
    button8 = Button(text='8', relief=RIDGE,width=5, command =lambda : get_input(entry,'8')).grid(row=1,column=2)
    button9 = Button(text='9', relief=RIDGE,width=5, command =lambda : get_input(entry,'9')).grid(row=1,column=3)


    button_plus = Button(text='+', relief=RIDGE,width=5, command =lambda : get_input(entry,'+')).grid(row=1,column=4)
    button_minus = Button(text='-', relief=RIDGE,width=5, command =lambda : get_input(entry,'-')).grid(row=2,column=4)
    button_multi = Button(text='*', relief=RIDGE,width=5, command =lambda : get_input(entry,'*')).grid(row=3,column=4)
    button_div = Button(text='/', relief=RIDGE,width=5, command =lambda : get_input(entry,'/')).grid(row=4,column=4)

    button_point = Button(text='.', relief=RIDGE,width=5, command =lambda : get_input(entry,'.')).grid(row=5,column=2)
    button_equ = Button(text='=', relief=RIDGE,width=5, command =lambda : cal(entry)).grid(row=5,column=3)


def calScientifique():
    global bg
    bg.title('Calculatrice scientifique')

    global entry
    global list_button_sci

    entry.grid(row=0, column=0, columnspan=7, sticky=N+W+S+E)
    buttonTan = Button(text='tan', relief=RIDGE,width=5, command =lambda : calTan(entry))
    buttonTan.grid(row=1,column=5)
    buttonSin = Button(text='sin', relief=RIDGE,width=5, command =lambda : calSin(entry))
    buttonSin.grid(row=2,column=5)
    buttonCos = Button(text='cos', relief=RIDGE,width=5, command =lambda : calCos(entry))
    buttonCos.grid(row=3,column=5)
    buttonFac = Button(text='x!', relief=RIDGE,width=5, command =lambda : calFac(entry))
    buttonFac.grid(row=1,column=6)
    buttonSquare = Button(text='x2', relief=RIDGE,width=5, command =lambda : calSquare(entry))
    buttonSquare.grid(row=2,column=6)
    buttonCube = Button(text='x3', relief=RIDGE,width=5, command =lambda : calCube(entry))
    buttonCube.grid(row=3,column=6)
    buttonFabs = Button(text='fabs', relief=RIDGE,width=5, command =lambda : calFabs(entry))
    buttonFabs.grid(row=4,column=5)
    buttonSqrt = Button(text='sqrt', relief=RIDGE,width=5, command =lambda : calSqrt(entry))
    buttonSqrt.grid(row=4,column=6)


    list_button_sci.append(buttonTan)
    list_button_sci.append(buttonSin)
    list_button_sci.append(buttonCos)
    list_button_sci.append(buttonFac)
    list_button_sci.append(buttonSquare)
    list_button_sci.append(buttonCube)
    list_button_sci.append(buttonFabs)
    list_button_sci.append(buttonSqrt)





if __name__ == '__main__':
    bg = Tk()
    # create a toplevel menu
    menuBar = Menu(bg)
    # display the menu
    bg.config(menu=menuBar)

    # create a lower level menu
    aideMenu = Menu(menuBar)
    menuBar.add_cascade(label="Aide", menu=aideMenu)
    aideMenu.add_command(label="Open")
    aideMenu.add_command(label="Save")
    aideMenu.add_separator()
    aideMenu.add_command(label="Exit", command=quitProgram)

    modeMenu = Menu(menuBar)
    menuBar.add_cascade(label="Mode", menu=modeMenu)
    modeMenu.add_command(label="Mode basique", command=calBasique)
    modeMenu.add_command(label="Mode scientifique", command=calScientifique)


    list_button_sci = []

    calBasique()
    bg.mainloop()
