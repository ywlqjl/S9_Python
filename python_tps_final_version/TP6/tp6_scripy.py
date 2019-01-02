'''
========================================
TP6_scripy YAN Wenli & PENG Hanyuan
========================================
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


'''
Pour une solution polynomiale simple,
on peut utiliser simplement la fonction numpy:
    polyfit (x, y, degree).
'''
def polyfitting_1():

    #x, y
    x = np.arange(1, 16, 1)
    num = [4.00, 5.20, 5.900, 6.80, 7.34,
           8.57, 9.86, 10.12, 12.56, 14.32,
           15.42, 16.50, 18.92, 19.58, 20.00]
    y = np.array(num)

    #Fit avec un polynôme cubique
    f1 = np.polyfit(x, y, 3)
    p1 = np.poly1d(f1)
    print(p1)

    #Fit y value
    # methode2: yvals=np.polyval(f1, x)
    yvals = p1(x)

    #Dessiner un graphe
    plot1 = plt.plot(x, y, 's',label='original values')
    plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc=4) #legend:right-down
    plt.title('polyfitting_1_numpy')
    plt.show()
    plt.savefig('test.png')


'''

Pour le fitting exponentiel et puissant,
on peut utiliser curve_fit dans scipy.optimize
'''

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

def polyfitting_2():
    xdata = np.linspace(0, 4, 50)
    y = func(xdata, 1.5, 2.3, 0.5)
    ydata = y + 0.2 * np.random.normal(size=len(xdata))
    plt.plot(xdata,ydata,'b-',label='data')
    #Ajustement des moindres carrés non linéaire
    popt, pcov = curve_fit(func, xdata, ydata)
    #popt[], trois inconnus en attente de résolution a,b,c
    y2 = [func(i, popt[0],popt[1],popt[2]) for i in xdata]
    plt.plot(xdata,y2,'r--',label='fit')
    plt.title('polyfitting_2_scripy')
    plt.legend()
    plt.show()
    print(popt)


polyfitting_1()
polyfitting_2()
