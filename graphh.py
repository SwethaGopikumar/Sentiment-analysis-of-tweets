
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.figure import Figure

import pandas as pd
style.use("ggplot")
tweets=pd.read_csv("final.csv",encoding='iso-8859-1')

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
    fig.text(0.5, 0.04,'tweets', ha='center')
    fig.text(0.04, 0.5, 'sentiment', va='center', rotation='vertical')

#ani = animation.FuncAnimation(fig, animate, interval=1000)
#plt.show()

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *

class mclass:
    def __init__(self,widow):
        self.window=window
        self.button1=Button(window,text="Growth of sentiment",command=self.plot)
        self.button1.pack()
        
    def plot(self):
        ani = animation.FuncAnimation(fig, animate, interval=1000)
        plt.show()
        canvas=FigureCanvasTkAgg(fig,master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()

        
window=Tk()
start=mclass(window)
window.mainloop()