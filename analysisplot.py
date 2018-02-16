# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 01:30:26 2017

@author: Admin
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
#import matplotlib.animation as animation
#from matplotlib import style

from tkinter import *
root=Tk()




import pandas as pd
style.use("ggplot")
tweets=pd.read_csv("hellpkaro.csv",encoding='iso-8859-1')

arr=tweets['sentiment_compound_polarity'].tolist()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
def animate(i):
    xar = []
    yar = []

    x = 0
    y = 0

    for i in range(len(tweets['text'])):
    
        x += 1
        if (arr[i]>0):
            #print('positive')
            y += 1
        elif (arr[i]<0):
            #print('negative')
            y-=1
    
        xar.append(x)
        yar.append(y)
        
    ax1.clear()
    ax1.plot(xar,yar)

ani = animation.FuncAnimation(fig, animate, interval=1000)
#plt.show()


        