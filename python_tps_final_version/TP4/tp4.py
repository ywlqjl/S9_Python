'''
======================
TP4 - matplotlib
YAN Wenli - PENG Hanyuan
======================
'''
import random
import numpy as np
from tkinter import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot

#datas
numbers_x = [1,2,3,4,5,6,7,8,9,10]
numbers_y = np.random.randint(30,size=10)
numbers_y2 = np.random.randint(30,size=10)
numbers_y3 = np.random.randint(20,size=10)


def quitProgram():
    bg.destroy()

def quick_sort(lists, left, right):

    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
            lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
    lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists

def drawScatter():

    global plot
    plot.figure('Scatter fig')

    ax = plot.gca()
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    l1 = ax.scatter(numbers_x, numbers_y, c='g', marker = 'o', s=10, alpha=0.5)
    l2 = ax.scatter(numbers_x, numbers_y2, c='blue', marker = '*', s=10, alpha=0.5)

    plot.plot([0, 10], [0, 30], color = 'red', linestyle = 'solid')
    plot.annotate(text="this point is important", xy=(5, 15), xytext=(6, 16),arrowprops={"arrowstyle":"->"})

    plot.legend(handles = [l1, l2,], labels = ['a', 'b'], loc = 'best')
    plot.show()


def drawLine():
    global plot
    plot.figure('Line fig')
    # plot.xlabel('X axis')
    # plot.ylabel('Y axis')
    ax = plot.gca()
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    g1 = ax.plot(numbers_x, numbers_y, c='r', linewidth=1, alpha=0.6)
    g2 = ax.plot(numbers_x, numbers_y2, color='#054E9F', linewidth=1, alpha=0.6)
    g3 = ax.plot(numbers_x, numbers_y3, color='#1DF09B', linewidth=1, alpha=0.6)
    plot.legend(handles = [g1,g2,g3,], labels = ['line1', 'line2','line3'], loc = 'best')
    plot.show()

def drawHisto():

    global plot
    plot.figure('Historique Bar fig')
    ax = plot.gca()
    ax.set_xlabel('value')
    ax.set_ylabel('count')

    xticks = np.arange(1, len(numbers_x)+1)
    bar_width=0.5

    ax.bar(xticks, numbers_y, width=bar_width, edgecolor='none')
    ax.set_xticks(xticks)

    ax.set_xticklabels(numbers_x)
    ax.set_xlim(0,len(xticks))
    plot.show()

def drawCamenbert():

    plot.figure('Camenbert fig',figsize = (5, 5))
    x = [1, 2, 3, 4, 10]
    plot.pie(x, labels = ['A', 'B', 'C', 'D', 'E'],
           colors = ['red', 'green', 'yellow', 'blue', 'pink'],
           explode = [0, 0.2, 0, 0, 0],
           autopct = lambda x: str(round(x, 2)) + '%',
           pctdistance = 0.7, labeldistance = 0.4,
           shadow = True)
    plot.legend(loc='upper left')
    plot.show()

def showAllFigs():
    fig = plot.figure()
    ax1 = fig.add_subplot(223)
    ax2 = fig.add_subplot(221)
    ax3 = fig.add_subplot(222)
    ax4 = fig.add_subplot(224)

    ax1.plot(range(5), color = 'blue')
    ax2.bar(range(5), range(5), color = 'green')
    ax3.plot(range(5), color = 'red')
    ax4.plot(range(5), color = 'black')

    # ax3 = fig.add_subplot(224)

    # plot.subplot(1, 2, 1)
    # plot.scatter(range(5), [x ** 2 for x in range(5)], color = 'blue')
    # # plot.subplot(2, 2, 2)
    # plot.bar(range(5), range(5), color = 'green')
    # # plot.subplot(2, 2, 4)
    # plot.plot(range(5), color = 'red')
def fun(x, y):
  return x**2 + y

def mesh_2d_3d():
    fig = plot.figure('3D Mesh fig') # titre
    ax = fig.add_subplot(111, projection='3d') #une image en 3D


    # x = y = np.arange(-3.0, 3.0, 0.05)
    # X, Y = np.meshgrid(x, y)
    # zs = np.array([fun(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
    # Z = zs.reshape(X.shape)

    # ax.plot_surface(X,Y,Z)
    x = np.random.sample(100)
    y = np.random.sample(100)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.scatter(x, y, zs=0, zdir='y', label='points in (x,z)')
    ax.legend()
    plot.show()

def mesh_3d():
    fig = plot.figure('3D Mesh fig')
    ax = fig.add_subplot(111, projection='3d')

    x = y = np.arange(-3.0, 3.0, 0.05)
    X, Y = np.meshgrid(x, y)
    zs = np.array([fun(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)

    ax.plot_surface(X,Y,Z)
    plot.show()


if __name__ == '__main__':

    bg = Tk()
    #window
    bg.geometry('720x200+500+200')
    bg.title('Python TP4 : Matplotlib')

    #labels
    label = Label(bg,text="Please choose a mode from the menu.").grid(row=0, column=0, columnspan=6, sticky=N+W+S+E)
    label_warning = Label(bg,
                            text = 'Warning: We choose single mode window. So you should close the current mode window when you want to open another mode!\n Otherwise, it will crash!',
                            bg = 'yellow',
                            height = 4,
                            wraplength = 300,
                            justify = 'center').grid(row=1, column=0, columnspan=6,sticky=N+W+S+E)

    btn_scatter = Button(text='Scatter fig',relief=RIDGE, width = 10, command=drawScatter).grid(row=3,column=0)
    btn_line = Button(text='Line fig',relief=RIDGE,width = 10,command=drawLine).grid(row=3,column=1)
    btn_histogramme = Button(text='Histo fig',relief=RIDGE,width = 10,command=drawHisto).grid(row=3,column=2)
    btn_camenbert = Button(text='Camenbert fig',relief=RIDGE,width = 10,command=drawCamenbert).grid(row=3,column=3)
    btn_2d_3d = Button(text='2D_in_3D fig',relief=RIDGE,width = 10,command=mesh_2d_3d).grid(row=3,column=4)
    btn_3d = Button(text='3D fig',relief=RIDGE,width = 10,command=mesh_3d).grid(row=3,column=5)
    btn_all = Button(text='Show all figures together',relief=RIDGE,width = 10,command=showAllFigs).grid(row=4,column=0, columnspan=6,sticky=N+W+S+E)


    #buttons
    menuBar = Menu(bg)
    bg.config(menu=menuBar)

    #menus
    modeMenu = Menu(menuBar)
    menuBar.add_cascade(label="Mode", menu=modeMenu)
    modeMenu.add_command(label="Scatter", command=drawScatter)
    modeMenu.add_command(label="Line", command=drawLine)
    modeMenu.add_command(label="Histo", command=drawHisto)
    modeMenu.add_command(label="Camenbert", command=drawCamenbert)
    modeMenu.add_command(label="22D_in_3D", command=mesh_2d_3d)
    modeMenu.add_command(label="3DMesh", command=mesh_3d)

    modeMenu.add_separator()
    modeMenu.add_command(label="Exit", command=quitProgram)

    bg.mainloop()
