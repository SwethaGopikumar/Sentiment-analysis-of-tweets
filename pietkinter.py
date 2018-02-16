# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 12:46:05 2017

@author: hp
"""
from nltk.sentiment.vader import SentimentIntensityAnalyzer
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
        self.box=Entry(window)
        self.button1=Button(window,text="Growth of sentiment",command=self.plot)
        self.button2=Button(window,text="Sentiment analysis",command=self.pie)
        self.box.pack()
        self.button1.pack(self,side="left")
        self.button2.pack(self,side="left")
        
    def plot(self):
        ani = animation.FuncAnimation(fig, animate, interval=1000)
        plt.show()
        canvas=FigureCanvasTkAgg(fig,master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()
        
    def pie(self):
        tweets=pd.read_csv("main_db.csv",encoding='iso-8859-1')
        
        sid = SentimentIntensityAnalyzer()
        
        tweets['sentiment_compound_polarity']=tweets.processedTweet.apply(lambda x:sid.polarity_scores(x)['compound'])
        tweets['sentiment_neutral']=tweets.processedTweet.apply(lambda x:sid.polarity_scores(x)['neu'])
        tweets['sentiment_negative']=tweets.processedTweet.apply(lambda x:sid.polarity_scores(x)['neg'])
        tweets['sentiment_pos']=tweets.processedTweet.apply(lambda x:sid.polarity_scores(x)['pos'])
        tweets['sentiment_type']=''
        tweets.loc[tweets.sentiment_compound_polarity>0,'sentiment_type']='POSITIVE'
        tweets.loc[tweets.sentiment_compound_polarity==0,'sentiment_type']='NEUTRAL'
        tweets.loc[tweets.sentiment_compound_polarity<0,'sentiment_type']='NEGATIVE'
        tweets.sentiment_type.value_counts().plot(kind='pie',title="sentiment analysis")
        tweets.to_csv('final.csv')
        canvas=FigureCanvasTkAgg(fig,master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()
    
    
window=Tk()
start=mclass(window)
window.mainloop()
