import random
import numpy as np
from tkinter import *
import tkinter.messagebox
import matplotlib.pyplot as plot

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

# numbers_x = np.random.randint(10,size=10)
numbers_x = [1,2,3,4,5,6,7,8,9,10]
# numbers_x_original = range(20)
# numbers_x = random.sample(numbers_x_original, 10)
numbers_y = np.random.randint(30,size=10)
numbers_y2 = np.random.randint(30,size=10)






def drawScatter():
    #创建图并命名
    global plot
    plot.figure('Scatter fig')
    ax = plot.gca()
    #设置x轴、y轴名称
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    #画散点图，以x_list中的值为横坐标，以y_list中的值为纵坐标
    #参数c指定点的颜色，s指定点的大小,alpha指定点的透明度
    ax.scatter(numbers_x, numbers_y, c='r', s=10, alpha=0.5)
    plot.show()


def drawLine():
    #创建图并命名
    plot.figure('Line fig')
    ax = plot.gca()
    #设置x轴、y轴名称
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    #画连线图，以x_list中的值为横坐标，以y_list中的值为纵坐标
    #参数c指定连线的颜色，linewidth指定连线宽度，alpha指定连线的透明度
    ax.plot(numbers_x, numbers_y, color='r', linewidth=1, alpha=0.6)
    ax.plot(numbers_x, numbers_y2, color='#054E9F', linewidth=1, alpha=0.6)
    plot.legend(loc='upper left')

    plot.show()

def drawHisto():
    # #数据
    # x_list = []
    # y_list = []

    plot.figure('Historique Bar fig')
    ax = plot.gca()
    ax.set_xlabel('value')
    ax.set_ylabel('count')

    #每个直方在x轴上的位置，代表着在x轴上的一个（些）绝对的位置，可以是整数或浮点数
    xticks = np.arange(1, len(numbers_x)+1)
    #每个直方的宽度
    bar_width=0.5

    #在xticks指定的位置画y_list指定高度的、width指定宽度的直方图
    #edgecolor指定每个直方的边框颜色
    #传入的xticks与y_list的长度必须相等！
    ax.bar(xticks, numbers_y, width=bar_width, edgecolor='none')
    ax.set_xticks(xticks)

    #每个直方下边显示的label，传入的参数为一个列表，列表里可以是数字也可以是字符串
    ax.set_xticklabels(numbers_x)
    #横轴的显示范围，该范围小于xticks的范围会造成一部分直方显示不出来
    ax.set_xlim(0,len(xticks))
    plot.legend()

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





if __name__ == '__main__':
    #main()
    bg = Tk()
    bg.geometry('500x200+500+200')
    bg.title('Python TP4 : Matplotlib')

    label = Label(bg,text="Please choose a mode from the menu.").pack()
    label_warning = Label(bg,
    text = 'Warning: We choose single mode window. So you should close the current mode window when you want to open another mode!\n Otherwise, it will crash!',
    bg = 'yellow',
    width = 400,
    height = 4,
    wraplength = 400,
    justify = 'center'
    )
    label_warning.pack()

    menuBar = Menu(bg)
    bg.config(menu=menuBar)

    modeMenu = Menu(menuBar)
    menuBar.add_cascade(label="Mode", menu=modeMenu)
    modeMenu.add_command(label="Scatter", command=drawScatter)
    modeMenu.add_command(label="Line", command=drawLine)
    modeMenu.add_command(label="Histo", command=drawHisto)
    modeMenu.add_command(label="Camenbert", command=drawCamenbert)

    modeMenu.add_separator()
    modeMenu.add_command(label="Exit", command=quitProgram)
    bg.mainloop()
